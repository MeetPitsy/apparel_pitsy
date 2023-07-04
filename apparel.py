import streamlit as st
from deta import Deta
import datetime

# Initialize Deta with your project key
deta = Deta('b0u5qbektag_2v3XHsha7iGaJ99d5Rrbv3X4StgkGQJ2')
db = deta.Base('pitsy')  # use 'pitsy' as your database name

st.title('Company Apparel Form')

with st.form('apparel_form'):
    st.markdown("## 🙋 What is your name?")
    name = st.text_input('', placeholder='Your Name')
    
    st.markdown("## 📧 What is your email?")
    email = st.text_input('', placeholder='Your Email')
    
    st.markdown("## 💵 What is your budget for the company apparel?")
    budget = st.number_input('', value=0, min_value=0, format='%d', step=1)
    
    st.markdown("## 👕 What type of apparel are you interested in?")
    apparel_type = st.text_input('', placeholder='Apparel Type')
    
    st.markdown("## 📦 How many units of each item do you need?")
    units = st.number_input('', value=1, min_value=1, format='%d', step=1)
    
    st.markdown("## 🕒 What is your target timeline for completion?")
    timeline = st.date_input('', value=datetime.datetime(2023, 7, 4))
    
    st.markdown("## 👥 Who is the intended audience for this apparel?")
    audience = st.text_input('', placeholder='Intended Audience')
    
    st.markdown("## 🎨 Do you have specific branding guidelines we should adhere to?")
    branding = st.text_input('', placeholder='Branding Guidelines')
    
    st.markdown("## ✏️ Do you already have a design or logo, or will design services be needed?")
    design_needed = st.selectbox('', ('Yes', 'No'))
    
    st.markdown("## 🏷️ What quality standards are you expecting for the apparel?")
    quality = st.text_input('', placeholder='Quality Standards')
    
    st.markdown("## 🌈 Are there specific colors you want to use in the apparel to match your branding?")
    colors = st.text_input('', placeholder='Specific Colors')
    
    st.markdown("## 🎁 Are there any special features you want the apparel to have?")
    special_features = st.text_input('', placeholder='Special Features')
    
    submitted = st.form_submit_button('Submit')
    if submitted:
        # store the responses in Deta database
        db.put({
            'name': name,
            'email': email,
            'budget': budget,
            'apparel_type': apparel_type,
            'units': units,
            'timeline': str(timeline),
            'audience': audience,
            'branding': branding,
            'design_needed': design_needed,
            'quality': quality,
            'colors': colors,
            'special_features': special_features,
        })
        st.write("Form has been submitted successfully!")
