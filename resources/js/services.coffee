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
