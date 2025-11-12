# Module 04: LangChain基础

> 目标：掌握LangChain核心组件，这是AI应用开发的框架基础

## 🎯 学习目标

- [ ] 理解Prompt模板
- [ ] 掌握Chat Models抽象
- [ ] 学会使用Output Parsers
- [ ] 理解Chain构建
- [ ] 掌握Memory机制

## 📊 练习列表（15题）

### Part 1: 核心组件 (5题)
- ex01_prompt_template.py - Prompt模板
- ex02_chat_models.py - Chat Models
- ex03_output_parsers.py - 输出解析器
- ex04_chains.py - 链构建
- ex05_runnables.py - Runnable接口

### Part 2: Memory (5题)
- ex06_conversation_memory.py - 对话记忆
- ex07_buffer_memory.py - BufferMemory
- ex08_summary_memory.py - SummaryMemory
- ex09_window_memory.py - WindowMemory
- ex10_custom_memory.py - 自定义Memory

### Part 3: 进阶 (5题)
- ex11_callbacks.py - 回调系统
- ex12_streaming_chain.py - 流式Chain
- ex13_fallback_chain.py - 降级Chain
- ex14_parallel_chains.py - 并行Chain
- ex15_langsmith.py - LangSmith追踪

## 🔥 核心概念

### Prompt模板

```python
from langchain.prompts import PromptTemplate

template = "你是一个{role}，请用{style}的方式回答：{question}"
prompt = PromptTemplate(template=template, input_variables=["role", "style", "question"])
```

### Chain构建

```python
from langchain.chains import LLMChain

chain = LLMChain(llm=llm, prompt=prompt)
result = chain.run(role="Python专家", style="简洁", question="什么是装饰器？")
```

## ⏭️ 下一步

完成本模块后，进入RAG和Agent开发！

