import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="My Webpage", page_icon=':ocean:', layout='wide')

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Assets
lottie_coding = 'https://assets9.lottiefiles.com/packages/lf20_xRmNN8.json'

# Header Section
with st.container():
    st.subheader('Hi, I am Lothar :wave:')
    st.title('An ERP Solution Administrator and Python Programmer from Namibia')
    st.write("I am passionate about finding ways to use Python and automation to be more efficient and effective in business settings")
    st.write('[GitHub >](https://github.com/lothartj)')
    st.write('[LinkedIn >](https://www.linkedin.com/in/lothar-tjipueja-a491b8271/)')

# What I do
with st.container():
    st.write('''As an ERP solution administrator and Python automation programmer, I have acquired a unique set of skills that enable me to streamline and optimize business processes.
              Through my expertise in ERP systems, I am able to ensure the smooth functioning of critical business operations. Furthermore, my proficiency in Python programming allows
              me to automate tasks and workflows, leading to increased efficiency and productivity. My ability to combine these two areas of expertise makes me an invaluable asset to any 
              organization seeking to improve its operational efficiency and effectiveness.''')
    
# Right Column
right_column = st.container()
with right_column:
    st_lottie(load_lottie(lottie_coding), speed=1, width=600, height=600, key='coding')

# Projects Section
with st.container():
    st.write('___')
    st.header('My Projects')
    st.write('##')
    image_column, text_column = st.columns((1,1))
    with image_column:
        # insert image here
        pass
    with text_column:
        st.subheader('Integrate Lottie Animations Inside Your Streamlit App')
        st.write('''This project demonstrates how to use Lottie animations in your Streamlit app using the 'streamlit-lottie' package. Lottie animations are a great way to 
                    add eye-catching visuals to your app and make it more engaging.''')
