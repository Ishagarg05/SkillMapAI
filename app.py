# import streamlit as st
# import Home
# import Plan_My_Journey
# import Saved
# import Firebasedb

# st.set_page_config(page_title="SkillMapAI", layout="wide")

# # Sidebar ek hi jagah
# st.sidebar.title("SkillMapAI")
# st.sidebar.subheader("Navigate")

# page = st.sidebar.radio("Go to", ["Home", "Account", "Plan My Journey", "Saved Roadmaps"])

# # Page render logic
# if page == "Home":
#     Home.app()
# elif page == "Account":
#     Firebasedb.app()
# elif page == "Plan My Journey":
#     Plan_My_Journey.app()
# elif page == "Saved Roadmaps":
#     Saved.app()
import streamlit as st
import Home
import Plan_My_Journey
import Saved
import Account

st.set_page_config(page_title="SkillMapAI", layout="wide")

st.sidebar.title("SkillMapAI 🚀")
st.sidebar.subheader("Navigate")

page = st.sidebar.radio(
    "Go to",
    ["Home", "Account", "Plan My Journey", "Saved Roadmaps"]
)

if page == "Home":
    Home.app()
elif page == "Account":
    Account.app()
elif page == "Plan My Journey":
    Plan_My_Journey.app()
elif page == "Saved Roadmaps":
    Saved.app()
