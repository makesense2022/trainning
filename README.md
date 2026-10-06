# Agent 训练材料：实际入口

> 2026-10-06：作为历史学习材料保存在公开 GitHub 仓库，本地项目停止维护。依赖清单分别固定在 LangChain 0.1.0 / 0.1.9，部分成本示例使用 2024 年定价；此次保留原内容，未升级或全面验证模型相关练习。Python 基础练习仍可单独参考。

实际课程位于 [ai-agent-training](ai-agent-training/README.md)，目前有 01–08 八个模块。根目录旧“五模块”路径不再作为操作入口，[原计划](archive/README-before-20261001.md) 保留。课程天数、题目数量与 FINAL_STATUS 等生成记录不证明个人已掌握。

本轮选择已存在的 Python 基础 ex01，离线完成启动 → 示例 → 校验 → 复盘路径；不要求 API key，不安装整套模型依赖：

```sh
git clone https://github.com/makesense2022/trainning.git
cd trainning
python3 ai-agent-training/01-python-basics/exercises/ex01_variables.py
python3 ai-agent-training/utils/check_ex01.py
```

2026-10-01 在 Python 3.9.6 下，原有 create_user_info、swap_values、variable_reassignment 三项测试通过。新入口运行原有断言且失败时返回非零；不修改原练习答案和学习记录。旧 test_ex01.py 直接运行会捕获失败但仍返回 0，因此不要仅以旧脚本 exit code 判定通过。

练习：先预测变量重新赋值和交换结果，再运行示例；修改时保留原题副本。复盘：解释动态类型、tuple 解包以及 `is True` 与数值类型的区别。自己的无提示答案与日期另记在模块 notes 文件；本轮只是复现现有答案，不记作新完成的个人练习。

需要模型的后续模块才使用 `ai-agent-training/env.example` 和内层 requirements.txt。外层 requirements.txt 是另一个历史版本（LangChain 0.1.0），内层为 0.1.9，均没有在本轮安装或验证新模型 API。不要合并两个清单或为基础练习创建服务。`utils/grade.py`、`test_all.py` 不存在，先用上面已验证的单题入口。
