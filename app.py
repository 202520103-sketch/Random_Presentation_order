import streamlit as st
import random

st.title("🎤 발표 순서 정하기")

# 버튼 3개
mode = st.radio("방식 선택해", ["숫자 입력", "이름 직접 입력", "txt 파일 업로드"])

names = []

# 1. 숫자 입력
if mode == "숫자 입력":
    num = st.number_input("인원 수 입력", min_value=1, step=1)

    if st.button("순서 정하기"):
        names = [f"{i+1}번" for i in range(int(num))]
        random.shuffle(names)
        st.write("👉 발표 순서:", names)

# 2. 이름 직접 입력
elif mode == "이름 직접 입력":
    input_names = st.text_area("이름을 쉼표로 구분해서 입력해 (예: 민수, 지수, 영희)")

    if st.button("순서 정하기"):
        names = [name.strip() for name in input_names.split(",")]
        random.shuffle(names)
        st.write("👉 발표 순서:", names)

# 3. txt 파일 업로드
elif mode == "txt 파일 업로드":
    file = st.file_uploader("txt 파일 업로드", type=["txt"])

    if file is not None:
        content = file.read().decode("utf-8")
        names = content.splitlines()

        if st.button("순서 정하기"):
            random.shuffle(names)
            st.write("👉 발표 순서:", names)
