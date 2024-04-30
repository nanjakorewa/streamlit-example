import time

import streamlit as st


# キャッシュ機能のデモ
@st.cache_data
def very_slow_function(a):
    time.sleep(10)
    return a


st.markdown("# データ分析アプリ")
st.text("予測モデルを作成するウェブアプリケーションです。")
st.markdown(f"{very_slow_function(100)}")
