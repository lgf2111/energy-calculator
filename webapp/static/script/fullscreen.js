var button = document.getElementById("fullscreen")
function getFullscreenElement() {
    return document.fullscreenElement
        || document.webkitFullscreenElement
        || document.mozFullscreenElement
        || document.msFullscreenElement
}
function toggleFullscreen() {
    if (getFullscreenElement()) {
        document.exitFullscreen()
    } else {
        document.getElementById("iframe").requestFullscreen().catch(console.log)
    }
}
button.addEventListener("click", ()=>{
    toggleFullscreen()
})

// document.addEventListener("fullscreenchange", ()=>{
//     console.log('change')
// })