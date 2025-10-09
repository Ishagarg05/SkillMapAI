import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from roadmap_prompt import learning_roadmap_prompt
from Firebasedb import save_roadmap, get_latest_roadmap


def app():
    # Load API key
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        st.error("🚫 Google API Key missing")
        st.stop()

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash",
        system_instruction="You're a Roadmap generator for Tools, Technology, and Programming languages."
    )

    st.title("✨ Plan My Journey")

    # Require login
    # if "user_email" not in st.session_state or not st.session_state["user_email"]:
    #     st.warning("⚠️ Please login first from Account page.")
    #     st.stop()

    # user_email = st.session_state["user_email"]

    if not st.session_state.get("logged_in", False):
            st.warning("⚠️ Please login first from Account page.")
            st.stop()

    user_email = st.session_state["user_email"]

   

    topic = st.text_input("Topic You Want to Learn")
    num_days = st.number_input("Duration (days)", min_value=7, max_value=180, value=28, step=1)

    if st.button("Generate Roadmap"):
        if topic.strip() == "":
            st.warning("Please enter a topic.")
        else:
            with st.spinner("Generating roadmap..."):
                full_prompt = learning_roadmap_prompt.format(topic=topic, num_days=num_days)
                response = model.generate_content(full_prompt)
                output = response.text

                roadmap = {
                    "topic": topic,
                    "num_days": num_days,
                    "roadmap_text": output
                }
                st.session_state["latest_roadmap"] = roadmap

                st.markdown("### 🧭 Your Personalized Learning Roadmap")
                st.markdown(output, unsafe_allow_html=True)

    # Save button (only if roadmap exists)
    if st.session_state.get("latest_roadmap"):
        if st.button("💾 Save Roadmap"):
            roadmap = st.session_state["latest_roadmap"]
            save_roadmap(
                user_email,
                roadmap["topic"],
                roadmap["num_days"],
                roadmap["roadmap_text"]
            )
            st.success("Saved to Firebase ✅")
            

    # 👉 Show roadmap agar already saved hai
    if st.session_state.get("latest_roadmap"):
        roadmap = st.session_state["latest_roadmap"]
        st.markdown("### 🧭 Your Personalized Learning Roadmap")
        st.markdown(roadmap["roadmap_text"], unsafe_allow_html=True)
