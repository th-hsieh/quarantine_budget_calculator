#from cs50 import SQL
from flask import Flask, render_template, request, redirect

app = Flask(__name__)     #DEFINE APP---> cannot be missed!!!

#db=SQL('sqlite:///quarantine_budget_result.db') we don't need this SQL here because we are just implementing a one-time server, 而且因為我不會用db

REGISTRANTS={}

AIRPORTS = [ 'Taipei Airport' , 'Taoyuan Airport' , 'Taichung Airport','Kaohsiung Airport' ]

DESTINATIONS= [ 'Taipei Municipality','New Taipei Municipality','Taoyuan Municipality','Taichung Municipality','Tainan Municipality','Kaousiung Municipality','Hsinchu','Miaoli','Changhua','Nantou','Yunlin','Chiayi','Pintung','Yilan','Hualien','Taitung','Penghu','Kinmen','Keelung' ]

TRANSPORTATION_METHODS=[ 'Bus', 'Taxi','Bus+Taxi' ]

@app.route('/') #default is 'GET'
def index():
	return render_template('index.html',airports=AIRPORTS,destinations=DESTINATIONS,transportation_methods=TRANSPORTATION_METHODS)  #parameter是因為airport & transportation_methods都需要選單

@app.route('/register', methods=['POST'])
def register():
	#REGISTRANTS{'name','airport','destination_address','transportation_method'}
	name=request.form.get('name')
	if not name:
		return render_template('error.html',message='Missing name')
	
	airport=request.form.get('airport')
	if not airport:
		return render_template('error.html', message='Missing Airport')
	if airport not in AIRPORTS:
		return render_template('error.html',message='invalid airport')
	
	destination=request.form.get('destination')
	if not destination:
		return render_template('error.html',message='Missing Destination')
	if destination not in DESTINATIONS:
		return render_template('error.html',message='invalid Destination')

	transportation_method=request.form.get('transportation_method')
	if not transportation_method:
		return render_template('error.html',message='Missing Transportation Method')
	if transportation_method not in TRANSPORTATION_METHODS:
		return render_template('error.html',message='invalid Transportation Method')
	
	### start to use user's data to do data analysis

	REGISTRANTS[name]=[airport,destination,transportation_method]
	

	####NO MATTER WHAT, the condition loop will always be entered!!!???
	if (list(REGISTRANTS.values())[0][0]=='Taipei Airport'):
		print(list(REGISTRANTS.values())[0][1])
		if (list(REGISTRANTS.values())[0][1]) == 'Keelung' or 'New Taipei Municipality' or 'Taipei Municipality' or 'Taoyuan Municipality':
			return render_template('budget.html', message='Billing according to the skip meter')
		elif (list(REGISTRANTS.values())[0][1] == 'Hsinchu' )or (list(REGISTRANTS.values())[0][1] =='Miaoli'):
			print('hi')
			return render_template('budget.html', message='1000TWD')


	#return render_template('success.html', message='Input Successfully!')


@app.route('/success')
def success():
	return render_template('success.html', message='Input Successfully!', registrants=REGISTRANTS)


