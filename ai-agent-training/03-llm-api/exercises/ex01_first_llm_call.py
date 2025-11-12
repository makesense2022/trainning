"""
练习 01: 第一个LLM调用
难度: 🟢 基础
预计时间: 15分钟

目标：
- 使用OpenAI SDK调用GPT模型
- 理解消息格式（role + content）
- 查看响应结构

前端类比：
这就像调用REST API，只不过返回的是AI生成的文本
"""

import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()


def simple_chat(user_message: str) -> str:
    """
    最简单的LLM调用
    
    步骤：
    1. 导入OpenAI库: from openai import OpenAI
    2. 创建客户端: client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    3. 调用API: client.chat.completions.create(...)
    4. 提取响应: response.choices[0].message.content
    
    参数:
        user_message: 用户输入的消息
    
    返回:
        str: LLM的回复
    
    示例:
        >>> simple_chat("你好")
        "你好！有什么我可以帮助你的吗？"
    """
    # TODO: 实现LLM调用
    # 提示：
    # from openai import OpenAI
    # client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {"role": "user", "content": user_message}
    #     ]
    # )
    # return response.choices[0].message.content
    pass


def chat_with_system_prompt(user_message: str, system_prompt: str) -> str:
    """
    带系统提示词的LLM调用
    
    System Prompt（系统提示词）：
    - 定义AI的"人设"和行为规范
    - 类似给AI下达"工作指令"
    - 例如："你是一个专业的Python教师"
    
    消息结构：
    [
        {"role": "system", "content": "你是..."},  # AI的人设
        {"role": "user", "content": "..."}         # 用户的问题
    ]
    
    参数:
        user_message: 用户消息
        system_prompt: 系统提示词
    
    返回:
        str: LLM的回复
    
    示例:
        >>> chat_with_system_prompt(
        ...     user_message="什么是变量？",
        ...     system_prompt="你是一个Python教师，用简单的语言解释概念"
        ... )
        "变量就像一个盒子，可以存放数据..."
    """
    # TODO: 实现带system prompt的调用
    # 提示：messages列表中先加system消息，再加user消息
    pass


def get_response_metadata(user_message: str) -> dict:
    """
    获取响应的元数据（token使用量、模型等）
    
    响应对象不仅包含文本，还有很多有用信息：
    - model: 使用的模型
    - usage.prompt_tokens: 输入token数
    - usage.completion_tokens: 输出token数
    - usage.total_tokens: 总token数
    
    参数:
        user_message: 用户消息
    
    返回:
        dict: {
            "content": "AI回复",
            "model": "gpt-3.5-turbo",
            "prompt_tokens": 10,
            "completion_tokens": 20,
            "total_tokens": 30
        }
    """
    # TODO: 实现并返回元数据
    # 提示：
    # response = client.chat.completions.create(...)
    # return {
    #     "content": response.choices[0].message.content,
    #     "model": response.model,
    #     "prompt_tokens": response.usage.prompt_tokens,
    #     "completion_tokens": response.usage.completion_tokens,
    #     "total_tokens": response.usage.total_tokens
    # }
    pass


def chat_with_parameters(
    user_message: str,
    temperature: float = 0.7,
    max_tokens: int = 100
) -> str:
    """
    带参数控制的LLM调用
    
    重要参数：
    
    temperature（温度）：
    - 范围：0.0 - 2.0
    - 0.0: 非常确定、重复性高（适合分类、提取）
    - 1.0: 默认值，平衡
    - 2.0: 非常随机、创意性强（适合创作）
    
    max_tokens（最大token数）：
    - 限制输出长度
    - 1 token ≈ 0.75个英文单词
    - 用于控制成本
    
    参数:
        user_message: 用户消息
        temperature: 温度参数
        max_tokens: 最大输出token数
    
    返回:
        str: LLM的回复
    """
    # TODO: 实现带参数的调用
    # 提示：在create()中加入temperature和max_tokens参数
    pass


# ============ 测试代码 ============

if __name__ == "__main__":
    # 测试前请确保设置了环境变量：
    # export OPENAI_API_KEY="sk-xxx"
    # 或在项目根目录创建 .env 文件
    
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ 请先设置 OPENAI_API_KEY 环境变量")
        print("   export OPENAI_API_KEY='sk-xxx'")
        exit(1)
    
    print("=" * 60)
    print("测试 1: 简单对话")
    print("=" * 60)
    try:
        response = simple_chat("用一句话介绍Python")
        print(f"回复: {response}")
    except Exception as e:
        print(f"错误: {e}")
    
    print("\n" + "=" * 60)
    print("测试 2: 带系统提示词")
    print("=" * 60)
    try:
        response = chat_with_system_prompt(
            user_message="什么是装饰器？",
            system_prompt="你是一个Python专家，用通俗易懂的语言解释技术概念，最多3句话"
        )
        print(f"回复: {response}")
    except Exception as e:
        print(f"错误: {e}")
    
    print("\n" + "=" * 60)
    print("测试 3: 获取元数据")
    print("=" * 60)
    try:
        metadata = get_response_metadata("你好")
        print(f"回复: {metadata['content']}")
        print(f"模型: {metadata['model']}")
        print(f"输入tokens: {metadata['prompt_tokens']}")
        print(f"输出tokens: {metadata['completion_tokens']}")
        print(f"总tokens: {metadata['total_tokens']}")
    except Exception as e:
        print(f"错误: {e}")
    
    print("\n" + "=" * 60)
    print("测试 4: 温度对比")
    print("=" * 60)
    prompt = "写一个关于AI的标题"
    
    print("温度=0.0 (确定性):")
    try:
        response1 = chat_with_parameters(prompt, temperature=0.0)
        print(f"  {response1}")
    except Exception as e:
        print(f"  错误: {e}")
    
    print("\n温度=1.5 (创造性):")
    try:
        response2 = chat_with_parameters(prompt, temperature=1.5)
        print(f"  {response2}")
    except Exception as e:
        print(f"  错误: {e}")
    
    print("\n" + "=" * 60)
    print("测试 5: max_tokens限制")
    print("=" * 60)
    try:
        response = chat_with_parameters(
            "详细介绍Python的历史",
            max_tokens=50  # 限制为50个tokens
        )
        print(f"回复（限制50 tokens）: {response}")
    except Exception as e:
        print(f"错误: {e}")


# ============ 进阶知识 ============

def demo_different_models():
    """
    演示不同模型的使用
    
    常用模型：
    - gpt-3.5-turbo: 便宜、快速、适合简单任务
    - gpt-4: 强大但贵、适合复杂推理
    - gpt-4-turbo-preview: GPT-4的快速版本
    """
    from openai import OpenAI
    client = OpenAI()
    
    models = [
        "gpt-3.5-turbo",
        # "gpt-4",  # 取消注释以测试GPT-4
    ]
    
    prompt = "用一句话解释量子计算"
    
    for model in models:
        print(f"\n使用模型: {model}")
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        print(f"回复: {response.choices[0].message.content}")
        print(f"Tokens: {response.usage.total_tokens}")


if __name__ == "__main__":
    # 取消注释以测试不同模型
    # demo_different_models()
    pass

