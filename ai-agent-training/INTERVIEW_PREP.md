# AI Agent 面试准备指南

> 为有14年前端经验的架构师准备的AI面试宝典

## 🎯 面试知识图谱

### 核心技术栈（必问）

```
AI开发技术栈
├── Python核心 ⭐⭐⭐⭐⭐
│   ├── 异步编程 (async/await)
│   ├── 装饰器
│   ├── 类型注解
│   └── 常用库 (pathlib, requests, pydantic)
│
├── LLM基础 ⭐⭐⭐⭐⭐
│   ├── Token机制
│   ├── Prompt Engineering
│   ├── Function Calling
│   ├── 流式响应
│   └── 成本优化
│
├── LangChain ⭐⭐⭐⭐⭐
│   ├── Prompt Template
│   ├── Chain构建
│   ├── Memory机制
│   ├── Callback系统
│   └── LangSmith调试
│
├── RAG ⭐⭐⭐⭐⭐
│   ├── Embedding原理
│   ├── 向量数据库
│   ├── 文档切分策略
│   ├── 检索优化
│   └── 评测指标
│
├── Agent ⭐⭐⭐⭐⭐
│   ├── ReAct思维链
│   ├── 工具定义
│   ├── 多Agent协作
│   ├── LangGraph
│   └── 错误处理
│
└── 工程实践 ⭐⭐⭐⭐
    ├── API设计
    ├── 错误处理
    ├── 监控日志
    ├── 部署运维
    └── 安全合规
```

## 💬 100个高频面试题

### 第一部分：Python基础 (15题)

#### 1. Python的GIL是什么？对多线程有什么影响？

**答案**：
- GIL (Global Interpreter Lock) 是Python的全局解释器锁
- 同一时刻只允许一个线程执行Python字节码
- **影响**：多线程无法利用多核CPU（CPU密集型任务）
- **解决**：
  - CPU密集型：用multiprocessing（多进程）
  - IO密集型：用asyncio（异步）

**面试加分**：
```python
# 错误：多线程做CPU密集任务（没有加速）
import threading

# 正确：多进程做CPU密集任务
import multiprocessing

# 最佳：异步做IO密集任务
import asyncio
```

---

#### 2. 装饰器的原理是什么？写一个缓存装饰器

**答案**：
装饰器是返回函数的高阶函数，利用闭包保存状态。

```python
from functools import wraps

def cache(func):
    """缓存装饰器"""
    cache_dict = {}
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 生成缓存key
        key = (args, tuple(sorted(kwargs.items())))
        
        if key not in cache_dict:
            cache_dict[key] = func(*args, **kwargs)
        
        return cache_dict[key]
    
    # 暴露缓存字典用于调试
    wrapper.cache = cache_dict
    return wrapper

@cache
def expensive_function(n):
    return n ** 2
```

---

#### 3. Python的类型系统和TypeScript有什么区别？

**对比**：

| 特性 | Python | TypeScript |
|-----|--------|-----------|
| 类型检查 | 运行时可选 | 编译时强制 |
| 类型注解 | 可选（PEP 484） | 必需 |
| 类型推断 | 有但较弱 | 强大 |
| 鸭子类型 | 是 | 否 |

```python
# Python: 运行时不检查
def add(a: int, b: int) -> int:
    return a + b

add("1", "2")  # 运行时才报错，类型检查工具会警告
```

```typescript
// TypeScript: 编译时就报错
function add(a: number, b: number): number {
    return a + b;
}

add("1", "2");  // 编译错误 ✅
```

---

### 第二部分：LLM基础 (20题)

#### 4. Token是什么？如何计算？

**答案**：
- Token是LLM处理文本的基本单位
- **不是字符**，不是单词，是子词(subword)
- 计算：使用Tokenizer（如tiktoken）

```python
import tiktoken

encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

text = "你好世界 Hello World"
tokens = encoding.encode(text)
print(f"Token数: {len(tokens)}")  # ~8个tokens

# 规律：
# 英文: 1个单词 ≈ 1-2 tokens
# 中文: 1个字 ≈ 1-2 tokens
# 代码: 符号、关键字各算tokens
```

