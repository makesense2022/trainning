"""
练习 04: 批量加载文档
难度: 🟡 进阶
预计时间: 20分钟

目标：批量加载和处理多个文档
"""

from langchain.document_loaders import TextLoader, DirectoryLoader
from pathlib import Path


def load_directory(directory: str, pattern: str = "*.txt") -> list:
    """
    批量加载目录中的所有文档
    
    参数:
        directory: 目录路径
        pattern: 文件模式
    
    返回:
        文档列表
    """
    # TODO: 使用DirectoryLoader
    loader = DirectoryLoader(directory, glob=pattern, loader_cls=TextLoader)
    return loader.load()


def process_multiple_files(file_paths: list) -> list:
    """
    处理多个文件
    
    参数:
        file_paths: 文件路径列表
    
    返回:
        文档列表
    """
    # TODO: 循环加载每个文件
    documents = []
    for file_path in file_paths:
        try:
            loader = TextLoader(file_path)
            docs = loader.load()
            documents.extend(docs)
        except Exception as e:
            print(f"加载 {file_path} 失败: {e}")
    return documents


if __name__ == "__main__":
    # 测试批量加载
    # docs = load_directory("./documents", "*.txt")
    # print(f"加载了 {len(docs)} 个文档")
    pass

