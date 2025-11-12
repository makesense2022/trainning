"""
练习 08: SummaryMemory
难度: 🟡 进阶
预计时间: 20分钟

目标：使用SummaryMemory压缩对话历史
"""

from langchain.memory import ConversationSummaryMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_summary_memory_chain() -> ConversationChain:
    """
    创建带SummaryMemory的对话链
    
    返回:
        ConversationChain实例
    """
    # TODO: 创建SummaryMemory和ConversationChain
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    memory = ConversationSummaryMemory(llm=llm)
    
    chain = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    return chain


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_summary_memory_chain()
        if chain:
            chain.run(input="我的名字是Alice")
            chain.run(input="我喜欢Python")
            chain.run(input="我的名字是什么？")  # 应该能记住

