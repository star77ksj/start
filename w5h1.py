import streamlit as st
from langchain_google_genai import GoogleGenerativeAI  # 올바른 모듈 경로로 수정

# 사용자로부터 API 키 입력받기
api_key = st.text_input('Enter your Gemini API Key:', type='password')

# 6하 원칙 입력받기
who = st.text_input('Who:')
what = st.text_input('What:')
when = st.text_input('When:')
where = st.text_input('Where:')
why = st.text_input('Why:')
how = st.text_input('How:')

# 생성 버튼
if st.button('Generate'):
    if api_key:
        # Gemini API 호출
        gemini = GoogleGenerativeAI(model="gemini-pro", google_api_key=api_key)
        prompt = f"Who: {who}\nWhat: {what}\nWhen: {when}\nWhere: {where}\nWhy: {why}\nHow: {how}"
        result = gemini.invoke(prompt)
        
        # 결과 출력
        st.write('Generated Text:')
        st.write(result)
    else:
        st.error('Please enter your Gemini API Key.')
