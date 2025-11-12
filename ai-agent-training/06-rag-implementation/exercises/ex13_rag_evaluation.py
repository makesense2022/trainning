"""
练习 13: RAG评测
难度: 🔴 挑战
预计时间: 45分钟

目标：使用RAGAS评测RAG系统质量
"""

from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.docstore.document import Document
import os
from dotenv import load_dotenv

load_dotenv()


def evaluate_rag_quality(qa_chain: RetrievalQA, test_cases: list) -> dict:
    """
    评测RAG质量
    
    参数:
        qa_chain: RAG链
        test_cases: 测试用例 [{"question": "...", "ground_truth": "..."}]
    
    返回:
        评测结果
    """
    # TODO: 运行测试用例并计算指标
    # 注意：完整实现需要使用RAGAS库
    results = []
    for case in test_cases:
        answer = qa_chain.run(case["question"])
        results.append({
            "question": case["question"],
            "answer": answer,
            "ground_truth": case["ground_truth"],
            "match": answer.lower() in case["ground_truth"].lower() or case["ground_truth"].lower() in answer.lower()
        })
    
    accuracy = sum(r["match"] for r in results) / len(results) if results else 0
    
    return {
        "accuracy": accuracy,
        "total": len(results),
        "correct": sum(r["match"] for r in results),
        "results": results
    }


if __name__ == "__main__":
    documents = [
        Document(page_content="Python是一种编程语言，由Guido van Rossum创建。")
    ]
    
    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings()
        vectorstore = Chroma.from_documents(documents, embeddings)
        retriever = vectorstore.as_retriever()
        llm = ChatOpenAI()
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=llm,
            chain_type="stuff",
            retriever=retriever
        )
        
        test_cases = [
            {"question": "Python是什么？", "ground_truth": "编程语言"},
            {"question": "谁创建了Python？", "ground_truth": "Guido"}
        ]
        
        evaluation = evaluate_rag_quality(qa_chain, test_cases)
        print(f"准确率: {evaluation['accuracy']:.2%}")

