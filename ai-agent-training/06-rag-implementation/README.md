# Module 06: RAG实现 - 让AI拥有外部知识

> 目标：2天掌握RAG（检索增强生成）核心技术，这是AI Agent的基础能力

## 🎯 学习目标

- [ ] 理解RAG的工作原理（检索 + 生成）
- [ ] 掌握文档切分策略
- [ ] 实现语义检索
- [ ] 构建完整的RAG链
- [ ] 评测RAG质量

## 🔥 RAG是什么？

### 问题：LLM的局限

```python
# 问题1：知识截止日期
user: "2024年11月发生了什么？"
llm:  "抱歉，我的知识截止到2023年4月"  ❌

# 问题2：私有数据
user: "我们公司的报销流程是什么？"
llm:  "我不知道你们公司的信息"  ❌

# 问题3：幻觉（Hallucination）
user: "Python 3.15有什么新特性？"
llm:  "Python 3.15加入了XXX特性"  ❌（编造的）
```

### 解决方案：RAG

**RAG = Retrieval (检索) + Augmented (增强) + Generation (生成)**

```
┌─────────────┐
│  用户提问    │ "公司报销流程是什么？"
└──────┬──────┘
       │
       ▼
┌─────────────────────┐
│  1. 向量化问题      │ [0.1, -0.3, 0.8, ...]
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  2. 语义检索        │ 在向量库中找相似内容
│  (Vector Search)    │ 
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  3. 找到相关文档    │ "报销需提交发票..."
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  4. 构造Prompt      │ 问题 + 相关文档
└──────┬──────────────┘
       │
       ▼
┌─────────────────────┐
│  5. LLM生成答案     │ 基于文档回答
└─────────────────────┘
```

### 代码示例

**传统方式（会瞎编）**：
```python
response = llm("公司报销流程是什么？")
# 可能瞎编一个流程
```

**RAG方式（基于事实）**：
```python
# 1. 检索相关文档
docs = vector_db.search("公司报销流程")
# docs = ["报销需提交发票、填写表格...", "审批流程为..."]

# 2. 构造增强Prompt
prompt = f"""
根据以下文档回答问题：

文档：
{docs}

问题：公司报销流程是什么？

请基于文档内容回答，不要编造。
"""

# 3. LLM生成答案
response = llm(prompt)
# 基于真实文档回答
```

## 📊 练习列表（13题）

### Part 1: 文档处理 (4题) 🟢🟡

| 题号 | 题目 | 难度 | 核心概念 | 预计时间 |
|-----|------|------|---------|---------|
| 01 | 加载PDF/Markdown | 🟢 | Document Loaders | 15分钟 |
| 02 | 文档切分策略 | 🟡 | Text Splitter | 25分钟 |
| 03 | 保留元数据 | 🟡 | Metadata | 20分钟 |
| 04 | 多文件批处理 | 🟡 | 批量处理 | 20分钟 |

### Part 2: 向量检索 (4题) 🟡

| 题号 | 题目 | 难度 | 核心概念 | 预计时间 |
|-----|------|------|---------|---------|
| 05 | 基础向量检索 | 🟡 | Similarity Search | 20分钟 |
| 06 | MMR检索 | 🟡 | 多样性 | 25分钟 |
| 07 | 混合检索 | 🔴 | BM25 + 向量 | 30分钟 |
| 08 | 重排序 | 🔴 | Re-ranking | 25分钟 |

### Part 3: RAG链构建 (5题) 🔴

| 题号 | 题目 | 难度 | 核心概念 | 预计时间 |
|-----|------|------|---------|---------|
| 09 | 简单RAG链 | 🟡 | RetrievalQA | 25分钟 |
| 10 | 带引用的RAG | 🔴 | Source Citation | 30分钟 |
| 11 | 对话式RAG | 🔴 | Chat History | 35分钟 |
| 12 | 多路检索融合 | 🔴 | Query Fusion | 40分钟 |
| 13 | RAG评测 | 🔴 | RAGAS | 45分钟 |

## 🔑 核心概念详解

### 1. 文档切分（Text Splitting）

**为什么要切分？**
- LLM有上下文长度限制（如4096 tokens）
- 小块更精准（检索粒度更细）
- 相似度更高（长文本可能包含多个主题）

