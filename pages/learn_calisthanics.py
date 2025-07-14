import streamlit as st

st.title("Learn Calisthanics")

level = st.selectbox("Choose your level", ["Beginner", "Intermediate", "Advanced"])

if level == "Beginner":
	st.markdown("### 🔰Beginner Level Workouts")
	st.markdown("- Pushups\n- Squats\n- Planks\n- Assisted Pull-Ups")

	st.image("assets/push-up.png")
	st.image("assets/strength.png")
