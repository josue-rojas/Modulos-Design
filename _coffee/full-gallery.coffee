document.addEventListener "DOMContentLoaded", ->
  timeoutDelay = ''
  window.selectImage = (src) ->
    $('.selected-image').removeClass('active')
    addDelay=->
      $('.selected-image img').attr('src', src)
      $('.selected-image').addClass('active')
    timeoutDelay = setTimeout(addDelay, 500)
