import json


def jsonAppender(repoName, html, description, timeCreated):

    #Reformatting Date RawData
    timeYear = timeCreated[0:4]
    timeMonth = timeCreated[5:7]
    timeDay = timeCreated[8:10]

    formattedTime = timeMonth + "/" + timeDay + "/" + timeYear

    #Formatting pythonic dictionary to githubData.json format
    dataToAppend = [{
        "name" : repoName,
        "url" : html,
        "description" : description,
        "updated_at" : formattedTime
    }]

    #Capturing old data
    with open("static/githubData.json") as dataViewer:
        oldData = json.load(dataViewer)

    #Checking if data is already present for repo
    for n in oldData:
        #remove old info and bump updated info to top
        if dataToAppend[0]['name'] == n['name']:

            filteredData = [d for d in oldData if d['name'] != n['name']]
            newData = dataToAppend + filteredData

            with open("static/githubData.json", "w") as writeToFile:
                json.dump(newData, writeToFile)

            break
        #add new repo to top
        else:
            newData = dataToAppend + oldData

            with open("static/githubData.json", "w") as writeToFile:
                json.dump(newData, writeToFile)