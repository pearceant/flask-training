from flask import Flask,render_template,redirect,url_for,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydata.db'
db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    department = db.relationship('Department' ,backref='all_departments')

class Department(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    company = db.Column(db.ForeignKey('company.id'))
    employee = db.relationship('Employee' ,backref='all_employees')

class Employee(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    gender = db.Column(db.String)
    email = db.Column(db.String)
    mob = db.Column(db.String) 
    department = db.Column(db.ForeignKey('department.id'))
    dependent = db.relationship('Dependent' ,backref='all_dependents')

class Dependent(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    relation = db.Column(db.String)
    employee = db.Column(db.ForeignKey('employee.id'))
# DB execution
#db.create_all()
#c1 = Company(id=1,name='Microsoft',address='California')
#c2 = Company(id=2,name='Apple',address='NY')
#c3 = Company(id=3,name='Google',address='New Jersey')
#c4 = Company(id=4,name='Microsoft',address='Texas')
#c5 = Company(id=5,name='Yahoo',address='California')
#db.session.add(c1)
#db.session.add(c2)
#db.session.add(c3)
#db.session.add(c4)
#db.session.add(c5)
#db.session.commit()
#d1 = Department(id=1,name='HR',description='Hiring & Management',company=1)
#d2 = Department(id=2,name='Sales',description='Lead conversion',company=3)
#d3 = Department(id=3,name='Tech',description='Building',company=3)
#db.session.add(d1)
#db.session.add(d2)
#db.session.add(d3)
#db.session.commit()
#e1 = Employee(id=1,name='Harsh' ,gender='M' ,email='xyz@demo.com', mob='998899' ,department=2)
#e2 = Employee(id=2,name='Joy' ,gender='F' ,email='joy@demo.com', mob='997799' ,department=1)
#db.session.add(e1)
#db.session.add(e2)
#db.session.commit()
#dd1 = Dependent(id=1,name='Richard',relation='Brother')
#dd2 = Dependent(id=2,name='Mark',relation='Son')
#db.session.add(dd1)
#db.session.add(dd2)
#db.session.commit()



@app.route('/',methods=['GET','POST'])
def home_fun():
    if request.method == 'POST' and request.form.get('action') == 'Create':
        id = int(request.form.get('id'))
        name = request.form.get('name')
        address = request.form.get('address')
        c_new = Company(id=id,name=name,address=address)
        db.session.add(c_new)
        db.session.commit()
        return redirect(url_for("home_fun"))


    if request.method == 'POST' and request.form.get('action') == 'Search':
        search_query = request.form.get('location')
        data_to_show = Company.query.filter_by(address=search_query)
    else:
        data_to_show = Company.query.all()
    return render_template("home.html",list_of_data=data_to_show)

@app.route('/company/<int:id>')
def company_fun(id):
    company_object = Company.query.get(id)
    return render_template("company.html",data=company_object)    

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


