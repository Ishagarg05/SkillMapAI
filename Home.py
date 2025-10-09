# # # # # # import streamlit as st

# # # # # # st.set_page_config(page_title="SkillMapAI", layout="centered")
# # # # # # st.title("🚀 SkillMapAI 🚀")
# # # # # # st.title("“Learning never exhausts the mind.” — Leonardo da Vinci")
# # # # # # st.markdown("---")

# # # # # # # Require login first
# # # # # # if "user_email" not in st.session_state or not st.session_state["user_email"]:
# # # # # #     st.warning("⚠️ Please login first from the Account page.")
# # # # # # else:
# # # # # #     # Buttons for navigation
# # # # # #     st.markdown("### Navigate:")
# # # # # #     col1, col2, col3 = st.columns(3)
# # # # # #     with col1:
# # # # # #         if st.button("Account"):
# # # # # #             st.session_state["page"] = "account"
# # # # # #     with col2:
# # # # # #         if st.button("Plan My Journey"):
# # # # # #             st.session_state["page"] = "generate"
# # # # # #     with col3:
# # # # # #         if st.button("Saved Roadmaps"):
# # # # # #             st.session_state["page"] = "saved"
# # # # # import streamlit as st

# # # # # st.set_page_config(page_title="SkillMapAI", layout="centered")

# # # # # # Initialize session_state
# # # # # if "page" not in st.session_state:
# # # # #     st.session_state["page"] = "Home"
# # # # # if "user_email" not in st.session_state:
# # # # #     st.session_state["user_email"] = None

# # # # # # Sidebar Navigation (appears once)
# # # # # st.sidebar.title("SkillMapAI")
# # # # # st.session_state["page"] = st.sidebar.radio("Navigate", ["Home", "Account", "Plan My Journey", "Saved Roadmaps"])

# # # # # # Main content
# # # # # if st.session_state["page"] == "Home":
# # # # #     st.title("🚀 Welcome to SkillMapAI 🚀")
# # # # #     st.markdown("*“Learning never exhausts the mind.”* — Leonardo da Vinci")
# # # # #     if not st.session_state["user_email"]:
# # # # #         st.info("⚠️ Please login first from Account page.")





# # # # import streamlit as st

# # # # st.set_page_config(page_title="SkillMapAI", layout="centered")

# # # # # Initialize session state
# # # # if "page" not in st.session_state:
# # # #     st.session_state["page"] = "Home"
# # # # if "user_email" not in st.session_state:
# # # #     st.session_state["user_email"] = None

# # # # # --- Sidebar (only once) ---
# # # # st.sidebar.title("SkillMapAI")
# # # # st.session_state["page"] = st.sidebar.radio(
# # # #     "Navigate",
# # # #     ["Home", "Account", "Plan My Journey", "Saved Roadmaps"]
# # # # )

# # # # # --- Main content ---
# # # # if st.session_state["page"] == "Home":
# # # #     st.title("🚀 Welcome to SkillMapAI 🚀")
# # # #     st.markdown("*“Learning never exhausts the mind.”* — Leonardo da Vinci")
# # # #     if not st.session_state["user_email"]:
# # # #         st.info("⚠️ Please login first from Account page.")
# # # import streamlit as st

# # # st.set_page_config(page_title="SkillMapAI", layout="centered")

# # # if "user_email" not in st.session_state:
# # #     st.session_state["user_email"] = None

# # # st.title("🚀 Welcome to SkillMapAI 🚀")
# # # st.markdown("*“Learning never exhausts the mind.”* — Leonardo da Vinci")

# # # if not st.session_state["user_email"]:
# # #     st.info("⚠️ Please login first from Account page.")
# # import streamlit as st
# # import Account
# # import Plan_My_Journey
# # import Saved

# # # Page Config
# # st.set_page_config(page_title="SkillMapAI", layout="centered")

# # # Session State for login
# # if "user_email" not in st.session_state:
# #     st.session_state["user_email"] = None

# # # Sidebar Navigation
# # st.sidebar.title("📌 Navigation")
# # page = st.sidebar.radio("Go to:", ["🏠 Home", "👤 Account", "🗺️ Plan My Journey", "💾 Saved Roadmaps"])

# # # Page Rendering
# # if page == "🏠 Home":
# #     st.title("🚀 Welcome to SkillMapAI 🚀")
# #     st.markdown("*“Learning never exhausts the mind.”* – Leonardo da Vinci")

# #     if not st.session_state["user_email"]:
# #         st.info("⚠️ Please login first from Account page.")

# # elif page == "👤 Account":
# #     Account.app()   # make sure Account.py has a function app()

# # elif page == "🗺️ Plan My Journey":
# #     Plan_My_Journey.app()   # make sure Plan_My_Journey.py has app()

# # elif page == "💾 Saved Roadmaps":
# #     Saved.app()   # make sure Saved_Roadmaps.py has app()
# import streamlit as st

# def app():
#     st.title("🚀 Welcome to SkillMapAI 🚀")
#     st.write("“Learning never exhausts the mind.” — Leonardo da Vinci")
#     st.info("⚠️ Please login first from Account page.")


import streamlit as st

def app():
    st.title("🚀 Welcome to SkillMapAI 🚀")
    st.write("“Learning never exhausts the mind.” — Leonardo da Vinci")

    # Check login status
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.info("⚠️ Please login first from Account page.")
    else:
        st.success("✅ You are logged in! Enjoy SkillMapAI 🎉")
        st.write("Explore the highlights 😄")