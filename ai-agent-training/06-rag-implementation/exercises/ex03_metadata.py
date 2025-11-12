"""
练习 03: 元数据管理
难度: 🟡 进阶
预计时间: 20分钟

目标：在RAG中使用元数据过滤和检索
"""

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def create_documents_with_metadata() -> list:
    """
    创建带元数据的文档
    
    返回:
        文档列表（包含metadata）
    """
    # TODO: 创建文档，每个文档包含metadata
    return [
        Document(
            page_content="Python是一种编程语言",
            metadata={"source": "doc1", "category": "programming", "year": 2024}
        ),
        Document(
            page_content="JavaScript用于前端开发",
            metadata={"source": "doc2", "category": "frontend", "year": 2024}
        ),
    ]


def search_with_metadata_filter(vectorstore: Chroma, query: str, filter_dict: dict) -> list:
    """
    使用元数据过滤搜索
    
    参数:
        vectorstore: 向量库
        query: 查询文本
        filter_dict: 过滤条件（如{"category": "programming"}）
    
    返回:
        过滤后的文档列表
    """
    # TODO: 使用where参数过滤
    return vectorstore.similarity_search(query, k=3, filter=filter_dict)


if __name__ == "__main__":
    documents = create_documents_with_metadata()
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        
        # 搜索并过滤
        results = search_with_metadata_filter(
            vectorstore,
            "编程",
            {"category": "programming"}
        )
        print(f"找到 {len(results)} 个文档")

