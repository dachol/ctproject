import streamlit as st
import pandas as pd #data frame 모듈
# import plotly.figure_factory as ff
#import plotly.express as px # 더 많이 쓰는 코드(동적임)
# import matplotlib.pyplot as plt 정적인 데이터 시각화 코드

# global variable 전역변수 선언
url="https://youtu.be/XyEOEBsa8I4"

st.set_page_config(layout='wide',page_title="My App") # 위젯 레이아웃 수정 코드 

# html variable
html='''
<html>
    <head>
        <title>This HTML App</title>
    </head>
    <body>
        <h1>This Long Text!!!</h1>
        <br>
        <hr>
        <h3>This a small text</h3>
    </body>
</html>
'''

with open('./leaf_html.html','r', encoding='utf-8') as f:
    filehtml=f.read()
    f.close()

# data app
df = pd.read_csv('./data/data.csv') #data frame

st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url) #직접 주소 넣어도 되지만, 변수로 부르기

    with st.expander('Content2_image..'):
        st.subheader('Content2_image..')
        st.image('./images/catdog.jfif')
        st.write('<h1>This is new title</h1>', unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)

    with st.expander('Content3_htmlContent..'): #ai X form을 통해 만든 웹소스코드를 그대로 붙여넣어 위젯 추가
        st.subheader('Content3_htmlContent..')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml,height=800)

       # st.dataframe(df) #st.table(df)로 해도 됨.
        #st.plotly_chart(df)
        #dff=df.groupby(by='name').sum()
        #st.table(dff)
        #st.plotly_chart(df)
        
with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')
