import streamlit as st

st.title('サンプルアプリ')
num = st.slider('数値を選んでください', 0, 100)
st.write(f'あなたが選んだ数値は {num} です！')
