"""
练习 01: Prompt模板
难度: 🟢 基础
预计时间: 15分钟

目标：掌握LangChain的Prompt模板系统
"""

from langchain.prompts import PromptTemplate, ChatPromptTemplate
from langchain.prompts.chat import SystemMessagePromptTemplate, HumanMessagePromptTemplate


def create_simple_prompt() -> PromptTemplate:
    """
    创建简单的Prompt模板
    
    返回:
        PromptTemplate实例
    
    示例模板：
        "你是一个{role}，请回答：{question}"
    """
    # TODO: 创建PromptTemplate
    pass


def create_chat_prompt() -> ChatPromptTemplate:
    """
    创建聊天Prompt模板（包含System和Human消息）
    
    返回:
        ChatPromptTemplate实例
    
    示例：
        System: "你是一个Python专家"
        Human: "{question}"
    """
    # TODO: 创建ChatPromptTemplate
    pass


def format_prompt(template: PromptTemplate, **kwargs) -> str:
    """
    格式化Prompt
    
    参数:
        template: PromptTemplate
        **kwargs: 变量值
    
    返回:
        格式化后的字符串
    """
    # TODO: 使用template.format()格式化
    pass


if __name__ == "__main__":
    # 测试简单Prompt
    prompt = create_simple_prompt()
    formatted = format_prompt(prompt, role="Python专家", question="什么是装饰器？")
    print(formatted)
    
    # 测试聊天Prompt
    chat_prompt = create_chat_prompt()
    messages = chat_prompt.format_messages(question="解释一下async/await")
    for msg in messages:
        print(f"{msg.__class__.__name__}: {msg.content}")

