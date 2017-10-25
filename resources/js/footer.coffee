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
  # this doesn't work sometimes in safari for some reason cause some 'body' changes size so it gives the wrong size in the beginning
  # so i will call this in other pages
  footerReposition()
  $(window).resize(footerReposition)
