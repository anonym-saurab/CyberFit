import streamlit as st

st.title("🎯 This Week's CyberFit Mission")

st.markdown("""
### Fitness Task: 
- 20 squats
- 15 sec plank

""")
st.image("assets/strength.png")

st.markdown("""
### 🔐 Cyber Task:
- Watch a short phishing awareness video
- Complete 1 question

""")

video_url = "https://youtube.com/shorts/8GyrX2Igvx8?si=SkBB_ZUd6Peuyv2B"
st.video(video_url)

q1 = st.radio("What should you check before clicking a link in an email?", ["Sender's name", "Spelling mistakes", "Actual URL behind the link", "All of the above"])

if q1 == "All of the above":
	st.success("🎉 You completed this week’s CyberFit Mission!")
