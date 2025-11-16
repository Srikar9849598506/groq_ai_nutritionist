import streamlit as st

from justcode import user_number_check

number=st.number_input("Enter the user number:", min_value=0, max_value=100, step=1)
if st.button("Check User Level"):
    result=user_number_check(number)
    st.write(result)
    