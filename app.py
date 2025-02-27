import streamlit as st
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import time

st.set_page_config(page_title="Sarcasm Detector", layout="wide")

MODEL_PATH = "model.h5"
model = load_model(MODEL_PATH)

tokenizer = Tokenizer(num_words=15000)

def preprocess_text(text):
    sequences = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(sequences, maxlen=200)
    return padded

# Sidebar Navigation
st.sidebar.title("🔍 Navigate")
page = st.sidebar.radio("Go to", ["Home", "Sarcasm Detection", "About"])

#Home Page
if page == "Home":
    st.title("🎭 Hinglish Sarcasm Detection")
    st.image("image.png", use_container_width=True)  
    st.markdown(
        """
        ## 🤖 **Understanding Sarcasm in Hinglish Tweets**
        
        ### 🚀 **The Challenge**  
        - Sarcasm in social media isn't always obvious—especially in **Hinglish**.  
        - Words say one thing, but the meaning? Often the opposite!  
        - Our AI model helps **decode sarcasm** so you don’t have to guess.  

        ### 🔍 **How It Works**  
        1️⃣ **Enter a tweet** on the **Detection Page**.  
        2️⃣ Our model analyzes the text and predicts whether it's **sarcastic or not**.  
        3️⃣ The model provides a **confidence score** along with the result.  

       ### 🎯 **Why This Matters?**  
        - Ever read a tweet and thought, *"Wait... was that sarcasm?"* 🤔  
        - Social media is full of hidden meanings—our AI helps you **decode the unsaid**.  
        - Whether you're a **content creator, researcher, or just curious**, this tool makes sarcasm detection **easy and fun!**  

        👉 **Give it a spin! Select "Sarcasm Detection" from the sidebar and test it out.**  
        """
    )


#Detection Page
elif page == "Sarcasm Detection":
    st.title("📝 Sarcasm Detector")
    st.markdown("### 🤖 **Enter a tweet below to check for sarcasm**")

    # Text Input
    user_input = st.text_area("✍️ Type your tweet here:", "")

    if st.button("Detect Sarcasm"):
        if user_input.strip():
            with st.spinner("🔄 Analyzing sarcasm... Please wait"):
                time.sleep(1)  
                processed_input = preprocess_text(user_input)
                prediction = model.predict(processed_input)[0][0]

                sarcasm_label = "😏 **Sarcastic**" if prediction > 0.5 else "😊 **Not Sarcastic**"
                st.markdown(f"### 🎯 Prediction: {sarcasm_label}")
                st.info(f"🔹 **Confidence Score:** {prediction:.2%}")
        else:
            st.warning("⚠️ Please enter a tweet.")

#About Page
elif page == "About":
    st.title("📜 About the Project")
    
    st.markdown(
        """
        ### **📝 About the Dataset**
        - Dataset consists of 9000+ **Hinglish social media posts**.
        - Contains **sarcastic & non-sarcastic** labeled tweets.
        - Preprocessed the data using **XLM-RoBERTa Transformer**.
        """
    )

    st.markdown("### 📩 **Contact Us**")
    st.write("📧 Email: `mohdadnankhan.india@gmail.com`")
    st.write("🌐 Github: [Sarcasm Detection Project](https://github.com/MohammadAdnanKhan/SarcasmX)")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("🔹 **Developed with ❤️**")
