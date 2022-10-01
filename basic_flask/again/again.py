from flask import Flask, render_template, redirect,url_for , request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///group.db'
db = SQLAlchemy(app)

class Courses(db.Model):   
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    roomnub = db.Column(db.String)
    semesters = db.relationship('Semesters',backref='all_semesters')

class Semesters(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    period = db.Column(db.String)
    courses = db.Column(db.ForeignKey('courses.id'))
    students = db.relationship('Students',backref='all_students')

class Students(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    firstname = db.Column(db.String)
    lastname = db.Column(db.String)
    address = db.Column(db.String)
    semesters = db.Column(db.ForeignKey('semesters.id'))

@app.route('/',methods=['GET','POST'])
def home_fun():
    if request.method == 'POST' and request.form.get('action') == 'Create':
        id = int(request.form.get('id'))
        name = request.form.get('name')
        roomnub = request.form.get('roomnub')
        c_new = Courses(id=id,name=name,roomnub=roomnub)
        db.session.add(c_new)
        db.session.commit()
        return redirect(url_for("home_fun"))


    if request.method == 'POST' and request.form.get('actions') == 'Search':
        search_query = request.form.get('name')
        data_to_show = Courses.query.filter_by(name=search_query)
    else:
        data_to_show = Courses.query.all()
    return render_template("home.html",list_of_data=data_to_show)

@app.route('/company/<int:id>')
def courses_fun(id):
    company_object = Courses.query.get(id)
    return render_template("comany.html",data=company_object) 



if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=8000) 






    
#db.create_all()
#cs1 = Courses(id=1, name='Chemistry', roomnub='Room 205')
#cs2 = Courses(id=2, name='English', roomnub='Room 109')
#cs3 = Courses(id=3, name='History', roomnub='Room 382')
#cs4 = Courses(id=4, name='Physics', roomnub='Room 441')
#cs5 = Courses(id=5, name='Maths', roomnub='Room 212')

#db.session.add(cs1)
#db.session.add(cs2)
#db.session.add(cs3)
#db.session.add(cs4)
#db.session.add(cs5)
#db.session.commit()

#sm1 = Semesters(id=1, period='3 months', courses=1 )
#sm2 = Semesters(id=2, period='2 months', courses=2 )
#sm3 = Semesters(id=3, period='1 months', courses=3 )
#sm4 = Semesters(id=4, period='5 months', courses=4 )
#sm5 = Semesters(id=5, period='4 months', courses=5 )

#db.session.add(sm1)
#db.session.add(sm2)
#db.session.add(sm3)
#db.session.add(sm4)
#db.session.add(sm5)
#db.session.commit()

#st1 = Students(id=1, firstname='Lisa', lastname='Moore', address='London', semesters= 1)
#st2 = Students(id=2, firstname='Mark', lastname='Andrews', address='Birmingham', semesters= 2)
#st3 = Students(id=3, firstname='William', lastname='Thomas', address='Bournmouth', semesters= 3)
#st4 = Students(id=4, firstname='Liam', lastname='Richards', address='Wigan', semesters= 4)
#st5 = Students(id=5, firstname='Martin', lastname='Scotts', address='Leeds', semesters= 5)
#st6 = Students(id=6, firstname='Melisa', lastname='Smith', address='Liverpool', semesters= 1)
#st7 = Students(id=7, firstname='Lee', lastname='Freeds', address='Newcastle', semesters= 2)

#db.session.add(st1)
#db.session.add(st2)
#db.session.add(st3)
#db.session.add(st4)
#db.session.add(st5)
#db.session.add(st6)
#db.session.add(st7)
#db.session.commit()