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

#photos
@app.route("/dashboard/photos")
def dashboardPhotos():
    return render_template("photos.html")

##webhook POST url
@app.route("/webhookpayload/", methods=['POST'])
def webhook():
    req_data = request.get_json()

    name = req_data['repository']['name']
    url = req_data['repository']['url']
    desc = req_data['repository']['description']
    created = req_data['repository']['created_at']

    backend.jsonAppender(name, url, desc, created)

    return '''Successfully submitted into database'''

#run website
app.run(host="0.0.0.0", port='80')