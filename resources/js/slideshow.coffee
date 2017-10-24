---
---
document.addEventListener "DOMContentLoaded", ->
  timeoutFunctions = [] #holds the variables for timeout funtion

  # --------------------
  # function changes slides in targetSlideshow
  window.changeSlide = (change=1, targetSlideshow, manuelChange=false) ->
    targetSlideshow = $(targetSlideshow).closest('.slideshow')
    current = parseInt(targetSlideshow.attr('current'))
    length = targetSlideshow.data('length')
    timeoutFunctionIndex = parseInt(targetSlideshow.data('timeoutFunctionID'))
    targetSlideshow.find('[data-pos='+current+']').removeClass('active')
    current = if current+change < 0 then length-1 else (current+change)%length
    targetSlideshow.find('[data-pos='+current+']').addClass('active')
    targetSlideshow.attr('current', current)
    if manuelChange # pause if manuel change
      clearTimeout(timeoutFunctions[timeoutFunctionIndex])
      targetSlideshow.addClass('pause')
      return ''
    speed = targetSlideshow.data('speed')
    timeoutFunctions[timeoutFunctionIndex] = setTimeout(changeSlide,speed, change, targetSlideshow, manuelChange, timeoutFunctionIndex)

  # autostart slidesshows who do not have pause
  $('.slideshow').each (index) ->
    $(this).attr('data-timoutFunctionID', index)
    timeoutFunction = ''
    timeoutFunctions.push(timeoutFunction)
    if $(this).hasClass('pause') then return
    changeSlide(1, this, false)
    return


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
