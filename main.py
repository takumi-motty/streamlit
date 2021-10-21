
import streamlit as st
import time


st.title('Streamlit 超入門')

st.write('Progress Bar')
'Start!!'

latest_iteration = st.empty()

bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!'

left_column, right_column = st.beta_columns(2)

button = left_column.button('右からむに文字を表示')
if button:
    right_column.write('右カラム')

expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# text= st.text_input('書いてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# '書いた事柄は,',text, 'です。'
# 'コンディション：', condition
