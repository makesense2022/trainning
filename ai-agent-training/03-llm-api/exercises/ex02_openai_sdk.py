"""
练习 02: OpenAI SDK完整用法
难度: 🟢 基础
预计时间: 10分钟

目标：掌握OpenAI Python SDK的基本用法
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def create_client() -> OpenAI:
    """
    创建OpenAI客户端
    
    返回:
        OpenAI客户端实例
    """
    # TODO: 使用环境变量中的API Key创建客户端
    pass


def list_models(client: OpenAI) -> list:
    """
    列出可用的模型
    
    返回:
        模型名称列表
    """
    # TODO: 调用 client.models.list()
    pass


def chat_completion_basic(client: OpenAI, user_message: str) -> str:
    """
    基础聊天完成调用
    
    参数:
        client: OpenAI客户端
        user_message: 用户消息
    
    返回:
        AI的回复
    """
    # TODO: 实现基础聊天调用
    pass


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("请设置OPENAI_API_KEY环境变量")
    else:
        client = create_client()
        print(list_models(client))
        print(chat_completion_basic(client, "Hello!"))

