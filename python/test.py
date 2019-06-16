
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("./auth-a66ff-firebase-adminsdk-yt9h9-932f8f488b.json")
firebase_admin.initialize_app(cred)

# print("Hello")
# i='u'+1
# print('u'+i)
# id=1
# x=str(id)
db = firestore.client()



# for i in range(0,29):
#     x=str(i)
#     doc_ref = db.collection(u'Supermarket').document(x)
#     doc_ref.set({
#         u'occupied': False
#     })  
#     # print x      
