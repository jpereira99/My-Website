from flask import Flask, render_template, request
import backend

app = Flask(__name__)

#home page
@app.route("/")
def home():
    return render_template("home.html")

#about page
@app.route("/about/")
def about():
    return render_template("about.html")

#portfolio dashboard
@app.route("/dashboard/")
def dashboard():
    return render_template("dashboard.html")


##individual dashboards

#software
@app.route("/dashboard/software")
def dashboardSoftware():

    return render_template("software.html")

#graphics
@app.route("/dashboard/graphics")
def dashboardGraphics():
    return render_template("graphics.html")
#graphics - logos
@app.route("/dashboard/graphics/logos")
def graphicLogo():
    return render_template("graphicsL.html")
#graphics - soccer kits
@app.route("/dashboard/graphics/kits")
def graphicKits():
    return render_template("graphicsK.html")
#graphics - misc
@app.route("/dashboard/graphics/misc")
def graphicMisc():
    return render_template("graphicsM.html")

#photos
@app.route("/dashboard/photos")
def dashboardPhotos():
    return render_template("photos.html")

##GitHub webhook POST url
@app.route("/webhookpayload/", methods=['POST'])
def webhook():
    req_data = request.get_json()

    name = req_data['repository']['name']
    url = req_data['repository']['html_url']
    desc = req_data['repository']['description']
    time = req_data['repository']['updated_at']

    backend.jsonAppender(name, url, desc, time)

    return '''Successfully submitted into database'''

##Flickr photo webhook POST url
@app.route("/webhookpayload/photo", methods=['POST'])
def webhook2():
    req_data = request.get_json()

    name = req_data['title']
    urlId = req_data['id']
    image = req_data['url_o']
    desc = req_data['description']['_content']

    backend.flickrPhotoAppender(name, urlId, image, desc)

    return '''Successfully submitted into database'''

##Flickr graphicL webhook POST url
@app.route("/webhookpayload/graphicsL", methods=['POST'])
def webhook3():
    req_data = request.get_json()

    name = req_data['title']
    urlId = req_data['id']
    image = req_data['url_o']
    desc = req_data['description']['_content']

    backend.flickrGraphicLAppender(name, urlId, image, desc)

    return '''Successfully submitted into database'''
##Flickr graphicK webhook POST url
@app.route("/webhookpayload/graphicsK", methods=['POST'])
def webhook4():
    req_data = request.get_json()

    name = req_data['title']
    urlId = req_data['id']
    image = req_data['url_l']
    desc = req_data['description']['_content']

    backend.flickrGraphicKAppender(name, urlId, image, desc)

    return '''Successfully submitted into database'''
##Flickr graphicM webhook POST url
@app.route("/webhookpayload/graphicsM", methods=['POST'])
def webhook5():
    req_data = request.get_json()

    name = req_data['title']
    urlId = req_data['id']
    image = req_data['url_o']
    desc = req_data['description']['_content']

    backend.flickrGraphicMAppender(name, urlId, image, desc)

    return '''Successfully submitted into database'''

#run website
app.run(host='0.0.0.0', port='80')
