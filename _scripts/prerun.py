# THINGS TO DO
# ADD JOIN FOR SASS
# this is easier than coffee since you can make a new .scss file and import whatever you are going to use
# -----------------------------------------------------------------
# this script is to join all coffee script files and sass files
# this is to make less request while keeping the files organized

# using python 2.7
# https://stackoverflow.com/questions/1515730/is-there-a-command-like-watch-or-inotifywait-on-the-mac
# only watch -------------
# _data for changes in sources
# _sass for changes in sass files
# resources/coffee for changes in coffee
import os, yaml

# if css convert to sass
# https://www.npmjs.com/package/css-scss (maybe need to write another script using js to run this if i dont find another)

# sassList = []
# jsList = []


# constants folder paths ...
project_root = '/'.join(os.getcwd().split('/')[:-1])
# print os.getcwd()
# exit()
data_folder = project_root + '/_data/'
resource_folder = project_root + '/resources/'
js_folder = resource_folder + '/js/'
coffee_folder = project_root + '/_coffee/'
sass_folder = project_root + '/_sass/'
css_folder = resource_folder + '/css/'

# this file is needed for jekyll to convert coffee -> js
coffeeFiles = ['coffee.coffee']


# change to root to find stuff
os.chdir(project_root)
# print data_folder
# os.chdir(coffee_folder)


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
                    os.rename(project_root+'/'+outputName, js_folder+outputName)
                # sass stuff
                elif key == 'sass':
                    outputName = file.split('.yml')[0] + '.scss'
                    scssOut = '---\n---\n'+''.join(['@import "'+ sass + '";\n' for sass in value])
                    outPut = open(outputName, "w")
                    outPut.write(scssOut)
                    os.rename(project_root+'/'+outputName, css_folder+outputName)
                    # print scssOut
                # elif key == 'sass':
                #     sassList = value
            #     # print k, "->", v
            # print 'sass' , sassList
            # print 'coffee' , ' '.join(coffeeList)
            # print
print "Done With coffee join"
