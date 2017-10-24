---
---
document.addEventListener "DOMContentLoaded", ->
  # current = 0
  $slides = $('.slideshow .slide')

  window.changeSlide = (change=1, targetSlideshow) ->
    # console.log(targetSlideshow)
    targetSlideshow = if $(targetSlideshow).is($('.slideshow')) then $(targetSlideshow) else $(targetSlideshow).closest('.slideshow')
    # console.log(targetSlideshow)
    # console.log(targetSlideshow)
    if targetSlideshow.hasClass('pause') then return false
    speed = targetSlideshow.data('speed')
    current = parseInt(targetSlideshow.attr('current'))
    length = targetSlideshow.data('length')
    # console.log(targetSlideshow.find('[data-pos='+current+']'))
    targetSlideshow.find('[data-pos='+current+']').removeClass('active')
    # console.log('change',(current+change))
    current = if current+change < 0 then length-1 else (current+change)%length
    targetSlideshow.find('[data-pos='+current+']').addClass('active')
    targetSlideshow.attr('current', current)
    console.log((current+change)%length)
  # $('.slideshow').each ->
  #   changeSlide(0, this)

  # -------------------
  # settings
  # speed =  $slides.closest('.slideshow').data('speed')
  # speed = if speed then speed else 3000 #check if it exist
  # auto = $slides.closest('.slideshow').data('auto')
  # auto = if auto==false then auto else true
  # slideTimout =''
  # -------------------
  # function to change slide
  # pauseState = false
  # window.changeSlide = (change=1, manual=pauseState, pressPause=false)->
  #   console.log(change)
  #   console.log('current',current)
  #   current = if current+change < 0 then $slides.length-1 else (current+change)%$slides.length
  #   $('.active').removeClass('active')
  #   $($slides[current]).addClass('active')
  #   clearTimeout(slideTimout)
  #   pauseState = if pressPause then !pauseState else manual
  #   # console.log(pressPause, 'pauseState ' + pauseState)
  #   if !pauseState
  #     slideTimout = setTimeout(changeSlide, speed)
  #   return
  # # -------------------
  # # auto start
  # if auto
  #   changeSlide()
