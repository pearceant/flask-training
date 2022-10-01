#app = Flask(__name__)

#@app.route('/')
def home_fun():
    return render_template("home.html")

@app.route('/contact_url')
def contact_fun():
    return render_template("contact.html")

@app.route('/education_url')
def education_fun():
    return render_template("education.html")

@app.route('/workex_url')
def workex_fun():
    return render_template("workex.html")

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8000)        