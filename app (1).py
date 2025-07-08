
import streamlit as st
st.title("Skill Compass - Career Roadmap generator")
skills = st.multiselect("Your current skills: ", ["Python", "Java", "SQL", "C++", "Excel", "HTML", "CSS", "JS"])
interest = st.selectbox("What are you interested in? ", ["Machine Learning", "Data Analysis", "Web Development"])
time = st.slider("Hours you can commit per week", 1, 20, 5)
goal = st.selectbox("What is your goal? ", ["Get internship", "Build Projects", "Get Job", "Freelance", "Explore Field"])

if st.button("Generate my Roadmap"):
  st.subheader("Input Summary:")
  st.write("Skills:", skills)
  st.write("Interest:", interest)
  st.write("Duration:", time)
  st.write("Goal:", goal)
  