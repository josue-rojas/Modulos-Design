document.addEventListener "DOMContentLoaded", ->
  positions = []
  window.getPositions = ->
    positions = []
    $('.view').each ->
      positions.push($(this).position().top)
    return positions
  getPositions()
  $(window).resize(getPositions)


  scrollTimeOut = null
  window.scrollToPos = (change,currPos, targetPos, down) ->
    if currPos == targetPos
      return
    currPos = currPos+change
    if down
      if currPos > targetPos
        currPos = targetPos
      change = if change > 0 and change < 30 then change+.25 else change
    else
      if currPos < targetPos
        currPos = targetPos
      change = if change < 0 and change > -30 then change-.25 else change
    window.scrollTo(0,currPos)
    scrollTimeOut = setTimeout(scrollToPos, 1, change, currPos, targetPos, down)

  $(window).keydown (e)->
    currPos = $(this).scrollTop()
    if e.which == 38
      clearTimeout(scrollTimeOut)
      targetPos = positions.filter (element)->
        return element < currPos
      targetPos = if targetPos[targetPos.length-1] then targetPos[targetPos.length-1] else positions[0]
      scrollToPos(change=-.50, currPos, targetPos, false)
    else if e.which == 40
      clearTimeout(scrollTimeOut)
      targetPos = positions.find (element)->
        return element > currPos
      targetPos = if targetPos then targetPos else positions[positions.length-1]
      scrollToPos(change=.50, currPos, targetPos, true)

    # scrollToPos(1, $(this).scrollTop(), positions[1])
  # lastScrollTop = 0;
  # $(window).scroll (event)->
  #   currPos = $(this).scrollTop()
  #   if currPos > lastScrollTop
  #     scrollToPos(change=1, currPos, positions[1])
  #   else
  #     return
  #     scrollToPos(change=-1, currPos, positions[0])
  #   lastScrollTop = currPos
