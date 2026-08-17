#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# @Time     : 2026/8/16 下午4:54
# @Author   : 陈李
# @File     :0002-函数进阶-匿名函数.py
# @software :PyCharm

# 匿名函数是没有名称的函数
"""
定义匿名函数 -> 一般是比较简单的函数
需要通过lambda表达式来申明函数
lambda 参数列表 : 函数体
用作简单函数，或者用于高级函数的参数
"""
Nobody = lambda a, b: a + b
print(Nobody(2, 3))
# sort() 中匿名函数的使用？
"""
# 示例：按字符串长度排序
words = ["apple", "banana", "cherry", "date"]
words.sort(key=len)
print(words) # 输出: ['date', 'apple', 'banana', 'cherry']
"""
words = ["apple", "banana", "cherry", "date"]
words.sort(key=lambda item: len(item))
# 与key= len 相比，这里多了一层py语言的调用，如果只是单纯的利用字符串的长度来排序那么前者更好
# 如果加入了，更加复杂的要求例如切片等内容则利用匿名函数进行简单的运算
# 按字符串长度排序，但如果长度相同，则按首字母排序
words.sort(key=lambda item: (len(item), item[0]))  # 比如这个
print(words)
# 命名函数和匿名函数的选择？
"""
命名函数准确，匿名函数简单，并且后者可以套入命名函数，取决于函数的负复杂程度
代码的可读性和可维护性比简洁更重要
"""