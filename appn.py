
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

import pandas as pd
import numpy as np
df = pd.read_csv("/content/drive/MyDrive/Book1.csv")

# Define a function to score each flow
def compute_match_score(row, user_skills, user_interest, user_goal, user_hours):
  score = 0
  if row["Interest"] == user_interest:
    score += 2
  if row["Goal"] == user_goal:
    score += 2
  if abs(row["WeeklyHours"] - user_hours) <= 2:
    score += 1
  row_skills = set([s.strip() for s in row["Skills"].split(",")])
  overlap = set(user_skills).intersection(row_skills)
  score += len(overlap)
  return score
#Applying to every row
df["Score"] = df.apply(lambda row: compute_match_score(row, skills, interest, goal, time), axis = 1)

#Get the best match
best_row = df.sort_values("Score", ascending = False).iloc[0]
st.subheader(" Recommended Roadmap:")
st.write(best_row["Path"])
