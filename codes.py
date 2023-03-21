import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
st.set_page_config(page_title="WELCOME",page_icon=":four_leaf_clover:",layout='wide')
def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code !=200:
        return None
    return r.json()
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

lottie_coding=load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_nDKE8Z.json")
with st.container():
 st.subheader("Presenting you")
st.title("CROP PRICE PREDICTION")
st.write("Find accurate predicted prices for your crops!")
st.write("[Learn more>>](https://www.sciencedirect.com/science/article/pii/S0168169920302301)")
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write("""By specifying commodity name, state, district, market, min_price, max_price, modal_price; we are able to obtain the most accurate predicted price for this fresh data which will ease the decision taking of the needy farmers whether to sell the crop for profit or not.
""")
        #st.write()
        with right_column:
            st_lottie(lottie_coding,height=300,key="coding")
with st.container():
    st.write("---")
    st.header("Contact us!")
    st.write("##")
    contact_form="""<form action="https://formsubmit.co/etishrees04@gmail.com" method="POST">
     <input type="text" name="Your name" required>
     <input type="email" name="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>"""
left_column,right_column=st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()