import pyrebase
from dotenv import load_dotenv
import os

load_dotenv()

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": "ai-powered-roadmap.firebaseapp.com",
    "projectId": "ai-powered-roadmap",
    "storageBucket": "ai-powered-roadmap.appspot.com",
    "messagingSenderId": "488070928735",
    "appId": "1:488070928735:web:xxxxxxx",
    "databaseURL": "https://ai-powered-roadmap-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# ------------------- Save roadmap -------------------
def save_roadmap(user_email, topic, num_days, roadmap_text):
    data = {
        "topic": topic,
        "num_days": num_days,
        "roadmap_text": roadmap_text
    }
    # push returns the unique key
    return db.child("roadmaps").child(user_email.replace(".", "_")).push(data)

# ------------------- Get all roadmaps -------------------
def get_roadmaps(user_email):
    data = db.child("roadmaps").child(user_email.replace(".", "_")).get()
    if data.each():
        # return list of dicts with ID and roadmap data
        return [{"id": item.key(), **item.val()} for item in data.each()]
    return []

# ------------------- Get latest roadmap -------------------
def get_latest_roadmap(user_email):
    all_roadmaps = get_roadmaps(user_email)
    if all_roadmaps:
        return all_roadmaps[-1]  # last saved roadmap
    return None

# ------------------- Delete roadmap -------------------
def delete_roadmap(user_email, roadmap_id):
    db.child("roadmaps").child(user_email.replace(".", "_")).child(roadmap_id).remove()
