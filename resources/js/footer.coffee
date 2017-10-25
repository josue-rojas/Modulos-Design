---
---


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
