const APIUrl = 'http://www.omdbapi.com/?t=dune&apikey=d4eeda95'

setInterval( () => {
    let className = document.getElementsByClassName('swiper-slide-active')
    let title = document.getElementById('title')
    // console.log(className[0].id);
},1000)

let result = async (api) => {
    const response = await fetch(api)
    let data = await response.json()
    showMovie(data)
}
result(APIUrl)

let showMovie = (data) => {
    console.log(data.Title);
}
