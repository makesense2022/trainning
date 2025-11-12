"""
练习 02: Chat Models
难度: 🟢 基础
预计时间: 15分钟

目标：掌握LangChain的Chat Models抽象
"""

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
import os
from dotenv import load_dotenv

load_dotenv()


def create_chat_model(model_name: str = "gpt-3.5-turbo") -> ChatOpenAI:
    """
    创建Chat Model
    
    参数:
        model_name: 模型名称
    
    返回:
        ChatOpenAI实例
    """
    # TODO: 创建ChatOpenAI实例
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("请设置OPENAI_API_KEY")
    
    return ChatOpenAI(model_name=model_name, temperature=0.7)


def simple_chat(llm: ChatOpenAI, message: str) -> str:
    """
    简单聊天
    
    参数:
        llm: Chat Model
        message: 用户消息
    
    返回:
        AI回复
    """
    # TODO: 使用llm.invoke()或llm.predict()
    messages = [HumanMessage(content=message)]
    response = llm.invoke(messages)
    return response.content


def chat_with_system(llm: ChatOpenAI, system_prompt: str, user_message: str) -> str:
    """
    带System消息的聊天
    
    参数:
        llm: Chat Model
        system_prompt: System提示
        user_message: 用户消息
    
    返回:
        AI回复
    """
    # TODO: 使用SystemMessage和HumanMessage
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_message)
    ]
    response = llm.invoke(messages)
    return response.content


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        llm = create_chat_model()
        result = simple_chat(llm, "用一句话介绍Python")
        print(result)

