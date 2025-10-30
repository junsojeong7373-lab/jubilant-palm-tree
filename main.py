import streamlit as st 
st.title('나의 웹서비스다!')
st.write('hello 빠이짜이쩬')
name=st.text_input('너의 이름은?')
if st.butten('인사말 생성'):
  st.write(name+'이야! 방가웡ㅎㅎ')
  st.balloons()
