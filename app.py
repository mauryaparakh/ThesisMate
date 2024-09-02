import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load environment variables
load_dotenv()

# Load CSS file
def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")
  
# Load the GROQ and OpenAI API KEY 
groq_api_key=os.getenv('GROQ_API_KEY')
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")

# Title
st.title("ThesisMate")

# Initialize the LLM and prompt template
llm = ChatGroq(groq_api_key=groq_api_key, model_name="Llama-3.1-70b-versatile")

prompt = ChatPromptTemplate.from_template("""
Answer the questions based on the provided context.
<context>
{context}
<context>
Questions: {input}
""")

# Function to set up vector embedding
def vector_embedding():
    if "vectors" not in st.session_state:
        st.session_state.embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
        st.session_state.loader = PyPDFLoader("Updated_Prof_Split.pdf")  # Data Ingestion
        st.session_state.docs = st.session_state.loader.load()  # Document Loading
        st.session_state.text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)  # Chunk Creation
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(st.session_state.docs[:20])  # Splitting
        st.session_state.vectors = FAISS.from_documents(st.session_state.final_documents, st.session_state.embeddings)  # Vector OpenAI embeddings

# Automatically load vectors when the app is loaded
vector_embedding()
st.write("The chatbot is ready")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Render the chat history immediately on page load
for chat in st.session_state.chat_history:
    st.markdown(f"<div class='stMarkdown userMessage'><b>You:</b> {chat['question']}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='stMarkdown botMessage'><b>Chatbot:</b> {chat['answer']}</div>", unsafe_allow_html=True)

# Input from user
prompt1 = st.text_input("Enter Your Question")

# Process the input and generate response
if prompt1:
    document_chain = create_stuff_documents_chain(llm, prompt)
    retriever = st.session_state.vectors.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)
    
    # Get the response
    response = retrieval_chain.invoke({'input': prompt1})
    answer = response['answer']
    
    # Store the question and answer in chat history
    st.session_state.chat_history.append({"question": prompt1, "answer": answer})
    
    # Re-display the updated chat history immediately after new input
    st.markdown(f"<div class='stMarkdown userMessage'><b>You:</b> {prompt1}</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='stMarkdown botMessage'><b>Chatbot:</b> {answer}</div>", unsafe_allow_html=True)
