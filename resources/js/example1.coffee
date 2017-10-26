---
---
# just the start of the joining of coffeessss
# do not want to waste time finding the the two line for each coffee and deleteing it
# this js is for main and default js (like things every page needs)

touch = false

document.addEventListener "DOMContentLoaded", ->
  # ---------------------------------------------------
  # check if it has touch (mobile)
  try
    document.createEvent('TouchEvent')
    document.documentElement.className += " touch"
    touch = true
  catch error
    document.documentElement.className += " no-touch"

  # getter for touch var to know if it has touch
  window.hasTouch = -> return touch
document.addEventListener "DOMContentLoaded", ->
  # -----------------------------------------
  # footer reposition when window resize
  state = true
  window.footerReposition = ->
    $footer = $('.footer')
    if ($('body').height()+ $footer.outerHeight() + $footer.height() > $(window).outerHeight())
      if state
        $footer.addClass 'content-footer'
        # $footer.fadeOut 300, ->
        #   $footer.addClass 'content-footer'
        #   $footer.fadeIn 400
        state = false
    else
      if !state
        $footer.removeClass 'content-footer'
        # $footer.fadeOut 300, ->
        #   $footer.removeClass 'content-footer'
        #   $footer.fadeIn 400
        state = true
  $(window).resize(footerReposition)

$(window).on 'load', ->
  footerReposition()
document.addEventListener "DOMContentLoaded", ->
  console.log($('body').height())
  # ---------------------------------------------------------------
  # functions for mobile toggle controls
  if hasTouch()
    $('.slideshow').removeClass('hasHover')
    $('.slideshow').on 'touchend', (event)->
      $this = $(event.target).closest('.slideshow')
      $buttons = $($this).find('.button-wrapper')
      if $buttons.hasClass('toggle')
        $buttons.removeClass('toggle')
        return
      $('.button-wrapper.toggle').removeClass('toggle')
      $buttons.addClass('toggle')

  # ---------------------------------------------------------------
  timeoutFunctions = [] #holds the variables for timeout funtion

  # function changes slides in targetSlideshow
  window.changeSlide = (change=1, targetSlideshow, manuelChange=false) ->
    targetSlideshow = $(targetSlideshow).closest('.slideshow')
    current = parseInt(targetSlideshow.attr('current'))
    length = targetSlideshow.data('length')
    index = parseInt(targetSlideshow.data('index'))
    targetSlideshow.find('[data-pos='+current+']').removeClass('active')
    current = if current+change < 0 then length-1 else (current+change)%length
    targetSlideshow.find('[data-pos='+current+']').addClass('active')
    targetSlideshow.attr('current', current)
    if manuelChange # pause if manuel change
      clearTimeout(timeoutFunctions[index])
      targetSlideshow.addClass('pause')
      return ''
    speed = targetSlideshow.data('speed')
    timeoutFunctions[index] = setTimeout(changeSlide,speed, change, targetSlideshow, manuelChange)

  # autostart slidesshows who do not have pause
  # and mobile setup
  $('.slideshow').each (index) ->
    $(this).attr('data-index', index)
    timeoutFunction = ''
    timeoutFunctions.push(timeoutFunction)
    if $(this).hasClass('pause') then return
    changeSlide(1, this, false)
    return
