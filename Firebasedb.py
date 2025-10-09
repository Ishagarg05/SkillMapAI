# # # import firebase_admin
# # # from firebase_admin import credentials, firestore

# # # # Initialize Firestore only once
# # # if not firebase_admin._apps:
# # #     cred = credentials.Certificate("serviceAccountKey.json")
# # #     firebase_admin.initialize_app(cred)

# # # db = firestore.client()

# # # def save_roadmap(user_email, topic, duration, roadmap_text):
# # #     """Save roadmap to Firestore."""
# # #     doc_ref = db.collection("roadmaps").document(user_email)
# # #     doc_ref.set({
# # #         "topic": topic,
# # #         "duration": duration,
# # #         "roadmap": roadmap_text
# # #     })
# # #     return True

# # # def get_roadmap(user_email):
# # #     """Fetch saved roadmap of a user."""
# # #     doc_ref = db.collection("roadmaps").document(user_email).get()
# # #     if doc_ref.exists:
# # #         return doc_ref.to_dict()
# # #     return None

# # # def get_all_roadmaps():
# # #     """Fetch all roadmaps (optional: for admin view)."""
# # #     roadmaps = db.collection("roadmaps").stream()
# # #     return [{r.id: r.to_dict()} for r in roadmaps]
# # import pyrebase

# # # --- Initialize Firebase ---
# # firebaseConfig = {
# #     "apiKey": "AIzaSyCr3im9zKcCqnOObUkbFokNWay1s77BfNY",
# #     "authDomain": "ai-powered-roadmap.firebaseapp.com",
# #     "projectId": "ai-powered-roadmap",
# #     "storageBucket": "ai-powered-roadmap.appspot.com",
# #     "messagingSenderId": "488070928735",
# #     "appId": "1:488070928735:web:xxxxxxx",
# #     "databaseURL": "https://ai-powered-roadmap-default-rtdb.firebaseio.com/"
# # }
# # firebase = pyrebase.initialize_app(firebaseConfig)
# # db = firebase.database()

# # # --- Save Roadmap ---
# # def save_roadmap(user_email, topic, num_days, roadmap_text):
# #     """
# #     Save a roadmap for a user. Each roadmap is stored under a unique timestamp.
# #     """
# #     import time
# #     timestamp = str(int(time.time()))
# #     data = {
# #         "topic": topic,
# #         "num_days": num_days,
# #         "roadmap_text": roadmap_text
# #     }
# #     db.child("roadmaps").child(user_email.replace('.', ',')).child(timestamp).set(data)

# # # --- Get All Roadmaps ---
# # def get_roadmap(user_email):
# #     """
# #     Retrieve all roadmaps for a user as a list of dictionaries.
# #     """
# #     roadmaps = db.child("roadmaps").child(user_email.replace('.', ',')).get()
# #     if roadmaps.each():
# #         result = []
# #         for r in roadmaps.each():
# #             result.append(r.val())
# #         return result
# #     return []
# import streamlit as st
# from Firebasedb import get_roadmap

# def app():
#     st.title("📂 Saved Roadmaps")

#     if "user_email" not in st.session_state or not st.session_state["user_email"]:
#         st.warning("⚠️ Please login first from Account page.")
#         st.stop()

#     roadmaps = get_roadmap(st.session_state["user_email"])
#     if roadmaps:
#         for i, r in enumerate(roadmaps, 1):
#             st.markdown(f"### {i}. {r['topic']} ({r['num_days']} days)")
#             st.markdown(r['roadmap_text'], unsafe_allow_html=True)
#             st.markdown("---")
#     else:
#         st.info("No saved roadmap found.")
# import pyrebase
# from dotenv import load_dotenv
# import os

# load_dotenv()

# firebaseConfig = {
#     "apiKey": os.getenv("FIREBASE_API_KEY"),
#     "authDomain": "ai-powered-roadmap.firebaseapp.com",
#     "projectId": "ai-powered-roadmap",
#     "storageBucket": "ai-powered-roadmap.appspot.com",
#     "messagingSenderId": "488070928735",
#     "appId": "1:488070928735:web:xxxxxxx",
#     "databaseURL": "https://ai-powered-roadmap-default-rtdb.firebaseio.com/"
# }
# firebase = pyrebase.initialize_app(firebaseConfig)
# db = firebase.database()

# def save_roadmap(user_email, topic, num_days, roadmap_text):
#     data = {
#         "topic": topic,
#         "num_days": num_days,
#         "roadmap_text": roadmap_text
#     }
#     db.child("roadmaps").child(user_email.replace(".", "_")).push(data)

# def get_roadmap(user_email):
#     data = db.child("roadmaps").child(user_email.replace(".", "_")).get()
#     if data.val():
#         return list(data.val().values())
#     return []
# import pyrebase
# from dotenv import load_dotenv
# import os

# load_dotenv()

# firebaseConfig = {
#     "apiKey": os.getenv("FIREBASE_API_KEY"),
#     "authDomain": "ai-powered-roadmap.firebaseapp.com",
#     "projectId": "ai-powered-roadmap",
#     "storageBucket": "ai-powered-roadmap.appspot.com",
#     "messagingSenderId": "488070928735",
#     "appId": "1:488070928735:web:xxxxxxx",
#     "databaseURL": "https://ai-powered-roadmap-default-rtdb.firebaseio.com/"
# }

# firebase = pyrebase.initialize_app(firebaseConfig)
# db = firebase.database()

# def save_roadmap(user_email, topic, num_days, roadmap_text):
#     data = {
#         "topic": topic,
#         "num_days": num_days,
#         "roadmap_text": roadmap_text
#     }
#     return db.child("roadmaps").child(user_email.replace(".", "_")).push(data)

# def get_roadmaps(user_email):
#     data = db.child("roadmaps").child(user_email.replace(".", "_")).get()
#     if data.each():
#         return [{"id": item.key(), **item.val()} for item in data.each()]
#     return []

# def delete_roadmap(user_email, roadmap_id):
#     db.child("roadmaps").child(user_email.replace(".", "_")).child(roadmap_id).remove()
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
