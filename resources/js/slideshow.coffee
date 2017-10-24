---
---
document.addEventListener "DOMContentLoaded", ->
  current = 0
  $slides = $('.slideshow .slide')
  changeSlide = ->
    if current >= $slides.length
      current = 0
    $('.active').removeClass('active')
    $($slides[current++]).addClass('active')
    setTimeout(changeSlide, 3000)
    return
  changeSlide()
