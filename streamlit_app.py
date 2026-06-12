import streamlit as st

# 1. 품새 목록 정의
품새목록 = ['태극1장', '태극2장', '태극3장']

# 2. 앱 제목 및 상단 디자인
st.title("🥋 태권도 심사 프로그램")
st.subheader("품새 목록")

# 품새 목록을 이쁘게 가로로 나열
cols = st.columns(len(품새목록))
for i, 품새 in enumerate(품새목록):
    cols[i].success(품새)

st.divider()  # 구분선

# 3. 심사 점수 입력 (0~100점 제한)
st.write("### 📝 심사 결과 확인")
심사_점수 = st.number_input(
    '심사 점수를 입력하시오 (0 ~ 100):', 
    min_value=0, 
    max_value=100, 
    value=80,  # 기본값
    step=1
)

# 슬라이더로도 조절하고 싶다면 아래 코드 주석을 해제하세요.
# 심사_점수 = st.slider('심사 점수를 선택하세요:', 0, 100, 80)

# 4. 합격 / 불합격 조건문 및 결과 출력
if st.button('결과 조회하기'):
    if 심사_점수 >= 80:
        st.balloons()  # 축하 효과 애니메이션
        st.success(f"🎉 축하합니다! {심사_점수}점으로 **합격**입니다!")
    else:
        st.error(f"😢 아쉽습니다. {심사_점수}점으로 **불합격**입니다. 조금 더 연습해봐요!")