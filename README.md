<h1>🤖 Chatbot with LangChain and Streamlit</h1>
A <strong>powerful question-answering chatbot</strong> that uses Google's Gemini AI model and FAISS vector storage to provide intelligent responses based on your knowledge base.
Natural language question answering
<h2>✨ Features</h2>
<strong>Natural Language Processing</strong>: Understands and responds to questions in conversational language

<strong>CSV-Based Knowledge Base</strong>: Easy to maintain and update your Q&A database

<strong>FAISS Vector Storage</strong>: Efficient similarity search for accurate responses

<strong>Streamlit Web Interface</strong>: User-friendly web application

<strong>Google Gemini AI Integration</strong>: Leverages cutting-edge AI technology

h2>🚀 Quick Start</h2>
<h3>Prerequisites</h3>
<strong>Python 3.8+</strong>

<strong>Google API Key</strong> (for Gemini AI)

<strong>HuggingFace Account</strong> (for embeddings)

<h3>Installation</h3>
1.<strong>Clone the repository</strong>:
git clone <your-repo-url>
cd <your-repo-directory>
2.<strong>Install dependencies</strong>:
pip install -r requirements.txt
3.<strong>Set up environment variables</strong>:

Create a <code>.env</code> file

Add your API key: <code>GOOGLE_API_KEY=your_api_key_here</code>
<h2>🛠️ Configuration</h2>
<h3>Model Settings</h3>
<strong>AI Model</strong>: Gemini-1.5-flash (Google)

<strong>Embeddings</strong>: sentence-transformers/all-MiniLM-L6-v2

<strong>Vector Store</strong>: FAISS

<strong>Web Framework</strong>: Streamlit

<h3>Knowledge Base Setup</h3>
Edit <code>codebasics_faqs.csv</code> with your questions and answers

Ensure there's a 'prompt' column for questions

Add corresponding answers in adjacent columns
<h2>🎯 Usage</h2>
<h3>Running the Application</h3>
streamlit run main.py
<h3>Access the Interface</h3>
Open your browser and navigate to: <code>http://localhost:8501</code>

<h3>Using the Chatbot</h3>
1.Click <strong>"Get the response"</strong> to initialize the vector database

2.Type your question in the text input field

3.Press Enter to get AI-generated responses
<h2>🔧 How It Works</h2>
<strong>Data Loading</strong>: Questions and answers are loaded from CSV file

<strong>Vector Embeddings</strong>: HuggingFace models create semantic embeddings

<strong>Storage</strong>: Vectors are stored in FAISS for efficient retrieval

<strong>Query Processing</strong>: Gemini AI generates answers based on similar questions

<strong>Web Interface</strong>: Streamlit provides interactive user experience
<h2>📋 Requirements</h2>
Key dependencies include:

<code>streamlit</code>

<code>langchain-google-genai</code>

<code>langchain-community</code>

<code>langchain-huggingface</code>

<code>faiss-cpu</code>

<code>python-dotenv</code>






