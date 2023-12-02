import streamlit as st

from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings, HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplates import css, bot_template, user_template



def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_conversation_chain(vectorstore, api_key):
    llm = ChatOpenAI(openai_api_key=api_key)
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question, conversation):
    response = conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    
            
    
    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
           st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)


def get_vectorstore(text_chunks, api_key):
    embeddings = OpenAIEmbeddings(openai_api_key=api_key)
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore





def main():
    st.set_page_config(page_title="📄 PDF Uploader & Analyzer: GPT Powered 🤖🔍", layout="wide", initial_sidebar_state="collapsed")
    st.title("📄📚 PDF Uploader & Analyzer: GPT Powered 🤖🔍")




    st.sidebar.title("User Input")
    api_key = st.sidebar.text_input("Enter your OpenAI API Key")
    pdf_docs = st.sidebar.file_uploader("Choose your PDF files 📁📚", type=["pdf"], accept_multiple_files=True)
  
    if pdf_docs and api_key:
        raw_text = get_pdf_text(pdf_docs)
        text_chunks = get_text_chunks(raw_text)
        vectorstore = get_vectorstore(text_chunks, api_key)
        conversation = get_conversation_chain(vectorstore, api_key)


        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            handle_userinput(user_question, conversation)

if __name__ == '__main__':
    main()