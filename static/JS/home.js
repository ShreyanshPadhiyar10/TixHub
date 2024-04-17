document.addEventListener('DOMContentLoaded', () => {
    const swiper = new Swiper('.mySwiper', {
        spaceBetween: 30,
        centeredSlides: true,
        autoplay: {
            delay: 2500,
            disableOnInteraction: false,
        },
        pagination: {
            el: ".swiper-pagination",
            clickable: true,
        },
    });

    // Set the background image dynamicly that came from database
    const slides = document.querySelectorAll('.mySwiper .swiper-slide');

    function updateBackgroundImage(slide) {
        const imageUrl = slide.getAttribute('data-image-src');
        slide.style.background = `url(${imageUrl}) no-repeat center center fixed`;
        slide.style.webkitBackgroundSize = "cover";
    }


    // Initialize the background images for the initial slides
    slides.forEach((slide) => {
        updateBackgroundImage(slide);
    });
});