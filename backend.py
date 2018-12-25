import json

"""GitHub"""
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

"""Photos"""
def flickrPhotoAppender(title, urlId, urlImage, desc):

    #Formatting TOS-friendly Flickr Link
    FlickrUrl = "https://www.flickr.com/photos/162734979@N02/" + urlId + "/in/album-72157704745702314/"

    #Formatting pythonic dictionary to githubData.json format
    dataToAppend = [{
        "title": title,
        "urlLink": FlickrUrl,
        "urlImage": urlImage,
        "desc": desc
    }]

    # Capturing old data and appending with new data
    with open("static/photoData.json") as dataViewer:
        oldData = json.load(dataViewer)

    newData = dataToAppend + oldData

    with open("static/photoData.json", "w") as writeToFile:
        json.dump(newData, writeToFile)

"""Graphics"""
def flickrGraphicLAppender(title, urlId, urlImage, desc):

    #Formatting TOS-friendly Flickr Link
    FlickrUrl = "https://www.flickr.com/photos/162734979@N02/" + urlId + "/in/album-72157703327998021/"

    #Formatting pythonic dictionary to githubData.json format
    dataToAppend = [{
        "title": title,
        "urlLink": FlickrUrl,
        "urlImage": urlImage,
        "desc": desc
    }]

    # Capturing old data and appending with new data
    with open("static/graphicLData.json") as dataViewer:
        oldData = json.load(dataViewer)

    newData = dataToAppend + oldData

    with open("static/graphicLData.json", "w") as writeToFile:
        json.dump(newData, writeToFile)

def flickrGraphicKAppender(title, urlId, urlImage, desc):

    #Formatting TOS-friendly Flickr Link
    FlickrUrl = "https://www.flickr.com/photos/162734979@N02/" + urlId + "/in/album-72157704794520915/"

    #Formatting pythonic dictionary to githubData.json format
    dataToAppend = [{
        "title": title,
        "urlLink": FlickrUrl,
        "urlImage": urlImage,
        "desc": desc
    }]

    # Capturing old data and appending with new data
    with open("static/graphicKData.json") as dataViewer:
        oldData = json.load(dataViewer)

    newData = dataToAppend + oldData

    with open("static/graphicKData.json", "w") as writeToFile:
        json.dump(newData, writeToFile)

def flickrGraphicMAppender(title, urlId, urlImage, desc):

    #Formatting TOS-friendly Flickr Link
    FlickrUrl = "https://www.flickr.com/photos/162734979@N02/" + urlId + "/in/album-72157704801809274/"

    #Formatting pythonic dictionary to githubData.json format
    dataToAppend = [{
        "title": title,
        "urlLink": FlickrUrl,
        "urlImage": urlImage,
        "desc": desc
    }]

    # Capturing old data and appending with new data
    with open("static/graphicMData.json") as dataViewer:
        oldData = json.load(dataViewer)

    newData = dataToAppend + oldData

    with open("static/graphicMData.json", "w") as writeToFile:
        json.dump(newData, writeToFile)