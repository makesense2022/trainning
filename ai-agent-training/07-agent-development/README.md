# Module 07: Agent开发 - 让AI拥有工具

> 目标：2天掌握AI Agent开发，从"对话机器人"进化到"能做事的智能体"

## 🎯 学习目标

- [ ] 理解Agent的本质（思考 + 工具调用）
- [ ] 掌握ReAct思维链
- [ ] 实现自定义工具
- [ ] 构建多工具Agent
- [ ] 处理Agent错误和兜底

## 🔥 Agent是什么？

### Chain vs Agent

**Chain（链）**：固定流程
```
用户提问 → 检索文档 → 生成答案
   ↓          ↓          ↓
  固定      固定       固定
```
像一条"生产线"，每次执行相同步骤。

**Agent（智能体）**：自主决策
```
用户提问 
   ↓
 [思考] 我需要什么工具？
   ↓
 选择工具A
   ↓
 [思考] 结果够不够？
   ↓
 选择工具B
   ↓
 [思考] 可以回答了
   ↓
 返回答案
```
像一个"员工"，自己判断该做什么。

### 代码对比

**Chain方式**（固定流程）：
```python
# 只能搜索文档，不能做其他事
chain = RetrievalQA.from_chain_type(
    llm=llm,
    retriever=retriever
)

result = chain("北京天气如何？")
# ❌ 无法回答，因为文档里没有天气信息
```

**Agent方式**（自主决策）：
```python
# 可以选择使用不同工具
tools = [
    search_document_tool,    # 搜索文档
    get_weather_tool,        # 查天气
    calculator_tool          # 计算器
]

agent = create_react_agent(llm, tools)

result = agent.invoke("北京天气如何？")
# ✅ Agent思考：需要天气工具 → 调用get_weather_tool → 返回答案
```

## 📊 练习列表（20题）

### Part 1: Agent基础 (5题) 🟢🟡

| 题号 | 题目 | 难度 | 核心概念 | 预计时间 |
|-----|------|------|---------|---------|
| 01 | 理解ReAct思维链 | 🟢 | Thought-Action | 15分钟 |
| 02 | 第一个简单Agent | 🟡 | Basic Agent | 20分钟 |
| 03 | Agent执行追踪 | 🟡 | Verbose Mode | 15分钟 |
| 04 | Agent vs Chain对比 | 🟡 | 概念理解 | 20分钟 |
| 05 | Agent的限制 | 🟡 | Max Iterations | 15分钟 |

### Part 2: 工具开发 (7题) 🟡🔴

| 题号 | 题目 | 难度 | 核心概念 | 预计时间 |
|-----|------|------|---------|---------|
| 06 | 定义简单工具 | 🟡 | Tool Decorator | 20分钟 |
| 07 | 带参数的工具 | 🟡 | Tool Args | 25分钟 |
| 08 | 工具的描述优化 | 🔴 | Tool Description | 30分钟 |
| 09 | 异步工具 | 🔴 | Async Tools | 30分钟 |
| 10 | 工具错误处理 | 🔴 | Error Handling | 25分钟 |
| 11 | RAG作为工具 | 🔴 | Tool Integration | 30分钟 |
| 12 | 多个工具组合 | 🔴 | Tool Composition | 35分钟 |

### Part 3: 高级Agent (8题) 🔴🔥

| 题号 | 题目 | 难度 | 核心概念 | 预计时间 |
|-----|------|------|---------|---------|
| 13 | 对话式Agent | 🔴 | Memory | 30分钟 |
| 14 | 带记忆的Agent | 🔴 | Chat History | 35分钟 |
| 15 | 结构化输出 | 🔴 | Output Parser | 30分钟 |
| 16 | Agent兜底策略 | 🔴 | Fallback | 30分钟 |
| 17 | 多Agent协作 | 🔥 | Multi-Agent | 60分钟 |
| 18 | LangGraph基础 | 🔥 | State Graph | 60分钟 |
| 19 | Human-in-the-Loop | 🔥 | Approval | 45分钟 |
| 20 | Agent评测 | 🔴 | Evaluation | 40分钟 |

## 🔑 核心概念详解

### 1. ReAct思维链