**面试陷阱**：
```python
# ❌ 错误：用len()计算
len("你好世界")  # 4（字符数）

# ✅ 正确：用tiktoken
len(encoding.encode("你好世界"))  # 6-8（token数）
```

---

#### 5. 如何优化LLM调用成本？

**答案**（5个维度）：

1. **选择合适模型**
```python
# 简单任务用便宜模型
if task == "分类":
    model = "gpt-3.5-turbo"  # $0.0015/1K tokens
else:
    model = "gpt-4"  # $0.03/1K tokens
```

2. **压缩Prompt**
```python
# ❌ 啰嗦的prompt (100 tokens)
prompt = "请你作为一个专业的Python工程师，用非常详细和专业的语言..."

# ✅ 简洁的prompt (20 tokens)
prompt = "作为Python专家，简洁回答："
```

3. **缓存结果**
```python
from functools import lru_cache

@lru_cache(maxsize=1000)
def llm_call(prompt):
    return client.chat.completions.create(...)
```

4. **限制输出长度**
```python
response = client.chat.completions.create(
    max_tokens=100,  # 限制输出
    stop=["\n\n"]    # 遇到双换行就停
)
```

5. **使用RAG而非Fine-tuning**
```python
# RAG: 检索成本低
cost = embedding_cost + retrieval_cost + generation_cost

# Fine-tuning: 训练成本高
cost = training_cost * epochs + generation_cost
```

---

#### 6. 什么是Temperature？如何选择？

**答案**：

Temperature控制输出的随机性：

| Temperature | 特点 | 适用场景 |
|------------|------|---------|
| 0.0 | 确定性，重复性高 | 分类、提取、代码生成 |
| 0.3-0.7 | 平衡 | 问答、总结 |
| 0.8-1.0 | 创造性 | 文案、故事、头脑风暴 |
| 1.2-2.0 | 非常随机 | 创意写作、诗歌 |

```python
# 提取结构化信息 → Temperature=0
extract_info(prompt, temperature=0)

# 写创意文案 → Temperature=1.2
generate_slogan(prompt, temperature=1.2)
```

**原理**：Temperature影响softmax概率分布
```
temperature=0  : 总选概率最高的token
temperature=1  : 按原始概率采样
temperature=2  : 概率分布更平坦（更随机）
```

---

### 第三部分：RAG (25题)

#### 7. RAG和Fine-tuning有什么区别？什么时候用哪个？

**核心区别**：

| 维度 | RAG | Fine-tuning |
|-----|-----|-------------|
| 知识存储 | 外部向量库 | 模型参数 |
| 更新成本 | 低（换文档） | 高（重新训练） |
| 推理成本 | 较高（需检索） | 低 |
| 可解释性 | 高（可查引用） | 低 |
| 适用场景 | 动态知识、私有数据 | 特定风格、领域知识内化 |

**选择建议**：
```python
if "知识会经常变化":
    use_rag()  # 如：新闻、公司文档
elif "需要改变语言风格":
    use_finetuning()  # 如：客服语气、特定格式
elif "两者都需要":
    use_both()  # 先Fine-tune语气，再RAG知识
```

---

#### 8. 如何选择chunk_size？

**答案**：

```python
# 经验法则
chunk_size = {
    "短问答": 200-500,      # 如FAQ
    "通用文档": 500-1000,   # 如技术文档
    "长文档": 1000-2000,    # 如研究论文
    "代码": 按函数/类切分    # 保持完整性
}

chunk_overlap = chunk_size * 0.1  # 10-20%重叠
```

**权衡**：
- 太小（<200）：上下文不足，语义不完整
- 太大（>2000）：检索不精准，噪音多

**测试方法**：
```python
# A/B测试不同chunk_size
for size in [500, 1000, 1500]:
    rag = build_rag(chunk_size=size)
    score = evaluate(rag, test_questions)
    print(f"Size {size}: {score}")
```

---

#### 9. 什么是Embedding？向量相似度如何计算？

**Embedding原理**：
- 把文本转为高维向量（如768维）
- 语义相似的文本，向量距离近

