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
        "created_at" : formattedTime
    }]

    #Capturing old data
    with open("static/githubData.json") as dataViewer:
        oldData = json.load(dataViewer)

    #Checking if data is already present for repo
    for n in oldData:
        if dataToAppend[0]['name'] == n['name']:
            break
        else:
            #Appending to database
            data = oldData + dataToAppend

            with open("static/githubData.json", "w") as writeToFile:
                json.dump(data, writeToFile)