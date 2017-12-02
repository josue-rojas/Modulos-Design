document.addEventListener "DOMContentLoaded", ->
  currentTab = window.location.hash

  $('.tab').css('display', 'none')

  window.activeTab = (tab)->
    currentTab = tab
    $('.background .image').addClass('tab-active')
    $('.front').addClass('tab-active')
    fade = ->
      $(tab).css('display', 'flex')
      $('.front').css('display', 'none')
      extra=-> # smoother fade needs a tiny delay
        $(tab).addClass('active')
      setTimeout(extra, 0)
    setTimeout(fade, 400)

  window.closeTab = ->
    window.location.hash = ''
    $('.background .image').removeClass('tab-active')
    $(currentTab).removeClass('active')
    fade = ->
      $('.front').css('display', 'flex')
      $(currentTab).css('display', 'none')
      extra=->
        $('.front').removeClass('tab-active')
      setTimeout(extra, 0)
    setTimeout(fade, 400)

  # set right tab for first time loading
  $currentTab = $(currentTab)
  if $currentTab.length
    activeTab(currentTab)

$(window).on 'load', ->
  start = ->
    $('.start').removeClass('start')
  setTimeout(start, 0)
