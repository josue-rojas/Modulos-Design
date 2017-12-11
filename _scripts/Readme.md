#### About the \_scripts files

- prerun.py
  > python file compiles coffee to js. it knows the files it needs to compile from the data files. it will get all the coffeescript from each data file it needs and puts it into one file, then converts it to js.

  > It also does a similar thing to sass files. It gets all the files it needs from the data file and makes a new scss file that imports the needed files.

- server.command
  > runs jekyll server and at the same time runs fswatch which watches for changges in \_coffee, \_sass, and \_data folder to run the prerun.py script.

- export.py
  >[README](https://github.com/josuerojasrojas/export-jekyll)

(!TODO split this file into different docs and move it to the docs folder)
