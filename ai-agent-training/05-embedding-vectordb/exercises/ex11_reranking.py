"""
练习 11: 重排序
难度: 🔴 挑战
预计时间: 25分钟

目标：对检索结果进行重排序，提高相关性
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def rerank_results(documents: list, query: str) -> list:
    """
    对检索结果重排序
    
    参数:
        documents: 文档列表
        query: 查询文本
    
    返回:
        重排序后的文档列表
    
    注意：这里使用简单的关键词匹配，实际应该使用专门的reranking模型
    """
    # TODO: 实现重排序逻辑
    # 计算每个文档的相关性分数
    scored_docs = []
    query_words = set(query.lower().split())
    
    for doc in documents:
        doc_words = set(doc.page_content.lower().split())
        # 计算交集（共同词数）
        score = len(query_words & doc_words)
        scored_docs.append((score, doc))
    
    # 按分数排序
    scored_docs.sort(key=lambda x: x[0], reverse=True)
    return [doc for score, doc in scored_docs]


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言"),
        Document(page_content="JavaScript用于前端开发"),
        Document(page_content="Python和JavaScript都是编程语言"),
    ]
    
    results = rerank_results(documents, "Python编程")
    for doc in results:
        print(doc.page_content)

