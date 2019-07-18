from flask import Flask,request,jsonify

app =Flask(__name__)

@app.route('/hello')
def hello():
	return 'hello'

@app.route('/Semester')
def Semester():
	semester = request.args['semester']
	return 'you are in :{}'.format(semester) + 'semester'

@app.route('/GPA')
def GPA():
	gpa = request.args['gpa']
	return 'your current GPA is  {}'.format(gpa)

@app.route('/post_data', methods=['GET','POST'])
def post_data():
	req_data =request.get_json()
	print(req_data)
	if 'contact' not in req_data:
		return 'contact is not givennnnn'

	if 'firstName' not in req_data:
		return 'First name is not here'

	if 'lastName' not in req_data:
		return 'LastName is not given'

	first_name = req_data['firstName']
	last_name = req_data ['lastName']
	phone =req_data['contact']
	return jsonify({
		"First Name" :first_name,
		"Last Name" : last_name,
		"Cell" : phone
		})
	#sadsadas


# @app.route('/post_data',methods=['GET','POST'])
# def postdata():
# 	req_data = request.get_json()
# 	print(req_data)
# 	if 'firstName' not in req_data:
# 		return 'First name is not provided'
# 	if 'lastName' not in req_data:
# 		return 'last name is not provided'

# 	first_name = req_data['firstName']
# 	last_name = req_data['lastName']
# 	return jsonify({
# 		"First Name ":first_name,
# 		"Last Name" : last_name
# 		})
