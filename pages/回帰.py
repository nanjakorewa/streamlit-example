import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.tree import DecisionTreeRegressor

import streamlit as st

if "target_column" not in st.session_state:
    st.session_state["target_column"] = "ターゲット指定なし"


st.markdown("# 回帰モデル")
st.markdown("## 回帰モデルを作りましょう")

uploaded_file = st.file_uploader("ファイルを入力してください")
if uploaded_file is not None:
    st.info("ファイルが正しくアップロードされました")

    df = pd.read_csv(uploaded_file)
    st.table(df.head(5))

    column_names = [c for c in df.columns]
    target_column = st.selectbox("ターゲットを選んでください", column_names)
    st.info(f"{target_column}を予測対象として予測モデルを作ります！")

    # target_columnが回帰に適切なデータか確認する
    numeric_columns = df.select_dtypes("number").columns
    if not target_column in numeric_columns:
        st.error(f"{target_column}は数値カラムではありません！")

    if st.button("モデル作成開始") or st.session_state["target_column"] == target_column:
        st.session_state["target_column"] = target_column
        X = df.copy()
        y = X[target_column]
        X = X.drop([target_column], axis=1)

        model = DecisionTreeRegressor(random_state=777, max_depth=3)
        model.fit(X, y)
        st.info(f"予測モデル作成が完了しました！")

        st.markdown("### 散布図の確認")
        col_x = st.selectbox("x軸にする列を選んでください", column_names)
        col_y = st.selectbox("y軸にする列を選んでください", column_names, index=1)

        fig = plt.figure(figsize=(5, 5))
        sns.scatterplot(data=df, x=col_x, y=col_y)
        st.pyplot(fig)
