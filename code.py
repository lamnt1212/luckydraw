import streamlit as st
import pandas as pd

st.set_page_config(
    initial_sidebar_state="collapsed"
    ,page_title="Lucky Draw"
    ,page_icon= ":slot_machine::"
    ,layout="centered")
st.header('Lucky Draw')
url = r'https://docs.google.com/spreadsheets/d/e/2PACX-1vSvbcJfhWi9yeviKzvF4HzNXTqggyMfXrQDiFEIf_eaAarC5q6IvVA_NHHQpS367irp7Wk1NW5X-9ak/pub?output=xlsx'
df=pd.read_excel(url,sheet_name='Sheet1',dtype={'Sdt':str,'Số may mắn':int})
with st.form("Lucky Draw"):
    sdt_input = st.text_input("Nhập số điện thoại của bạn")
    filtered_df = df[(df['sdt'] == sdt_input)]
    submit = st.form_submit_button("Rút số may mắn")
if submit and len(filtered_df)>0:
    st.success('Con số may mắn của bàn là: ' + str(filtered_df['luckynumber'].iloc[0]),icon='🎉')
    st.toast('Anh/chị vui lòng lưu lại ảnh hoặc ghi nhớ con số này',icon ='🎉')
elif submit and len(filtered_df)==0:
    st.error("Sdt không nằm trong danh sách",icon='🚨')
else:
    pass
sidebar_collapsed ="""
    <style>
        [data-testid="collapsedControl"] {display: none}
    </style>
    """
st.markdown(sidebar_collapsed, unsafe_allow_html=True,)

hide_streamlit_style ="""
            <style> 
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://i.ibb.co/C6rKrbk/FB-IMG-1703430257016.jpg");
    }
   </style>
    """,
    unsafe_allow_html=True
)
