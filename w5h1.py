import streamlit as st
import google.generativeai as genai
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

# API 키 입력받기
GOOGLE_API_KEY = st.text_input('Google API 키를 입력하세요:', type='password')
if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)

# 스트림릿 앱 제목
st.title('5W1H 기반 글쓰기 도우미')

# 5W1H 입력 받기
who = st.text_input('누가 (Who):', '')
what = st.text_input('무엇을 (What):', '')
when = st.text_input('언제 (When):', '')
where = st.text_input('어디서 (Where):', '')
why = st.text_input('왜 (Why):', '')
how = st.text_input('어떻게 (How):', '')

# 글 생성 버튼
if st.button('글 생성하기'):
    if who and what and when and where and why and how:
        # 프롬프트 템플릿 생성
        template = """
        다음 정보를 바탕으로 논리적이고 자연스러운 글을 작성해주세요:
        
        누가: {who}
        무엇을: {what}
        언제: {when}
        어디서: {where}
        왜: {why}
        어떻게: {how}
        """
        
        prompt = PromptTemplate(
            input_variables=["who", "what", "when", "where", "why", "how"],
            template=template
        )
        
        # LLM 모델 설정
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", temperature=1)
        
        # 최종 프롬프트 생성
        final_prompt = prompt.format(
            who=who,
            what=what,
            when=when,
            where=where,
            why=why,
            how=how
        )
        
        # 글 생성
        response = llm.invoke(final_prompt)
        
        # 결과 출력
        st.subheader('생성된 글:')
        st.write(response.content)
    else:
        st.warning('모든 항목을 입력해주세요.')
