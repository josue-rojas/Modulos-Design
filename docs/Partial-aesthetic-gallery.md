### About \_includes/aesthetic-gallery

<img src='https://github.com/josuerojasrojas/Modulos-Design/blob/master/docs/Partial-aesthetic-gallery?raw=true'>

This partial is for a gallery of (link)images in <strong>aesthetic layout only</strong>.

In the data file(!TODO LINK ABOUT DATA FILES) it should look and include (assumes you have all other things that aesthetic layout needs):

```YAML
---
  sass:
    - "defaults.sass"
    - "sizes.sass"
    - "mixins.sass"
    - "default-gallery.sass"
  coffee:
    - "main.coffee"
    - "aesthetic.coffee"
  js:
    - "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"
  # ...... include other things that aesthetic layout needs (TODO link aesthetic layout about)
  partials:
    -
      partial-name: "aesthetic-gallery"
      link: "gallery" #link that aesthetic layout looks for
      title: "Gallery" # title that appears on top of box
      images:
        -
          src: '/resources/images/example1.jpg'
          link: 'http://josuerz.xyz'
          text: "Josue's Portfolio" #text when hover over image
        -
          src: '/resources/images/example2.jpg'
          link: 'http://dream-deferred.xyz'
          text: 'A Dream Deferred'
      id: 0
```
