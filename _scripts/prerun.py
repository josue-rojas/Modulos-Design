# THINGS TO DO
# make more efficient
# need cleaner to check if constants still exist
# this has to be used after data changes
# -----------------------------------------------------------------
# this script is to join all coffee script files and sass files
# this is to make less request while keeping the files organized, the only downside is that it might take up more space
# for now since github is hosting it doesnt matter

# using python 2.7
# https://stackoverflow.com/questions/1515730/is-there-a-command-like-watch-or-inotifywait-on-the-mac
# only watch -------------
# _data for changes in sources
# _sass for changes in sass files
# _coffee for changes in coffee
import os, yaml, sys, json

# constants folder paths ...
project_root = '/'.join(os.getcwd().split('/')[:-1])
data_folder = project_root + '/_data/'
resource_folder = project_root + '/resources/'
js_folder = resource_folder + 'js/'
coffee_folder = project_root + '/_coffee/'
sass_folder = project_root + '/_sass/'
css_folder = resource_folder + 'css/'
scripts_folder = project_root + '/_scripts/'
constantsJSON = project_root + '/_scripts/constants.json'

# local node modules
cofee = project_root + '/node_modules/.bin/coffee'
uglifyjs = project_root + '/node_modules/.bin/uglifyjs '

# change to root to find stuff
os.chdir(project_root)

# open json file...
with open(constantsJSON) as json_File:
    dependents = json.load(json_File)
def updateConst(newData):
    with open(constantsJSON, 'w') as json_File:
        json.dump(newData, json_File)


# this makes coffee -> js and or sass -> scss
def renderFiles(change, rCoffee=True, rSass=True):
    dataFile = change.split('/')[-1].split('.')[0]
    stream = open(change, "r")
    coffeeList = []
    sassList = []
    for doc in yaml.load_all(stream):
        for key,value in doc.items():
            # coffee stuff
            if rCoffee and key == 'coffee':
                print '\nmaking coffe'
                coffee = ' '.join([coffee_folder + name for name in value])
                print coffee
                coffeeOut = dataFile + '.coffee'
                jsOut = dataFile + '.js'
                os.system('echo "' + coffee + '" | xargs cat > ' + coffeeOut)
                os.system(cofee + ' -o ' + js_folder + ' -c ' + coffeeOut)
                os.system(uglifyjs + js_folder + jsOut + ' -c  --keep-fnames -m -o ' + js_folder + jsOut )
                os.system('rm ' + coffeeOut)
                coffeeList = value
            # sass stuff
            elif rSass and key == 'sass':
                print '\nmaking scss'
                outputName = dataFile + '.scss'
                scssOut = '---\n---\n'+''.join(['@import "'+ sass + '";\n' for sass in value])
                outPut = open(css_folder + outputName, "w")
                outPut.write(scssOut)
                sassList = value
                # os.rename(project_root+'/'+outputName, css_folder+outputName)#this should be one step in open
    return (coffeeList, sassList)


# get change file and its name
change = sys.argv[1]
fileName = change.split('/')[-1].split('.')[0]
# get the type of change (_data, _coffee, or _sass)
folder = change.split('/')[-2]

# if the change was from a data file
# - update cacheCofee
# - update cacheSass
# - make js files
# - make scss file
if folder == '_data':
    renderFiles(change)
    # coffeeList, sassList = renderFiles(change)
    # cleanup should not effect jekyll render cause its not watching this
    # update the constants
    # start with coffee clean
    # print dependents['coffee']
    # for cup in dependents['coffee'].keys():
    #     if cup in coffeeList:
    #         print 'cup is ' + cup

    # print coffeeList
    # print sassList

# elif the change is from coffee folder
# - read constants.json
# - get all who depend on the files (should be a list)
#-  create js file for them (update files)
elif folder == '_coffee':
    coffeeDep = dependents['coffee'].get(fileName, [])
    if len(coffeeDep) == 0:
        dependents['coffee'][fileName] = []
        updateConst(dependents)
        print 'adding coffee to constants.json'
        exit()
    for dep in coffeeDep:
        renderFiles(data_folder + dep, rSass=False)

# finally elif the change is from sass folder
# - read constants.json
# - get all who depend on the files
# - create a scss file for them (update files)
elif folder == '_sass':
    sassDep = dependents['sass'].get(fileName, [])
    if len(sassDep) == 0: # no sass thing......
        dependents['sass'][fileName] = []
        updateConst(dependents)
        print 'adding sass to constants.json'
        exit()
    for dep in sassDep:
        renderFiles(data_folder+ dep, rCoffee=False)


print "\nDone With " + change
