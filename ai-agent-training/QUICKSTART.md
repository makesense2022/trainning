> 2026-10-01：当前离线复现与材料状态见 [主入口](../README.md)。下文是保留的课程计划；“完整/已完成/生产级/几天掌握”不等同于个人验收。模型配置和旧依赖未在本轮联网复核。

# 快速开始指南

> 10分钟设置好开发环境，立即开始学习

## 📋 前置要求

- ✅ Python 3.9+ (建议3.11)
- ✅ 代码编辑器 (推荐VS Code)
- ✅ Git
- ✅ 至少一个LLM API Key (OpenAI/DeepSeek/Anthropic)

## 🚀 5步开始

### 步骤 1: 检查Python版本

```bash
python --version
# 应显示: Python 3.9.x 或更高
```

如果没有Python或版本过低：
- Mac: `brew install python@3.11`
- Windows: 下载 https://www.python.org/downloads/
- Linux: `sudo apt install python3.11`

### 步骤 2: 创建虚拟环境

```bash
cd /Users/zhangjunnan/Documents/Projects/trainning/ai-agent-training

# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
source venv/bin/activate  # Mac/Linux
# 或
.\venv\Scripts\activate   # Windows

# 确认激活成功（命令行前面会显示(venv)）
```

### 步骤 3: 安装依赖

```bash
# 升级pip
pip install --upgrade pip

# 安装所有依赖
pip install -r requirements.txt

# 验证安装（应该显示版本号）
python -c "import langchain; print(langchain.__version__)"
```

**如果遇到安装问题**：

```bash
# 清理pip缓存
pip cache purge

# 使用国内镜像（更快）
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 步骤 4: 配置API Key

```bash
# 复制环境变量模板
cp env.example .env

# 编辑.env文件（使用任意编辑器）
nano .env  # 或 vim .env 或 code .env
```

在`.env`文件中填入您的API Key：

```bash
# 至少配置一个
OPENAI_API_KEY=sk-your-actual-key-here
# 或
DEEPSEEK_API_KEY=sk-your-actual-key-here
# 或
ANTHROPIC_API_KEY=sk-ant-your-actual-key-here
```

**获取API Key**：
- OpenAI: https://platform.openai.com/api-keys
- DeepSeek: https://platform.deepseek.com/api_keys
- Anthropic: https://console.anthropic.com/settings/keys

**建议**: DeepSeek性价比最高（价格是OpenAI的1/10），适合学习

### 步骤 5: 测试环境

```bash
# 测试Python环境
python -c "print('✅ Python环境OK')"

# 测试依赖安装
python -c "import langchain, openai, chromadb; print('✅ 依赖安装OK')"

# 测试API Key（需要先配置.env）
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('✅ API Key已配置' if os.getenv('OPENAI_API_KEY') or os.getenv('DEEPSEEK_API_KEY') else '❌ 请配置API Key')"
```

如果以上都显示 ✅，恭喜您，环境配置完成！

## 🎯 开始第一个练习

### 方式 1: 命令行测试（推荐）

```bash
# 进入Python基础模块
cd 01-python-basics

# 打开第一个练习
cat exercises/ex01_variables.py

# 编辑并完成练习
code exercises/ex01_variables.py  # 或使用您喜欢的编辑器

# 运行测试
python -m pytest tests/test_ex01.py -v

# 看到全部通过✅，说明您完成了！
```

### 方式 2: Jupyter Notebook（可选）

```bash
# 启动Jupyter
jupyter notebook

# 浏览器会自动打开
# 导航到 01-python-basics/exercises/
# 创建新的notebook开始练习
```

### 方式 3: VS Code（推荐）

1. 打开VS Code
2. 安装Python扩展
3. 选择虚拟环境（左下角）
4. 打开 `01-python-basics/exercises/ex01_variables.py`
5. 直接运行和调试

## 📝 学习流程

### 每道题的标准流程

```bash
# 1. 阅读题目
cat 01-python-basics/exercises/ex01_variables.py

