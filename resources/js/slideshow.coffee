---
---
document.addEventListener "DOMContentLoaded", ->
  current = 0
  $slides = $('.slideshow .slide')
  # -------------------
  # settings
  speed =  $slides.closest('.slideshow').data('speed')
  speed = if speed then speed else 3000 #check if it exist
  auto = $slides.closest('.slideshow').data('auto')
  auto = if auto==false then auto else true
  slideTimout =''
  # -------------------
  # function to change slide
  pauseState = false
  window.changeSlide = (change=1, manual=pauseState, pressPause=false)->
    $('.active').removeClass('active')
    $($slides[current]).addClass('active')
    current = if current+change < 0 then $slides.length-1 else (current+change)%$slides.length
    clearTimeout(slideTimout)
    pauseState = if pressPause then !pauseState else manual
    # console.log(current)
    # console.log(pressPause, 'pauseState ' + pauseState)
    if !pauseState
      slideTimout = setTimeout(changeSlide, speed)
    return
  # -------------------
  # auto start
  if auto
    changeSlide()
