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
