#!/bin/bash

# Colors
# http://wiki.bash-hackers.org/snipplets/add_color_to_your_scripts
ESC_SEQ="\x1b["
COL_RESET=$ESC_SEQ"39;49;00m"
COL_RED=$ESC_SEQ"31;01m"
COL_GREEN=$ESC_SEQ"32;01m"
COL_YELLOW=$ESC_SEQ"33;01m"
COL_BLUE=$ESC_SEQ"34;01m"
COL_MAGENTA=$ESC_SEQ"35;01m"
COL_CYAN=$ESC_SEQ"36;01m"

cd "$(dirname "$0")"

root=$(pwd)
root="${root%/_scripts}"
coffee="$root/_coffee/"
data="$root/_data/"
scripts="$root/_scripts"
sass="$root/_sass"
pythonScript="$scripts/prerun.py"

echo -e  $COL_RED"Watching:"$COL_RESET
echo -e  $COL_YELLOW$coffee$COL_RESET
echo -e  $COL_YELLOW$sass$COL_RESET
echo -e  $COL_YELLOW$data$COL_RESET
echo


cd $root; jekyll server & cd $scripts; fswatch -0 $coffee $sass $data |  xargs -0 -n1 python $pythonScript
