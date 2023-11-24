import streamlit as st
import pandas as pd
import altair  as alt
from PIL import Image

st.title("Nathaly Segura")

#Elevator Pitch. your branding
st.subheader("The data lover")

col1,col2 = st.columns([3,1])
with col1:
    st.subheader("About me")
    st.text("Passionate about the power of data to drive insights.")
with col2:
    #Add an image
    image = Image.open('me.jpg')
    st.image(image,width = 250)

st.sidebar.caption('Wish to connect?')
st.sidebar.write('xyz@gmail.com')
pdf_file = open('NathalySeguraSanchezCone.pdf','rb')
st.sidebar.download_button('Download Resume',pdf_file,file_name='NathalySeguraSanchezCon.pdf',mime='pdf')

#Experience
st.subheader("Relevant experience")
experience_table = pd.DataFrame({
    "Job Title" : ["Data Analyst","Data Specialist"],
    "Company" : ["Major's Office", "AXA Colpatria"],
    "Job Description" : ["sssss","yerdbjfdnv"]
})
experience_table = experience_table.set_index('Job Title')
st.table(experience_table)

#Project GRID
st.subheader("Projects")
titanic = pd.read_csv('titanic.csv')
interval = alt.selection_interval()
scatter = alt.Chart(titanic).mark_point().encode(
    alt.X('Age'),
    alt.Y('Fare')
    color=alt.condition(interval,'Sex',alt.value('lightgray'))
).interactive()
scatter

