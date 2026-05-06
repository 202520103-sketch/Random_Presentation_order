%%writefile app.py

import streamlit as st
import random
import pandas as pd # To read uploaded files easily

st.set_page_config(layout="centered", page_title="발표 순서 랜덤 생성기")

st.title('발표 순서 랜덤 생성기')
st.write('발표자 정보를 입력하고 랜덤으로 순서를 생성합니다.')

# Initialize session state for input_method if not already set
if 'input_method' not in st.session_state:
    st.session_state.input_method = None

st.write("어떻게 발표자를 입력하시겠습니까?")
col1, col2, col3 = st.columns(3)

with col1:
    if st.button('1. 인원수 입력'):
        st.session_state.input_method = '인원수 입력'
with col2:
    if st.button('2. 이름 직접 입력'):
        st.session_state.input_method = '이름 직접 입력'
with col3:
    if st.button('3. 파일에서 읽기'):
        st.session_state.input_method = '파일에서 읽기'

# Use the selected input method from session state
input_method = st.session_state.input_method

participants = []

if input_method == '인원수 입력':
    st.subheader('인원수 입력')
    num_participants = st.number_input('발표에 참여할 인원수를 입력해주세요 (양의 정수):', min_value=1, value=5, step=1)
    if num_participants > 0:
        participants = list(range(1, num_participants + 1))

elif input_method == '이름 직접 입력':
    st.subheader('이름 직접 입력')
    names_input = st.text_area('발표자 이름을 쉼표(,) 또는 줄바꿈으로 구분하여 입력해주세요 (예: 김철수, 이영희, 박지성):')
    if names_input:
        # Split by comma or newline and clean up names
        names_list = [name.strip() for name in names_input.replace('\n', ',').split(',') if name.strip()]
        if names_list:
            participants = names_list
        else:
            st.warning("유효한 이름이 입력되지 않았습니다.")

elif input_method == '파일에서 읽기':
    st.subheader('파일에서 읽기')
    uploaded_file = st.file_uploader("발표자 이름이 한 줄에 하나씩 적힌 텍스트 파일 (.txt) 또는 CSV 파일 (.csv)을 업로드해주세요.", type=["txt", "csv"])
    if uploaded_file is not None:
        try:
            if uploaded_file.name.endswith('.txt'):
                string_data = uploaded_file.read().decode('utf-8')
                names_list = [name.strip() for name in string_data.split('\n') if name.strip() and not name.startswith('#')]
                if names_list:
                    participants = names_list
                else:
                    st.warning("업로드된 파일이 비어있거나 유효한 이름이 없습니다. 주석(#)이 아닌 이름을 입력해주세요.")
            elif uploaded_file.name.endswith('.csv'):
                df = pd.read_csv(uploaded_file, header=None)
                # Assume names are in the first column
                names_list = df.iloc[:, 0].astype(str).tolist()
                names_list = [name.strip() for name in names_list if name.strip()]
                if names_list:
                    participants = names_list
                else:
                    st.warning("업로드된 CSV 파일이 비어있거나 유효한 이름이 없습니다.")
        except Exception as e:
            st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")

# Only show the 'Generate Order' button if an input method has been selected
if input_method is not None:
    if st.button('발표 순서 생성') and participants:
        st.subheader('생성된 발표 순서:')
        random.shuffle(participants)
        for i, participant in enumerate(participants):
            st.write(f"{i+1}번째 발표자: {participant}")
    elif st.button('발표 순서 생성') and not participants:
        st.warning("발표자가 한 명도 없습니다. 위에서 발표자 정보를 입력해주세요.")
