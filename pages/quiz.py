import streamlit as st

# Streamlit 애플리케이션 제목
st.title("한국 정치 퀴즈")

# 문제와 선택지
question = "다음 중 대한민국의 최초 여성 대통령은 누구인가요?"
options = ["박근혜", "문재인", "이명박", "김대중"]

# 사용자에게 문제와 선택지를 표시
st.write(question)

# 라디오 버튼을 사용하여 선택지 제공
selected_option = st.radio("답을 선택하세요:", options)

# 정답 확인 버튼
if st.button("정답 확인"):
    # 정답
    correct_answer = "박근혜"
    
    if selected_option == correct_answer:
        st.write("정답입니다! 박근혜가 대한민국의 최초 여성 대통령입니다.")
    else:
        st.write(f"틀렸습니다. 정답은 {correct_answer}입니다.")

# 추가적인 설명
st.write("박근혜는 2013년부터 2017년까지 대한민국의 제11대 대통령을 역임했습니다.")
