# AI-Blog-Generator


# 📝 AI Blog Generator

A lightweight Streamlit application that uses the **LLaMA 2 quantized GGUF model** to generate blog articles tailored to different audiences — researchers, data scientists, or the general public.

This app runs entirely locally using the **`llama-cpp-python`** library and a quantized `.gguf` model file, such as `llama-2-7b-chat.Q3_K_S.gguf`.

---

## 🚀 Features

* Generate unique, high-quality blog posts from any topic
* Choose the intended audience for tone and depth
* Customize blog length
* Fast inference using quantized LLaMA 2 models
* 100% private and offline

---

## 🧱 Requirements

* Python 3.9+
* A local `.gguf` model file (e.g. `llama-2-7b-chat.Q3_K_S.gguf`)
* `llama-cpp-python`
* `streamlit`

---

## 📦 Installation

```bash
# 1. Clone the repository (if needed)
git clone https://github.com/your-username/ai-blog-generator.git
cd ai-blog-generator

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit llama-cpp-python
```

---

## 📁 Folder Structure

```
ai-blog-generator/
├── app.py                          # Main Streamlit app
├── models/
│   └── llama-2-7b-chat.Q3_K_S.gguf  # Your LLaMA 2 quantized GGUF model file
├── README.md
├── requirements.txt                # Optional dependency file
```

---

## 🧠 Model Setup

Download a quantized `.gguf` LLaMA 2 model file from [TheBloke's Hugging Face page](https://huggingface.co/TheBloke) and place it in the `models/` folder.

Example used:

```
models/llama-2-7b-chat.Q3_K_S.gguf
```

Update the path in `app.py` if your location is different.

---

## ▶️ Running the App

```bash
streamlit run app.py

