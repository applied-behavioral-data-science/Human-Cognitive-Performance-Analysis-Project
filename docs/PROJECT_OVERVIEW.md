# The Applied Behavioral Data Science Collective – Project 1 Overview  
Human Cognitive Performance Analysis Project

---

## Dataset
**Human Cognitive Performance Dataset** (80,000 participants)

This dataset includes lifestyle variables such as:
- sleep duration  
- stress level  
- screen time  
- exercise time  
- caffeine intake  
- age  
- gender  

And cognitive outcomes such as:
- cognitive score  
- reaction time  

---

## Project Goal
Explore which daily lifestyle habits show the strongest relationships with cognitive performance.

---

## Shared Research Question
**Which lifestyle habits show the strongest relationships with cognitive performance?**

We are focusing specifically on relationships with:
- **Cognitive_Score**
- **Reaction_Time**

---

## Team Variable Assignments
- **Carolina** — Screen Time  
- **Umaima** — Caffeine Intake  
- **Byron** — Exercise Time  
- **Maitreya** — Stress Level  
- **Sarah** — Sleep Duration  

---

## Analysis Plan (Per Person)
Each member will analyze their assigned lifestyle variable and compare it against both outcomes.

### Main Comparisons
- variable vs **Cognitive_Score**
- variable vs **Reaction_Time**

### Group Comparisons
- breakdown by **Age Group**
- breakdown by **Gender**

### Strength Metrics
Each member will compute:
- correlation with **Cognitive_Score**
- correlation with **Reaction_Time**

---

## EDA Plan (Per Person)
Each member should complete:

1. **Variable Check**
   - range (min/max)
   - missing values
   - outliers or strange values

2. **Distribution**
   - visualization of the variable’s distribution
   - short written description of the pattern

3. **Summary Statistics**
   - mean, median, standard deviation, min, max

4. **Cognitive Score Comparison**
   - visualization of variable vs cognitive score
   - brief interpretation of relationship strength/pattern

5. **Reaction Time Comparison**
   - visualization of variable vs reaction time
   - brief interpretation of relationship strength/pattern

6. **Age Group Breakdown**
   - compare relationships across age bins
   - example bins: 18–29, 30–44, 45–59, 60+

7. **Gender Breakdown**
   - compare relationships across male/female groups

8. **Strength Metrics**
   - correlation with cognitive score
   - correlation with reaction time

9. **Interpretation Notes**
   - 3 key observations
   - 1 surprising trend/threshold
   - 1 discussion question for the group

---

## Expected Outputs (Per Person)
Each member will share:
- key visuals (charts/plots)
- correlation values (cognitive score + reaction time)
- short interpretation summary
- one discussion question

---

## Collaboration Notes
Members may use any tool (Python, R, Excel, SPSS, Tableau, etc.).  
The main goal is consistency in outputs so results can be compared and combined.

We are observing relationships, not proving causation.  
**Correlation does not imply causation.**

---

## Project Timeline (Flexible Milestones)

### Week 0 (Kickoff Week)
- dataset chosen + variables assigned
- GitHub repository created
- cleaned dataset uploaded
- members added to repository

### Weeks 1–2 (EDA Phase)
By the end of Week 2, each member should aim to complete:
- distribution analysis
- cognitive score comparison
- reaction time comparison
- age group breakdown
- gender breakdown
- correlation values (cognitive score + reaction time)
- short written interpretation + discussion question

### Week 2 (Check-In Zoom)
Goal of this meeting:
- share early findings
- compare which variables show stronger patterns
- discuss surprising trends or inconsistencies
- decide what belongs in the final report
- discuss whether we want to include a predictive model

### Weeks 3–4 (Synthesis + Report Phase)
During this phase, we will:
- finalize and clean visualizations
- combine findings into a shared report
- write a final conclusions section as a group

### Weeks 4–5 (Optional Add-On: Interactive Predictor Tool)
If the group agrees, we will:
- build a simple regression model
- create an interactive tool (Streamlit)
- allow users to input habit values and view a predicted cognitive score

### Final Wrap-Up Zoom (End of Project)
Goal of this meeting:
- finalize conclusions
- finalize report formatting
- ensure GitHub repo is portfolio-ready
- confirm group credits/contributions

---

## Repository Organization
- `data/` → dataset files (raw + cleaned versions)
- `notebooks/` → each member’s analysis file (any format is fine)
- `outputs/` → exported charts, tables, and final report drafts
- `docs/` → project overview + meeting notes

---

## File Naming Suggestions

### Notebooks
Use a clear naming format such as:
- `carolina_screen_time`
- `umaima_caffeine_intake`
- `byron_exercise_time`
- `maitreya_stress_level`
- `sarah_sleep_duration`

(extensions may vary depending on tool: .ipynb, .Rmd, .xlsx, etc.)

### Figures
Use a consistent naming style such as:
- `screen_time_distribution.png`
- `screen_time_cognitive_score.png`
- `screen_time_reaction_time.png`
- `screen_time_age_breakdown.png`
- `screen_time_gender_breakdown.png`

---

## Final Deliverables (Group Output)
Our final group project will include:
- a shared insight report combining all findings
- a set of clean visualizations
- an optional interactive "Try Your Habits" predictor tool (Streamlit)

All deliverables are group-owned, and all contributors will be credited.

