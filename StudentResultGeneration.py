import streamlit as st
st.title("🎓 Student Marks Calculator")
st.write("Enter marks for 5 subjects")
sub1 = st.number_input("Subject 1 Marks", min_value=0, max_value=100)
sub2 = st.number_input("Subject 2 Marks", min_value=0, max_value=100)
sub3 = st.number_input("Subject 3 Marks", min_value=0, max_value=100)
sub4 = st.number_input("Subject 4 Marks", min_value=0, max_value=100)
sub5 = st.number_input("Subject 5 Marks", min_value=0, max_value=100)
if st.button("Calculate Result"):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    percentage = total / 5
    st.success(f"Total Marks: {total}")
    st.info(f"Percentage: {percentage}%")
    if percentage >= 90:
        st.write("Grade: A+")
    elif percentage >= 75:
        st.write("Grade: A")
    elif percentage >= 60:
        st.write("Grade: B")
    elif percentage >= 40:
        st.write("Grade: C")
    else:
        st.write("Grade: Fail")