```python
from openai import OpenAI
client = OpenAI()

# 生成Embedding
text1 = "Python是一种编程语言"
embedding1 = client.embeddings.create(
    input=text1,
    model="text-embedding-ada-002"
).data[0].embedding

# embedding1 = [0.001, -0.023, ..., 0.045]  # 1536维向量
```

**相似度计算**：

1. **余弦相似度**（最常用）
```python
import numpy as np

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

# 范围：-1到1，越接近1越相似
```

2. **欧式距离**
```python
def euclidean_distance(v1, v2):
    return np.linalg.norm(np.array(v1) - np.array(v2))

# 距离越小越相似
```

3. **点积**
```python
def dot_product(v1, v2):
    return np.dot(v1, v2)

# 值越大越相似（适用于归一化向量）
```

---

#### 10. 如何评测RAG质量？

**答案**：使用RAGAS框架，4个关键指标

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,        # 忠实度
    answer_relevancy,    # 答案相关性
    context_precision,   # 上下文精度
    context_recall       # 上下文召回
)

# 评测数据
eval_data = {
    "question": ["什么是Python?"],
    "answer": ["Python是一种编程语言"],
    "contexts": [["Python由Guido创建..."]],
    "ground_truth": ["Python是高级编程语言"]
}

result = evaluate(eval_data, metrics=[...])

# 结果解读：
# faithfulness=0.95  → 95%的答案有文档支持（越高越好）
# answer_relevancy=0.88 → 88%的答案相关（越高越好）
# context_precision=0.82 → 82%的检索是准确的
# context_recall=0.79 → 79%的关键信息被检索到
```

**诊断**：
```python
if faithfulness < 0.8:
    print("改进Prompt：要求严格引用文档")
if context_precision < 0.7:
    print("优化Embedding模型或切分策略")
if context_recall < 0.7:
    print("增加检索数量k，或使用混合检索")
```

---

### 第四部分：Agent (20题)

#### 11. Agent和Chain有什么区别？

**本质区别**：

```python
# Chain: 固定流程
user_input → retrieve_docs → generate_answer
    ↓            ↓                ↓
  确定         确定             确定

# Agent: 动态决策
user_input
    ↓
  [LLM思考: 我需要什么工具？]
    ↓
  选择Tool A
    ↓
  [LLM思考: 结果够不够？]
    ↓
  选择Tool B
    ↓
  [LLM思考: 可以回答了]
    ↓
  返回答案
```

**比喻**：
- Chain = 生产线（固定步骤）
- Agent = 员工（自主决策）

**代码对比**：
```python
# Chain: 只能做一件事
chain = RetrievalQA.from_chain_type(llm, retriever)
chain("天气如何？")  # ❌ 无法回答（文档里没有）

# Agent: 自己选工具
agent = create_react_agent(llm, [doc_tool, weather_tool])
agent("天气如何？")  # ✅ 自动调用weather_tool
```

---

#### 12. 什么是ReAct？

**ReAct = Reasoning (推理) + Acting (行动)**

**思维过程**：
```
User: 北京明天天气如何？如果下雨，推荐室内活动

[Thought] 需要先查天气
[Action] get_weather("北京", "明天")
[Observation] 明天北京有雨，15-20°C

[Thought] 确实会下雨，需要推荐室内活动
[Action] search_activities("室内", "北京")
[Observation] 找到：博物馆、电影院、图书馆...

[Thought] 有足够信息了，可以回答
[Final Answer] 北京明天有雨...推荐去博物馆...
```

**实现**：
```python
from langchain.agents import create_react_agent

agent = create_react_agent(
    llm=llm,
    tools=[get_weather_tool, search_activities_tool],
    prompt=react_prompt  # ReAct格式的prompt
)

result = agent.invoke({"input": "..."})
```

---

#### 13. 如何定义一个好的Tool？

**5个关键要素**：

```python
from langchain.tools import tool

