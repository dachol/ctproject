import streamlit as st
import pandas as pd #data frame 모듈
# import plotly.figure_factory as ff
import plotly.express as px # 더 많이 쓰는 코드(동적임)
# import matplotlib.pyplot as plt 정적인 데이터 시각화 코드

# global variable 전역변수 선언
url="https://youtu.be/XyEOEBsa8I4"

# data app
df = pd.read_csv('./data/data.csv') #data frame
df = pd.DataFrame({
    "name": ["kim", "lee", "park","cho"],
    "grade": [2, 2, 2, 2],
    "number": [1, 2, 3, 4],
    "kor":[90,90,90,100],
    "math":[90,90,100,90],
    "eng":[90,90,100,80],
    "info":[100,100,100,100]
})

df_melted = df.melt(id_vars=["name"], value_vars=["kor", "math", "eng", "info"],
                    var_name="과목", value_name="점수")

fig = px.bar(df_melted, x="과목", y="점수", color="name", barmode="group", title="과목별 점수")

st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url) #직접 주소 넣어도 되지만, 변수로 부르기

    with st.expander('Content2...'):
        st.subheader('Content2...')
        st.dataframe(df) #st.table(df)로 해도 됨.
        #st.plotly_chart(df)
        #dff=df.groupby(by='name').sum()
        #st.table(dff)
        st.plotly_chart(fig)
        
with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')
