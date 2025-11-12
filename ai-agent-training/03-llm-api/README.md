# Module 03: LLM API 调用 - 从HTTP到AI

> 目标：1天掌握LLM API调用，理解Token、流式响应、错误处理

## 🎯 学习目标

- [ ] 用Python调用OpenAI/DeepSeek API
- [ ] 理解Token计算和成本估算
- [ ] 实现流式响应（SSE）
- [ ] 掌握错误处理和重试策略
- [ ] 比较不同LLM的特点和定价

## 📊 练习列表（15题）

### Part 1: 基础API调用 (5题) 🟢

| 题号 | 题目 | 难度 | 前端类比 | 预计时间 |
|-----|------|------|---------|---------|
| 01 | 第一个LLM调用 | 🟢 | fetch/axios | 15分钟 |
| 02 | 使用官方SDK | 🟢 | npm包 | 10分钟 |
| 03 | Chat模型参数 | 🟡 | API参数 | 15分钟 |
| 04 | System Prompt设计 | 🟡 | 配置文件 | 20分钟 |
| 05 | 多轮对话 | 🟡 | 状态管理 | 20分钟 |

### Part 2: 高级特性 (5题) 🟡

| 题号 | 题目 | 难度 | 前端类比 | 预计时间 |
|-----|------|------|---------|---------|
| 06 | 流式响应(Streaming) | 🟡 | SSE | 25分钟 |
| 07 | Token计算 | 🟡 | 文本处理 | 15分钟 |
| 08 | 成本估算器 | 🟡 | 计费系统 | 20分钟 |
| 09 | 函数调用(Function Call) | 🔴 | RPC | 30分钟 |
| 10 | JSON模式输出 | 🟡 | 结构化数据 | 20分钟 |

### Part 3: 工程化 (5题) 🔴

| 题号 | 题目 | 难度 | 前端类比 | 预计时间 |
|-----|------|------|---------|---------|
| 11 | 错误处理 | 🟡 | try/catch | 20分钟 |
| 12 | 指数退避重试 | 🔴 | 重试策略 | 25分钟 |
| 13 | 速率限制处理 | 🔴 | 限流 | 25分钟 |
| 14 | 请求批处理 | 🔴 | 批量请求 | 30分钟 |
| 15 | 多模型切换 | 🔴 | 适配器模式 | 30分钟 |

## 🔥 核心概念

### 1. LLM API基本结构

**前端的HTTP请求**：
```javascript
const response = await fetch('https://api.example.com/chat', {
  method: 'POST',
  headers: { 
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${API_KEY}`
  },
  body: JSON.stringify({
    model: 'gpt-3.5-turbo',
    messages: [
      { role: 'user', content: 'Hello!' }
    ]
  })
});
const data = await response.json();
```

**Python + OpenAI SDK**：
```python
from openai import OpenAI

client = OpenAI(api_key="sk-xxx")
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)
print(response.choices[0].message.content)
```

### 2. Token与成本

**Token是什么？**
- 类似"计价单位"，不是字符数
- 1 token ≈ 0.75个英文单词 ≈ 1个中文字
- 示例："你好世界" ≈ 4 tokens, "Hello world" ≈ 2 tokens

**成本计算**：
```python
# GPT-3.5-turbo 定价（2024年）
INPUT_PRICE = 0.0015 / 1000   # $0.0015 per 1K tokens
OUTPUT_PRICE = 0.002 / 1000   # $0.002 per 1K tokens

def calculate_cost(input_tokens, output_tokens):
    return (input_tokens * INPUT_PRICE + 
            output_tokens * OUTPUT_PRICE)

