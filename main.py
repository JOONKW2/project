import streamlit as st

# 페이지 설정
st.set_page_config(
    page_title="Global Cybersecurity Threats Dashboard",
    page_icon="🛡️",
    layout="wide"
)

# 제목 섹션
st.markdown("<h1 style='text-align: center; color: #007ACC;'>🛡️ 국가별 · 연도별 사이버 공격 유형과 그 영향 🛡️</h1>", unsafe_allow_html=True)
st.markdown("### 👥 팀 프로젝트 by 20704 권준성, 21025 이서준, 20707 김용현", unsafe_allow_html=True)
st.markdown("---")

# 소개 섹션
st.markdown("#### 📌 프로젝트 소개")
st.write("""
본 프로젝트는 2015년부터 2024년까지 전 세계에서 발생한 사이버 공격 데이터를 분석하여,  
국가별 및 연도별 사이버 위협의 유형과 그 영향을 시각적으로 보여주는 것을 목표로 합니다.
""")

# 분석 항목 요약
st.markdown("#### 🔍 주요 분석 항목")
st.markdown("""
- 📅 **연도별 사이버 공격 추세**  
- 🌐 **국가별 피해 규모 및 사용자 영향**  
- 💥 **공격 유형별 발생 빈도 및 피해 규모**  
- 🛠️ **사용된 보안 취약점과 방어 기술**  
- ⏱️ **사건 해결까지 걸린 시간 분석**
""")

# 데이터 출처 요약
st.markdown("#### 📂 데이터 개요")
st.write("""
- 데이터 범위: **2015년 ~ 2024년**
- 포함 정보: 국가, 연도, 공격 유형, 피해 산업, 금전적 손실, 영향 사용자 수, 취약점 유형 등
""")

# 하단 크레딧
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>© 2025 CyberSec Team Project</div>", unsafe_allow_html=True)
