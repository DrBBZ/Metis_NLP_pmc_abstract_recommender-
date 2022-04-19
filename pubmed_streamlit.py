




import streamlit as st

    
st.title("A Journal Recommendation System For Vegetarian/Plant-Based Diet")
st.header("This system recommends top 5 PubMed Central journal articles that interests you")
st.subheader("Enter topics that interests you:")
st.selectbox("Condition", ['vegan', 'vegetarian', 'plant-based'], index=1)
if st.button("Recommend Me:"):
    st.write("The Top 5 Suggested Articles Are:")
st.text("Disclaimer: \nThis system and its recommendations are not official medical advice. \nPlease use at your own risk.")

