import requests
import flask
import os

parameters=["receiver","message","attachments","isOnlyMessage","isOnlyAttchments"]
func_response_headers= {'Access-Control-Allow-Origin': '*','Content-Type':'application/json'}
ultramsg_headers = {'content-type': 'application/x-www-form-urlencoded'}
secret_key=os.environ.get("ACCESS_TOKEN")

def broadcast(request=flask.request):
        request_json=request.get_json(silent=True)
        if request.method != "POST":
                return flask.make_response({"error":"Only 'POST' method allowed"}, 405,func_response_headers)
        else:
                bearer_token=request.headers.get("Authorization",None)
                if not bearer_token:
                        return flask.make_response({"message":"Provide token in headers"},401,func_response_headers)
                else:
                        token_parts=bearer_token.split()
                        if token_parts[0].lower() != "bearer":
                                return flask.make_response({"message":"Authorization header must start with bearer"},401,func_response_headers)
                        elif len(token_parts) ==1:
                                return flask.make_response({"message":"Toekn not found"},401,func_response_headers)
                        elif len(token_parts)>2:
                                return flask.make_response({"message":"Authorization must be of the form Bearer Token"},401,func_response_headers)
                        elif token_parts[1] != secret_key:
                                return flask.make_response({"message":"wrong token"},401,func_response_headers)
                        else:
                                if request_json and all(k in request_json for k in parameters):
                                        if request_json["isOnlyMessage"]=="True":
                                                for receiver in request_json["receiver"]:
                                                        payload = "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&body="+request_json["message"]+"&priority=10&referenceId="
                                                        response = requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/chat", data=payload, headers=ultramsg_headers)
                                                        print(response.text)
                                                        if response.text[2]=="e" :
                                                                return flask.make_response({"error":str(response.json()["error"])}, 500,func_response_headers)
                                                return flask.make_response({"message":"Sent Succesfully"}, 200,func_response_headers)
                                        elif request_json["isOnlyAttchments"]=="True":
                                                for receiver in request_json["receiver"]:
                                                                for attachment in request_json["attachments"]:
                                                                        if attachment["send_as"]=="image":
                                                                                img_payload= "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&image="+attachment["URL"]+"&caption=&referenceId=&nocache="
                                                                                response=requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/image", headers=ultramsg_headers,data=img_payload)
                                                                        elif attachment["send_as"]=="video":
                                                                                video_payload = "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&video="+attachment["URL"]+"&caption=&referenceId=&nocache="
                                                                                response=requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/video", data=video_payload, headers=ultramsg_headers)
                                                                        else:
                                                                                payload = "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&filename="+attachment["file_name"]+"&document="+attachment["URL"]+"&referenceId=&nocache="
                                                                                response=requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/document", data=payload, headers=ultramsg_headers)
                                                                        if response.text[2]=="e" :
                                                                                return flask.make_response({"error":str(response.json()["error"])}, 500,func_response_headers)
                                                return flask.make_response({"message":"Sent Succesfully"}, 200,func_response_headers)
                                        else:
                                                for receiver in request_json["receiver"]:
                                                                payload = "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&body="+request_json["message"]+"&priority=10&referenceId="
                                                                response = requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/chat", data=payload, headers=ultramsg_headers)
                                                                for attachment in request_json["attachments"]:
                                                                        if attachment["send_as"]=="image":
                                                                                img_payload= "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&image="+attachment["URL"]+"&caption=&referenceId=&nocache="
                                                                                response=requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/image", headers=ultramsg_headers,data=img_payload)
                                                                        elif attachment["send_as"]=="video":
                                                                                video_payload = "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&video="+attachment["URL"]+"&caption=&referenceId=&nocache="
                                                                                response=requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/video", data=video_payload, headers=ultramsg_headers)
                                                                        else:
                                                                                payload = "token="+os.environ.get("ULTRAMSG_WHATSAPP_TOKEN")+"&to="+receiver+",&filename="+attachment["file_name"]+"&document="+attachment["URL"]+"&referenceId=&nocache="
                                                                                response=requests.request("POST", "https://api.ultramsg.com/"+os.environ.get("ULTRAMSG_INSTANCE_ID")+"/messages/document", data=payload, headers=ultramsg_headers)
                                                                        if response.text[2]=="e" :
                                                                                return flask.make_response({"error":str(response.json()["error"])}, 500,func_response_headers)
                                                return flask.make_response({"message":"Sent Succesfully"}, 200,func_response_headers)
                                else:
                                        return flask.make_response({"error":"Missing parameters(receiver,message,attachments,isOnlyMessage,isOnlyAttchments)"}, 400,func_response_headers)
