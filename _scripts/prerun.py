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

# this file is needed for jekyll to convert coffee -> js
# coffeeFiles = ['coffee.coffee']
coffeeFiles = []

todo = sys.argv[1]

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
                if (todo=='all' or todo=='coffee') and key == 'coffee':
                    # join the coffee file needed by the project into 1 then move that in the resources folder
                    coffee = ' '.join([coffee_folder + name for name in (coffeeFiles + value)])
                    outputName = file.split('.yml')[0]
                    os.system('echo "' + coffee + '" | xargs cat > ' + outputName + '.coffee')
                    os.system(' coffee -o ' + js_folder + ' -c ' + outputName+ '.coffee')
                    os.system(' uglifyjs ' + js_folder + outputName+'.js' + ' -c -m -o ' + js_folder + outputName+'.js' )
                    os.system('rm ' + outputName+'.coffee')
                    # os.rename(project_root+'/'+outputName, js_folder+outputName)
                # sass stuff
                elif (todo=='all' or todo=='sass') and key == 'sass':
                    outputName = file.split('.yml')[0] + '.scss'
                    scssOut = '---\n---\n'+''.join(['@import "'+ sass + '";\n' for sass in value])
                    outPut = open(outputName, "w")
                    outPut.write(scssOut)
                    os.rename(project_root+'/'+outputName, css_folder+outputName)

print "Done With script"
