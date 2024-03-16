

// To get movie name in api every seconds
let movieInterval = setInterval( () => {
    let className = document.getElementsByClassName('swiper-slide-active')
    if (className.length > 0) { // Check if an element with the class exists
        let name = className[0].id
        id = document.getElementById(name)
        finalName = movieToLink(name)
        // console.log(finalName);
        let APIUrl = `http://www.omdbapi.com/?t=${finalName}&apikey=d4eeda95`
        result(APIUrl)
    }
}, 800)
// To fetch the api

let result = async (api) => {
    const response = await fetch(api)
    let data = await response.json()
    showMovie(data)
}

// To convert a movie name with a proper link
function movieToLink(movieName) {
    for(let i = 0; i < movieName.length; i++) {
        if(movieName[i] === " ") {
            movieName = movieName.replace(" ", "+")
            return movieName
        }
    }
    return movieName
}

// To show the data in home page
let showMovie = (data) => {
    if(id.firstElementChild === null) {
        id.innerHTML += `
        <div class="container d-flex justify-content-end flex-column h-100 text-container text-white">
        <div class="row">
            <div class="col">
                <div>
                    <div class="movie-text text-center text-lg-start">
                        <h1 class="mb-lg-3 mb-2 fs-1" id="title">${data.Title}</h1>
                        <p>${data.Genre}<span class="ms-2 d-none d-lg-inline"><img src="../static/IMAGE/ICONS/calendar.png"
                                    class="img-fluid align-baseline" width="18px" alt=""> ${data.Year}</span><span class="ms-2 d-none d-lg-inline"><img
                                    src="../static/IMAGE/ICONS/clock.png" width="25px" class="img-fluid" alt="">${data.Runtime}</span></p>
                    </div>

                    <div class="rating-sec mb-3 d-none d-lg-flex">
                        <p class="d-flex mb-0 align-self-center">${data.Ratings[0].Value}</p>
                        <button type="button" class="btn text-white border-white border-2 px-2 rounded-0 py-1 ms-3">PG - 13</button>
                    </div>
                    <div class="movie-btn d-none d-lg-block">
                        <button class="btn">Book Tickets</button>
                        <button class="btn">Review</button>
                        <button class="btn">More</button>
                    </div>
                </div>
            </div>
            <div class="col align-self-end d-none d-lg-flex">
                <div class="text-end right-sec">
                    <p>${data.Director} : <span>Director</span></p>
                    <p>${data.Actors} : <span>Stars</span></p>
                    <p>${data.Plot}</p>
                </div>
            </div>
        </div>
    </div>
        `
    }

}