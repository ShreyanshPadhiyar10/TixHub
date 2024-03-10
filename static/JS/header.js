let page = document.getElementById('pages');
let hamburger = document.getElementById('hamburger');
let canvasHeaderDiv = page.firstElementChild;
let canvasBodyDiv = page.lastElementChild;
let canvasBodyDivUl = canvasBodyDiv.children[0];

let windowWidth = window.innerWidth;

function removeCanvas() {
    page.classList.remove("offcanvas", "offcanvas-start", "canvasStyle")
    canvasHeaderDiv.classList.add("d-none")
    canvasBodyDivUl.classList.replace("flex-column", "flex-row")
    hamburger.classList.add('d-none')
}

function addCanvas() {
    page.classList.add("offcanvas", "offcanvas-start", "canvasStyle")
    canvasHeaderDiv.classList.remove("d-none")
    canvasBodyDivUl.classList.replace("flex-row", "flex-column")
    hamburger.classList.remove('d-none')
}



if(windowWidth >= 1200) {
    removeCanvas()
}else {
    addCanvas()
}

window.onresize = () => {
    if (window.innerWidth > 1200) {
        removeCanvas()
    }
    else {
        addCanvas()
    }
}