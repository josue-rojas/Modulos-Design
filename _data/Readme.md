# About this folder:

this folder contains configs for certain things of the page
- To search a partial do ⌘f or open search in your browser and type in 'partial-name: [name of partial]'

- you need to write all sass, css, coffee, and js files needed for the page, Order matters
- need to write partials in order that they would appear
  - some partials take file locations or data


## YML Struture/ and Partial imports
YML files should be name the page title (will change this in case title has space remind me if i don't)
```YAML
---
  sass:
  # all sass to be imported by page. this is ued to make each page's scss imports
  # some partial should have it's own sass to import make sure to import it to have it's style
  # or import any that overrides
    - "main.sass" # necessary ALWAYS
    - "footer.sass" # necessary if using default layout
    - "slideshow.sass"
  css:
  # all css to be imported by page
  # all pages import bootstrap.css in default layout
    - "/navbar.css" # necessary if using default layout
  coffee:
  # all coffee to be imported by page
  # some partial may have it's own coffee to import, make sure to import for functionality (this is used when joining the coffee together)
    - "main.coffee" # necessary if using default layout
    - "footer.coffee" # necessary if using default layout
    - "slideshow.coffee"
  js:
  # all javascript to be imported by page (all pages import jquery and bootstrap js in default layout)
    - "js/example.js"
 partials:
  # all partials to be rendered in page
  # IMPORTANT: every partial has an id which is just the position in the list
  # this is used to get any resources that it has from the YML
  # below is th list of partials and it's resources(if you create a new one make sure to update this)
    -
      partial-name: slideshow
      # slideshow can have multiple
      # slideshow: imports "slideshow.coffee" "css/slideshow.css"
        images: # list of images
          - "example1/test_1.jpg"
          - "example1/test_4.jpg"
        speed: 2000 # speed in milliseconds to change slides
        auto: true # boolean of autostart slideshow
        controls: true #boolean wether to have buttons or not (can only be false if autoplay is true)
        id: 0 # partials place in this list, used to load/find it's resources
    -
```
