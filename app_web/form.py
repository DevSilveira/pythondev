import streamlit as st
import data

st.title("Movies")

name = st.text_input("Movie's name:")
year = st.number_input("Movie's release year:", min_value=1960, max_value=2025)
score = st.slider("Movie's score:", min_value=0.0, max_value=10.0)

if st.button("Add"):
    data.insert_data(name, year, score)
    st.success("Movie was registered!")

movies = data.get_data()
st.header("Movies List")
st.table(movies)
