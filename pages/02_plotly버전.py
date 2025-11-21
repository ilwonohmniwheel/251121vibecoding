# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# 설정
# -------------------------
st.set_page_config(page_title="MBTI by Country 🌍", layout="wide")
st.title("MBTI 비율 상/하위국가 보기 📊")
st.markdown("MBTI 유형을 선택하면 해당 유형의 비율이 높은 상위 10개국과 낮은 10개국을 인터랙티브한 막대그래프로 보여줍니다. ✨")

# 데이터 경로 (업로드된 파일의 로컬 경로를 사용)
DATA_URL = "/mnt/data/countriesMBTI_16types.csv"

# -------------------------
# 데이터 로드
# -------------------------
@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    # 기대되는 포맷: 첫 열 Country, 나머지 16개 MBTI 컬럼 (소수 비율)
    return df

df = load_data(DATA_URL)

# 컬럼 검증/정렬
all_columns = list(df.columns)
if "Country" not in df.columns:
    st.error("데이터에 'Country' 열이 없습니다. 파일 포맷을 확인해주세요.")
    st.stop()

mbti_columns = [c for c in all_columns if c != "Country"]
mbti_columns_sorted = sorted(mbti_columns)  # 보기 편하게 정렬

# 사이드바 컨트롤
with st.sidebar:
    st.header("설정")
    selected_mbti = st.selectbox("MBTI 유형 선택", mbti_columns_sorted, index=0)
    top_n = st.slider("표시할 국가 수 (상/하)", min_value=5, max_value=20, value=10, step=1)
    sort_by = st.radio("정렬 방식", ("값 내림차순 (기본)", "값 오름차순"), index=0)
    st.markdown("---")
    st.markdown("데이터 파일: `/mnt/data/countriesMBTI_16types.csv`")
    st.caption("※ 필요시 원본 CSV로 교체하세요.")

# -------------------------
# 데이터 처리
# -------------------------
# 선택 컬럼 존재 확인
if selected_mbti not in df.columns:
    st.error(f"선택한 MBTI({selected_mbti}) 컬럼이 데이터에 없습니다.")
    st.stop()

# 정렬 및 상위/하위 추출
df_sorted_desc = df.sort_values(by=selected_mbti, ascending=False).reset_index(drop=True)
top_df = df_sorted_desc.head(top_n).copy()
bottom_df = df_sorted_desc.tail(top_n).copy().sort_values(by=selected_mbti, ascending=True)

# 그래프 그리기 함수
def make_bar(df_bar, mbti_col, title):
    fig = px.bar(
        df_bar,
        x=mbti_col,
        y="Country",
        orientation="h",
        text=mbti_col,
        hover_data={mbti_col:":.4f"},
    )
    fig.update_traces(texttemplate="%{text:.4f}", textposition="outside")
    fig.update_layout(
        title=title,
        yaxis=dict(autorange="reversed"),  # 상단부터 내림차순으로 보이게
        margin=dict(l=160, r=20, t=60, b=20),
        height=450,
    )
    fig.update_xaxes(title_text="비율 (proportion)")
    fig.update_yaxes(title_text="")
    return fig

# -------------------------
# 레이아웃: 상단/하단 그래프
# -------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"상위 {top_n}개국 — `{selected_mbti}` 비율이 높은 나라 🏆")
    fig_top = make_bar(top_df, selected_mbti, f"Top {top_n} countries by {selected_mbti}")
    st.plotly_chart(fig_top, use_container_width=True)

with col2:
    st.subheader(f"하위 {top_n}개국 — `{selected_mbti}` 비율이 낮은 나라 🥉")
    fig_bottom = make_bar(bottom_df, selected_mbti, f"Bottom {top_n} countries by {selected_mbti}")
    st.plotly_chart(fig_bottom, use_container_width=True)

# -------------------------
# 추가: 데이터 표와 다운로드
# -------------------------
st.markdown("---")
st.subheader("원본 데이터 (선택된 MBTI 기준 정렬)")
st.dataframe(df_sorted_desc[["Country", selected_mbti]].reset_index(drop=True))

# CSV 다운로드
@st.cache_data
def to_csv_bytes(df_):
    return df_.to_csv(index=False).encode('utf-8')

csv_bytes = to_csv_bytes(df_sorted_desc[["Country", selected_mbti]])
st.download_button(
    label="정렬된 데이터 다운로드 (CSV)",
    data=csv_bytes,
    file_name=f"mbti_{selected_mbti}_by_country.csv",
    mime="text/csv"
)

st.caption("Made with ❤️ by Streamlit — Plotly로 인터랙티브 막대그래프 제공")
