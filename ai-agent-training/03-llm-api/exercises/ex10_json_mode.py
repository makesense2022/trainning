"""
练习 10: JSON模式输出
难度: 🟡 进阶
预计时间: 20分钟

目标：让LLM输出严格的JSON格式
"""

from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()


def chat_with_json_mode(client: OpenAI, prompt: str) -> dict:
    """
    使用JSON模式获取结构化输出
    
    参数:
        client: OpenAI客户端
        prompt: 提示词（要求返回JSON）
    
    返回:
        解析后的JSON字典
    """
    # TODO: 设置response_format为json_object
    if not os.getenv("OPENAI_API_KEY"):
        return {"error": "请设置API Key"}
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "你是一个JSON输出助手，只返回有效的JSON。"},
            {"role": "user", "content": prompt}
        ],
        response_format={"type": "json_object"}
    )
    
    content = response.choices[0].message.content
    return json.loads(content)


def extract_structured_data(client: OpenAI, text: str) -> dict:
    """
    从文本中提取结构化数据
    
    参数:
        client: OpenAI客户端
        text: 文本（如"Alice, 25岁, 北京"）
    
    返回:
        结构化数据 {"name": "Alice", "age": 25, "city": "北京"}
    """
    # TODO: 使用JSON模式提取
    prompt = f"从以下文本提取信息，返回JSON格式：{text}\n格式：{{\"name\": \"\", \"age\": 0, \"city\": \"\"}}"
    return chat_with_json_mode(client, prompt)


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        result = extract_structured_data(client, "张三，28岁，上海")
        print(result)

