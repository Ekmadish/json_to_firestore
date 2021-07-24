import firebase_admin as fb
from firebase_admin import firestore
import json

cred = fb.credentials.Certificate('ServiceAccountKey.json')
default_app = fb.initialize_app(cred)
db = firestore.client()

df_file = open("data.json")
df = df_file.read() 

dict = json.loads(df)

# add your collections manually
my_doc_ref = db.collection('OrdersItem').document()

for fruit in range(20): 
    my_doc_ref.set(dict)