# 2. 理解要求（查看注释和TODO）

# 3. 编写代码

# 4. 快速测试
python 01-python-basics/exercises/ex01_variables.py

# 5. 运行正式测试
pytest 01-python-basics/tests/test_ex01.py -v

# 6. 通过后，查看参考答案（对比学习）
cat 01-python-basics/solutions/ex01_solution.py

# 7. 查看进度
python utils/progress.py --module 01-python-basics
```

### 推荐学习节奏

```
🌅 上午 (4小时):
  09:00-11:00  完成10-15道练习
  11:00-13:00  完成10-15道练习

🌆 下午 (3小时):
  14:00-15:30  完成8-10道练习
  15:30-17:00  完成8-10道练习

🌙 晚上 (3小时):
  19:00-20:30  复习+难题攻坚
  20:30-22:00  综合项目

💪 按这个节奏，7-10天完成所有内容！
```

## 🛠️ 常用命令速查

```bash
# 查看总体进度
python utils/progress.py

# 查看某个模块进度
python utils/progress.py --module 01-python-basics

# 运行单个测试文件
pytest tests/test_ex01.py -v

# 运行整个模块的测试
pytest 01-python-basics/tests/ -v

# 查看测试覆盖率
pytest tests/ --cov=exercises --cov-report=html

# 检查代码风格
black exercises/
flake8 exercises/

# 类型检查
mypy exercises/ex01_variables.py
```

## 💡 VS Code 推荐配置

创建 `.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "./venv/bin/python",
  "python.testing.pytestEnabled": true,
  "python.testing.pytestArgs": ["tests"],
  "python.linting.enabled": true,
  "python.linting.flake8Enabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.codeActionsOnSave": {
      "source.organizeImports": true
    }
  }
}
```

安装推荐插件：
- Python (Microsoft)
- Pylance
- Jupyter
- autoDocstring

## 🐛 常见问题

### Q: import错误怎么办？

```bash
# 确保虚拟环境已激活
source venv/bin/activate

# 重新安装依赖
pip install -r requirements.txt
```

### Q: pytest找不到模块？

```bash
# 添加项目根目录到PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:$(pwd)"

# 或在测试文件中添加：
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))
```

### Q: API调用失败？

```bash
# 检查.env文件是否存在
ls -la .env

# 检查API Key是否正确
cat .env | grep API_KEY

# 测试API连接
python -c "from openai import OpenAI; print(OpenAI().models.list())"
```

### Q: 中文显示乱码？

```bash
# 设置环境变量
export LANG=zh_CN.UTF-8
export LC_ALL=zh_CN.UTF-8
```

## 📚 推荐学习资源

### 官方文档
- [Python官方文档](https://docs.python.org/zh-cn/3/)
- [LangChain文档](https://python.langchain.com/)
- [OpenAI API文档](https://platform.openai.com/docs)

### 社区资源
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [LangChain Discord](https://discord.gg/langchain)
- Stack Overflow: 搜索Python/LangChain问题

## 🆘 获取帮助

遇到问题时：

1. **查看题目提示** - 每道题都有详细注释
2. **运行测试** - 测试会告诉您哪里错了
3. **查看错误信息** - Python的错误信息很清楚
4. **参考答案** - solutions目录有参考实现
5. **搜索引擎** - 大部分问题Google都有答案

## ✅ 环境检查清单

完成设置后，确认：

- [ ] Python 3.9+ 已安装
- [ ] 虚拟环境已创建并激活
- [ ] requirements.txt 所有依赖已安装
- [ ] .env 文件已配置API Key
- [ ] 第一个测试能成功运行
- [ ] VS Code (或其他编辑器) 已配置好

全部✅？开始您的AI Agent开发之旅吧！🚀

---

**下一步**：进入 `01-python-basics` 开始第一个练习！

```bash
cd 01-python-basics
cat README.md
```

