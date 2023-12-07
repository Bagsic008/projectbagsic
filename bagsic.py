import streamlit as st


# Find more emoji's here:https://www.webfx.com/tools/emoji_cheat_sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


# ---- Header ----
with st.container():
 st.title("Bagsic Webpage :tada:")
 image_column, text_column=st.columns(2)

    #Image from a local file
with image_column:
        st.image("theia.jpg")

with text_column: 
        st.header("Hi I am Atheia Klaire Bagsic")       
        st.write("AGE: 18 years old")
        st.write("BIRTHDATE: May 07, 2005")
        st.write("I am currently studying at SNSU - Surigao Del Norte State University")   
        st.title("Hobbies")  
        st.write("I am good at:")
        st.write("Animation, Video Editing and Drawing") 
        st.write("*If you want to ask more information about me or want to make a project connected with my hobbies just get intouch with my Facebook Account")       
            
        st.write("---") 
        st.header("👉 Get In Touch With Me! 👈") 
        st.markdown("[Learn More >](https://www.facebook.com/atheaklaire.bagsic.3)")
        st.write("##")