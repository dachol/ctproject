import streamlit as st
import pandas as pd
import plotly.express as px  # 동적 시각화용

# 전역 변수
url = "https://youtu.be/XyEOEBsa8I4"

# 데이터 로드
df = pd.read_csv('./data/data.csv')

# 학생별 총점 컬럼 추가
df['total'] = df[['kor', 'math', 'eng', 'info']].sum(axis=1)

# 웹앱 제목
st.title('This is my first webapp!')

col1, col2 = st.columns((4, 1))

with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url)

    with st.expander('Content2...'):
        st.subheader('학생별 성적 데이터')
        st.dataframe(df)

        # 학생별 총점 그래프
        fig_total = px.bar(df, x='name', y='total', title='학생별 총점')
        st.plotly_chart(fig_total)

        # 과목별 평균 그래프 (데이터를 전치해서 시각화)
        subject_avg = df[['kor', 'math', 'eng', 'info']].mean().reset_index()
        subject_avg.columns = ['subject', 'average_score']
        fig_subject = px.bar(subject_avg, x='subject', y='average_score', title='과목별 평균 점수')
        st.plotly_chart(fig_subject)

with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')
        st.write("✔ 학생별 성적 비교\n✔ 과목별 학급 평균 확인\n✔ Plotly 시각화 활용")