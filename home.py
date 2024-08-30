#pip install streamlit
import streamlit
"안녕하세요? 반갑습니다."
#streamlit run home.py
10
import streamlit as st

with st.echo():
    a, b = 3, 7
    st.write(f'{a}+{b}={a*b}')


print(1)
with st.echo():
    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")

import streamlit as st

st.title("Hello, :rocket:")
st.header("스트림릿 설치")
st.write("# Welcome to Streamlit! :star2:")
st.code("pip install streamlit")

with st.echo():
    import streamlit
    st.write("Hi, Welcome.")
