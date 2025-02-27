# 🎭 Hinglish Sarcasm Detection

## 🤖 About the Project

Detecting sarcasm is a complex challenge, especially in **Hinglish (Hindi + English)**, where informal spellings, slang, and code-mixed text make traditional sentiment analysis ineffective. This project leverages **XLM-RoBERTa**, a transformer-based deep learning model, to accurately detect sarcasm in social media posts. Our solution enhances **content moderation, brand sentiment analysis, and online interactions** by providing a more nuanced understanding of sarcasm.

## 🚀 Features
- **Hinglish Text Support**: Handles mixed-language text with ease.
- **Transformer-Based Model**: Uses **XLM-RoBERTa** for contextual sarcasm detection.
- **Streamlit Web App**: An interactive UI for real-time analysis.
- **Confidence Score**: Provides a probability score for better interpretation.
- **Optimized Training**: Implemented **Adam optimizer** and **Early Stopping** for efficient learning.

## 📂 Dataset
- **9,800 Hinglish tweets** labeled as **sarcastic (yes) or non-sarcastic (no)**.
- **Preprocessing**: Text cleaning, tokenization, and sentiment analysis.
- **Visualizations**: **Bigrams, word clouds, and sentiment distribution** for better insights.

## ⚙️ How It Works
1. **Text Tokenization**: Converts Hinglish text into tokenized sequences.
2. **Transformer Embeddings**: Uses **XLM-RoBERTa** to generate contextual representations.
3. **Model Prediction**: Classifies tweets as **sarcastic** or **not sarcastic**.
4. **Confidence Score**: Provides a probability measure for better decision-making.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/MohammadAdnanKhan/SarcasmX.git
cd SarcasmX
```

### 2️⃣ Create a Virtual Environment
```sh
python -m venv sarcasm_env
source sarcasm_env/bin/activate  # On Mac/Linux
sarcasm_env\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Download the Model Files
- Ensure `model.h5` and `tokenizer.pkl` are placed in the project directory.

### 5️⃣ Run the Streamlit App
```sh
streamlit run app.py
```

---

## 📊 Results & Evaluation
- **High Precision & Recall**: Achieved strong sarcasm detection performance.
- **Fine-Tuned Model**: Adapted **XLM-RoBERTa** for Hinglish social media text.
- **Evaluation Metrics**: Used **F1-score, accuracy, and confusion matrix** for analysis.

## 📌 Challenges Faced
- **Code-Mixed Text**: Informal Hinglish writing styles made tokenization complex.
- **Limited Datasets**: High-quality Hinglish sarcasm datasets are scarce.
- **Computational Cost**: Transformer-based models require significant resources.

## 💎 Contact & Contributions
- **📧 Email:** mohdadnankhan.india@gmail.com
- **🌐 GitHub:** [SarcasmX](https://github.com/MohammadAdnanKhan/SarcasmX)
- Open to **issues, suggestions, and pull requests** for improvements!

---

🔹 *Developed with ❤️ to decode sarcasm in Hinglish tweets!*