@tool
def search_knowledge_base(query: str, limit: int = 3) -> str:
    """
    在公司知识库中搜索相关文档
    
    适用场景:
    - 查询公司政策、流程
    - 技术文档查找
    - 历史项目信息
    
    Args:
        query: 搜索关键词，如"报销流程"、"Python规范"
        limit: 返回结果数量，默认3
    
    Returns:
        相关文档摘要，JSON格式
    
    示例:
        >>> search_knowledge_base("报销流程")
        {"docs": [...], "total": 5}
    """
    # 实现...
    pass
```

**5个要素**：
1. **清晰的名称**：`search_knowledge_base`（不要叫`tool1`）
2. **详细的描述**：LLM根据描述选工具
3. **明确的参数**：类型注解 + 说明
4. **使用场景**：告诉LLM什么时候用
5. **示例**：帮助LLM理解

---

#### 14. Agent为什么会失败？如何提高可靠性？

**常见失败原因**：

1. **工具选择错误**
```python
# 问题：描述不清
@tool
def tool1(x: str):
    """A tool"""  # 太模糊

# 解决：详细描述
@tool
def search_documents(query: str):
    """在文档库中搜索，适合查询公司信息、技术文档"""
```

2. **参数传递错误**
```python
# 问题：LLM传错了参数类型
@tool
def calculate(expression: str):
    return eval(expression)

# LLM可能传：calculate(expression=123)  # 类型错误

# 解决：用Pydantic验证
from pydantic import BaseModel

class CalculatorInput(BaseModel):
    expression: str

@tool(args_schema=CalculatorInput)
def calculate(expression: str):
    ...
```

3. **无限循环**
```python
# 问题：Agent一直重复相同操作

# 解决：限制迭代次数
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    max_iterations=5,  # 最多5轮
    max_execution_time=60  # 最多60秒
)
```

4. **幻觉（编造工具）**
```python
# 问题：LLM调用了不存在的工具

# 解决：严格的Prompt
prompt = """
可用工具：
{tools}

重要：只能使用上述工具，不要编造工具！
"""
```

**提高可靠性的5个方法**：

```python
# 1. 好的工具描述
# 2. 参数验证
# 3. 限制迭代
# 4. 错误处理
# 5. 人工审批（关键操作）

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint import MemorySaver

agent = create_react_agent(
    model,
    tools,
    checkpointer=MemorySaver(),  # 支持中断和恢复
    interrupt_before=["sensitive_action"]  # 敏感操作前中断
)
```

---

### 第五部分：工程实践 (20题)

#### 15. 如何设计一个生产级RAG系统的架构？

**答案**（分层架构）：

```
┌─────────────────────────────────────┐
│         用户层 (Frontend)            │
│  Next.js + React Query + Zustand   │
└────────────┬────────────────────────┘
             │ REST API / WebSocket
┌────────────▼────────────────────────┐
│         API层 (Backend)              │
│         FastAPI + Pydantic          │
├─────────────────────────────────────┤
│  ┌──────────┐  ┌──────────────┐    │
│  │ 认证授权  │  │  速率限制     │    │
│  └──────────┘  └──────────────┘    │
└────────────┬────────────────────────┘
             │
┌────────────▼────────────────────────┐
│      业务逻辑层 (Services)           │
├─────────────────────────────────────┤
│  ┌──────────────┐  ┌─────────────┐ │
│  │  RAG服务     │  │  Agent服务  │ │
│  └──────────────┘  └─────────────┘ │
└────────┬────────────────┬───────────┘
         │                │
    ┌────▼──────┐    ┌───▼───────┐
    │ 向量数据库  │    │  LLM API  │
    │ Pinecone   │    │  OpenAI   │
    └───────────┘    └───────────┘
         │
    ┌────▼──────┐
    │ 关系数据库  │
    │ PostgreSQL│
    └───────────┘
```

**关键组件**：

1. **文档处理Pipeline**
```python
class DocumentPipeline:
    def process(self, file):
        # 1. 加载
        docs = self.loader.load(file)
        # 2. 清洗
        docs = self.cleaner.clean(docs)
        # 3. 切分
        chunks = self.splitter.split(docs)
        # 4. Embedding
        vectors = self.embedder.embed(chunks)
        # 5. 存储
        self.vectorstore.add(vectors)
