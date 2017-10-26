---
layout: default
permalink: /readme
title: readme
---

# Showcase
A sample of dummy or real sites that will be used to show our skills at web development

#### INIT
First install jekyll in your computer to run https://jekyllrb.com/docs/quickstart/

NEED:
- [Jekyll](https://jekyllrb.com/docs/installation/)
- [Fswatch](https://github.com/emcrisostomo/fswatch)
- python 2.7

#### Start
To run with scripts
(the scripts watch \_coffee, \_sass, and \_data to join files)
- clone
- MUST HAVE FSWATCH AND PYTHON 2.7
- go to \_scripts and open server.command
To run just
- clone this repo
- open terminal
- cd into this directory
- and type 'jekyll server'
- finally in the browser go to http://localhost:4000/


### Folder structures

### \_data
> [Readme](https://github.com/josuerojasrojas/Showcase/blob/master/_data/Readme.md)

### \_includes
> folder that includes partials (ie. footer, header, nav, etc.)

### \_layouts
> folder contains layouts for the pages

### \_sass
> folder contains sass files for the pages each page should have it's own sass file and each partial should also have it's own. In the resource folder the there should be different scss that imports necessary stylesheets for their respective page.

#### resources
> folder should contain images , js , css or other resources for the page.

## NOTE: for each page it should have it's own folder with it's name of the site.

More rules to follow as more sites get created.

### Some stuff used
- [To run scripts when change is made locally](https://github.com/emcrisostomo/fswatch)
- [Script to join coffee](https://stackoverflow.com/questions/4575260/join-multiple-coffeescript-files-into-one-file-multiple-subdirectories)
