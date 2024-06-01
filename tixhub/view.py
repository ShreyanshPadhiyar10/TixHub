from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from base.models import Movie_details, Theatre_details, Booking
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
import razorpay
from django.views.decorators.csrf import csrf_exempt
from tixhub import settings

def home(req):
    return render(req, "index.html")

def more_details(request, movie_id):
    movie = get_object_or_404(Movie_details, id = movie_id)
    
    return render(request, 'More/more.html', {'movie' : movie})

@login_required
def ticket_booking(request, movie_id):
    movie = get_object_or_404(Movie_details, id = movie_id)
    
    all_theatres = Theatre_details.objects.all()
    
    # Get data from submited form and store them in bookings model
    if request.method == 'POST':
        theatre_name = request.POST.get('theatre')
        date = request.POST.get('date')
        time = request.POST.get('time')
        selected_seats = request.POST.getlist('tickets[]')
        
        if not selected_seats:
            return redirect('book_ticket', movie_id=movie_id)
        
        theatre = get_object_or_404(Theatre_details, id=theatre_name)
        
        amount = len(selected_seats) * 200 * 100
        
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        razorpay_order = client.order.create({"amount": amount, "currency": "INR", "payment_capture": "1"})
        
        booking = Booking.objects.create(
            user=request.user,
            movie=movie,
            theatre=theatre,
            date=date,
            time=time,
            seats=','.join(selected_seats),
            razorpay_order_id=razorpay_order['id']
        )
        # return redirect("booking_success", booking_id = booking.id)
        return render(request, "Payment/payment.html", {
            'movie': movie,
            'theatre': theatre,
            'date': date,
            'time': time,
            'seats': selected_seats,
            'amount': amount,
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key_id': settings.RAZORPAY_KEY_ID,
            'booking_id': booking.id
        })
    
    return render(request, 'Bookings/ticket_booking.html', {'movie' : movie, 'all_theatres' : all_theatres})

@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        data = request.POST
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        try:
            client.utility.verify_payment_signature({
                'razorpay_order_id': data.get('razorpay_order_id'),
                'razorpay_payment_id': data.get('razorpay_payment_id'),
                'razorpay_signature': data.get('razorpay_signature')
            })
            booking_id = data.get('booking_id')
            booking = get_object_or_404(Booking, id=booking_id)
            booking.razorpay_payment_id = data.get('razorpay_payment_id')
            booking.razorpay_signature = data.get('razorpay_signature')
            booking.save()
            return render(request, 'Bookings/booking_success.html', id=booking_id)
        except razorpay.errors.SignatureVerificationError:
            return render(request, 'payment_failed.html')
    return redirect('home')

# If booking data stored then display this page
def booking_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'Bookings/booking_success.html', {'booking': booking})

# filter the booked data from database
def get_booked_seats(request, movie_id, theatre_id, date, time):
    theatre = get_object_or_404(Theatre_details, id=theatre_id)
    
    bookings = Booking.objects.filter(movie_id=movie_id, theatre=theatre, date=date, time=time)
    booked_seats = []
    for booking in bookings:
        booked_seats.extend(booking.seats.split(','))
    return JsonResponse({'booked_seats': booked_seats})
