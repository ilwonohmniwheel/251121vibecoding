import streamlit as st
import pandas as pd
import altair as alt

# 데이터 로드
df = pd.read_csv('countriesMBTI_16types.csv')

st.title("🌍 MBTI 유형별 국가 분포 시각화 웹앱")
st.write("선택한 MBTI 유형의 비율이 높은/낮은 국가들을 인터랙티브하게 확인해보세요!")

# MBTI 선택
mbti_list = [col for col in df.columns if col != 'Country']
selected_mbti = st.selectbox("MBTI 유형을 선택하세요", mbti_list)

# 데이터 정렬
df_sorted = df.sort_values(by=selected_mbti, ascending=False)

top10 = df_sorted.head(10)
bottom10 = df_sorted.tail(10)

st.subheader(f"🔝 {selected_mbti} 비율이 높은 10개 국가")
chart_top = (
    alt.Chart(top10)
    .mark_bar()
    .encode(
        x=alt.X(selected_mbti, title=f"{selected_mbti} 비율"),
        y=alt.Y('Country', sort='-x'),
        tooltip=['Country', selected_mbti]
    )
    .interactive()
)
st.altair_chart(chart_top, use_container_width=True)

st.subheader(f"🔻 {selected_mbti} 비율이 낮은 10개 국가")
chart_bottom = (
    alt.Chart(bottom10)
    .mark_bar()
    .encode(
        x=alt.X(selected_mbti, title=f"{selected_mbti} 비율"),
        y=alt.Y('Country', sort='x'),
        tooltip=['Country', selected_mbti]
    )
    .interactive()
)
st.altair_chart(chart_bottom, use_container_width=True)
