import streamlit as st
import pandas as pd

st.title("Excelクイズ学習ツール")

# Excelの読み込み
try:
    df = pd.read_excel('quiz_data.xlsx')
except Exception as e:
    st.error(f"Excelファイルが読み込めませんでした: {e}")
    st.stop()

# 状態の初期化
if 'question_index' not in st.session_state:
    st.session_state.question_index = 0
    st.session_state.score = 0
    st.session_state.answered = False  # 回答したかどうかのフラグ

# クイズ画面
if st.session_state.question_index < len(df):
    row = df.iloc[st.session_state.question_index]
    st.subheader(f"第 {st.session_state.question_index + 1} 問")
    st.write(row['問題'])
    
    options = [row['選択肢A'], row['選択肢B'], row['選択肢C']]
    
    # 回答前
    if not st.session_state.answered:
        answer = st.radio("答えを選んでください", options, key=f"q_{st.session_state.question_index}")
        if st.button("回答する"):
            st.session_state.answer_selected = answer
            st.session_state.answered = True
            st.rerun() # 画面を更新して「回答後」の状態にする
            
    # 回答後
    else:
        st.write(f"あなたの回答: {st.session_state.answer_selected}")
        if st.session_state.answer_selected == row['正解']:
            st.success("正解です！")
            # スコア加算は回答した瞬間に一度だけ行う工夫が必要ですが、
            # ここではシンプルにするため「次へ」の中で処理します。
        else:
            st.error(f"残念！ 正解は {row['正解']} でした。")
        
        if st.button("次へ進む"):
            # スコアの集計
            if st.session_state.answer_selected == row['正解']:
                st.session_state.score += 1
            
            # 次の問題へ移動し、回答フラグをリセット
            st.session_state.question_index += 1
            st.session_state.answered = False
            st.rerun()

else:
    st.balloons()
    st.header("クイズ終了！")
    st.write(f"あなたのスコアは {st.session_state.score} / {len(df)} でした。")
    if st.button("最初からやり直す"):
        st.session_state.question_index = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()
