import streamlit as st
import random

# 기본 설정
st.set_page_config(page_title="발표 순서 정하기", page_icon="🎤", layout="centered")

# 스타일 (CSS)
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    color: white;
}
.stButton>button {
    background-color: #ff4b5c;
    color: white;
    border-radius: 10px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
.result-box {
    background-color: rgba(255,255,255,0.1);
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 제목
st.markdown('<div class="title">🎤 발표 순서 뽑기</div>', unsafe_allow_html=True)
st.write("")

# 모드 선택 (카드 느낌)
mode = st.radio("방식 선택", ["🎲 숫자 입력", "✍️ 이름 입력", "📄 파일 업로드"])

names = []

# 결과 출력 함수
def show_result(names):
    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    for i, name in enumerate(names, start=1):
        st.write(f"**{i}번 👉 {name}**")
    st.markdown('</div>', unsafe_allow_html=True)

# 1. 숫자 입력
if mode == "🎲 숫자 입력":
    num = st.number_input("인원 수", min_value=1, step=1)

    if st.button("✨ 순서 뽑기"):
        names = [f"{i+1}번 사람" for i in range(int(num))]
        random.shuffle(names)
        show_result(names)

# 2. 이름 입력
elif mode == "✍️ 이름 입력":
    input_names = st.text_area("이름 입력 (쉼표로 구분)")

    if st.button("✨ 순서 뽑기"):
        names = [name.strip() for name in input_names.split(",") if name.strip()]
        random.shuffle(names)
        show_result(names)

# 3. 파일 업로드
elif mode == "📄 파일 업로드":
    file = st.file_uploader("txt 파일 업로드", type=["txt"])

    if file is not None:
        content = file.read().decode("utf-8")
        names = content.splitlines()

        if st.button("✨ 순서 뽑기"):
            random.shuffle(names)
            show_result(names)
