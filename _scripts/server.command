#!/bin/bash

cd "$(dirname "$0")"

root=$(pwd)
root="${root%/_scripts}"
coffee="$root/_coffee/"
data="$root/_data/"
scripts="$root/_scripts"
sass="$root/_sass"
pythonScript="$scripts/prerun.py"
echo "watching " $coffee
echo "and running " $pythonScript

# run local npm packages (python uses this)
# alias npm-exec='PATH=$(npm bin):$PATH'
# npm-exec which coffee
# alias

cd $root; jekyll server & cd $scripts; fswatch -0 $coffee $sass $data |  xargs -0 -n1 python $pythonScript
