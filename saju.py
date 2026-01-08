import streamlit as st
from datetime import date
import time
import os

# 1. 페이지 설정 및 디자인 (블루나잇님 스타일 145라인 규격 완벽 유지)
st.set_page_config(page_title="사주까기 PRO - 정밀 리포트", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0f172a; color: white; }
    .stButton>button { 
        width: 100%; border-radius: 50px; 
        background: linear-gradient(45deg, #1e3a8a, #3b82f6);
        color: white; font-size: 18px; font-weight: bold; height: 3.5em;
    }
    .result-card { 
        background-color: #1e293b; padding: 25px; border-radius: 15px; 
        border: 1px solid #334155; margin-bottom: 20px; 
    }
    .consult-box { 
        background: linear-gradient(135deg, #1e293b, #0f172a); 
        padding: 40px; border-radius: 20px; border: 2px solid #facc15; 
        text-align: center; margin-top: 30px;
    }
    .streamlit-expanderHeader { 
        background-color: #1e293b !important; color: #60a5fa !important; 
        font-weight: bold !important; border-radius: 10px !important; 
        font-size: 1.1em !important;
    }
    .stInfo { background-color: #1e3a8a !important; color: white !important; }
    .stSuccess { background-color: #064e3b !important; color: #ecfdf5 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔮 사주까기 PRO - 정밀 마스터 리포트")

# 2. 정보 입력 (날짜 범위 확장 유지)
with st.sidebar:
    st.header("👤 내 정보")
    u_name = st.text_input("성명", "홍길동") 
    u_birth = st.date_input("출생일 (양력)", value=date(1980, 1, 1), min_value=date(1900, 1, 1), max_value=date(2050, 12, 31))
    u_time = st.selectbox("출생 시간", [f"{i}시" for i in range(24)] + ["모름"])
    
    st.write("---")
    is_relation = st.checkbox("👥 나로 인한 상관관계 (궁합/자녀/지인/직원채용) 함께 보기")
    
    t_name, t_birth = "", None
    if is_relation:
        st.header("👥 분석 대상 정보")
        t_name = st.text_input("대상 성명", "심청이")
        t_birth = st.date_input("대상 생년월일", value=date(2015, 1, 1), min_value=date(1900, 1, 1), max_value=date(2050, 12, 31))
        t_time = st.selectbox("대상 출생 시간", [f"{i}시" for i in range(24)] + ["모름"])
    
    st.write("---")
    go = st.button("정밀 분석 리포트 생성 🔮")

# --- [정밀 사주 분석 엔진: 오행 데이터 및 철학적 해설] ---
def get_saju_analysis(birth_date):
    day, month = birth_date.day, birth_date.month
    score = (day % 10) + (month % 12)
    # 반환 데이터셋: 오행, 강약, 성향, 진로, 비법, 행운숫자, 행운방위, 철학적해설
    if score >= 18: return "火", "신강", "열정적 리더형", "IT·예술·에너지", "시각적 학습 및 짧은 집중력", "2, 7", "남쪽", "발산하는 태양의 기운으로 예절을 중시하며 화려함을 추구하는 성품"
    elif score >= 12: return "木", "중화", "창의적 성장형", "교육·바이오·기획", "칭찬 중심의 자기주도 학습", "3, 8", "동쪽", "쭉 뻗어가는 나무처럼 인자하고 성장을 멈추지 않는 창조적 기질"
    elif score >= 7: return "金", "신약", "논리적 분석형", "금융·법학·공학", "체계적인 계획 및 정돈된 환경", "4, 9", "서쪽", "숙살지기를 품은 바위처럼 의리가 있고 결단력이 날카로운 원칙주의자"
    elif score >= 3: return "水", "신강", "심층적 사유형", "연구·심리·철학", "충분한 사유 시간 및 과정 중심", "1, 6", "북쪽", "만물을 적시는 강물처럼 지혜가 깊고 유연하며 통찰력이 뛰어난 전략가"
    else: return "土", "중화", "포용적 중재형", "상담·부동산·복지", "반복 숙달 및 안정적 환경", "0, 5", "중앙", "만물을 품는 대지처럼 신의가 두텁고 중도를 지키는 묵직한 포용력"

# 3. 분석 결과 실행
if go:
    res_area = st.container()
    with st.spinner('음양오행의 배합과 지지의 변화를 정밀 분석 중입니다...'):
        time.sleep(1)
        u_el, u_pw, u_ds, u_jb, u_tp, u_num, u_dir, u_phi = get_saju_analysis(u_birth)
        if is_relation: t_el, t_pw, t_ds, t_jb, t_tp, t_num, t_dir, t_phi = get_saju_analysis(t_birth)

    with res_area:
        st.subheader(f"✨ {u_name}님을 위한 항목별 정밀 진단")
        with st.expander("📅 1. 사주 원국 및 인생 대운 흐름", expanded=True):
            st.write(f"본인의 일간은 **{u_el}**의 기운을 타고났으며, 현재 **{u_pw}**한 상태로 지지의 변화에 따라 운의 흐름이 결정됩니다.")
        with st.expander("📜 2. 초년·중년·말년 평생운 총평"):
            st.write(f"**{u_ds}**의 특성이 강하며 인성(印星)의 조화가 이루어지는 중년 이후 대발하는 사주입니다.")
        with st.expander("📅 3. 2026년(丙午년) 1년 상세 총운"):
            st.success(f"2026년 병오년은 {u_name}님의 {u_el} 기운과 반응하여 문서와 명예운이 상승하는 해입니다.")
        
        # [복구 완료] 4. 내 아이의 공부 DNA (상세 설명 구조 원상복구)
        with st.expander("🎓 4. 내 아이의 공부 DNA (성향/진로/비법)", expanded=True):
            if is_relation:
                st.info(f"📍 분석 대상: {t_name} / 오행 기운: {t_el}")
                c1, c2 = st.columns(2)
                with c1:
                    st.markdown(f"### 🧠 공부 성향: **{t_ds}**")
                    st.write(f"- **타고난 기질:** {t_phi}")
                    st.markdown(f"### 🏛️ 추천 전공 및 진로")
                    st.write(f"- **추천 전공:** {t_jb} 관련 학과")
                with c2:
                    st.markdown("### 📅 최적의 공부 시기")
                    st.success("청소년기 대운의 흐름이 학업 성취에 매우 유리함")
                    st.markdown("### ⚡ 집중력 강화 비법")
                    st.warning(f"**학습 전략:** {t_tp}")
            else: st.write("아이 정보를 입력하시면 정밀 리포트가 생성됩니다.")

        with st.expander("📆 5. 2026년 월별 세부 흐름"):
            monthly_desc = ["1월: 새로운 계획 구체화", "2월: 주변 도움으로 활로", "3월: 문서/계약운 강세", "4월: 이동수 발생 주의", "5월: 재물운 안정 시기", "6월: 기초 공사 단계", "7월: 대인관계 화합 중요", "8월: 명예 및 인정 상승", "9월: 내실 기하는 시기", "10월: 실속 챙기는 달", "11월: 건강 관리 유의", "12월: 풍요로운 마무리"]
            cols = st.columns(3)
            for i, desc in enumerate(monthly_desc): cols[i % 3].write(f"**{desc}**")
        with st.expander("🍀 6. 오늘의 운세 (행운 분석)"):
            st.info(f"**{u_el}** 기운에 이로운 행운의 숫자 **[{u_num}]**번과 **[{u_dir}]** 방위를 적극 활용하세요.")
        if is_relation:
            with st.expander(f"👥 7. {u_name}님과 {t_name}님의 상관관계"):
                st.success(f"두 분은 서로의 용신을 돕는 상생의 인연입니다.")
        else:
            with st.expander("✨ 7. 재물·건강·연애·직업운 상세 분석"):
                st.write(f"현재 {u_pw}한 기질에 맞춰 재물운과 건강운의 균형을 유지하십시오.")

        # [8번 항목 철학적 심화 유지]
        with st.expander("🐯 8. 개인 기운 분석", expanded=True):
            st.markdown(f"### 🧬 오행 분포 기반 **{u_name}** 님만의 고유 기질")
            st.write(f"**[{u_el}]** 기운을 중심으로 분석한 철학적 해설: {u_phi}")
            st.write(f"본인의 사주 원국은 **{u_pw}**한 기세를 띄고 있으며, 이는 **{u_ds}**로서의 강력한 실천력 혹은 통찰력을 뒷받침하는 근간이 됩니다.")

        with st.expander("📝 9. 사주까기의 특별 조언"):
            st.warning("일간의 강약을 조절하여 복을 부르는 개운법을 실천해 보세요.")

        # --- [상담 섹션: PC/배포 모두 작동하는 이중 경로] ---
        st.markdown("---")
        st.markdown("""
            <div class='consult-box'>
                <h2 style='color: #facc15;'>🔮 아직 풀리지 않은 "대운의 비밀과 해석이" 궁금하신가요?</h2>
                <p style='font-size: 1.2em; color: white; margin-top: 10px;'>
                    그러시다면 지금 <b>QR을 스캔</b> 하세요
                </p>
            </div>
        """, unsafe_allow_html=True)

        _, col_qr, _ = st.columns([1.2, 1, 1.2]) 
        with col_qr:
            # 1. 배포용 (같은 폴더)
            qr_path = "my_QR.jpg"
            # 2. PC용 백업 (바탕화면)
            desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "my_QR.jpg")
            
            if os.path.exists(qr_path):
                st.image(qr_path, width=300)
                st.markdown("<p style='text-align: center; font-weight: bold; color: #facc15; font-size: 1.2em;'>사주까기 전문가 상담 QR</p>", unsafe_allow_html=True)
            elif os.path.exists(desktop_path):
                st.image(desktop_path, width=300)
                st.markdown("<p style='text-align: center; font-weight: bold; color: #facc15; font-size: 1.2em;'>사주까기 전문가 상담 QR</p>", unsafe_allow_html=True)
            else:
                st.info("⚠️ 'my_QR.jpg' 사진을 이 폴더나 바탕화면에 넣어주세요.")

st.write("---")
st.info("💡 본 리포트는 블루나잇 블루나잇님의 음양오행 정밀 알고리즘을 바탕으로 생성되었습니다.")