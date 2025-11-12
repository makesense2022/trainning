"""
练习 04: System Prompt设计
难度: 🟡 进阶
预计时间: 20分钟

System Prompt是定义AI"人设"的关键
"""

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


def create_role_prompt(role: str, style: str) -> str:
    """
    创建角色Prompt
    
    参数:
        role: 角色（如"Python专家"、"教师"）
        style: 风格（如"简洁"、"详细"）
    
    返回:
        System Prompt字符串
    """
    # TODO: 创建角色Prompt
    return f"你是一个{role}，请用{style}的方式回答问题。"


def create_task_prompt(task: str, constraints: list) -> str:
    """
    创建任务Prompt
    
    参数:
        task: 任务描述
        constraints: 约束条件列表
    
    返回:
        System Prompt字符串
    """
    # TODO: 组合任务和约束
    constraints_str = "\n".join(f"- {c}" for c in constraints)
    return f"任务：{task}\n约束条件：\n{constraints_str}"


def chat_with_system_prompt(client: OpenAI, system_prompt: str, user_message: str) -> str:
    """
    使用System Prompt进行对话
    
    参数:
        client: OpenAI客户端
        system_prompt: System Prompt
        user_message: 用户消息
    
    返回:
        AI回复
    """
    # TODO: 调用API，包含system消息
    if not os.getenv("OPENAI_API_KEY"):
        return "请设置API Key"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    if os.getenv("OPENAI_API_KEY"):
        client = OpenAI()
        system_prompt = create_role_prompt("Python专家", "简洁")
        result = chat_with_system_prompt(client, system_prompt, "什么是装饰器？")
        print(result)

