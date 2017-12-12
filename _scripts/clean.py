import os, yaml, sys, json


constantsJSON = os.getcwd() + '/constants.json'
with open(constantsJSON) as json_File:
    dictionaryFile = json.load(json_File)

for key in dictionaryFile:
    values = dictionaryFile[key]
    for otherKey in values:
        print otherKey +"."+ key
