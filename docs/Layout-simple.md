### About \_layouts/simple

(!TODO ADD A PREVIEW IMAGE HERE)

__This layout does not use partials__

It is meant to resemble a business card in the way that it only displays minimal but important information.

The data file example and explanation:
```YAML
---
  sass:
    - "defaults"
    - "sizes.sass"
    - "mixins.sass"
    - "simple.sass"  
  coffee:
    - "simple.coffee" 
  css:
     # This is the font it use, it can be replace if you override it in a new sass file after simple.sass
    - "https://fonts.googleapis.com/css?family=Barlow+Semi+Condensed:100,200,400"
  js:
    - "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"
  background-image: '/resources/simple/space.jpg'
  card:
    # use for 'profile image', can be a link or local image
    image: 'https://avatars0.githubusercontent.com/u/10749061?v=4'
    name: 'Josue Rojas'
    description: 'Software Developer / Wonderer'
    # social links supported [github, linkedin, facebook, and instagram] cause only have those images
    social-links:
      Github: "https://github.com/josuerojasrojas"
      LinkedIn: "https://www.linkedin.com/in/josuerojasz/"
      Facebook: "https://www.facebook.com/withcheesepls"
      Instagram: "https://www.instagram.com/withcheesepls/"
    # links are just extra links that are hidden in a sort of menu
    links:
      -
        name: 'Projects'
        link: '/projects'
      -
        name: 'Resume'
        link: 'https://goo.gl/yFs4U6'
  # footer text
  footer:
    text: 'Developed by © <a href="http://modulos-design.com">Modulos-Design</a>'
```
