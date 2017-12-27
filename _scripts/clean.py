import os, sys, json, copy

project_root = '/'.join(os.getcwd().split('/')[:-1])
constantsJSON = project_root + '/_scripts/constants.json'

with open(constantsJSON) as json_File:
    dictionaryFile = json.load(json_File)
    cloneDict = copy.deepcopy(dictionaryFile)

for key in dictionaryFile:
    values =  dictionaryFile[key]
    for otherKey in values:
        datavalue = values[otherKey]
        if not os.path.isfile(project_root + '/_'+ key +'/' + otherKey +"."+ key):
            cloneDict[key].pop(otherKey)
            datavalue = []
        pop = 0
        for i in range(0, len(datavalue)):
            if not os.path.isfile(project_root + '/_data/' + datavalue[i]):
                cloneDict[key][otherKey].pop(i - pop)
                pop += 1
                os.system('rm ' + project_root + '/resources/js/' + datavalue[i][ :-4] + ".js")
                os.system('rm ' + project_root + '/resources/css/' + datavalue[i][ :-4] + ".css")



with open(constantsJSON, 'w') as json_File:
    json.dump(cloneDict, json_File, indent=4,sort_keys=True)