```

2. **检索优化**
```python
class HybridRetriever:
    def retrieve(self, query):
        # 向量检索
        vector_results = self.vector_search(query)
        # 关键词检索
        keyword_results = self.bm25_search(query)
        # 融合
        return self.rerank(vector_results + keyword_results)
```

3. **缓存层**
```python
from functools import lru_cache
from redis import Redis

class LLMCache:
    def __init__(self):
        self.redis = Redis()
    
    def get_or_generate(self, prompt):
        key = hash(prompt)
        if cached := self.redis.get(key):
            return cached
        
        result = self.llm.generate(prompt)
        self.redis.setex(key, 3600, result)  # 1小时过期
        return result
```

**监控指标**：
```python
metrics = {
    "latency": {
        "retrieval": "< 100ms",
        "generation": "< 2s",
        "total": "< 3s"
    },
    "quality": {
        "faithfulness": "> 0.85",
        "relevancy": "> 0.80"
    },
    "cost": {
        "per_query": "< $0.01"
    }
}
```

---

## 🎤 行为面试题

### 项目经验类

**Q: 介绍一个您做过的AI项目**

**STAR回答法**：
- **Situation**: 背景（公司需要智能客服）
- **Task**: 任务（降低人工客服成本）
- **Action**: 行动（设计RAG系统、训练、部署）
- **Result**: 结果（节省40%人力，满意度85%）

**模板**：
```
我们公司[背景]，需要[需求]。

我负责[角色]，主要工作是[技术方案]：
1. 用LangChain构建RAG系统
2. 集成xxx向量数据库
3. 实现xxx功能

技术难点是[问题]，我通过[方案]解决了。

最终达到了[数据指标]，带来了[业务价值]。
```

---

### 技术深度类

**Q: 您如何保持技术更新？**

**回答要点**：
1. **关注官方**：LangChain GitHub、OpenAI Blog
2. **实践项目**：每周尝试新特性
3. **社区交流**：Discord、Twitter
4. **输出总结**：写博客、做分享

---

## 📝 简历优化建议

### 项目描述模板

**标题**：[项目名] - [一句话描述]

**技术栈**：Python, LangChain, OpenAI, ChromaDB, FastAPI, React

**项目描述**：
- 开发了xxx，实现了xxx功能
- 使用xxx技术，解决了xxx问题
- 优化了xxx，提升了xxx%

**技术亮点**：
- 具体技术点1 + 数据
- 具体技术点2 + 数据
- 具体技术点3 + 数据

**业务价值**：
- 指标1：xx%
- 指标2：xx秒
- 指标3：节省xx成本

---

## 🔥 模拟面试题

### 场景题：设计一个智能客服

**面试官**："如果让你设计一个智能客服系统，你会怎么做？"

**回答思路**：

1. **需求确认**（先问问题）
   - 业务场景？（电商/SaaS/银行）
   - 预算？（决定模型选择）
   - QPS？（决定架构）
   - 准确率要求？（决定技术方案）

2. **方案设计**
   ```
   用户提问 
     ↓
   意图识别 (分类模型)
     ↓
   ├─ 简单问题 → FAQ匹配 → 直接回答
   ├─ 复杂问题 → RAG检索 → 生成回答
   └─ 无法处理 → 转人工
   ```

3. **技术选型**
   - LLM: GPT-3.5-turbo (成本考虑)
   - 向量库: Pinecone (稳定性)
   - 框架: LangChain + FastAPI
   - 缓存: Redis

4. **评测方案**
   - A/B测试
   - 人工评分
   - 用户满意度

5. **优化迭代**
   - 收集badcase
   - 优化Prompt
   - 扩充知识库

---

**祝您面试成功！🎉**

完成本训练营的所有练习后，您已经具备：
- ✅ 扎实的Python基础
- ✅ LLM应用开发能力
- ✅ RAG系统实现经验
- ✅ Agent开发技能
- ✅ 3个拿得出手的项目
- ✅ 系统的知识体系

**您已经准备好了！**

