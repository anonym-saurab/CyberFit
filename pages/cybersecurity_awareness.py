import streamlit as st

st.title("🛡️ Cybersecurity Awareness Lesson")

topic = st.radio("Choose a topic", ["Strong Passwords", "Phishing Detection", "Social Media Safety", "What is Malware?"])

if topic == "Phishing Detection":
	st.markdown("### What is phishing ?")
	st.image("assets/hacker.png")
	st.markdown("""
	**Phishing** is a type of scam where attackers trick you into clicking fake links.

    	**Signs of Phishing Emails:**
    	- Urgent tone
    	- Suspicious links
    	- Unknown sender
	""")

	if st.button("Take mini quiz"):
		st.switch_page("pages/quizzes.py")
