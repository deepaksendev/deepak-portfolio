from flask import Flask, render_template  # type: ignore[import]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/thosnetv2')
def thosnetv2():
    return render_template('thosnetv2.html')

@app.route('/facedetection')
def facedetection():
    return render_template('facedetection.html')

@app.route('/swadeshi')
def swadeshi():
    return render_template('swadeshi.html')

@app.route('/websuiteai')
def websuiteai():
    return render_template('websuiteai.html')

if __name__ == '__main__':
    app.run(debug=True)