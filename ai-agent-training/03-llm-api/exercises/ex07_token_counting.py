"""
练习 07: Token计算
难度: 🟡 进阶
预计时间: 15分钟

目标：理解Token机制，计算文本的token数
"""

import tiktoken
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def count_tokens(text: str, model: str = "gpt-3.5-turbo") -> int:
    """
    计算文本的token数
    
    参数:
        text: 文本
        model: 模型名称
    
    返回:
        token数量
    """
    # TODO: 使用tiktoken计算
    pass


def estimate_cost(prompt_tokens: int, completion_tokens: int, model: str = "gpt-3.5-turbo") -> float:
    """
    估算API调用成本
    
    GPT-3.5-turbo定价（2024）:
    - Input: $0.0015 / 1K tokens
    - Output: $0.002 / 1K tokens
    
    参数:
        prompt_tokens: 输入token数
        completion_tokens: 输出token数
        model: 模型名称
    
    返回:
        成本（美元）
    """
    # TODO: 计算成本
    pass


def analyze_text_tokens(text: str) -> dict:
    """
    分析文本的token信息
    
    返回:
        {
            "text": 原文,
            "tokens": token数,
            "chars": 字符数,
            "tokens_per_char": 每字符token数,
            "estimated_cost": 估算成本（假设1000输入+500输出）
        }
    """
    # TODO: 分析文本
    pass


if __name__ == "__main__":
    text = "你好世界 Hello World"
    print(analyze_text_tokens(text))

