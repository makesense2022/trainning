"""
测试文件: ex01_variables.py
"""
import sys
from pathlib import Path

# 添加exercises目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent / "exercises"))

from ex01_variables import create_user_info, swap_values, variable_reassignment


def test_create_user_info():
    """测试创建用户信息"""
    result = create_user_info()
    
    assert isinstance(result, dict), "返回值应该是字典类型"
    assert result["name"] == "张三", "name应该是'张三'"
    assert result["age"] == 28, "age应该是28"
    assert result["is_active"] is True, "is_active应该是True"
    assert result["salary"] == 15000.5, "salary应该是15000.5"
    
    # 检查类型
    assert isinstance(result["name"], str), "name应该是字符串"
    assert isinstance(result["age"], int), "age应该是整数"
    assert isinstance(result["is_active"], bool), "is_active应该是布尔值"
    assert isinstance(result["salary"], float), "salary应该是浮点数"


def test_swap_values():
    """测试值交换"""
    # 测试整数
    a, b = swap_values(5, 10)
    assert a == 10 and b == 5, "5和10交换后应该是10和5"
    
    # 测试字符串
    a, b = swap_values("hello", "world")
    assert a == "world" and b == "hello", "字符串交换失败"
    
    # 测试混合类型
    a, b = swap_values(42, "answer")
    assert a == "answer" and b == 42, "混合类型交换失败"


def test_variable_reassignment():
    """测试变量重新赋值"""
    result = variable_reassignment()
    
    assert isinstance(result, list), "最终结果应该是列表类型"
    assert result == [1, 2, 3], "最终结果应该是[1, 2, 3]"


if __name__ == "__main__":
    # 手动运行测试
    try:
        test_create_user_info()
        print("✅ test_create_user_info 通过")
    except AssertionError as e:
        print(f"❌ test_create_user_info 失败: {e}")
    
    try:
        test_swap_values()
        print("✅ test_swap_values 通过")
    except AssertionError as e:
        print(f"❌ test_swap_values 失败: {e}")
    
    try:
        test_variable_reassignment()
        print("✅ test_variable_reassignment 通过")
    except AssertionError as e:
        print(f"❌ test_variable_reassignment 失败: {e}")

