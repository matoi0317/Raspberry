import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore, storage

def send_pdf(pdf):
    cred = credentials.Certificate('karute-81f3c-firebase-adminsdk-na7p6-099144bd72.json')
    firebase_admin.initialize_app(cred, {'storageBucket': 'karute-81f3c.appspot.com'})

    bucket = storage.bucket()
    filename = pdf
    content_type = 'application/pdf'
    blob = bucket.blob(filename)
    with open(filename, 'rb') as f:
        blob.upload_from_file(f, content_type=content_type)