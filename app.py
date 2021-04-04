from flask import Flask, request,redirect, url_for, render_template
import africastalking
import os
app = Flask(__name__)
username = "sandbox"
api_key = "e3550f613f96b899612d002898750ce48ecc1d990f784a6412a7baadcd2a056e"
africastalking.initialize(username, api_key)
sms = africastalking.SMS



@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)

    # ussd logic
    if text == "":
        # main menu
        response = "CON Welcome to Treach.\n To subscribe press 1\n"
        response += "1. Subscribe\n"
        response += "2. Receive more info\n"
    elif text == "1":
        # sub menu 1
        try:
            response = "END Thank you for subscribing to Treach.\n You will Receive an SMS shortly"
            # sending the sms
            sms_response = sms.send(
                "Thank you for believing in Treach.\n Do you know the important skills to know as a Teacher. Check out https://www.treach.com on how this was done.", sms_phone_number)
            print(sms_response)
        except Exception as e:
            # show us what went wrong
            response = f"END Oh no, we have a problem: {e} Try again Later"
            print(f"Oh no, we have a problem: {e} Try again Later")
    elif text == "2":
        # sub menu 2
        try:
            response = "END An SMS will be sent shortly {}".format(phone_number)
            # sending the sms
            sms_response = sms.send(
                "Thank you for believing in Treach.\n Treach is for teachers and educators. Check out https://www.treach.com on how this was done.", sms_phone_number)
            print(sms_response)
        except Exception as e:
            # show us what went wrong
            response = f"END Oh no, we have a problem: {e} Try again Later"
            print(f"Oh no, we have a problem: {e} Try again Later")
   
    else:
        response = "END Invalid input. Try again."

    return response

@app.route('/send', methods=['POST','GET'])
def sms_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    sms_phone_number = []
    sms_phone_number.append(phone_number)
    
    if request.method == 'POST':
    	try:
    		message= request.form['message']
    		sms_response = sms.send(message,'+2348112806410')
    		print(sms_response)
    		return redirect(url_for('success'))
    	except Exception as e:
    	       print('Failed')
    else:
            message = request.args.get('message')
            return render_template('message.html')

@app.route('/success')
def success():
    	return('Successfully Sent')
    	
if __name__ == "__main__":
    app.run(debug= True, host="0.0.0.0", port=os.environ.get("PORT"))
