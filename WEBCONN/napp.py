import os
from flask import request
from flask import Flask
from flask import render_template
from flask import url_for
import scim_put 
import scim_get_u
import scim_delete
import scim_delete_dom
import scim_get_g
import scim_put_group
import scim_update_group
import scim_delete_group
import scim_update_rm_group
import privateapps 
import get_pub_id 
import uba_uci
import uba_uci_update
import uba_uci_reset
import ucidemos
import scim_bulk_load

tenant = 'null'
token = 'null'
app = Flask(__name__)

@app.route('/login',methods=['POST','GET'])
def login():
	error = None
	if request.method == 'POST':
		global tenant
		tenant = request.form['tenant']
		global token
		token = request.form['token']
		if request.form['select'] == 'useradd':
			return render_template('useradd.html')
		if request.form['select'] == 'userread':
			return render_template('userread.html')
		if request.form['select'] == 'userdelete':
			return render_template('userdelete.html')
		if request.form['select'] == 'bulkdelete':
			return render_template('bulkdelete.html')
		if request.form['select'] == 'groupread':
			return render_template('groupread.html')
		if request.form['select'] == 'groupcreate':
			return render_template('groupcreate.html')
		if request.form['select'] == 'groupupdate':
			return render_template('groupupdate.html')
		if request.form['select'] == 'groupdelete':
			return render_template('groupdelete.html')
		if request.form['select'] == 'groupuserdel':
			return render_template('groupuserdel.html')
		if request.form['select'] == 'privateapp':
			return render_template('privateapp.html')
		if request.form['select'] == 'getpubid':
			return render_template('getpubid.html')
		if request.form['select'] == 'ubauci':
			return render_template('ubauci.html')
		if request.form['select'] == 'ubauciupdate':
			return render_template('ubauciupdate.html')
		if request.form['select'] == 'ubaucireset':
			return render_template('ubaucireset.html')
		if request.form['select'] == 'ucidemo':
			return render_template('ucidemo.html')
		if request.form['select'] == 'bulkuseradd':
			return render_template('bulkuseradd.html')
	return render_template('init.html')
@app.route('/useradd',methods=['POST','GET'])
def useradd():
	if request.method == 'POST':
		s = scim_put.main(tenant,token,request.form['upn'],request.form['lname'],request.form['uname'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/userread',methods=['POST','GET'])
def userread():
	if request.method == 'POST':
		s= scim_get_u.main(tenant,token,request.form['upn'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/userdelete',methods=['POST','GET'])
def userdelete():
	if request.method == 'POST':
		s= scim_delete.main(tenant,token,request.form['upn'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/bulkdelete',methods=['POST','GET'])
def bulkdelete():
	if request.method == 'POST':
		s= scim_delete_dom.main(tenant,token,request.form['dom'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/groupread',methods=['POST','GET'])
def groupread():
	if request.method == 'POST':
		s= scim_get_g.main(tenant,token,request.form['group'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/groupcreate',methods=['POST','GET'])
def groupcreate():
	if request.method == 'POST':
		s= scim_put_group.creategroup(tenant,token,request.form['group'],request.form['upn'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/groupupdate',methods=['POST','GET'])
def groupupdate():
	if request.method == 'POST':
		s= scim_update_group.updategroup(tenant,token,request.form['upn'],request.form['group'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/groupdelete',methods=['POST','GET'])
def groupdelete():
	if request.method == 'POST':
		s= scim_delete_group.deletegroup(tenant,token,request.form['group'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/groupuserdel',methods=['POST','GET'])
def groupuserdel():
	if request.method == 'POST':
		s= scim_update_rm_group.updategroup(tenant,token,request.form['upn'],request.form['group'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/privateapp',methods=['POST','GET'])
def privateapp():
	if request.method == 'POST':
		file = request.files['file']
		if file.filename == '':
			s = "No se cargó el archivo"
			return render_template('result.html',message=s)
		if file:
			file.save("apps.csv")
			s = privateapps.main(tenant,token)
			os.remove("apps.csv")
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/getpubid',methods=['POST','GET'])
def getpubid():
	if request.method == 'POST':
		s= get_pub_id.main(tenant,token,request.form['pub'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/ubauci',methods=['POST','GET'])
def ubauci():
	if request.method == 'POST':
		s= uba_uci.getuci(tenant,token,request.form['upn'],request.form['date'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/ubauciupdate',methods=['POST','GET'])
def ubauciupdate():
	if request.method == 'POST':
		s= uba_uci_update.updateuci(tenant,token,request.form['upn'],request.form['uci'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/ubaucireset',methods=['POST','GET'])
def ubaucireset():
	if request.method == 'POST':
		s= uba_uci_reset.resetuci(tenant,token,request.form['upn'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
@app.route('/ucidemo',methods=['POST','GET'])
def ucidemo():
	if request.method == 'POST':
		(s,color) = ucidemos.main(tenant,token,request.form['upn'],request.form['gc'],request.form['rtime'])
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('resultdemo.html',message=s,color=color)
@app.route('/bulkuseradd',methods=['POST','GET'])
def bulkuseradd():
	if request.method == 'POST':
		file = request.files['file']
		if file.filename == '':
			s = "No se cargó el archivo"
			return render_template('result.html',message=s)
		if file:
			file.save("users.csv")
			s = scim_bulk_load.main(tenant,token)
			os.remove("users.csv")
		if s == 'Unauthorized':
			return render_template('authfail.html')
		else:
			return render_template('result.html',message=s)
