# About this folder:

this folder contains configs for certain things of the page

- you need to write all local css/scss and js files needed for the page
- need to write partials in order that they would appear
  - some partials take file locations or data

### scss
> include all css/scss files to be included

### js
> include all js files to be included

### Partials
> Include all partials to be rendered
> Important: every partial has an id which is just and position in the list. This is used to get any resources that it has

- slideshow
 - images: (Necessary) list of images locations
 - Options:
  - speed: is speed (milliseconds) at which slide changes, default is 3000
  - auto: boolean autostart, default is true
 - check out example1.yml
