"""
练习 37: 自定义异常
难度: 🟡 进阶
预计时间: 15分钟

创建自定义异常类，提高代码可读性和错误处理
"""


class ValidationError(Exception):
    """验证错误异常"""
    pass


class InsufficientFundsError(Exception):
    """余额不足异常"""
    def __init__(self, balance: float, amount: float):
        self.balance = balance
        self.amount = amount
        message = f"余额不足：当前余额{balance}，需要{amount}"
        super().__init__(message)


def validate_age(age: int):
    """
    验证年龄
    
    参数:
        age: 年龄
    
    抛出:
        ValidationError: 如果年龄无效
    """
    # TODO: 如果age < 0 或 age > 150，抛出ValidationError
    if age < 0 or age > 150:
        raise ValidationError(f"无效的年龄: {age}")


def withdraw(balance: float, amount: float) -> float:
    """
    取款
    
    参数:
        balance: 当前余额
        amount: 取款金额
    
    返回:
        新的余额
    
    抛出:
        InsufficientFundsError: 如果余额不足
    """
    # TODO: 检查余额，不足则抛出InsufficientFundsError
    if amount > balance:
        raise InsufficientFundsError(balance, amount)
    return balance - amount


class APIError(Exception):
    """API错误基类"""
    def __init__(self, message: str, status_code: int = 500):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class NotFoundError(APIError):
    """404错误"""
    def __init__(self, resource: str):
        super().__init__(f"资源未找到: {resource}", 404)
        self.resource = resource


if __name__ == "__main__":
    # 测试验证
    try:
        validate_age(25)  # 正常
        validate_age(-5)  # 抛出异常
    except ValidationError as e:
        print(f"验证错误: {e}")
    
    # 测试取款
    try:
        result = withdraw(100, 50)  # 正常
        print(f"取款成功，余额: {result}")
        withdraw(100, 150)  # 抛出异常
    except InsufficientFundsError as e:
        print(f"取款失败: {e}")

