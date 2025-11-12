# AI Agent 开发加速训练营

> 为有14年前端经验的架构师定制的Python + LangChain + AI Agent速成课程

## 🎯 课程目标

**10天内掌握AI Agent开发核心技能**，能够：
- 用Python构建生产级AI应用
- 理解并实现RAG（检索增强生成）
- 开发具备工具调用能力的AI Agent
- 应对AI相关技术面试

## 📊 学习路径（建议时间分配）

```
Day 1-2  : Python基础 + 进阶（80道题）          ████████░░
Day 3-4  : LLM API + LangChain基础（30道题）    ████████░░
Day 5-6  : Embedding + VectorDB + RAG（25道题） ████████░░
Day 7-8  : Agent开发 + 工具调用（20道题）       ████████░░
Day 9-10 : 综合项目 + 面试准备（3个项目）      ████████░░
```

## 📁 目录结构

```
ai-agent-training/
├── 01-python-basics/           # Python基础（40题）
├── 02-python-advanced/         # Python进阶（40题）
├── 03-llm-api/                 # LLM API调用（15题）
├── 04-langchain-basics/        # LangChain基础（15题）
├── 05-embedding-vectordb/      # 向量数据库（12题）
├── 06-rag-implementation/      # RAG实现（13题）
├── 07-agent-development/       # Agent开发（20题）
├── 08-final-projects/          # 综合项目（3个）
├── utils/                      # 工具函数和配置
└── README.md                   # 本文件
```

## 🚀 快速开始

### 1. 环境配置

```bash
# 创建虚拟环境
python3 -m venv venv
source venv/bin/activate  # Mac/Linux

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置API Key

```bash
# 复制环境变量模板
cp .env.example .env

# 编辑.env文件，填入您的API Key
# OPENAI_API_KEY=sk-xxx
# DEEPSEEK_API_KEY=sk-xxx
```

### 3. 开始学习

按照目录顺序，每个模块都有：
- 📖 `README.md` - 概念讲解和学习目标
- 💡 `exercises/` - 练习题目（带详细注释）
- ✅ `tests/` - 自动化测试用例
- 🎯 `solutions/` - 参考答案（完成后再看）

### 4. 运行测试

```bash
# 进入任意模块目录
cd 01-python-basics

# 运行单个测试
python -m pytest tests/test_ex01.py -v

# 运行所有测试
python -m pytest tests/ -v

# 查看覆盖率
python -m pytest tests/ --cov=exercises --cov-report=html
```

## 📝 学习建议

### 对于有14年前端经验的您

1. **类比学习**：每个Python概念都会对照JS/TS
2. **跳过理论**：直接看代码，理解模式
3. **测试驱动**：先看测试用例，理解需求，再写代码
4. **快速迭代**：不要追求完美，先跑通再优化

### 难度分级

- 🟢 **基础题**：5-15分钟，掌握语法
- 🟡 **进阶题**：15-30分钟，理解原理
- 🔴 **挑战题**：30-60分钟，综合应用
- 🔥 **项目题**：2-4小时，真实场景

## 🎓 评分标准

每道题完成后，运行测试：

```bash
# 查看您的得分
python utils/grade.py --module 01-python-basics
```

**通过标准**：
- 每个模块 >= 80% 测试通过
- 综合项目全部功能实现

**优秀标准**：
- 每个模块 >= 95% 测试通过
- 代码质量（PEP8, 类型注解, 文档）
- 性能优化（时间/空间复杂度）

## 📚 各模块详细说明

### Module 01: Python基础 (40题, ~8小时)

**前端对照学习法**
- 变量/类型 ←→ JS的let/const
- List/Dict ←→ Array/Object
- 函数/装饰器 ←→ Function/HOC
- 模块/包 ←→ import/export

**关键突破点**：
- 列表推导式（比map/filter更简洁）
- 多重赋值和解包
- 上下文管理器（with语句）

### Module 02: Python进阶 (40题, ~8小时)

**异步编程**（您的强项）
- async/await ←→ JS完全一致
- asyncio ←→ Event Loop
- 并发vs并行

**面向对象**
- Class ←→ ES6 Class
- 魔术方法（\_\_init\_\_, \_\_call\_\_等）
- 多继承和MRO

### Module 03: LLM API (15题, ~4小时)

- HTTP调用（requests ←→ axios）
- 流式响应（SSE）
- Token计算和成本估算
- 错误处理和重试策略

### Module 04: LangChain基础 (15题, ~4小时)

- Prompt模板
- Chat Models抽象
- Output Parsers
- Memory机制

### Module 05: Embedding + VectorDB (12题, ~4小时)

- 向量的本质（数学角度）
- ChromaDB/FAISS使用
- 相似度搜索
- 混合检索

### Module 06: RAG实现 (13题, ~4小时)

- 文档切分策略
- 检索链构建
- 上下文压缩
- 评测指标（Faithfulness, Relevance）

### Module 07: Agent开发 (20题, ~6小时)

- ReAct思维链
- 工具定义和注册
- Agent类型对比
- 错误处理和兜底

### Module 08: 综合项目 (3个, ~12小时)

1. **个人知识库RAG** - 本地文档问答
2. **多工具Agent** - 天气、搜索、计算器
3. **完整应用** - FastAPI后端 + React前端

## 🔥 面试高频问题覆盖

每个模块都包含"面试角"部分：

- [ ] Transformer架构原理
- [ ] Prompt Engineering最佳实践
- [ ] RAG vs Fine-tuning对比
- [ ] Agent框架对比（LangChain vs LangGraph vs AutoGen）
- [ ] 向量数据库选型
- [ ] Token优化策略
- [ ] 评测体系（RAGAS, TruLens）
- [ ] 生产部署考虑

## 🎯 完成检查清单

### Week 1: Python + LLM基础
- [ ] 完成Module 01-02所有练习（80题）
- [ ] 成功调用至少2个LLM API
- [ ] 理解async/await和装饰器

### Week 2: LangChain + RAG
- [ ] 搭建第一个RAG系统
- [ ] 理解Embedding和向量搜索
- [ ] 掌握文档切分策略

### Week 3: Agent + 项目
- [ ] 实现一个多工具Agent
- [ ] 完成综合项目1和2
- [ ] 准备面试题库

## 📖 推荐资源

**官方文档**：
- [LangChain Documentation](https://python.langchain.com/)
- [LangSmith](https://smith.langchain.com/) - 调试工具
- [OpenAI Cookbook](https://cookbook.openai.com/)

**进阶阅读**：
- ReAct论文
- RAG评测最佳实践
- Agent设计模式

## 🆘 求助方式

1. 每道题的`README.md`都有提示
2. 先看测试用例理解需求
3. `solutions/`里有参考答案（但先自己尝试！）
4. 搜索错误信息（90%的问题Stack Overflow有答案）

## 💪 给自己的挑战

- 🏃‍♂️ **速度挑战**：7天完成所有基础练习
- 🎯 **质量挑战**：所有测试100%通过
- 🚀 **创新挑战**：用Next.js给Agent做个UI

---

**准备好了吗？让我们开始吧！** 🚀

从 `01-python-basics` 开始您的AI Agent开发之旅！

