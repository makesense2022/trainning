# Module 01: Python基础 - 前端架构师的类比学习法

> 目标：2天内掌握Python核心语法，以您14年的JS/TS经验为基础，快速建立对应关系

## 🎯 学习目标

- [ ] 理解Python的变量、类型系统（对比JS）
- [ ] 掌握List、Dict、Set等数据结构
- [ ] 熟练使用列表推导式和生成器
- [ ] 理解函数定义、参数传递、闭包
- [ ] 掌握模块和包的导入机制
- [ ] 了解上下文管理器和异常处理

## 📊 练习列表（40题）

### Part 1: 变量和类型 (10题) 🟢

| 题号 | 题目 | 难度 | JS对照 | 预计时间 |
|-----|------|------|--------|---------|
| 01 | 变量赋值和类型推断 | 🟢 | let/const | 5分钟 |
| 02 | 数字类型和运算 | 🟢 | Number | 5分钟 |
| 03 | 字符串操作和格式化 | 🟢 | String | 10分钟 |
| 04 | 布尔值和逻辑运算 | 🟢 | Boolean | 5分钟 |
| 05 | None vs undefined/null | 🟢 | null/undefined | 5分钟 |
| 06 | 类型转换和检查 | 🟢 | typeof, Number() | 10分钟 |
| 07 | 多重赋值和解包 | 🟡 | 解构赋值 | 10分钟 |
| 08 | 海象运算符(walrus) | 🟡 | - | 10分钟 |
| 09 | 类型注解（Type Hints） | 🟡 | TypeScript | 15分钟 |
| 10 | 动态类型陷阱 | 🟡 | - | 10分钟 |

### Part 2: 数据结构 (10题) 🟢🟡

| 题号 | 题目 | 难度 | JS对照 | 预计时间 |
|-----|------|------|--------|---------|
| 11 | List基础操作 | 🟢 | Array | 10分钟 |
| 12 | List切片(slicing) | 🟡 | slice() | 15分钟 |
| 13 | List推导式 | 🟡 | map/filter | 15分钟 |
| 14 | Dict基础操作 | 🟢 | Object | 10分钟 |
| 15 | Dict推导式 | 🟡 | - | 10分钟 |
| 16 | Set集合操作 | 🟢 | Set | 10分钟 |
| 17 | Tuple元组 | 🟢 | - | 10分钟 |
| 18 | 嵌套数据结构 | 🟡 | 嵌套对象 | 15分钟 |
| 19 | 数据结构选择 | 🟡 | - | 10分钟 |
| 20 | 性能对比 | 🔴 | - | 20分钟 |

### Part 3: 函数 (10题) 🟢🟡

| 题号 | 题目 | 难度 | JS对照 | 预计时间 |
|-----|------|------|--------|---------|
| 21 | 函数定义和调用 | 🟢 | function | 5分钟 |
| 22 | 参数默认值 | 🟢 | 默认参数 | 5分钟 |
| 23 | *args和**kwargs | 🟡 | ...rest | 15分钟 |
| 24 | Lambda表达式 | 🟢 | 箭头函数 | 10分钟 |
| 25 | 高阶函数 | 🟡 | HOF | 15分钟 |
| 26 | 闭包 | 🟡 | Closure | 15分钟 |
| 27 | 装饰器基础 | 🔴 | HOC | 20分钟 |
| 28 | 带参数的装饰器 | 🔴 | - | 25分钟 |
| 29 | 递归 | 🟡 | Recursion | 15分钟 |
| 30 | 函数式编程 | 🔴 | map/reduce | 20分钟 |

### Part 4: 控制流和异常 (10题) 🟢

