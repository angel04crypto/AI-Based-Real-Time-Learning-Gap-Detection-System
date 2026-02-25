import streamlit as st
from concepts import concepts
from ai_logic import analyze_explanation,find_missing_keywords

st.title("AI-Based Real-Time Learning Gap Detector")
tab1, tab2 = st.tabs(["Concept Analysis", "Focus Area"])

# Select subject
with tab1:
    subject = st.selectbox("Select Subject", list(concepts.keys()))

# Select topic
    topic = st.selectbox("Select Topic", list(concepts[subject].keys()))

    student_input = st.text_area(
        "Explain the selected topic in your own words:",
        height=150
    )

    if st.button("Analyze Understanding"):
        if student_input.strip() == "":
            st.warning("Please enter your explanation.")
        else:
            reference = concepts[subject][topic]
            similarity, level, feedback = analyze_explanation(student_input, reference)

            st.subheader("Confidence Meter")
            st.progress(float(similarity))
            st.write(f"Confidence Score: {round(similarity*100, 1)}%")
            

            st.subheader("Analysis Result")
            st.write(f"Understanding Level: {level}")
            st.write(f"Similarity Score: {round(similarity, 2)}")
            st.write(f"Feedback: {feedback}")

            if level != "Good Understanding":
                st.info("Correct Explanation")
                st.write(reference)

with tab2:
    st.header("Where Should You Focus?")

    if 'similarity' in locals():

        missing = find_missing_keywords(student_input, reference)

        if similarity >= 0.75:
            st.success("Great work! Only minor revision needed.")
            st.write("Focus on refining your explanation clarity.")

        elif similarity >= 0.5:
            st.warning("You need to strengthen your understanding.")
            st.write("Suggested focus areas:")
            st.write(", ".join(missing))

        else:
            st.error("Significant learning gap detected.")
            st.write("You should focus on these key concepts:")
            st.write(", ".join(missing))

            st.info("Recommendation: Review the correct explanation carefully.")
    else:
        st.info("Run analysis first in the Concept Analysis tab.")