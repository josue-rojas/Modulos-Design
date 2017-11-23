# About this folder:

this folder contains configs for certain things of the page
- To search a partial do ⌘f or open search in your browser and type in 'partial-name: [name of partial]'

## YML Struture/ and Partial imports
YML files is named after a variable in front matter of each page called 'data_file'

- sass is imported from the \_sass folder
- coffee is imported from the \_coffee folder
- js is imported from the resources folder (no need to type resources)
- css is imported from the resources folder
- you need to write all sass, css, coffee, and js files needed for the page, Order matters
- need to write partials in order that they would appear
  - some partials take file locations or data


```YAML
---
  sass:
  # all sass to be imported by page. this is ued to make each page's scss imports
  # some partial should have it's own sass to import make sure to import it to have it's style
  # or import any that overrides
    - "main.sass" # necessary ALWAYS
    - "navbar.sass" # necessary if using default layout
    - "footer.sass" # necessary if using default layout
    - "slideshow.sass"
    - "column-box-2.sass"
    - "map-box.sass"
    - "column-gallery-3.sass"
  css:
  # all css to be imported by page
  # if css is in local then need to specify root for root folder location and then the pathname
  # all pages import bootstrap.css in default layout
    - "root/resources/css/style.css"
  coffee:
  # all coffee to be imported by page
  # some partial may have it's own coffee to import, make sure to import for functionality (this is used when joining the coffee together)
    - "main.coffee" # necessary if using default layout
    - "footer.coffee" # necessary if using default layout
    - "slideshow.coffee"
  js:
  # all javascript to be imported by page (all pages import jquery and bootstrap js in default layout)
    - "js/example.js"
  navbar:
  # this is mandatory for default layout!!!
    brand_name: "Showcase" # name of brand...
    links: #links to be in the navbar
      Title: "/links"
      Example: "/example"
  partials:
  # all partials to be rendered in page
  # IMPORTANT: every partial has an id which is just the position in the list
  # this is used to get any resources that it has from the YML
  # below is th list of partials and it's resources(if you create a new one make sure to update this)
    -
      partial-name: "slideshow"
      # slideshow can have multiple
      # slideshow: imports "slideshow.coffee" "slideshow.sass"
        images: # list of images
          - "example1/test_1.jpg"
          - "example1/test_4.jpg"
        speed: 2000 # speed in milliseconds to change slides
        auto: true # boolean of autostart slideshow
        controls: true # boolean wether to have buttons or not (can only be false if autoplay is true)
        fade: true # boolean to add fade transition effect or not
        id: 0 # partials place in this list, used to load/find it's resources
    -
      partial-name: "column-box-2"
      # imports "column-box-2.sass"
      title: "Title" # title of to be display on box
      column-1: # this contains data for column 1
        text: "hello this is the text for column-1 in this box thingy"
        source: "root/resource/image/1.jpg" # source of image (root needed if local file), can also be url
        link: "google.com" # link for the image when clicked
      column-2: # this contains data for column 2
        text: "hello this is the text for column-2 in this box thingy"
        image:
          source: "root/resource/image/1.jpg"
          link: "google.com"
      id: 1
    -
      partial-name: "map-box"
      # imports "map-box.sass"
      title: "Title"
      map-query: "bronx" #ummm... https://developers.google.com/maps/documentation/embed/start get the query from there.
      contact-lines:
        # contact information line by line
        - "gmail@gmail.com"
        - "123 maple street"
        - "bronx ny, 10467"
      id: 2
    -
      partial-name: "column-gallery-3"
      # imports column-gallery-3.sass
      images:
        -
          source: 'root/resource/image/1.jpg'
          text-overlay: 'some text shown on hover'
      id: 3
```
