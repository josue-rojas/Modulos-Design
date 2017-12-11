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

### [Read more on how tos, layouts, pages, partials, and other things about this project here](https://github.com/josuerojasrojas/Modulos-Design/tree/master/docs)


### Some stuff used
- [To run scripts when change is made locally](https://github.com/emcrisostomo/fswatch)
- [Script to join coffee](https://stackoverflow.com/questions/4575260/join-multiple-coffeescript-files-into-one-file-multiple-subdirectories)
- [Run local node packages in terminal](https://stackoverflow.com/questions/9679932/how-to-use-package-installed-locally-in-node-modules)
- [HTML compress using liquid templating](https://github.com/penibelst/jekyll-compress-html)
- [To-do-Show i use it when random thoughts appear of to-dos](https://atom.io/packages/todo-show)
