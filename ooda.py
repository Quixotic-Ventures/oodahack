import streamlit as st
import pandas as pd

df = pd.read_csv('data_with_title.csv')

st.sidebar.title('Documents Loaded')

for index, row in df.iterrows():
    if st.sidebar.button(row['title']):
        # st.write(f"You clicked on: {row['url']}")
        st.sidebar.write(row['url'])

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

tactic = st.selectbox('Select a tactic', ['Initial Access', 'Execution', 'Persistence', 'Privilege Escalation', 'Defense Evasion', 'Credential Access', 'Discovery', 'Lateral Movement', 'Collection', 'Command and Control', 'Exfiltration', 'Impact'])