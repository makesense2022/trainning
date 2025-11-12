"""
练习 08: 成本估算器
难度: 🟡 进阶
预计时间: 20分钟

目标：计算LLM API调用的成本
"""

# GPT-3.5-turbo定价（2024年，示例）
PRICING = {
    "gpt-3.5-turbo": {
        "input": 0.0015 / 1000,   # $0.0015 per 1K tokens
        "output": 0.002 / 1000    # $0.002 per 1K tokens
    },
    "gpt-4": {
        "input": 0.03 / 1000,     # $0.03 per 1K tokens
        "output": 0.06 / 1000     # $0.06 per 1K tokens
    }
}


def calculate_cost(prompt_tokens: int, completion_tokens: int, model: str = "gpt-3.5-turbo") -> float:
    """
    计算API调用成本
    
    参数:
        prompt_tokens: 输入token数
        completion_tokens: 输出token数
        model: 模型名称
    
    返回:
        成本（美元）
    """
    # TODO: 根据定价计算成本
    if model not in PRICING:
        return 0.0
    
    pricing = PRICING[model]
    input_cost = (prompt_tokens / 1000) * pricing["input"]
    output_cost = (completion_tokens / 1000) * pricing["output"]
    return input_cost + output_cost


def estimate_text_cost(text: str, model: str = "gpt-3.5-turbo") -> dict:
    """
    估算文本的成本（假设作为输入）
    
    参数:
        text: 文本
        model: 模型名称
    
    返回:
        成本信息字典
    """
    import tiktoken
    
    # TODO: 计算token数和成本
    encoding = tiktoken.encoding_for_model(model)
    tokens = len(encoding.encode(text))
    cost = calculate_cost(tokens, 0, model)
    
    return {
        "tokens": tokens,
        "estimated_cost": cost,
        "cost_per_1k_tokens": PRICING.get(model, {}).get("input", 0) * 1000
    }


def compare_models_cost(prompt_tokens: int, completion_tokens: int) -> dict:
    """
    对比不同模型的成本
    
    参数:
        prompt_tokens: 输入token数
        completion_tokens: 输出token数
    
    返回:
        各模型的成本对比
    """
    # TODO: 计算各模型的成本
    results = {}
    for model in PRICING.keys():
        results[model] = calculate_cost(prompt_tokens, completion_tokens, model)
    return results


if __name__ == "__main__":
    # 测试成本计算
    cost = calculate_cost(1000, 500, "gpt-3.5-turbo")
    print(f"1000输入+500输出tokens成本: ${cost:.4f}")
    
    # 对比模型
    comparison = compare_models_cost(1000, 500)
    for model, cost in comparison.items():
        print(f"{model}: ${cost:.4f}")

