import json


def jsonAppender(repoName, url, description, timeCreated):

    dataToAppend = [{
        "name" : repoName,
        "url" : url,
        "description" : description,
        "created_at" : timeCreated
    }]

    with open("static/githubData.json") as dataViewer:
        oldData = json.load(dataViewer)

    data = oldData + dataToAppend


    with open("static/githubData.json", "w") as writeToFile:
        json.dump(data, writeToFile)

def githubData():

    with open("static/githubData.json") as dataViewer:
        showcase = json.load(dataViewer)

    return showcase