from flask import Flask,render_template, request, url_for, jsonify, make_response, Blueprint
import dbaccess as dbfile
app=Blueprint('home',__name__,template_folder='templates')

app = Flask(__name__)
#, root_path='codetest/'
dbconn=dbfile.create_connection()

@app.route('/')
def show():
   mydata=dbfile.show_emp(dbconn)
   return render_template('showemp.html',dbres=mydata)

@app.route('/search/<val>',methods=['POST'])
def search(val):
   req = request.get_json()
   print("req value: ",req)
   res = make_response(jsonify(req), 200)
   print("res value:",res)
   mydata=dbfile.srch_emp(dbconn,val)
   return render_template('showemp.html',dbres=mydata)

@app.route('/add')
def addrecord():
    return render_template('addemp.html')

@app.route('/add',methods=['POST'])
def addemp():
   empval=(request.form['addName'] ,request.form['addDesg'],request.form['addAddr'],request.form['addPhn'])
   dbfile.insert_emp(dbconn,empval)
   mydata=dbfile.show_emp(dbconn)
   return render_template('showemp.html',dbres=mydata)

@app.route('/delete/<id>',methods=['POST'])
def delemp(id):
   dbfile.delete_emp(dbconn,id)
   mydata=dbfile.show_emp(dbconn)
   return render_template('showemp.html',dbres=mydata)

if __name__ == '__main__':
   app.run()
