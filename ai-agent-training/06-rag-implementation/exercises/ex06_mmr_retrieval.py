"""
练习 06: MMR检索
难度: 🟡 进阶
预计时间: 25分钟

目标：使用MMR（Maximal Marginal Relevance）提高检索多样性
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def mmr_search(vectorstore: Chroma, query: str, k: int = 3, fetch_k: int = 10) -> list:
    """
    MMR检索（平衡相关性和多样性）
    
    参数:
        vectorstore: 向量库
        query: 查询文本
        k: 返回数量
        fetch_k: 初始检索数量（用于MMR算法）
    
    返回:
        多样化的文档列表
    """
    # TODO: 使用max_marginal_relevance_search
    return vectorstore.max_marginal_relevance_search(
        query,
        k=k,
        fetch_k=fetch_k
    )


def compare_search_methods(vectorstore: Chroma, query: str):
    """
    对比普通检索和MMR检索
    
    参数:
        vectorstore: 向量库
        query: 查询文本
    
    返回:
        对比结果字典
    """
    # TODO: 对比similarity_search和max_marginal_relevance_search
    normal_results = vectorstore.similarity_search(query, k=3)
    mmr_results = mmr_search(vectorstore, query, k=3)
    
    return {
        "normal": [doc.page_content for doc in normal_results],
        "mmr": [doc.page_content for doc in mmr_results]
    }


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="Python用于数据科学"),
        Document(page_content="Python用于Web开发"),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        
        comparison = compare_search_methods(vectorstore, "Python")
        print("普通检索:", comparison["normal"])
        print("MMR检索:", comparison["mmr"])

