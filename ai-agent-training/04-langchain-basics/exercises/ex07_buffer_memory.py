"""
练习 07: BufferMemory
难度: 🟢 基础
预计时间: 15分钟

目标：使用BufferMemory保存对话历史
"""

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_conversation_with_memory() -> ConversationChain:
    """
    创建带记忆的对话链
    
    返回:
        ConversationChain实例
    """
    # TODO: 创建BufferMemory和ConversationChain
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    memory = ConversationBufferMemory()
    
    chain = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )
    return chain


def chat_with_memory(chain: ConversationChain, message: str) -> str:
    """
    使用记忆进行对话
    
    参数:
        chain: 对话链
        message: 用户消息
    
    返回:
        AI回复
    """
    # TODO: 调用链并返回回复
    if chain is None:
        return "请设置API Key"
    
    return chain.run(input=message)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_conversation_with_memory()
        if chain:
            print(chat_with_memory(chain, "我的名字是Alice"))
            print(chat_with_memory(chain, "我的名字是什么？"))  # 应该能记住

