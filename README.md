# AI Agent 开发实战训练营 🚀

## 📚 课程结构

本课程专为**有丰富前端经验**的开发者设计，通过5个模块、40+实战题目，帮助你在**5-7天**内掌握AI Agent开发。

### 学习路径

```
Day 1-2: Python基础 + 进阶 (模块01-02)
Day 3-4: LangChain基础 + API调用 (模块03)
Day 5-6: RAG实现 (模块04)
Day 7: Agent开发 (模块05)
```

### 📁 模块目录

- **[01-python-basics](./01-python-basics/)** - Python基础语法速通（10题）
- **[02-python-advanced](./02-python-advanced/)** - Python进阶特性（8题）
- **[03-langchain-basics](./03-langchain-basics/)** - LangChain核心概念（10题）
- **[04-rag-implementation](./04-rag-implementation/)** - RAG检索增强生成（8题）
- **[05-agent-development](./05-agent-development/)** - Agent智能体开发（6题）

### 🎯 学习建议

1. **环境准备**：先完成 `00-setup` 环境配置
2. **顺序学习**：严格按照 01→02→03→04→05 的顺序
3. **实践为主**：每道题都要实际编码，不要只看答案
4. **测试驱动**：每题都有测试文件，通过测试才算完成
5. **记录笔记**：把遇到的问题记录在各模块的 `notes.md` 中

### 📊 评分标准

每道题会根据以下维度评分（总分100）：
- **功能完整性**（40分）：是否实现所有要求
- **代码质量**（30分）：代码风格、注释、可读性
- **测试通过**（20分）：是否通过所有测试用例
- **最佳实践**（10分）：是否使用了推荐的方法和模式

**总分对照**：
- 90-100分：优秀 ⭐⭐⭐
- 80-89分：良好 ⭐⭐
- 70-79分：合格 ⭐
- <70分：需改进

### 🔧 环境要求

- Python 3.9+
- 推荐使用 `venv` 或 `conda` 管理虚拟环境
- 需要准备的API Key：
  - OpenAI API Key 或
  - DeepSeek API Key 或
  - 其他兼容OpenAI格式的API

### 🚀 开始学习

```bash
# 1. 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Mac/Linux
# 或 venv\Scripts\activate  # Windows

# 2. 安装依赖
pip install -r requirements.txt

# 3. 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的API Key

# 4. 开始第一个模块
cd 01-python-basics
```

### 📝 提交作业

完成每个模块后，在模块目录下运行：
```bash
python test_all.py
```

所有测试通过后，提交你的代码供我评分。

---

**准备好了吗？让我们开始吧！** 💪

