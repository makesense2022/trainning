"""
练习 01: Embedding基础
难度: 🟢 基础
预计时间: 15分钟

目标：理解Embedding（嵌入）的基本概念
"""

import numpy as np
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_simple_embedding(text: str) -> list:
    """
    创建文本的Embedding（使用OpenAI）
    
    参数:
        text: 文本
    
    返回:
        Embedding向量（列表）
    """
    # TODO: 使用OpenAI Embeddings API
    if not os.getenv("OPENAI_API_KEY"):
        # 如果没有API Key，返回模拟向量
        return [0.1] * 1536
    
    client = OpenAI()
    # TODO: 调用embeddings API
    pass


def calculate_cosine_similarity(vec1: list, vec2: list) -> float:
    """
    计算两个向量的余弦相似度
    
    参数:
        vec1: 向量1
        vec2: 向量2
    
    返回:
        相似度（0-1之间，越接近1越相似）
    """
    # TODO: 实现余弦相似度计算
    vec1 = np.array(vec1)
    vec2 = np.array(vec2)
    
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 0.0
    
    return float(dot_product / (norm1 * norm2))


def compare_texts_similarity(text1: str, text2: str) -> float:
    """
    比较两个文本的相似度
    
    参数:
        text1: 文本1
        text2: 文本2
    
    返回:
        相似度分数
    """
    # TODO: 获取两个文本的embedding，然后计算相似度
    pass


if __name__ == "__main__":
    # 测试余弦相似度
    vec1 = [1, 0, 0]
    vec2 = [1, 0, 0]
    print(f"相同向量相似度: {calculate_cosine_similarity(vec1, vec2)}")  # 应该是1.0
    
    vec3 = [0, 1, 0]
    print(f"垂直向量相似度: {calculate_cosine_similarity(vec1, vec3)}")  # 应该是0.0
    
    # 测试文本相似度
    if os.getenv("OPENAI_API_KEY"):
        similarity = compare_texts_similarity("Python编程", "Python开发")
        print(f"文本相似度: {similarity}")

