### Creating a new page

All pages must go in pages folder in a folder that makes sense for it.....

First and really important is the [Front Matter](https://jekyllrb.com/docs/frontmatter/). Each page must have

- layout - which says which layout from \_layout folder to use
- title - just the title of the page as it would appear on html (!NOTE MIGHT MOVE THIS FILE)
- permalink - the route that jekyll will use in this repo (export the page might change (!NOTE ADD LINK TO EXPORT README HERE))
- data_file - the file in \_data folder to get all information for the page (!NOTE ADD LINK TO DATA FILES HERE)
- analytics - boolean that says to use analytics or not. This can be false if exporting to be use on some other domain (basically anything that will not use modulos-design.com)
- favicon - boolean to use favicons or not (!NOTE CHANGE THIS WHEN ADD OPTION TO USE OWN FAVICON)

After the front matter is the html code or partials.
if using partials from data file then use the partials partial.

an example of this
  ```html
  ---
  layout: default
  title: Example 1
  permalink: /example1
  data_file: example1
  analytics: true
  favicon: true
  ---
  {% include partials.html %}
  ```

  After you created a page you can make a data file (if you haven't done so) or make coffee, sass, or just create something new.
  (!NOTE LINK TO COFFEE, SASS, NEW PARTIALS, AND DATA FILES HERE)