| 题号 | 题目 | 难度 | JS对照 | 预计时间 |
|-----|------|------|--------|---------|
| 31 | if/elif/else | 🟢 | if/else | 5分钟 |
| 32 | for循环 | 🟢 | for...of | 10分钟 |
| 33 | while循环 | 🟢 | while | 5分钟 |
| 34 | 循环控制(break/continue) | 🟢 | break/continue | 5分钟 |
| 35 | enumerate和zip | 🟡 | entries() | 10分钟 |
| 36 | 异常处理 | 🟡 | try/catch | 15分钟 |
| 37 | 自定义异常 | 🟡 | Error类 | 15分钟 |
| 38 | 上下文管理器(with) | 🟡 | - | 15分钟 |
| 39 | 列表推导式中的条件 | 🟡 | - | 10分钟 |
| 40 | 生成器和yield | 🔴 | Generator | 20分钟 |

## 🔥 核心概念突破

### 1. 列表推导式（List Comprehension）

**JS方式**：
```javascript
// JS: 过滤+映射
const numbers = [1, 2, 3, 4, 5];
const doubled = numbers
  .filter(x => x % 2 === 0)
  .map(x => x * 2);
// [4, 8]
```

**Python方式**：
```python
# Python: 一行搞定
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers if x % 2 == 0]
# [4, 8]
```

### 2. 装饰器（Decorator）

**JS方式**（HOC）：
```javascript
function withLogging(fn) {
  return function(...args) {
    console.log(`Calling ${fn.name}`);
    return fn(...args);
  }
}

const add = withLogging((a, b) => a + b);
```

**Python方式**：
```python
def with_logging(fn):
    def wrapper(*args, **kwargs):
        print(f"Calling {fn.__name__}")
        return fn(*args, **kwargs)
    return wrapper

@with_logging  # 语法糖
def add(a, b):
    return a + b
```

### 3. 上下文管理器（Context Manager）

**JS方式**（需手动清理）：
```javascript
const file = fs.openSync('file.txt', 'r');
try {
  // 操作文件
} finally {
  fs.closeSync(file);  // 必须手动关闭
}
```

**Python方式**（自动清理）：
```python
with open('file.txt', 'r') as file:
    # 操作文件
# 自动关闭，即使发生异常
```

## 📝 如何使用本模块

### 1. 阅读题目
```bash
cd 01-python-basics/exercises
cat ex01_variables.py
```

每个文件都有详细的注释说明

### 2. 完成练习
在标记位置编写代码：
```python
def solution():
    """
    TODO: 在这里实现您的代码
    """
    pass  # 删除这行，写您的代码
```

### 3. 运行测试
```bash
# 单个测试
pytest tests/test_ex01.py -v

# 所有测试
pytest tests/ -v

# 显示详细输出
pytest tests/test_ex01.py -v -s
```

### 4. 查看进度
```bash
python ../utils/progress.py --module 01
```

### 5. 参考答案
完成后可以对照：
```bash
cat solutions/ex01_solution.py
```

## 💡 学习提示

### 给前端开发者的建议

1. **不要死记硬背**：看到Python语法，立即在脑中转换成JS
2. **用JS思维理解**：Python的`[x for x in list]` = JS的`.map()`
3. **注意陷阱**：
   - Python的`and/or` ≠ JS的`&&/||`（返回值不同）
   - Python的`is` ≠ JS的`===`（is检查身份，不是值）
   - Python没有`undefined`，只有`None`

### 快速测试技巧

```python
# 在Python文件末尾加上这个
if __name__ == "__main__":
    # 快速测试代码
    result = solution()
    print(result)
```

然后直接运行：
```bash
python exercises/ex01_variables.py
```

## 🎯 完成标准

- [ ] 所有40道题通过pytest测试
- [ ] 能用Python重写您之前的一个JS工具函数
- [ ] 理解Python的"鸭子类型"和动态特性
- [ ] 掌握装饰器和上下文管理器

## ⏭️ 下一步

完成本模块后，进入 `02-python-advanced`：
- 异步编程（async/await）
- 面向对象（Class）
- 类型系统（Pydantic）
- 常用库（requests, pathlib）

---

**开始时间**：_________  
**完成时间**：_________  
**用时**：_____ 小时  
**测试通过率**：_____%

