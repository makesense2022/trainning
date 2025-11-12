"""
练习 06: 流式响应(Streaming)
难度: 🟡 进阶
预计时间: 25分钟

目标：实现流式响应，类似ChatGPT的打字效果
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def stream_chat_completion(client: OpenAI, user_message: str) -> str:
    """
    流式聊天完成
    
    参数:
        client: OpenAI客户端
        user_message: 用户消息
    
    返回:
        完整的回复（所有token拼接）
    
    提示：
    1. 设置 stream=True
    2. 遍历响应chunk
    3. 提取 chunk.choices[0].delta.content
    4. 拼接所有内容
    """
    # TODO: 实现流式响应
    pass


def stream_with_print(client: OpenAI, user_message: str):
    """
    流式响应并实时打印（类似ChatGPT效果）
    
    参数:
        client: OpenAI客户端
        user_message: 用户消息
    
    提示：
    使用 print(..., end='', flush=True) 实现逐字打印
    """
    # TODO: 实现实时打印的流式响应
    pass


if __name__ == "__main__":
    if not os.getenv("OPENAI_API_KEY"):
        print("请设置OPENAI_API_KEY环境变量")
    else:
        client = OpenAI()
        result = stream_chat_completion(client, "讲一个短故事")
        print(f"\n完整回复: {result}")

