### About \_includes/footer

This is a very basic footer

It is only used on layouts that depend on partials. For instance the default or contentonly layouts.

In the data file(!TODO LINK ABOUT DATA FILES) it should look and include:
(Also this is usually the last partial)

```YAML
---
  sass:
    - "defaults.sass"
    - "sizes.sass"
    - "mixins.sass"
    - "footer.sass"
  coffee:
    - "main.coffee"
    - "footer.coffee"
  js:
    - "https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"
  partials:
    -
      partial-name: 'footer'
      social:
        # all social supporter are 'Facebook', 'Instagram', 'WhatsApp', 'Twitter', 'LinkedIn'
        Facebook: 'https://www.facebook.com/habty.bayssa'
        Instagram: 'https://www.instagram.com/yegta1/'
        WhatsApp: 'https://api.whatsapp.com/send?phone=13478397738'
        Twitter: 'https://twitter.com/hg_gutta'
      # main-text will appear bigger than sub-text (unless overriden)
      main-text: 'Yegeta Barya Habtamu Ministry © 2017'
      # sub-text will appear smaller than main-text (unless overriden)
      sub-text: '<a href="http://modulos-design.com">Developed by Modulos-Design</a>'
      id: 0

```
