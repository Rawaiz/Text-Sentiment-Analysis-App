import streamlit as st
from transformers import pipeline

# Sentiment model
sentiment_model = pipeline("sentiment-analysis")

# Emoji list (a bunch of common emojis)
all_emojis = "😀 😁 😂 🤣 😃 😄 😅 😆 😉 😊 🙂 🙃 😋 😎 😍 🥰 😘 😗 😙 😚 😐 😑 😶 🙄 😏 😣 😥 😮 😯 😪 😫 😴 😌 😛 😜 🤪 😝 🤑 🤗 🤔 🤐 🤨 😐 🙃 🤡 🤠 😇 🤥 😷 🤒 🤕 🤢 🤮 🤧 😵 🤯 🤠 😎 🤓 🧐 🤠"

st.title("Text Sentiment App with All Emojis")

st.write("Type something to check its sentiment:")

user_input = st.text_input("Your sentence")

if user_input:
    result = sentiment_model(user_input)[0]
    label = result['label']
    confidence = round(result['score'] * 100, 2)

    # Basic emoji for sentiment
    if label == "POSITIVE":
        sentiment_emoji = "🙂"
        color = "green"
    elif label == "NEGATIVE":
        sentiment_emoji = "🙁"
        color = "red"
    else:
        sentiment_emoji = "😐"
        color = "orange"

    st.markdown(f"**Sentiment:** <span style='color:{color};'>{label} {sentiment_emoji}</span>", unsafe_allow_html=True)
    st.write(f"**Confidence:** {confidence}%")

    st.write("---")
    st.write("### Here are some emojis you can use:")
    st.write(all_emojis)