**切分策略**：

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

# 策略1：按字符数切分
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,        # 每块1000字符
    chunk_overlap=200,      # 重叠200字符（保留上下文）
    separators=["\n\n", "\n", "。", ".", " "]  # 分隔符优先级
)

text = "很长的文档..."
chunks = splitter.split_text(text)
```

**chunk_overlap的作用**：
```
Chunk 1: "...Python是一种编程语言。它的语法简洁..."
                                    ↓ 重叠部分
Chunk 2: "...它的语法简洁。Python有很多库..."
```
避免在句子中间切断，保留上下文。

### 2. 向量检索算法

**余弦相似度（Cosine Similarity）**：

```python
import numpy as np

def cosine_similarity(vec1, vec2):
    """
    向量夹角越小，越相似
    
    范围：-1 到 1
    1: 完全相同方向
    0: 垂直（无关）
    -1: 完全相反方向
    """
    dot_product = np.dot(vec1, vec2)
    norm = np.linalg.norm(vec1) * np.linalg.norm(vec2)
    return dot_product / norm

# 示例
query_vec = [0.1, 0.5, 0.3]       # "Python教程"的向量
doc1_vec = [0.12, 0.48, 0.32]    # "Python学习指南"的向量
doc2_vec = [-0.5, 0.2, 0.8]      # "Java开发手册"的向量

sim1 = cosine_similarity(query_vec, doc1_vec)  # 0.999（非常相似）
sim2 = cosine_similarity(query_vec, doc2_vec)  # 0.123（不太相似）
```

**MMR（Maximal Marginal Relevance）**：

平衡"相关性"和"多样性"：
```python
# 普通检索：可能返回5个几乎一样的结果
results = vector_db.similarity_search("Python", k=5)
# ["Python教程", "Python指南", "Python手册", "Python学习", "Python介绍"]
# ❌ 全是重复的

# MMR检索：既相关又多样
results = vector_db.max_marginal_relevance_search("Python", k=5)
# ["Python教程", "Python Web开发", "Python数据分析", "Python性能优化", "Python最佳实践"]
# ✅ 覆盖不同方面
```

### 3. RAG链的实现

**LangChain的RetrievalQA**：

```python
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI

# 1. 创建向量库
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings()
)

# 2. 创建检索器
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 3}  # 返回3个最相关的块
)

# 3. 创建RAG链
qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(temperature=0),
    chain_type="stuff",  # 把所有文档"塞"进prompt
    retriever=retriever,
    return_source_documents=True  # 返回引用
)

# 4. 提问
result = qa_chain({"query": "什么是RAG？"})
print(result["result"])           # 答案
print(result["source_documents"]) # 来源文档
```

**chain_type的选择**：

| 类型 | 原理 | 优点 | 缺点 | 适用场景 |
|-----|------|------|------|---------|
| stuff | 所有文档塞进一个prompt | 简单、快速 | 受上下文长度限制 | 文档少（<4个） |
| map_reduce | 每个文档单独总结，再汇总 | 无长度限制 | 慢、成本高 | 文档多 |
| refine | 逐个文档迭代优化答案 | 答案质量高 | 很慢 | 需要精准答案 |
| map_rerank | 每个文档打分，取最高分 | 可解释性好 | 成本高 | 需要置信度 |

### 4. RAG评测（重要！面试必问）

**评测指标**（使用RAGAS框架）：

```python
from ragas import evaluate
from ragas.metrics import (
    faithfulness,       # 忠实度：答案是否基于文档？
    answer_relevancy,   # 相关性：答案是否回答问题？
    context_precision,  # 上下文精度：检索是否准确？
    context_recall      # 上下文召回：是否遗漏关键信息？
)

# 评测数据
data = {
    "question": ["什么是Python?"],
    "answer": ["Python是一种编程语言"],
    "contexts": [["Python是由Guido创建的语言..."]],
    "ground_truth": ["Python是一种高级编程语言"]
}

# 运行评测
result = evaluate(
    data,
    metrics=[faithfulness, answer_relevancy, context_precision, context_recall]
)

