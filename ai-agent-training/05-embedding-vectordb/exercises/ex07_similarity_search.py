"""
练习 07: 相似度搜索
难度: 🟡 进阶
预计时间: 20分钟

目标：在向量库中进行相似度搜索
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def similarity_search_basic(vectorstore: Chroma, query: str, k: int = 3) -> list:
    """
    基础相似度搜索
    
    参数:
        vectorstore: 向量库
        query: 查询文本
        k: 返回结果数量
    
    返回:
        相似文档列表
    """
    # TODO: 使用similarity_search
    return vectorstore.similarity_search(query, k=k)


def similarity_search_with_score(vectorstore: Chroma, query: str, k: int = 3) -> list:
    """
    带相似度分数的搜索
    
    参数:
        vectorstore: 向量库
        query: 查询文本
        k: 返回结果数量
    
    返回:
        (文档, 分数) 元组列表
    """
    # TODO: 使用similarity_search_with_score
    return vectorstore.similarity_search_with_score(query, k=k)


def similarity_search_by_vector(vectorstore: Chroma, query_vector: list, k: int = 3) -> list:
    """
    使用向量进行搜索
    
    参数:
        vectorstore: 向量库
        query_vector: 查询向量
        k: 返回结果数量
    
    返回:
        相似文档列表
    """
    # TODO: 使用similarity_search_by_vector
    return vectorstore.similarity_search_by_vector(query_vector, k=k)


if __name__ == "__main__":
    # 创建测试向量库
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="JavaScript用于前端开发"),
        Document(page_content="AI是人工智能"),
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        
        results = similarity_search_basic(vectorstore, "编程", k=2)
        for doc in results:
            print(doc.page_content)

