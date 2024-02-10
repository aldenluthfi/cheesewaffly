var x = 0
var speed = Math.floor(document.documentElement.clientWidth / 500)

function getTranslateX(element) {
    const style = window.getComputedStyle(element)
    const matrix = new DOMMatrixReadOnly(style.transform)
    return matrix.m41
}

function marquee() {
    var text = document.querySelector('.sliding')

    x = getTranslateX(text) - speed

    if (x <= -Math.floor(0.25 * text.getBoundingClientRect().width)) {
        x = -x + speed
    }

    text.style.webkitTransform = `translate(${x}px, 0px)`
    text.style.transform = `translate(${x}px, 0px)`

    requestAnimationFrame(marquee)
}

marquee()

