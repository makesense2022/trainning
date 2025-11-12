"""
练习 11: 对话式RAG
难度: 🔴 挑战
预计时间: 35分钟

目标：实现支持多轮对话的RAG系统
"""

from langchain.chains import ConversationalRetrievalChain
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_conversational_rag(documents: list) -> ConversationalRetrievalChain:
    """
    创建对话式RAG链
    
    参数:
        documents: 文档列表
    
    返回:
        ConversationalRetrievalChain实例
    """
    # TODO: 创建向量库和对话式RAG链
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever()
    llm = ChatOpenAI()
    
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return chain


def chat_with_rag(chain: ConversationalRetrievalChain, question: str, chat_history: list = None) -> dict:
    """
    使用RAG进行对话
    
    参数:
        chain: RAG链
        question: 问题
        chat_history: 对话历史
    
    返回:
        {
            "answer": 答案,
            "sources": 来源文档
        }
    """
    # TODO: 调用链并返回结果
    if chain is None:
        return {"answer": "请设置API Key", "sources": []}
    
    if chat_history is None:
        chat_history = []
    
    result = chain({"question": question, "chat_history": chat_history})
    return {
        "answer": result["answer"],
        "sources": result.get("source_documents", [])
    }


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="Python由Guido创建"),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        chain = create_conversational_rag(documents)
        if chain:
            chat_history = []
            result1 = chat_with_rag(chain, "Python是什么？", chat_history)
            chat_history.append((result1["answer"], "Python是什么？"))
            result2 = chat_with_rag(chain, "谁创建的？", chat_history)
            print(result2["answer"])

