# THINGS TO DO
# add options to run one thing only saving time on not doing other things
# -----------------------------------------------------------------
# this script is to join all coffee script files and sass files
# this is to make less request while keeping the files organized

# using python 2.7
# https://stackoverflow.com/questions/1515730/is-there-a-command-like-watch-or-inotifywait-on-the-mac
# only watch -------------
# _data for changes in sources
# _sass for changes in sass files
# _coffee for changes in coffee
import os, yaml


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
                if key == 'coffee':
                    # join the coffee file needed by the project into 1 then move that in the resources folder
                    coffee = ' '.join([coffee_folder + name for name in (coffeeFiles + value)])
                    outputName = file.split('.yml')[0] + '.coffee'
                    os.system('echo "' + coffee + '" | xargs cat > ' + outputName)
                    os.system(' coffee -o ' + js_folder + ' -c ' + outputName)
                    # print js_folder+file.split('.yml')[0]+'.js'
                    os.system(' uglifyjs ' + js_folder+file.split('.yml')[0]+'.js' + ' -c -m -o ' +js_folder+file.split('.yml')[0]+'.js' )
                    os.system('rm ' + outputName)
                    # os.rename(project_root+'/'+outputName, js_folder+outputName)
                # sass stuff
                elif key == 'sass':
                    outputName = file.split('.yml')[0] + '.scss'
                    scssOut = '---\n---\n'+''.join(['@import "'+ sass + '";\n' for sass in value])
                    outPut = open(outputName, "w")
                    outPut.write(scssOut)
                    os.rename(project_root+'/'+outputName, css_folder+outputName)

print "Done With coffee,sass join"
