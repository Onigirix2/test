import streamlit as st
import pandas as pd

st.title("Excelクイズ学習ツール")

# Excelファイルの読み込み（GitHubに一緒にアップロードしておく前提）
# ブラウザ上でファイルをアップロードして試す場合は st.file_uploader を使います
@st.cache_data
def load_data():
    # 本番は 'quiz_data.xlsx' などファイル名を指定
    # ここでは動作確認用に簡易的なデータを作成します
    data = {
        '問題': ['Pythonのフレームワークは？', 'Streamlitの実行コマンドは？'],
        '選択肢A': ['Django', 'run'],
        '選択肢B': ['Ruby on Rails', 'hello'],
        '選択肢C': ['Laravel', 'start'],
        '正解': ['Django', 'run']
    }
    return pd.DataFrame(data)

df = load_data()

# Excelファイルを読み込む部分
df = pd.read_excel('quiz_data.xlsx')

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
    answer = st.radio("答えを選んでください", options)
    
    if st.button("回答する"):
        if answer == row['正解']:
            st.success("正解です！")
            st.session_state.score += 1
        else:
            st.error(f"残念！ 正解は {row['正解']} でした。")
        
        # 次の問題へ進むボタンを表示
        if st.button("次の問題へ"):
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
