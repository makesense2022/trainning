"""
练习 10: 带引用的RAG
难度: 🔴 挑战
预计时间: 30分钟

目标：RAG返回答案时包含来源文档引用
"""

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_rag_with_sources(documents: list) -> RetrievalQA:
    """
    创建带引用的RAG链
    
    参数:
        documents: 文档列表
    
    返回:
        RetrievalQA链（配置为返回来源）
    """
    # TODO: 创建向量库和RAG链，设置return_source_documents=True
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI()
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain


def query_with_sources(qa_chain: RetrievalQA, question: str) -> dict:
    """
    查询并获取来源
    
    参数:
        qa_chain: RAG链
        question: 问题
    
    返回:
        {
            "answer": 答案,
            "sources": 来源文档列表
        }
    """
    # TODO: 调用链并提取答案和来源
    if qa_chain is None:
        return {"answer": "请设置API Key", "sources": []}
    
    result = qa_chain({"query": question})
    return {
        "answer": result["result"],
        "sources": result.get("source_documents", [])
    }


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言", metadata={"source": "doc1"}),
        Document(page_content="Python由Guido创建", metadata={"source": "doc2"}),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        qa_chain = create_rag_with_sources(documents)
        if qa_chain:
            result = query_with_sources(qa_chain, "Python是什么？")
            print(f"答案: {result['answer']}")
            print(f"来源数量: {len(result['sources'])}")

