#!/bin/bash

cd "$(dirname "$0")"

root=$(pwd)
root="${root%/_scripts}"
coffee="$root/_coffee/"
scripts="$root/_scripts"
sass="$root/_sass"
pythonScript="$scripts/prerun.py"
echo "watching " $coffee
echo "and running " $pythonScript

cd $root; jekyll server & cd $scripts;fswatch -o -0 "$coffee" |  xargs -0 -n1 python $pythonScript & cd $scripts;fswatch -o -0 "$sass" |  xargs -0 -n1 python $pythonScript
