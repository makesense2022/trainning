"""
练习 06: 对话记忆
难度: 🟡 进阶
预计时间: 20分钟

目标：实现对话记忆功能
"""

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_memory_chain() -> ConversationChain:
    """
    创建带记忆的对话链
    
    返回:
        ConversationChain实例
    """
    # TODO: 创建Memory和Chain
    if not os.getenv("OPENAI_API_KEY"):
        return None
    
    llm = ChatOpenAI()
    memory = ConversationBufferMemory()
    
    chain = ConversationChain(
        llm=llm,
        memory=memory
    )
    return chain


def chat_with_context(chain: ConversationChain, message: str) -> str:
    """
    带上下文的对话
    
    参数:
        chain: 对话链
        message: 消息
    
    返回:
        AI回复
    """
    # TODO: 调用链
    if chain is None:
        return "请设置API Key"
    
    return chain.run(input=message)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        chain = create_memory_chain()
        if chain:
            print(chat_with_context(chain, "我的名字是Alice"))
            print(chat_with_context(chain, "我的名字是什么？"))

