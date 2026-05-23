## 🚀 Customer Support RAG Chatbot
An intelligent AI-powered Customer Support Chatbot built using Streamlit, LangChain, Ollama, and ChromaDB.
This project uses Retrieval-Augmented Generation (RAG) to answer customer support questions from uploaded PDF and TXT documents using local LLMs.

## 📌 Features
- 📄 Load support documents from PDF and TXT files
- 🤖 Ask questions in natural language
- 🧠 Uses local LLMs with Ollama (phi3, mistral)
- 🔍 Semantic search using embeddings
- 🗂️ Vector database with ChromaDB
- ⚡ Interactive Streamlit UI
- 🔒 Fully local and offline support
  
## 🛠️ Tech Stack
- Python
- Streamlit
- LangChain
- Ollama
- ChromaDB
- PyPDF
- Recursive Text Splitter
  
## 📂 Project Structure
```text
Customer_Support_RAG_Chatbot/
│
├── app.py
├── support_docs/
│   ├── sample.txt
│   └── support_guide.pdf
│
├── chroma_db/
│
├── requirements.txt
└── README.md
```

## ⚙️ Installation
### 1️⃣ Clone Repository
```
git clone https://github.com/Likithkumarr/Customer_Support_RAG_Chatbot.git
```
### 2️⃣ Change Directory
```
cd Customer_Support_RAG_Chatbot
```
### Create Virtual Environment
```
python -m venv venv
```
Activate environment:
### Windows
```
venv\Scripts\activate
```
### Linux / Mac'
```
source venv/bin/activate
```
### Install Dependencies
```
pip install -r requirements.txt
```
Or
### manually install:
```
pip install streamlit langchain langchain-community langchain-text-splitters langchain-chroma langchain-ollama chromadb pypdf
```
## 🤖 Install Ollama
### Download Ollama:
```
Ollama Official Website
```
### Pull required models:
```
ollama pull phi3
ollama pull mistral
ollama pull nomic-embed-text
```
### Start Ollama server:
```
ollama serve
```

## 📄 Add Documents

#### Place your support documents inside:
```
support_docs/
```
#### Supported formats:
- .pdf
- .txt

#### Example TXT file:
```
How to create an account:
1. Go to the website homepage.
2. Click on "Sign Up".
3. Enter your email and password.
4. Verify your email address.
```

## ▶️ Run Application
```
streamlit run app.py
```
#### Application will open in browser:
```
http://localhost:8501
```
## 💬 Example Questions
```
How do I create an account?
```
```
How can I change my email?
```
```
How do I delete my account?
```
## 🧠 How It Works
```
User Question
      ↓
Retriever searches documents
      ↓
Relevant chunks retrieved
      ↓
LLM generates answer
      ↓
Answer displayed in Streamlit
```
## 📸 Sample Workflow
1.Upload support documents <br>
2.Start Streamlit app <br>
3.Ask customer support questions <br>
4.Get AI-generated answers from documents <br>

## 🔍 RAG Pipeline
#### This project follows the Retrieval-Augmented Generation (RAG) architecture:

- Document Loading
- Text Splitting
- Embedding Generation
- Vector Storage
- Semantic Retrieval
- LLM Response Generation
## 📦 Models Used
Purpose	Model
LLM	phi3 / mistral
Embeddings	nomic-embed-text

## 🚀 Future Improvements
- Chat history support
- Multiple file upload
- Source citation display
- Conversation memory
- Authentication system
- Docker deployment
- Cloud deployment

## 🤝 Contributing
#### Contributions are welcome!

1.Fork the repository <br>
2.Create new branch <br>
3.Commit changes <br>
4.Push to branch <br>
5.Open Pull Request <br>

## 📜 License
This project is licensed under the MIT License.

## 👨‍💻 Author
### Likith Kumar Osuri

#### GitHub:
Likithkumarr GitHub Profile

#### Project Repository:
Customer_Support_RAG_Chatbot Repository
