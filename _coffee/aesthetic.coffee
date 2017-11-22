document.addEventListener "DOMContentLoaded", ->
  currentTab = ''
  window.activeTab = (tab)->
    currentTab = tab
    $('.background .image').addClass('tab-active')
    $('.front').addClass('tab-active')
    $(tab).addClass('active')
  window.closeTab = ->
    $('.background .image').removeClass('tab-active')
    $(currentTab).removeClass('active')
    $('.front').removeClass('tab-active')

$(window).on 'load', ->
  start = ->
    console.log('hello')
    $('.start').removeClass('start')
  setTimeout(start, 0)
