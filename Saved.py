# # import streamlit as st
# # from Firebasedb import get_roadmap

# # st.title("📂 Saved Roadmaps")

# # if "user_email" not in st.session_state or not st.session_state["user_email"]:
# #     st.warning("⚠️ Please login first from Account page.")
# #     st.stop()

# # roadmaps = get_roadmap(st.session_state["user_email"])
# # if roadmaps:
# #     for i, r in enumerate(roadmaps, 1):
# #         st.markdown(f"### {i}. {r['topic']} ({r['num_days']} days)")
# #         st.markdown(r['roadmap_text'], unsafe_allow_html=True)
# #         st.markdown("---")
# # else:
# #     st.info("No saved roadmap found.")
# import streamlit as st
# from Firebasedb import get_roadmap   # dhyaan rahe file ka naam sahi ho

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
import streamlit as st
from Firebasedb import get_roadmaps, delete_roadmap

def app():
    st.title("📚 Saved Roadmaps")

    if "user_email" not in st.session_state or not st.session_state["user_email"]:
        st.warning("⚠️ Please login first from Account page.")
        st.stop()

    user_email = st.session_state["user_email"]

    roadmaps = get_roadmaps(user_email)

    if not roadmaps:
        st.info("No saved roadmaps yet.")
        return

    for roadmap in roadmaps:
        with st.expander(f"📘 {roadmap['topic']} ({roadmap['num_days']} days)"):
            st.markdown(roadmap["roadmap_text"], unsafe_allow_html=True)

            # Delete button
            if st.button(f"🗑️ Delete '{roadmap['topic']}'", key=f"del_{roadmap['id']}"):
                delete_roadmap(user_email, roadmap["id"])
                st.success(f"Deleted roadmap for {roadmap['topic']} ✅")
                st.rerun()  # refresh page

