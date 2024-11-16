import streamlit as st
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core import prompts


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
    try:
        if not api_key:
            st.error('API 키를 입력해주세요.')
            st.stop()
            
        # Gemini 모델 설정
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash-002", google_api_key=api_key)
        
        # 입력값 검증
        if not (who and what and when and where and why and how):
            st.warning('모든 항목을 입력해주세요.')
            st.stop()
            
        # 프롬프트 템플릿 생성
        template = """Who: {who}
What: {what}
When: {when}
Where: {where}
Why: {why}
How: {how}"""

        prompt = prompts.PromptTemplate(
            template=template,
            input_variables=["who", "what", "when", "where", "why", "how"]
        )
        
        # 프롬프트 생성 및 결과 얻기
        final_prompt = prompt.format(who=who, what=what, when=when, where=where, why=why, how=how)
        result = llm.invoke(final_prompt)
        
        # 결과 출력
        st.write('생성된 텍스트:')
        st.write(result.content)
        
    except Exception as e:
        st.error(f'오류가 발생했습니다: {str(e)}')
