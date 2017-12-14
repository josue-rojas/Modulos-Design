### About \_includes/default-navbar

This is a very basic navbar.

It is only used on layouts that use partials and do no have a navbar. For example default or contentonly.

In the data file(!TODO LINK ABOUT DATA FILES) it should look include:

```YAML
---
  sass:
    - "defaults.sass"
    - "sizes.sass"
    - "mixins.sass"
    - "default-navbar.sass"
  coffee:
    - "main.coffee"
    - "default-navbar.coffee"
  js:
    - "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"
  partials:
    -
      partial-name: "default-navbar"
      # banner is optional without this it will just show the navbar
      banner:
        # background is optional for the banner but it will show a color (which can be overrident of course)
        background-image: '/resources/example1/test_1.jpg'
        text: 'This is some text on the banner'
      title: 'Josue Rojas
      title-link: '#'
      sub-title: 'Conquerer of Worlds'
      # active link is to set which page is presented 
      active-link: 'other'
      # links are yout own links and titles
      links:
        -
          title: 'hello'
          link: '#hello'
        -
          title: 'other'
          link: '#other'
        -
          title: 'home'
          link: '#home'
      id: 0
```
