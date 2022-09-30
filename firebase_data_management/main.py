from datetime import datetime
import firebase_admin
from firebase_admin import firestore
import flask
# import os
from time import sleep

func_response_headers= {'Access-Control-Allow-Origin': '*','Content-Type':'application/json'}
firebase_admin.initialize_app()
db=firestore.client()

def broadcast_data_update(count):
        pass

def broadcast_data_create(request=flask.request):
    request_json=request.get_json(silent=True)
    try:
        ref=db.collection("products").document()
        if request_json["onlyGroups"]=="true":
            broadcast_name="Groups"
        else:
            broadcast_name=",".join(request_json["receiver"])
        ref.set({
            "broadcast_name": broadcast_name,
            "created_at": datetime.now(),
            "is_task_finished":False,
            "total_receiver":len(request_json["receiver"]),
            "send_count":0,
            })
        # {"broadcast_started_time":datetime.now(),"receivers_len":request_json["receiver_count"]}
        # documents = len(list(db.collection("Broadcast1").get()))
        # print(documents)
        # documents=list(db.collection("Broadcast"+request_json["collection_name"]).get())
        return flask.make_response({"message":"Added Succesfully"}, 200,func_response_headers)
    except Exception as e:
         return flask.make_response({"error":e}, 400,func_response_headers)


# import requests
# url = "https://api.ultramsg.com/instance15736/contacts"
# querystring = {"token":"n9cs341yftntz4qk"}
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.request("GET", url, headers=headers, params=querystring)
# groups_list=[]
# for i in response.json():
#     if i["isGroup"]==True:
#         groups_list.append(i["id"])
# print(groups_list)
# print(len(groups_list))