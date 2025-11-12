"""
练习 05: 基础检索
难度: 🟡 进阶
预计时间: 20分钟

目标：实现基础的RAG检索流程
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_retriever(documents: list, k: int = 3):
    """
    创建检索器
    
    参数:
        documents: 文档列表
        k: 返回文档数量
    
    返回:
        检索器对象
    """
    # TODO: 创建向量库和检索器
    if not os.getenv("OPENAI_API_KEY"):
        from langchain.embeddings.fake import FakeEmbeddings
        embeddings = FakeEmbeddings(size=1536)
    else:
        embeddings = OpenAIEmbeddings()
    
    vectorstore = Chroma.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": k})
    return retriever


def basic_rag_qa(documents: list, question: str) -> str:
    """
    基础RAG问答
    
    参数:
        documents: 文档列表
        question: 问题
    
    返回:
        答案
    """
    # TODO: 创建检索器和QA链
    if not os.getenv("OPENAI_API_KEY"):
        return "请设置API Key"
    
    retriever = create_retriever(documents)
    llm = ChatOpenAI()
    
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever
    )
    
    result = qa_chain.run(question)
    return result


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种高级编程语言，由Guido van Rossum创建。"),
        Document(page_content="Python支持多种编程范式，包括面向对象和函数式编程。"),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        answer = basic_rag_qa(documents, "Python是什么？")
        print(answer)

