# Modulos-Design

Sets of moodulos that enables us to make sites faster by reusing code.

#### INIT/NEED:
- [Jekyll](https://jekyllrb.com/docs/installation/)
- [Fswatch](https://github.com/emcrisostomo/fswatch)
- [PYAML](https://github.com/yaml/pyyaml)
- python 2.7
- Node Packages (install using 'npm install')
  - [Coffee npm](https://www.npmjs.com/package/coffee-script)
  - [uglifyjs npm](https://www.npmjs.com/package/uglify-js)
- (only tested in mac)

#### Start

```bash
cd some/folder/projects
# clone if you have not done so
git clone git@github.com:josuerojasrojas/Modulos-Design.git

# To run with scripts
# (the scripts watch \_coffee, \_sass, and \_data to join files)
cd Modulos-Design
# install node packages
npm install
npm start

# To run just without scripts
# _Note: this will not make new coffee or scss files in resources folder (this is regular jekyll)_
# jekyll server #instead of npm start

open http://localhost:4000
```

### Folder structures

- \_coffee
> folder that contains all coffee file for the partials and stuff
> [Readme](https://github.com/josuerojasrojas/Showcase/blob/master/_coffee/Readme.md)

- \_data
> this folder contains all data on how each page is gonna render
> [Readme](https://github.com/josuerojasrojas/Showcase/blob/master/_data/Readme.md)

- \_includes
> folder that includes partials (ie. footer, header, nav, etc.)

- \_layouts
> folder contains layouts for the pages

- \_sass
> folder contains sass files for the pages each page should have it's own sass file and each partial should also have it's own. In the resource folder the there should be different scss that imports necessary stylesheets for their respective page.
> [Readme](https://github.com/josuerojasrojas/Showcase/blob/master/_sass/Readme.md)


- \_scripts
> folder contains scripts. right now it only has script to watch and render coffee and sass files from multiple ones.
> [Readme](https://github.com/josuerojasrojas/Showcase/blob/master/_scripts/Readme.md)


- pages
> folder contains all the pages in their respective folders

- resources
> folder should contain images , js , css or other resources for the page.


### Some stuff used
- [To run scripts when change is made locally](https://github.com/emcrisostomo/fswatch)
- [Script to join coffee](https://stackoverflow.com/questions/4575260/join-multiple-coffeescript-files-into-one-file-multiple-subdirectories)
- [Run local node packages in terminal](https://stackoverflow.com/questions/9679932/how-to-use-package-installed-locally-in-node-modules)
