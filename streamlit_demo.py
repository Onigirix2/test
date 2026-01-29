import streamlit as st
import pandas as pd
import numpy as np

st.title("データ可視化デモ")

# 1. 適当なデータを作る
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

# 2. 折れ線グラフを表示（これだけでOK！）
st.line_chart(chart_data)

# 3. 地図に点を打つ（緯度・経度のデータがあれば1行）
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [35.68, 139.76],
    columns=['lat', 'lon']
)
st.map(map_data)
