// To add 60 seats in page
let seats = document.querySelector(".all-seats");
for (var i = 0; i < 49; i++) {
    seats.insertAdjacentHTML(
        "beforeend",
        '<input type="checkbox" name="tickets" id="s' +
        (i + 2) +
        '" /><label for="s' +
        (i + 2) +
        '" class="seat"></label>'
    );
}
console.log(seats);


let book = document.getElementById("book");
book.onclick = () => {
    let checkedBoxes = document.querySelectorAll('input[name=tickets]:checked');
    checkedBoxes.forEach((checkbox) => {
        let label = checkbox.nextElementSibling;
        label.classList.add("booked");
        checkbox.disabled = true
        checkbox.checked = false
    })
}

// To count ticket amount and qty
let tickets = seats.querySelectorAll("input");
tickets.forEach((ticket) => {
    ticket.addEventListener("change", () => {
        let amount = document.querySelector(".amount").innerHTML;
        let count = document.querySelector(".count").innerHTML;
        amount = Number(amount);
        count = Number(count);

        if (ticket.checked) {
            count += 1;
            amount += 200;
        } else {
            count -= 1;
            amount -= 200;
        }
        document.querySelector(".amount").innerHTML = amount;
        document.querySelector(".count").innerHTML = count;
    });
});

// To get next 7 days date
let dates = document.querySelectorAll(".dates input");
let currentDate = new Date();
currentDate.setDate(currentDate.getDate()); // Set the date to tomorrow

for (let i = 0; i < dates.length; i++) {
    let date = new Date(currentDate);
    let day = date.toLocaleString("en-US", { weekday: "short" });
    let dayNumber = date.getDate();

    dates[i].nextElementSibling.children[0].textContent = day;
    dates[i].nextElementSibling.children[1].textContent = dayNumber;

    currentDate.setDate(currentDate.getDate() + 1); // Increment the date by one day
}








// // <!-- HTML code remains the same -->

// let seat = document.querySelectorAll(".all-seats input");
// // console.log(seat);
// // let dates = document.querySelectorAll(".date");
// let times = document.querySelectorAll(".time");
// let bookedSeats = {}; // Object to store booked seats for each date and time


// // Function to book seats for a specific date and time
// function bookSeats(date, time) {
//     let selectedSeats = [];
//     seat.forEach((s) => {
//         // console.log(s);
//         if (s.checked) {
//             selectedSeats.push(s.id);
//             // console.log(s.id);
//         }
//     });
//     bookedSeats[`${date} ${time}`] = selectedSeats;
// }

// // Function to display booked seats for a specific date and time
// function displayBookedSeats(date, time) {
//     console.log(date, time);
//     let bookedSeatsForDateAndTime = bookedSeats[`${date} ${time}`];
//     console.log(bookedSeatsForDateAndTime);
//     if (bookedSeatsForDateAndTime) {
//         for (let i = 0; i < bookedSeatsForDateAndTime.length; i++) {
//             seat.forEach((s) => {
//                 if (bookedSeatsForDateAndTime[i] === s.id) {
//                     s.disabled = true;
//                     s.checked = false;
//                     s.nextElementSibling.classList.add("booked");
//                 }
//             });
//         }
//     }
// }

// dates.forEach((date) => {
//     // console.log(date);
//     date.addEventListener("click", () => {
//         let selectedDate = date.nextElementSibling.children[1].textContent;
//         // console.log("hgj",selectedDate);
//         times.forEach((time) => {
//             // console.log(time);
//             time.addEventListener("click", () => {
//                 let selectedTime = time.textContent;
//                 // console.log(selectedTime);
//                 displayBookedSeats(selectedDate, selectedTime);
//             });
//         });
//     });
// });

// // Event listener for book button
// document.getElementById("book").addEventListener("click", () => {
//     let selectedDate = document.querySelectorAll("input[name=date]:checked")[0].nextElementSibling.children[1].textContent;
//     let selectedTime = document.querySelectorAll("input[name=time]:checked")[0].nextElementSibling.textContent;
//     bookSeats(selectedDate, selectedTime);
//     console.log(bookedSeats);
// });
