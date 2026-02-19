from flask import Flask, render_template

app = Flask(__name__)

DASHBOARD_URL = "https://public.tableau.com/views/Dashboard_17715013790160/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no"
STORY_URL = "https://public.tableau.com/views/Visualization_17714250009400/Story1?:embed=y&:display_count=yes&:showVizHome=no"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", tableau_url=DASHBOARD_URL)


@app.route("/story")
def story():
    return render_template("story.html", tableau_url=STORY_URL)


if __name__ == "__main__":
    app.run(debug=True)
