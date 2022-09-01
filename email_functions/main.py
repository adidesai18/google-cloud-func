import flask
import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

def get_bearer_token(request=flask.request):
    bearer_token=request.headers.get("Authorization")
    if not bearer_token:
        flask.abort(401,"Provide token in headers")
        headers= {
        'Access-Control-Allow-Origin': '*',
        'Content-Type':'application/json'
        }
        flask.make_response({"message":"Provide token in headers"},410,headers)
    token_parts=bearer_token.split()
    if token_parts[0].lower() != "bearer":
        flask.abort(401,"Authorization header must start with bearer")
        headers= {
        'Access-Control-Allow-Origin': '*',
        'Content-Type':'application/json'
        }
        return flask.make_response({"message":"Authorization header must start with bearer"},401,headers)
    elif len(token_parts) ==1:
        flask.abort(401,"Toekn not found")
    elif len(token_parts)>2:
        flask.abort(401,"Authorization must be of the form Bearer Token")
    else:
        return token_parts[1]


def send_email(request=flask.request):
    parameters=["sender","receiver","subject","message"]
    request_json=request.get_json(silent=True)
    print(request.method)
    if request.method != "GET":
        # headers= {
        #     'Access-Control-Allow-Origin': '*',
        #     'Content-Type':'application/json'
        #     }
        # return flask.make_response({"error":f"{e}"}, 500,headers)
        flask.abort(405)
    bearer_token=get_bearer_token(request) # returns list [bearer,token] so index 1
    secret_key=os.environ.get("ACCESS_TOKEN")
    if bearer_token != secret_key:
        flask.abort(401,{"message": "wrong token."})
    elif request_json and all(k in request_json for k in parameters):
        # message = Mail(
        # from_email='from_email@example.com',
        # to_emails='to@example.com',
        # subject='Sending with Twilio SendGrid is Fun',
        # html_content='<strong>and easy to do anywhere, even with Python</strong>')
        try:
            # sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
            # print(sg.api_key)
            # response = sg.send(message)
            headers= {
            'Access-Control-Allow-Origin': '*',
            'Content-Type':'application/json'
            }
            return flask.make_response(request_json, 200,headers)
        except Exception as e:
            headers= {
            'Access-Control-Allow-Origin': '*',
            'Content-Type':'application/json'
            }
            return flask.make_response({"error":f"{e}"}, 500,headers)
            # flask.abort(500,{"error":f"{e}"})
    else:
        # flask.abort(400)
        headers= {
        'Access-Control-Allow-Origin': '*',
        'Content-Type':'application/json'
        }
        return flask.make_response({"error":"Missing parameters(sender,receiver,subject,message)"}, 400,headers)
