"""
练习 04: Embedding对比
难度: 🟡 进阶
预计时间: 20分钟

目标：对比不同Embedding模型的效果
"""

from langchain.embeddings import OpenAIEmbeddings, HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()


def compare_embeddings(texts: list) -> dict:
    """
    对比不同Embedding模型
    
    参数:
        texts: 文本列表
    
    返回:
        对比结果
    """
    # TODO: 使用不同模型生成Embedding并对比
    results = {}
    
    if os.getenv("OPENAI_API_KEY"):
        openai_emb = OpenAIEmbeddings()
        openai_results = openai_emb.embed_documents(texts)
        results["openai"] = {
            "dimension": len(openai_results[0]),
            "count": len(openai_results)
        }
    
    # 本地模型
    hf_emb = HuggingFaceEmbeddings()
    hf_results = hf_emb.embed_documents(texts)
    results["huggingface"] = {
        "dimension": len(hf_results[0]),
        "count": len(hf_results)
    }
    
    return results


if __name__ == "__main__":
    texts = ["Python是一种编程语言", "JavaScript用于前端开发"]
    comparison = compare_embeddings(texts)
    print(comparison)

