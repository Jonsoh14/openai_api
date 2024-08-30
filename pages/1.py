import streamlit as st
with st.echo():
    name = st.text_input("이름 입력하시오.")

    if st.button("저장"):
        st.write(f"{name} 저장 완료.")
        st.session_state["이름"] = name
        #st.session_state.이름 = name