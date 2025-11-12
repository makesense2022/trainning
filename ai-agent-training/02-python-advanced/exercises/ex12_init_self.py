"""
练习 12: __init__和self
难度: 🟢 基础
预计时间: 10分钟

目标：理解Python类的初始化和self
"""


class BankAccount:
    """银行账户类"""
    
    def __init__(self, owner: str, initial_balance: float = 0.0):
        """
        初始化账户
        
        参数:
            owner: 账户所有者
            initial_balance: 初始余额
        """
        # TODO: 初始化属性
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount: float):
        """
        存款
        
        参数:
            amount: 金额
        """
        # TODO: 增加余额
        if amount > 0:
            self.balance += amount
    
    def withdraw(self, amount: float) -> bool:
        """
        取款
        
        参数:
            amount: 金额
        
        返回:
            是否成功
        """
        # TODO: 减少余额（检查余额是否足够）
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return True
        return False
    
    def get_balance(self) -> float:
        """获取余额"""
        return self.balance


if __name__ == "__main__":
    account = BankAccount("Alice", 100.0)
    account.deposit(50.0)
    print(f"余额: {account.get_balance()}")
    success = account.withdraw(30.0)
    print(f"取款成功: {success}, 余额: {account.get_balance()}")

