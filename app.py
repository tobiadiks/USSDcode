from flask import Flask, request
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
        response += "1. Get a Tip\n"
        response += "2. Check your Subscription\n"
    elif text == "1":
        # sub menu 1
        try:
            response = "END Treach Tip Coming through.\n You will Receive an SMS shortly"
            # sending the sms
            sms_response = sms.send(
                "Teaching is important.Teaching is changing.\nTeaching is hard.And at the intersection of these three truths lies the constant need for a variety of support for teachers–new teachers or experienced.\nIt’s one thing for trained educational psychologists to offer dry academic papers saying what the data says should happen, or for blogs and social media platforms to make recommendations.But it’s quite another when your colleagues make them–especially experienced colleagues dropping nuggets of wisdom to the next wave of teaching professionals trying to find their footing.", sms_phone_number)
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
                "Your subscription remains 20 units. \n Enjoy Treach for free at https://treach.azurewebsites.net ", sms_phone_number)
            print(sms_response)
        except Exception as e:
            # show us what went wrong
            response = f"END Oh no, we have a problem: {e} Try again Later"
            print(f"Oh no, we have a problem: {e} Try again Later")
   
    else:
        response = "END Invalid input. Try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
