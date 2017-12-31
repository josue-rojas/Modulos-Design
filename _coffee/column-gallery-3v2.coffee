document.addEventListener "DOMContentLoaded", ->

  $('.image-click').click ->
    # $('.gallery').removeClass('hide')
    $('.image-click').removeClass('show')
    $('.default-nav').removeClass('active')
  $('.image-wrapper').click (e) ->
    e.stopPropagation()

  $('.gallery .image').click (e) ->
    imageURL = $(this).data('image')
    $image = $('.image-click img')
    $image.attr('src', imageURL)
    height = document.getElementById('actual-image').height
    $image.closest('.image-click').addClass('show')
    $('.default-nav').removeClass('active')

    # $(this).closest('.gallery').addClass('hide')

  window.closeImage = ->
    # $('.gallery').removeClass('hide')
    $('.image-click').removeClass('show')
