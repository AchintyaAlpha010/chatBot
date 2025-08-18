from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS  # Updated import
from langchain_community.document_loaders.csv_loader import CSVLoader  # Updated import
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.schema import Document
from langchain.chains import RetrievalQA

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

vector_store_filepath = "faiss_index"
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

def create_vector_db():
    loader = CSVLoader(file_path='codebasics_faqs.csv', source_column='prompt')
    data = loader.load()
    vector_store = FAISS.from_documents(documents=data, embedding=embeddings)
    vector_store.save_local(vector_store_filepath)

def get_qa_chain():
    vector_store = FAISS.load_local(
        vector_store_filepath, 
        embeddings, 
        allow_dangerous_deserialization=True
    )
    retriever = vector_store.as_retriever()
    chain = RetrievalQA.from_chain_type(llm=llm,
             chain_type="stuff",
             retriever=retriever,
             input_key="query",
             return_source_documents=True,
             
        )
    return chain

if __name__ == "__main__":
    chain = get_qa_chain()
    result = chain.invoke({"query": "do you provide internship? Do you have EMI option?"})
    print("Answer:", result['result'])
    print("\nSource documents:")
