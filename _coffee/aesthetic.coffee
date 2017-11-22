document.addEventListener "DOMContentLoaded", ->
  window.blurBackground= ->
    if $('.background .image').hasClass('tab-active')
      $('.background .image').removeClass('tab-active')
    else
      $('.background .image').addClass('tab-active')

$(window).on 'load', ->
  start = ->
    console.log('hello')
    $('.start').removeClass('start')
  setTimeout(start, 0)
