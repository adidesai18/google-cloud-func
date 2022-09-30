import firebase_admin
from firebase_admin import firestore



firebase_admin.initialize_app()
db=firestore.client()
ref=db.collection("Broadcast_Number").document("count_number").get().to_dict()["count"]
print(ref.to_dict())