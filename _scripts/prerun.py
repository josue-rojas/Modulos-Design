# THINGS TO DO
# make more efficient
# -----------------------------------------------------------------
# this script is to join all coffee script files and sass files
# this is to make less request while keeping the files organized

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


# local noe modules
cofee = project_root + '/node_modules/.bin/coffee'
uglifyjs = project_root + '/node_modules/.bin/uglifyjs '


# this is assuming all are file changes do are not in another deeper folder
todo = sys.argv[1].split('/')[-2]
print "todo: "  + sys.argv[1]

# change to root to find stuff
os.chdir(project_root)

# check wether file is from _coffee, _sass, or _data folder
def checkFile(filePath):
    return filePath.split('/')[-2]

# this makes coffee -> js and or sass -> scss
def renderFiles(change, rCoffee=True, rSass=True):
    dataFile = change.split('/')[-1].split('.')[0]
    stream = open(change, "r")
    for doc in yaml.load_all(stream):
        for key,value in doc.items():
            # coffee stuff
            if key == 'coffee' and rCoffee:
                print 'making coffe\n'
                coffee = ' '.join([coffee_folder + name for name in value])
                print coffee
                coffeeOut = dataFile + '.coffee'
                jsOut = dataFile + '.js'
                os.system('echo "' + coffee + '" | xargs cat > ' + coffeeOut)
                os.system(cofee + ' -o ' + js_folder + ' -c ' + coffeeOut)
                os.system(uglifyjs + js_folder + jsOut + ' -c  --keep-fnames -m -o ' + js_folder + jsOut )
                os.system('rm ' + coffeeOut)
            # sass stuff
            elif key == 'sass' and rSass:
                print 'making scss\n'
                outputName = dataFile + '.scss'
                scssOut = '---\n---\n'+''.join(['@import "'+ sass + '";\n' for sass in value])
                outPut = open(css_folder + outputName, "w")
                outPut.write(scssOut)
                # os.rename(project_root+'/'+outputName, css_folder+outputName)#this should be one step in open


# get change file and its name
change = sys.argv[1]
fileName = change.split('/')[-1].split('.')[0]
# get the type of change (_data, _coffee, or _sass)
folder = checkFile(change)

# if the change was from a data file
# - update cacheCofee
# - update cacheSass
# - make js files
# - make scss file
if folder == '_data':
    renderFiles(change)

# elif the change is from coffee folder
# - read constants.json
# - get all who depend on the files (should be a list)
#-  create js file for them (update files)
elif folder == '_coffee':
    with open(constantsJSON) as json_data:
        dependents = json.load(json_data)['coffee'][fileName]
        for dep in dependents:
            renderFiles(data_folder+ dep, rSass=False)

# finally elif the change is from sass folder
# - read constants.json
# - get all who depend on the files
# - create a scss file for them (update files)
elif folder == '_sass':
    with open(constantsJSON) as json_data:
        dependents = json.load(json_data)['sass'][fileName]
        for dep in dependents:
            renderFiles(data_folder+ dep, rCoffee=False)


exit()

# def makeSCSS(ymlPath):


# TOO many for loop
# for file in os.listdir('_data'):
#     if file.endswith(".yml"):
#         yml = os.path.join('_data', file)
#         stream = open(yml, "r")
#         for doc in yaml.load_all(stream):
#             for key,value in doc.items():
#                 # coffee stuff
#                 if (todo=='_data' or todo=='_coffee') and key == 'coffee':
#                     # join the coffee file needed by the project into 1 then move that in the resources folder
#                     coffee = ' '.join([coffee_folder + name for name in value])
#                     coffeeOut = file.split('.yml')[0]+ '.coffee'
#                     jsOut = file.split('.yml')[0] + '.js'
#                     os.system('echo "' + coffee + '" | xargs cat > ' + coffeeOut)
#                     os.system(cofee + ' -o ' + js_folder + ' -c ' + coffeeOut)
#                     os.system(uglifyjs + js_folder + jsOut + ' -c  --keep-fnames -m -o ' + js_folder + jsOut )
#                     os.system('rm ' + coffeeOut)
#                     # os.rename(project_root+'/'+outputName, js_folder+outputName)
#                 # sass stuff
#                 elif (todo=='_data' or todo=='_sass') and key == 'sass':
#                     outputName = file.split('.yml')[0] + '.scss'
#                     scssOut = '---\n---\n'+''.join(['@import "'+ sass + '";\n' for sass in value])
#                     outPut = open(outputName, "w")
#                     outPut.write(scssOut)
#                     os.rename(project_root+'/'+outputName, css_folder+outputName)

print "Done With script"
