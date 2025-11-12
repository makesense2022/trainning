"""
练习 03: Chat模型参数
难度: 🟡 进阶
预计时间: 15分钟

重要参数：
- temperature: 控制随机性 (0.0-2.0)
- max_tokens: 最大输出长度
- top_p: 核采样
- frequency_penalty: 频率惩罚
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def chat_with_temperature(client: OpenAI, prompt: str, temp: float) -> str:
    """
    使用不同temperature调用
    
    参数:
        client: OpenAI客户端
        prompt: 提示词
        temp: temperature值
    
    返回:
        AI回复
    """
    # TODO: 设置temperature参数
    pass


def chat_with_max_tokens(client: OpenAI, prompt: str, max_tokens: int) -> str:
    """
    限制输出长度
    
    参数:
        client: OpenAI客户端
        prompt: 提示词
        max_tokens: 最大token数
    
    返回:
        AI回复（会被截断）
    """
    # TODO: 设置max_tokens参数
    pass


def compare_temperatures(client: OpenAI, prompt: str) -> dict:
    """
    对比不同temperature的效果
    
    返回:
        {
            "low_temp": temperature=0.0的回复,
            "medium_temp": temperature=0.7的回复,
            "high_temp": temperature=1.5的回复
        }
    """
    # TODO: 对比不同temperature
    pass


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        result = compare_temperatures(client, "写一个关于AI的标题")
        print(result)

