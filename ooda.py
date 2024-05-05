import streamlit as st


st.sidebar.title('OODA')

name = st.sidebar.text_input('Pull in additional data', help="please enter the URL")

uploaded_file = st.sidebar.file_uploader("Add additional PDFs", type=["pdf"])

st.sidebar.button('Filter')


st.title('Trending Topics')

one = st.button('Topic 1')
two = st.button('Topic 2')
three = st.button('Topic 3')

if one: 
    st.write('Summary of Topic 1')
    st.write('Sources')

# insert divider line
st.write('---------------------------------------------------------------------------------')
st.title('MITRE Tactics and Techniques')