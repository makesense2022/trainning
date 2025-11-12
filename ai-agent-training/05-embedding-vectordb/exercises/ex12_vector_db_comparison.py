"""
练习 12: 向量库对比
难度: 🔴 挑战
预计时间: 30分钟

目标：对比不同向量数据库的特点
"""

from langchain.docstore.document import Document


def compare_vector_databases() -> dict:
    """
    对比不同向量数据库
    
    返回:
        对比结果
    """
    # TODO: 对比ChromaDB、FAISS、Pinecone等
    return {
        "chromadb": {
            "特点": "轻量、内嵌、易用",
            "适用": "原型开发、小规模数据",
            "优势": "简单、快速上手",
            "劣势": "不适合大规模数据"
        },
        "faiss": {
            "特点": "快速、开源、Facebook开发",
            "适用": "大规模数据、高性能需求",
            "优势": "速度快、支持GPU",
            "劣势": "需要手动管理索引"
        },
        "pinecone": {
            "特点": "托管服务、稳定",
            "适用": "生产环境",
            "优势": "无需运维、稳定",
            "劣势": "需要付费"
        }
    }


if __name__ == "__main__":
    comparison = compare_vector_databases()
    for db, info in comparison.items():
        print(f"\n{db.upper()}:")
        for key, value in info.items():
            print(f"  {key}: {value}")