**ReAct = Reasoning (推理) + Acting (行动)**

**思维过程**：
```
User: 如果我的文档作者今天在北京，他会觉得冷吗？

[Thought] 我需要知道两件事：1)文档作者在哪 2)北京天气
[Action] 使用search_document工具查询作者位置
[Observation] 作者在"北京"

[Thought] 现在我知道作者在北京了，需要查北京天气
[Action] 使用get_weather工具查询北京天气
[Observation] 北京今天10°C，晴

[Thought] 10°C算比较冷，可以回答了
[Final Answer] 北京今天10°C，对于大多数人来说会觉得有点冷，建议作者穿件外套。
```

**代码实现**：
```python
from langchain.agents import create_react_agent
from langchain import hub

# 使用LangChain Hub的标准ReAct prompt
prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # 打印思维过程
    max_iterations=5  # 最多思考5轮
)

result = agent_executor.invoke({"input": "..."})
```

### 2. 工具定义

**方式1：使用@tool装饰器**（推荐）：

```python
from langchain.tools import tool

@tool
def get_weather(city: str) -> str:
    """
    获取城市的天气信息
    
    Args:
        city: 城市名称，如"北京"、"上海"
    
    Returns:
        天气描述字符串
    """
    # 实际实现
    api_result = weather_api.get(city)
    return f"{city}今天{api_result['temp']}°C，{api_result['condition']}"

# LangChain会自动：
# 1. 从docstring提取描述
# 2. 从类型注解推断参数
# 3. 生成工具的JSON Schema
```

**为什么描述重要？**

LLM通过描述决定调用哪个工具：

```python
# ❌ 糟糕的描述
@tool
def tool1(x: str) -> str:
    """A tool"""  # 太模糊
    ...

# ✅ 好的描述
@tool
def search_knowledge_base(query: str) -> str:
    """
    在公司知识库中搜索相关文档
    
    适用场景：
    - 查询公司政策、流程
    - 查找技术文档
    - 历史项目信息
    
    Args:
        query: 搜索关键词，如"报销流程"、"Python最佳实践"
    
    Returns:
        相关文档摘要
    """
    ...
```

**方式2：使用Tool类**：

```python
from langchain.tools import Tool

def _get_weather(city: str) -> str:
    # 实际实现
    return f"{city}天气"

weather_tool = Tool(
    name="get_weather",
    description="获取城市天气，输入城市名称",
    func=_get_weather
)
```

### 3. 工具参数验证

使用Pydantic进行严格类型检查：

```python
from pydantic import BaseModel, Field
from langchain.tools import StructuredTool

class WeatherInput(BaseModel):
    """获取天气的输入参数"""
    city: str = Field(description="城市名称")
    unit: str = Field(
        default="celsius",
        description="温度单位：celsius（摄氏度）或 fahrenheit（华氏度）"
    )

@tool("get_weather", args_schema=WeatherInput)
def get_weather(city: str, unit: str = "celsius") -> str:
    """获取城市天气"""
    # 参数会自动验证
    ...
```

### 4. Agent类型对比

| 类型 | 特点 | 适用场景 | LangChain实现 |
|-----|------|---------|--------------|
| ReAct | 思考-行动循环 | 通用 | create_react_agent |
| OpenAI Functions | 使用函数调用 | OpenAI模型 | create_openai_functions_agent |
| Structured Chat | 结构化输入 | 复杂参数 | create_structured_chat_agent |
| Self-Ask | 分解子问题 | 复杂推理 | create_self_ask_agent |
| Plan-and-Execute | 先规划后执行 | 多步任务 | PlanAndExecute |

**选择建议**：
- 90%场景用**ReAct**
- 用OpenAI模型 → **OpenAI Functions**（更快、更准）
- 需要规划 → **Plan-and-Execute**

### 5. LangGraph（新一代Agent框架）

**为什么需要LangGraph？**

传统Agent的问题：
```
❌ 流程不可控（LLM决定一切）
❌ 难以调试
❌ 无法加入人工审批
❌ 无法处理复杂流程（如条件分支）
```

LangGraph的解决方案：
```
✅ 明确定义状态转移
✅ 可视化流程图
✅ 支持人工介入
✅ 支持复杂的循环、分支
```

