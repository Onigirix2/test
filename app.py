import streamlit as st
import pandas as pd

st.title("Excelクイズ学習ツール")

# Excelファイルを読み込む（一番シンプルな書き方）
# ※GitHub上に 'quiz_data.xlsx' がアップロードされている必要があります
try:
    df = pd.read_excel('quiz_data.xlsx')
except Exception as e:
    st.error(f"Excelファイルが読み込めませんでした: {e}")
    st.stop()

# セッション（状態）の初期化
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0

# 全問題が終わったかチェック
if st.session_state.question_index < len(df):
    row = df.iloc[st.session_state.question_index]
    
    st.subheader(f"第 {st.session_state.question_index + 1} 問")
    st.write(row['問題'])
    
    # 選択肢ボタンの作成
    options = [row['選択肢A'], row['選択肢B'], row['選択肢C']]
    answer = st.radio("答えを選んでください", options, key=f"q_{st.session_state.question_index}")
    
    if st.button("回答する"):
        if answer == row['正解']:
            st.success("正解です！")
            st.session_state.score += 1
        else:
            st.error(f"残念！ 正解は {row['正解']} でした。")
        
        # 次の問題へ進む
        if st.button("次へ進む"):
            st.session_state.question_index += 1
            st.rerun()
else:
    st.balloons()
    st.header("クイズ終了！")
    st.write(f"あなたのスコアは {st.session_state.score} / {len(df)} でした。")
    if st.button("最初からやり直す"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.rerun()
