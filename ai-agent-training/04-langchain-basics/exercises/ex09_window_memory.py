"""
练习 09: WindowMemory
难度: 🟡 进阶
预计时间: 15分钟

目标：使用WindowMemory只保留最近N轮对话
"""

from langchain.memory import ConversationBufferWindowMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_window_memory_chain(k: int = 2) -> ConversationChain:
    """
    创建带窗口记忆的对话链
    
    参数:
        k: 保留的对话轮数
    
    返回:
        ConversationChain实例
    """
    # TODO: 使用ConversationBufferWindowMemory
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    memory = ConversationBufferWindowMemory(k=k)
    
    chain = ConversationChain(
        llm=llm,
        memory=memory
    )
    return chain


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_window_memory_chain(k=2)
        if chain:
            chain.run(input="第一轮对话")
            chain.run(input="第二轮对话")
            chain.run(input="第三轮对话")
            # 只有最近2轮会被记住

