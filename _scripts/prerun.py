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
import os, yaml, sys


# constants folder paths ...
project_root = '/'.join(os.getcwd().split('/')[:-1])
data_folder = project_root + '/_data/'
resource_folder = project_root + '/resources/'
js_folder = resource_folder + 'js/'
coffee_folder = project_root + '/_coffee/'
sass_folder = project_root + '/_sass/'
css_folder = resource_folder + 'css/'
node_modules = project_root + '/node_modules/.bin/'
cofee = node_modules + 'coffee'
uglifyjs = node_modules + 'uglifyjs '


# this file is needed for jekyll to convert coffee -> js
# coffeeFiles = ['coffee.coffee']
coffeeFiles = []

# this is assuming all are file changes do are not in another deeper folder
todo = sys.argv[1].split('/')[-2]

# change to root to find stuff
os.chdir(project_root)

# TOO many for loop
for file in os.listdir('_data'):
    if file.endswith(".yml"):
        yml = os.path.join('_data', file)
        stream = open(yml, "r")
        for doc in yaml.load_all(stream):
            for key,value in doc.items():
                # coffee stuff
                if (todo=='_data' or todo=='_coffee') and key == 'coffee':
                    # join the coffee file needed by the project into 1 then move that in the resources folder
                    coffee = ' '.join([coffee_folder + name for name in (coffeeFiles + value)])
                    coffeeOut = file.split('.yml')[0]+ '.coffee'
                    jsOut = file.split('.yml')[0] + '.js'
                    os.system('echo "' + coffee + '" | xargs cat > ' + coffeeOut)
                    os.system(cofee + ' -o ' + js_folder + ' -c ' + coffeeOut)
                    os.system(uglifyjs + js_folder + jsOut + ' -c  --keep-fnames -m -o ' + js_folder + jsOut )
                    os.system('rm ' + coffeeOut)
                    # os.rename(project_root+'/'+outputName, js_folder+outputName)
                # sass stuff
                elif (todo=='_data' or todo=='_sass') and key == 'sass':
                    outputName = file.split('.yml')[0] + '.scss'
                    scssOut = '---\n---\n'+''.join(['@import "'+ sass + '";\n' for sass in value])
                    outPut = open(outputName, "w")
                    outPut.write(scssOut)
                    os.rename(project_root+'/'+outputName, css_folder+outputName)

print "Done With script"
