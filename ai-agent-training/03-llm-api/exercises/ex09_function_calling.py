"""
练习 09: 函数调用 (Function Calling)
难度: 🔴 挑战
预计时间: 30分钟

这是Agent的基础！让LLM能够调用您定义的函数
"""

from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()


def define_weather_tool() -> dict:
    """
    定义天气查询工具
    
    返回:
        工具定义（OpenAI Function格式）
    """
    # TODO: 定义工具schema
    pass


def call_with_function(client: OpenAI, user_message: str, tools: list) -> dict:
    """
    使用函数调用功能
    
    参数:
        client: OpenAI客户端
        user_message: 用户消息
        tools: 工具列表
    
    返回:
        {
            "message": LLM的回复,
            "function_calls": 函数调用列表（如果有）
        }
    """
    # TODO: 实现函数调用
    pass


def execute_function_call(function_name: str, arguments: dict):
    """
    执行函数调用
    
    参数:
        function_name: 函数名
        arguments: 参数字典
    
    返回:
        函数执行结果
    """
    # TODO: 根据函数名执行对应函数
    if function_name == "get_weather":
        # 模拟天气查询
        city = arguments.get("city", "Unknown")
        return f"{city}今天晴天，25°C"
    pass


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        tools = [define_weather_tool()]
        result = call_with_function(client, "北京天气如何？", tools)
        print(result)

