from datetime import datetime
import firebase_admin
from firebase_admin import firestore
import flask
import os

func_response_headers= {'Access-Control-Allow-Origin': '*','Content-Type':'application/json'}
firebase_admin.initialize_app()
db=firestore.client()

def broadcast_data_update(count):
        pass

def broadcast_data_create(request=flask.request):
    request_json=request.get_json(silent=True)
    try:
        ref=db.collection("Broadcast1").document("Broadcast"+request_json["collection_name"])
        ref.set({"broadcast_started_time":datetime.now(),"receivers_len":request_json["receiver_count"]})
        # documents = len(list(db.collection("Broadcast1").get()))
        # print(documents)
        # documents=list(db.collection("Broadcast"+request_json["collection_name"]).get())
        return flask.make_response({"message":"Added Succesfully"}, 200,func_response_headers)
    except Exception as e:
         return flask.make_response({"error":e}, 400,func_response_headers)


