import streamlit as st
import os
import chromadb

from dotenv import load_dotenv
from google import genai
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

# =========================================================
# PAGE CONFIG
# =========================================================
st.set_page_config(
    page_title="Company AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# =========================================================
# LOAD ENV
# =========================================================
load_dotenv()

API_KEY = os.getenv("Gemini_API_Key")

if not API_KEY:
    st.error("❌ Gemini API key not found in .env (Course_AI_Lab)")
    st.stop()

# =========================================================
# GEMINI CLIENT
# =========================================================
@st.cache_resource
def init_gemini():
    return genai.Client(api_key=API_KEY)

gemini_client = init_gemini()

# =========================================================
# EMBEDDING FUNCTION
# =========================================================
def get_embedding(text):
    response = gemini_client.models.embed_content(
        model="gemini-embedding-001",
        contents=text
    )
    return response.embeddings[0].values

# =========================================================
# CHROMA DB
# =========================================================
@st.cache_resource
def init_chromadb():
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_or_create_collection(
        name="company_documents"
    )
    return collection

collection = init_chromadb()

# =========================================================
# BUILD KNOWLEDGE BASE (IMPORTANT FIX)
# =========================================================
def build_knowledge_base():
    loader = DirectoryLoader(
        "company_documents/",
        glob="*.txt",
        loader_cls=TextLoader
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    texts = [c.page_content for c in chunks]

    embeddings = [get_embedding(t) for t in texts]

    collection.add(
        documents=texts,
        embeddings=embeddings,
        ids=[f"doc_{i}" for i in range(len(texts))],
        metadatas=[
            {"source": c.metadata.get("source", "unknown")}
            for c in chunks
        ]
    )

# 👉 AUTO FIX: build DB if empty
if collection.count() == 0:
    with st.spinner("📚 Building knowledge base..."):
        build_knowledge_base()

# =========================================================
# LLM
# =========================================================
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=API_KEY,
    temperature=0
)

# =========================================================
# RAG FUNCTION
# =========================================================
def get_rag_response(query, n_results=3):

    try:
        # Embed query
        query_embedding = get_embedding(query)

        # Search Chroma
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        docs = results["documents"][0]

        if not docs:
            return "I don't know based on the provided documents."

        context = "\n\n---\n\n".join(docs)

        prompt = f"""
You are a professional HR assistant.

Answer ONLY using the context below.

If not found, say:
"I don't know based on the provided documents."

Context:
{context}

Question:
{query}

Answer:
"""

        response = llm.invoke(prompt)

        return response.content

    except Exception as e:
        return f"Error: {str(e)}"

# =========================================================
# STREAMLIT UI
# =========================================================
st.title("🤖 Company Knowledge Base AI Assistant")
st.caption("Powered by Gemini + ChromaDB + RAG")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
prompt = st.chat_input("Ask about company policies...")

if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Searching knowledge base..."):
            answer = get_rag_response(prompt)

        st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})

# =========================================================
# SIDEBAR INFO
# =========================================================
with st.sidebar:
    st.title("🏢 Company AI")

    st.metric("Documents Indexed", collection.count())
    st.metric("Model", "Gemini 2.5 Flash")
    st.metric("Embeddings", "Gemini")

    st.markdown("### Example Questions")
    st.markdown("- What is leave policy?")
    st.markdown("- Can I work remotely?")
    st.markdown("- Maternity benefits?")


   
