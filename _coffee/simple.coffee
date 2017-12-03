document.addEventListener "DOMContentLoaded", ->
  $('.dropdown').click (e)->
    $dropdown = $(e.target).closest('.dropdown')
    if $dropdown.hasClass('active')
      $dropdown.removeClass('active')
      $dropdown.closest('.link-list-wrapper').find('.links-list').removeClass('active')
    else
      $dropdown.addClass('active')
      $dropdown.closest('.link-list-wrapper').find('.links-list').addClass('active')
