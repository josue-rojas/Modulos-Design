document.addEventListener "DOMContentLoaded", ->
  start=->
    console.log('hello')
    $('.start').removeClass('start')
  setTimeout(start, 0)
