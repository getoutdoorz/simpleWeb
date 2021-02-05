from flask import Flask, send_file, render_template

DEVELOPMENT_ENV  = True

app = Flask(__name__)

app.static_folder = 'static'

app_data = {
    "name":         "Cade's Starter Template for a Flask Web App",
    "description":  "A basic Flask app using bootstrap for layout",
    "author":       "Cade Curry",
    "html_title":   "Cade's Starter Template for a Flask Web App",
    "project_name": "Outside",
    "keywords":     "flask, webapp, template, basic"
}


@app.route('/')
def index():
    return render_template('index.html', app_data=app_data)


@app.route('/about')
def about():
    return render_template('about.html', app_data=app_data)


@app.route('/mission')
def service():
    return render_template('mission.html', app_data=app_data)


@app.route('/design')
def design():
    return render_template('design.html', app_data=app_data)

# @app.route('/')
# def index():
#     return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=DEVELOPMENT_ENV)
