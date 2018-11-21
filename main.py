from flask import Flask, render_template

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

#individual dashboard
#((Maybe research html templates))
@app.route("/dashboard/<medium>")
def dashboardMedium(medium):
    return render_template("dashboardMedium.html", medium=medium)


#run website
if __name__ == "__main__":
    app.run(app.run(host='0.0.0.0')