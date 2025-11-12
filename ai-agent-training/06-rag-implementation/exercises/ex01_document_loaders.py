"""
练习 01: 文档加载器
难度: 🟢 基础
预计时间: 15分钟

目标：使用LangChain加载各种格式的文档
"""

from langchain.document_loaders import TextLoader, PyPDFLoader
from pathlib import Path


def load_text_file(file_path: str) -> list:
    """
    加载文本文件
    
    参数:
        file_path: 文件路径
    
    返回:
        文档列表
    """
    # TODO: 使用 TextLoader 加载
    pass


def load_pdf_file(file_path: str) -> list:
    """
    加载PDF文件
    
    参数:
        file_path: PDF文件路径
    
    返回:
        文档列表
    """
    # TODO: 使用 PyPDFLoader 加载
    pass


def extract_text_from_documents(documents: list) -> list:
    """
    从文档中提取文本内容
    
    参数:
        documents: LangChain文档列表
    
    返回:
        文本内容列表
    """
    # TODO: 提取每个document的page_content
    pass


if __name__ == "__main__":
    # 测试文本加载
    # docs = load_text_file("test.txt")
    # print(extract_text_from_documents(docs))
    pass