print(result)
# {
#   "faithfulness": 0.95,        # 95%的答案有文档支持
#   "answer_relevancy": 0.92,    # 92%的答案相关
#   "context_precision": 0.88,   # 88%的检索是准确的
#   "context_recall": 0.85       # 85%的关键信息被检索到
# }
```

**如何提升RAG质量？**

1. **Faithfulness（忠实度）低** → 改进Prompt，要求"仅基于文档回答"
2. **Answer Relevancy（相关性）低** → 改进LLM或温度参数
3. **Context Precision（精度）低** → 优化Embedding模型或切分策略
4. **Context Recall（召回）低** → 增加检索数量（k值）或使用混合检索

## 🎓 面试高频问题

### Q1: RAG和Fine-tuning有什么区别？

| 维度 | RAG | Fine-tuning |
|-----|-----|-------------|
| 知识来源 | 外部文档（动态） | 模型参数（固定） |
| 更新成本 | 低（换文档） | 高（重新训练） |
| 推理成本 | 较高（需检索） | 较低 |
| 适用场景 | 动态知识、私有数据 | 特定任务、风格模仿 |

**答案**：RAG是"外挂知识库"，Fine-tuning是"内化知识"。RAG更灵活，Fine-tuning更高效。

### Q2: 如何选择chunk_size？

**答案**：
- **太小**（<200）：上下文不足，语义不完整
- **太大**（>2000）：检索精度下降，相似度降低
- **推荐**：500-1000字符，根据文档类型调整
- **技巧**：chunk_overlap设为chunk_size的10-20%

### Q3: 向量数据库如何选型？

| 数据库 | 特点 | 适用场景 |
|-------|------|---------|
| ChromaDB | 轻量、内嵌 | 原型、开发 |
| FAISS | 快速、开源 | 百万级数据 |
| Pinecone | 托管、稳定 | 生产环境 |
| Weaviate | 功能丰富 | 复杂查询 |

### Q4: 如何处理多轮对话？

**答案**：使用ConversationalRetrievalChain，它会：
1. 把历史对话+当前问题 → 生成独立的查询（Standalone Question）
2. 用独立查询检索文档
3. 结合历史+文档+当前问题生成答案

```python
from langchain.chains import ConversationalRetrievalChain

chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=retriever,
    return_source_documents=True
)

# 多轮对话
chat_history = []
response1 = chain({"question": "什么是Python?", "chat_history": chat_history})
chat_history.append((response1["question"], response1["answer"]))

response2 = chain({"question": "它有什么特点?", "chat_history": chat_history})
# "它"会被正确理解为"Python"
```

## 💡 实战技巧

### 1. Chunk可视化
```python
def visualize_chunks(chunks):
    """可视化文档切分效果"""
    for i, chunk in enumerate(chunks):
        print(f"\n{'='*60}")
        print(f"Chunk {i+1} ({len(chunk)} chars)")
        print(f"{'='*60}")
        print(chunk[:200] + "..." if len(chunk) > 200 else chunk)
```

### 2. 检索结果调试
```python
def debug_retrieval(query, retriever):
    """调试检索结果"""
    docs = retriever.get_relevant_documents(query)
    for i, doc in enumerate(docs):
        print(f"\n文档 {i+1}:")
        print(f"内容: {doc.page_content[:200]}...")
        print(f"来源: {doc.metadata}")
        print(f"相似度: {doc.metadata.get('score', 'N/A')}")
```

### 3. Prompt模板优化
```python
from langchain.prompts import PromptTemplate

template = """
你是一个专业的问答助手。请根据以下上下文回答问题。

规则：
1. 仅基于提供的上下文回答，不要编造信息
2. 如果上下文中没有答案，明确说"根据提供的信息无法回答"
3. 回答要简洁、准确
4. 引用上下文中的具体内容

上下文：
{context}

问题：{question}

答案：
"""

prompt = PromptTemplate(
    template=template,
    input_variables=["context", "question"]
)
```

## ⏭️ 下一步

完成本模块后，您将掌握：
- ✅ RAG的完整实现流程
- ✅ 文档处理和切分策略
- ✅ 向量检索优化技巧
- ✅ RAG质量评测方法

下一步进入 `07-agent-development`，学习如何让RAG成为Agent的工具！

