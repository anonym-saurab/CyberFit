import streamlit as st

st.title("🧠 Cyber Awareness Quiz")

q1 = st.radio("What is a strong password ?", ["123456", "password123", "mypassword@#2014"])

if q1 ==  "mypassword@#2014":
	st.success("✅ Correct!")
else:
	st.error("❌ Weak password!")


### load more later
