#!/usr/bin/env python3
"""
批量生成练习题模板的脚本
用于快速创建剩余题目的框架
"""

import os
from pathlib import Path

# 题目模板
EXERCISE_TEMPLATE = '''"""
练习 {num}: {title}
难度: {difficulty}
预计时间: {time}

{description}
"""


def solution():
    """
    {task_description}
    
    {examples}
    """
    # TODO: 在这里实现您的代码
    pass


if __name__ == "__main__":
    # 测试代码
    result = solution()
    print(result)
'''

TEST_TEMPLATE = '''"""
测试文件: ex{num:02d}_{name}.py
"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from ex{num:02d}_{name} import solution


def test_solution():
    """测试solution函数"""
    result = solution()
    # TODO: 添加断言
    assert result is not None


if __name__ == "__main__":
    test_solution()
    print("✅ 测试通过")
'''

# 模块配置
MODULES = {
    "01-python-basics": {
        "exercises": [
            (8, "walrus_operator", "海象运算符 :=", "🟡", "10分钟"),
            (9, "type_hints", "类型注解", "🟡", "15分钟"),
            (10, "dynamic_typing", "动态类型陷阱", "🟡", "10分钟"),
            (12, "list_slicing", "List切片技巧", "🟡", "15分钟"),
            (15, "dict_comprehension", "字典推导式", "🟡", "10分钟"),
            (16, "sets", "Set集合操作", "🟢", "10分钟"),
            (17, "tuples", "Tuple元组", "🟢", "10分钟"),
            (18, "nested_structures", "嵌套数据结构", "🟡", "15分钟"),
            (22, "default_args", "默认参数", "🟢", "5分钟"),
            (24, "lambda", "Lambda表达式", "🟢", "10分钟"),
            (25, "higher_order", "高阶函数", "🟡", "15分钟"),
            (26, "closures", "闭包", "🟡", "15分钟"),
            (28, "decorator_params", "带参装饰器", "🔴", "25分钟"),
            (29, "recursion", "递归", "🟡", "15分钟"),
            (30, "functional", "函数式编程", "🔴", "20分钟"),
            (33, "while_loops", "while循环", "🟢", "5分钟"),
            (34, "loop_control", "循环控制", "🟢", "5分钟"),
            (35, "enumerate_zip", "enumerate和zip", "🟡", "10分钟"),
            (37, "custom_exceptions", "自定义异常", "🟡", "15分钟"),
            (38, "context_managers", "上下文管理器", "🟡", "15分钟"),
            (39, "conditional_comprehension", "推导式条件", "🟡", "10分钟"),
            (40, "generators", "生成器和yield", "🔴", "20分钟"),
        ]
    }
}


def generate_exercise(module: str, num: int, name: str, title: str, difficulty: str, time: str):
    """生成单个练习题"""
    module_path = Path(__file__).parent.parent / module
    exercises_dir = module_path / "exercises"
    tests_dir = module_path / "tests"
    
    exercises_dir.mkdir(parents=True, exist_ok=True)
    tests_dir.mkdir(parents=True, exist_ok=True)
    
    # 生成练习文件
    exercise_file = exercises_dir / f"ex{num:02d}_{name}.py"
    if not exercise_file.exists():
        content = EXERCISE_TEMPLATE.format(
            num=num,
            title=title,
            difficulty=difficulty,
            time=time,
            description=f"对比学习：\nJS:  ...\nPython: ...",
            task_description="实现函数功能",
            examples="示例：\n        solution() -> ..."
        )
        exercise_file.write_text(content, encoding="utf-8")
        print(f"✅ 生成: {exercise_file}")
    
    # 生成测试文件
    test_file = tests_dir / f"test_ex{num:02d}.py"
    if not test_file.exists():
        content = TEST_TEMPLATE.format(num=num, name=name)
        test_file.write_text(content, encoding="utf-8")
        print(f"✅ 生成: {test_file}")


def main():
    """主函数"""
    for module, config in MODULES.items():
        print(f"\n生成 {module} 的题目...")
        for num, name, title, difficulty, time in config["exercises"]:
            generate_exercise(module, num, name, title, difficulty, time)
    
    print("\n✅ 批量生成完成！")


if __name__ == "__main__":
    main()