# 1000个输入tokens + 500个输出tokens
cost = calculate_cost(1000, 500)
# ≈ $0.0025 (不到3分钱)
```

### 3. 流式响应（Streaming）

**为什么需要流式？**
- LLM生成文本需要时间（10-30秒）
- 流式可以逐字显示，提升用户体验
- 类似ChatGPT的打字效果

**前端SSE**：
```javascript
const eventSource = new EventSource('/api/stream');
eventSource.onmessage = (event) => {
  const token = event.data;
  displayText += token;  // 逐字追加
};
```

**Python实现**：
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "讲个故事"}],
    stream=True  # 开启流式
)

for chunk in response:
    if chunk.choices[0].delta.content:
        token = chunk.choices[0].delta.content
        print(token, end='', flush=True)  # 逐字打印
```

### 4. 函数调用（Function Calling）

**这是Agent的基础！**

让LLM"调用"您定义的工具：

```python
# 1. 定义工具
tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "获取城市天气",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string"}
            },
            "required": ["city"]
        }
    }
}]

# 2. LLM决定调用
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "北京天气如何？"}],
    tools=tools
)

# 3. LLM返回函数调用请求
function_call = response.choices[0].message.tool_calls[0]
# function_call.function.name == "get_weather"
# function_call.function.arguments == '{"city": "北京"}'

# 4. 您执行真正的函数
result = get_weather("北京")

# 5. 把结果返回给LLM
```

## 🎓 面试高频问题

### Q1: Token是怎么计算的？
**答案**：使用Tokenizer（如tiktoken）。不同模型的tokenizer不同。中文一般1字=1token，英文1词≈1-2tokens。

### Q2: 如何优化成本？
**答案**：
1. 使用更便宜的模型（如gpt-3.5 vs gpt-4）
2. 缓存结果
3. 压缩prompt（去掉不必要的内容）
4. 使用停止词(stop tokens)提前结束生成

### Q3: 流式响应如何实现？
**答案**：服务端用Server-Sent Events (SSE)，客户端监听事件流。Python用`yield`生成器实现。

### Q4: API调用失败怎么办？
**答案**：
1. 捕获异常（APIError, Timeout, RateLimit）
2. 指数退避重试（1s, 2s, 4s, 8s...）
3. 记录日志
4. 降级方案（切换模型或返回默认响应）

### Q5: 不同LLM如何选择？

| 模型 | 优势 | 劣势 | 适用场景 |
|-----|------|------|---------|
| GPT-4 | 最强能力 | 贵、慢 | 复杂推理、代码 |
| GPT-3.5 | 便宜、快 | 能力较弱 | 简单对话、分类 |
| Claude | 长上下文 | 贵 | 文档分析 |
| DeepSeek | 极便宜 | 中文好 | 成本敏感场景 |

## 📝 实战项目

完成15道题后，您将构建：

**项目：智能客服API包装器**
- 支持多模型切换
- 自动重试和降级
- Token统计和成本报告
- 流式响应支持
- 对话历史管理

这将是您的第一个"AI产品"雏形！

## 💡 调试技巧

### 1. 查看完整请求
```python
import json

# 打印发送的消息
messages = [{"role": "user", "content": "Hello"}]
print("发送:", json.dumps(messages, ensure_ascii=False, indent=2))

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# 打印响应
print("响应:", response.model_dump_json(indent=2))
```

### 2. 使用LangSmith追踪
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# 所有调用会自动记录到LangSmith平台
# 可视化查看请求、响应、耗时
```

### 3. 本地调试技巧
```python
# 设置超时避免卡死
response = client.chat.completions.create(
    ...,
    timeout=30.0  # 30秒超时
)

# 打印token使用
print(f"输入: {response.usage.prompt_tokens} tokens")
print(f"输出: {response.usage.completion_tokens} tokens")
print(f"总计: {response.usage.total_tokens} tokens")
```

## ⏭️ 下一步

完成本模块后，您已经可以：
- ✅ 调用任意LLM API
- ✅ 理解Token和成本
- ✅ 处理流式响应
- ✅ 实现工程化的API调用

下一步进入 `04-langchain-basics`，学习如何用LangChain简化这些操作！

