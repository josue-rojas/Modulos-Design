# About this folder:

this folder contains configs for certain things of the page
- To search a partial do ⌘f or open search in your browser and type in 'partial-name: [name of partial]'

- you need to write all local css/scss and js files needed for the page
- need to write partials in order that they would appear
  - some partials take file locations or data


## YML Struture/ and Partial imports
YML files should be name the page title (will change this in case title has space remind me if i don't)
```YAML
---
scss:
  # all css to be imported by page. (all pages import bootstrap css in default layout)
  # some partial should have it's own sass to import make sure to import it to have it's style
  # or import any that overrides
  - "css/example.css"
  - "css/slideshow.css"
 js:
  # all javascript to be imported by page (all pages import jquery and bootstrap js in default layout)
  # some partial may have it's own js to import, make sure to import for functionality
  - "js/slideshow.js"
 partials:
  # all partials to be rendered in page
  # IMPORTANT: every partial has an id which is just the position in the list
  # this is used to get any resources that it has from the YML
  # below is th list of partials and it's resources(if you create a new one make sure to update this)
  - 
    partial-name: slideshow 
    # slideshow can have multiple
    # slideshow: imports "js/slideshow.js" "css/slideshow.css" 
      images: # list of images
        - "example1/test_1.jpg"
        - "example1/test_4.jpg"
       speed: 2000 # speed in milliseconds to change slides
       auto: true # boolean of autostart slideshow
       id: 0 # partials place in this list, used to load it's resources
  - 
```
