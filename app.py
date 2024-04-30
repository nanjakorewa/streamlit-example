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


# ここ以下のコードは処理内容と関係ありません
st.markdown("## リンク")
st.markdown(
    """- [github](https://github.com/nanjakorewa/streamlit-example)
- [youtube](https://www.youtube.com/@K_DM)"""
)

iframe_html = """<iframe width="560" height="315" src="https://www.youtube.com/embed/de0SAWKJdhE?si=quIy0xchIPybz9Ro" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>"""

st.markdown(iframe_html, unsafe_allow_html=True)
