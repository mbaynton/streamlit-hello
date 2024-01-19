import streamlit as st

start=st.date_input('start Date')
end=st.date_input('end Date')
if start and end:
 st.write(end-start)
