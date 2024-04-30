import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier

import streamlit as st

if "target_column" not in st.session_state:
    st.session_state["target_column"] = "ターゲット指定なし"


st.markdown("# 分類モデル")
st.markdown("## 分類モデルを作りましょう")

uploaded_file = st.file_uploader("ファイルを入力してください")
if uploaded_file is not None:
    st.info("ファイルが正しくアップロードされました")

    df = pd.read_csv(uploaded_file)
    st.table(df.head(5))

    column_names = [c for c in df.columns]
    target_column = st.selectbox("ターゲットを選んでください", column_names)
    st.info(f"{target_column}を予測対象として予測モデルを作ります！")

    if st.button("モデル作成開始") or st.session_state["target_column"] == target_column:
        st.session_state["target_column"] = target_column
        X = df.copy()
        y = X[target_column]
        X = X.drop([target_column], axis=1)

        model = DecisionTreeClassifier(random_state=777, max_depth=3)
        model.fit(X, y)
        st.info(f"予測モデル作成が完了しました！")