**基本示例**：

```python
from langgraph.graph import StateGraph, END

# 1. 定义状态
class AgentState(TypedDict):
    messages: list
    current_tool: str
    result: str

# 2. 定义节点
def think_node(state):
    # LLM思考
    ...
    return state

def act_node(state):
    # 执行工具
    ...
    return state

# 3. 构建图
workflow = StateGraph(AgentState)
workflow.add_node("think", think_node)
workflow.add_node("act", act_node)

# 4. 定义边（流程）
workflow.add_edge("think", "act")
workflow.add_conditional_edges(
    "act",
    lambda state: "continue" if state["need_more"] else "end",
    {
        "continue": "think",
        "end": END
    }
)

workflow.set_entry_point("think")
agent = workflow.compile()
```

## 🎓 面试高频问题

### Q1: Agent和Chain有什么区别？

**答案**：
- **Chain**：固定流程，A→B→C，适合确定性任务
- **Agent**：动态决策，LLM选择工具和执行顺序，适合开放性任务

比喻：Chain是"菜谱"（固定步骤），Agent是"厨师"（根据情况调整）

### Q2: 如何提高Agent的可靠性？

**答案**：
1. **好的工具描述**：让LLM理解何时使用
2. **限制max_iterations**：防止无限循环
3. **Prompt Engineering**：明确任务边界
4. **兜底策略**：工具失败时的处理
5. **人工审批**：关键操作需要确认

### Q3: Agent为什么会失败？

**常见原因**：
1. **工具选择错误**：描述不清晰
2. **参数错误**：LLM传错了参数
3. **无限循环**：一直在重复相同操作
4. **幻觉**：LLM编造了不存在的工具

**解决方案**：
```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=5,              # 限制迭代次数
    max_execution_time=60,         # 限制总时间
    early_stopping_method="force", # 强制停止
    handle_parsing_errors=True     # 处理解析错误
)
```

### Q4: LangChain vs LangGraph vs AutoGen？

| 框架 | 特点 | 适用场景 |
|-----|------|---------|
| LangChain Agent | 简单、快速 | 单Agent、简单任务 |
| LangGraph | 可控、可视化 | 复杂流程、需要审批 |
| AutoGen | 多Agent对话 | 需要多个角色协作 |

**建议**：先学LangChain，再学LangGraph

### Q5: 如何评测Agent质量？

**评测维度**：
1. **任务完成率**：多少问题被正确解决？
2. **工具使用准确率**：是否选对了工具？
3. **效率**：平均迭代次数
4. **成本**：Token使用量

```python
# 简单的评测框架
test_cases = [
    {"input": "北京天气", "expected_tool": "get_weather"},
    {"input": "计算2+3", "expected_tool": "calculator"},
]

for case in test_cases:
    result = agent.invoke(case["input"])
    actual_tool = extract_tool_from_result(result)
    print(f"{'✅' if actual_tool == case['expected_tool'] else '❌'}")
```

## 💡 调试技巧

### 1. 启用详细日志
```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,  # 打印思维过程
    return_intermediate_steps=True  # 返回中间步骤
)

result = agent_executor.invoke({"input": "..."})
print(result["intermediate_steps"])  # 查看每一步
```

### 2. 使用LangSmith追踪
```python
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "my-agent-debug"

# 所有执行会自动记录到LangSmith
# 可视化查看：思考过程、工具调用、时间分布
```

### 3. 单独测试工具
```python
# 先测试工具本身是否正常
result = get_weather.invoke("北京")
print(result)

# 再测试Agent是否能正确选择
```

## 🚀 实战项目

完成本模块后，您将构建：

**项目：多功能AI助手**
- 搜索知识库（RAG工具）
- 查询天气（API工具）
- 计算器（Python工具）
- 发送邮件（集成工具）
- 对话历史记忆
- 人工审批关键操作

这就是一个生产级Agent的雏形！

## ⏭️ 下一步

完成本模块后，您将掌握：
- ✅ ReAct思维链原理
- ✅ 自定义工具开发
- ✅ 多工具Agent构建
- ✅ Agent调试和优化

下一步进入 `08-final-projects`，完成3个综合项目，整合所有知识！

