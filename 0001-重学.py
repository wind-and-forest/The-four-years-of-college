# 2025/6/7
# C:\Users\陈李佳\Desktop\白菜\2024年编程学习.clj\初等练习\较难的知识点(两周)\面对对象的特点\pythonProject
# 面向对象，解释型 强类型，动态脚本语言
# 检查错误，语法，命名，缩进，输入错误
# DEBUG 断点测试 小虫虫是 用来检查修改错误的 点数字标红调试
# 快捷键：ctrl+/ 注释 +Z 撤销 +F 查找
print('Hellow world')
# 变量 标识符 数值类型 字符串 格式化输出
# 变量命名规则：开头无_、数字、关键字除非加\
a = 1
b = 'apple'
c = [1, 2, 3]
d = (1, 2)
e = {'keyword': 'banana'}
f = False
g = {1, 2, 3}
666
13.14
"黑马程序员"
print("黑马程序员")
a = 10
b = 20
a, b = b, a
print(a, b)

a = 100
b = 200
c = 300
# d = a
# e = b
# b = c
# c = a
# a = e
# print(c,a,b)
# c,a,b = a,b,c
# print(c,a,b)
# 判定数据类型：isinstance(数据类型, 类型)，得到布尔值大写
s1 = "人生苦短"
s2 = "我用python"
print(s1 + "," + s2)
f = str("100")
print(f)
print(int(f))

# 字符串的格式化 %占位符（其中占位符，为变量占位）
# 利用f"内容{变量}"常用，企业开发端的标准形式
# age = "3"
# name = "唐三"
# print(f"你好：{age}{name}")
#
# name = input("请输入你的名字：")
# age = input("请输入你的年龄：")
# print(f"你的名字是：{name}")
# print(f"你的年龄是：{age}")
# x = float(input("x = "))
# y = float(input("y = "))
# print("x + y =", x+y)
# print("x - y =", x-y)
# 0.0009999999 ---> 精度损失：计算机中二进制是无法准确表示小数点所以对于浮点数的运算时会存在精度损失的可能
"""
=
+=   num = num + ?

"""
# 除法运算得到的结果时浮点数
"""
== 等于
!= 不等于
>
<
>=
<=
比较运算符所得到的值时是布尔值 True False
"""
"""
逻辑运算符
and or not

"""
# object1 = input("输入内容：")
# if object1 == "1":
#     print("yes")
# else:
#     print("no")
# num = float(input("请输入数字："))
# if num > 0:
#     print(f"{num}是一个正数")
# elif num < 0:
#     print(f"{num}是一个负数")
# else:
#     print(f"{num}是0")
""""
x = float(input("边长1："))
y = float(input("边长2："))
z = float(input("边长3："))
"""
# if x + y < z or x + z < y or y + z < x:
#     print("不是三角形")
# elif x == y == z:
#     print("等边三角形")
# elif x == y or x == z or y == z:
#     print("等腰三角形")
# else:
#     print("普通三角形")

# match...case 模式匹配，用一个清晰的模板去精准匹配数据的结构和内容，匹配成功则响应操作
# 工作日安排
# day = input("please input the day of the week(1-7):")
# match day:
#     case "1":
#         print("Monday")
#     case "2":
#         print("Tuesday")
#     case "3":
#         print("Wednesday")
#     case "4":
#         print("Thursday")
#     case "5":
#         print("Friday")
#     case "6"|"7":
#         print("Weekend")
#     case _:
#         print("Input Error")
# 匹配模式是从上到下匹配的，|表示或者，在多种匹配模式表示任意一个
# _表示其他的所有情况

# 简单游戏指令系统 match...case 实现
# instruction = input("please enter your instruction:")
# match instruction:
#     case "上"|"w"|"W":
#         print("The character moves upwards.")
#     case "下"|"s"|"S":
#         print("The character moves downward.")
#     case "左"|"a"|"A":
#         print("The character moves to the left.")
#     case "右"|"d"|"D":
#         print("The character moves to the right.")
#     case "跳"|" ":
#         print("The character jump.")
#     case "攻击"|"j"|"J":
#         print("The character attack.")
#     case "退出"|"ESC"|"esc":
#         print("The character exit.")
#     case _:
#         print("Your instruction is incorrect.")

"""
While loop 最后会终止而非不断循环
total = 0
i = 1
while i<=100:
    if i%2==0:
        total += i
    i += 1
else :
    print(total)
"""
# for循环 本质是一种轮询遍历机制，对一批内容进行逐个处理
"""
for 元素 in 待处理数据集:
    循环体代码
else:
    循环结束时，执行的代码
"""
# msg = 'hello_Python'
# for i in msg:
#     print(i)
# else:
#     pass
""""
range(start,end,step) -> 从零开始走到end，不包括end，同时还有步长可以调节判定并获取奇数偶数
计算1-100之间的所有奇数之和
total = 0
for i in range(101):
    if i%2 == 1:
        total += i
    else:
        pass
print(total)
"""
"""
计算100—500之间的所有3的倍数的数字之和

total = 0
for i in range(100,501):
    if i%3 == 0:
        total += i
else:
    print(total)

"""
"""
嵌套循环
分清内外循环，先外后内
m = int(input("请输入长方形的长度："))
n = int(input("请输入长方形的宽度："))
s = ""
for j in range(n):
    for i in range(m):
        s += "*  "
    else:
        print(s)
        s = "" # 或许有更好的方法，因为这里回归了
else:
    pass
"""

# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} * {i} = {j*i}",end="\t") # 制表符可以使内容对齐
#     else:
#         print()
# else:
#     pass

# 用户密码匹配, break 直接中断，continue 中断直接进行下一次循环
"""
i = 0
while True:
    i +=1
    name = input("请输入你的用户名：")
    password = input("请输入你的密码：")
    if name == "" or password == "":
        print("Your name and password couldn't be none!")
        continue
    elif name == "admin" and password == "666888":
        print("登录成功，进入B站首页~")
        break
    elif name == "zhangsan" and password == "123456":
        print("登录成功，进入B站首页~")
        break
    elif name == "taoge" and password == "888666":
        print("登录成功，进入B站首页~")
        break
    elif i == 5:
        print("You could operate any more!")
        break
    else:
        print("用户名或密码错误，请重新输入！")
        print(f"你还有{5-i}次操作机会！")
"""
# random 随机数生成，导入random导入模块
# import random
# random_number = random.randint(1,100)
#
# while True:
#     answer = input("请猜一个1到100的的数字：")
#     try:  # 截取错误获取反馈得到正确的数据。
#         int(answer)
#     except ValueError:
#         print("你输入错误了！")
#         continue
#     answer = int(answer)
#     if answer < 1 or answer >100:
#         print("your answer extend the edge! ")
#         continue
#     if random_number == answer:
#         print("你猜对了！")
#         break
#     else:
#         if random_number < answer:
#             print("Your answer is too big.")
#         else :
#             print("your answer is too small.")
""""""
# 数据存取：集合set，列表list，元组tuple，字典tuple，字符串str
# list[]
# list1 = [1,2,3,4] # 元素有序，元素可以修改，存取不同类型
# # 访问列表中的元素
# print(list1[3]) # 开始是从0而来的
# print(list1[-4]) # 反向索引从-1开始的，暗藏着循序
#
# # 指定索引可以修改内容，不可以索引越界。
# list1[3] = 7
# print(list1[3])
#
# # 删除操作（指定位置）del
# del list1[0] # 记得 顺序起始是0
# print(list1)
#
# # 遍历，也就是直接用 list1 这个集合
#
# for i in list1 :
#     print(i)
#
# # list[开始索引:结束索引:步长]
# print(list1[0:3:2]) # 注意这里是冒号。正向索引可以使用，反向索引也可以使用。

# 对象的方法
"""
s.append()
s.insert()
s.remove()
s.pop()
s.sort() 整理排序
s.reverse() 反转排序
"""
# s = []
# for i in range(10):
#     num = float((input(f"请输入10个有效数字，这是第{i+1}个:")))
#     s.append(num)
# s.sort()
# print(s[0]) # 最小的
# print(s[9]) # 最大的
# total = 0
# for j in s:
#     total += j
# a = total/10
# print(a)
# 可以使用sum()和len()函数 min()max()
# print("平均值：",sum(s)/len(s))

# 1,合并列表，遍历相加/相加后整理
"""
解包内容
num_list = [*num_list1 + *bum_list2]
可以直接用相加
组包内容

"""
# 2,去除重复元素的列表 对比内容判断列表是否重复。
"""
for num in num_list1:
    if num not in new_list:
        new_list.append(num)
print(newlist) (本质内容的筛选) 
"""
# # # 注意使用 in 这个判断的逻辑运算符
# # l = []
# for i in range(1,21):
#     l.append((i**2))
# print(l)
# new_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
# l2= [i**2 for i in new_list if i%2 ==0]
#
# # for j in new_list:
# #     if j%2 == 0:
# #         print(j**2)
# #         l2.append(j**2)
# #     else:
# #         pass
# print(l2)
# 字符串类型：不可修改：其中的内容无法修改。有序，可迭代性：通过for循环可以将每一个元素输出来。
# 切片含头不含尾。步长方向要与首尾方向一致。如果从后往前截取，则会得到反转字符串的效果
"""
find()      获得的是指定字符串的索引
count()     获得次数
upper()
lower()
split()     按照指定字母切割形成列表
strip()     去除两端空格
replace()    把原字母替换为指定字母
startswith()  判断开头字符串，提供布尔值 

"""
# mail = input('请输入邮箱：')
# if mail.count("@") == 1 and mail.count(".") >= 1:
#     print(f"{mail}")
# else:
#     print(f"{mail}")

# 判断个数用count 判断存在用in
"""
s = input("请输入一个字符串：")
s_d = s[::-1]
if s == s_d:
    print("该字符串运用的回文")
else:
    print("该字符串没有运用回文"))
"""
# l1 =[]
# for i in range(10):
#     s = input(f"请输入第{i+1}个字符串:")
#     s_d = s[::-1]
#     s_d.upper()
#     l1.append(s_d)
# for j in l1:
#     print(j)
"""--------------"""
# # tuple 元组：不可修改的序列,元组是有要有顺序的。其中单元素需要在后面加上逗号，不然系统会认为这是数据计算的括号。
# # count()index()数数和查找索引
# t1 = (22,334,542,653) # 组包
# print(type(t1))
# a, b, c, d = t1 # 解包
# # 在元组解包时 *表示收集剩下的元素,然后转化为列表
# a, b, *c =t1
"""
关于数据容器的使用：行列，以及是否可变。
"""
# print("学号 \t 姓名 \t 语文 \t 数学 \t 英语 \t 总分 \t 平均分")
# students = (("S001", "王林", 85, 92, 78),
#             ("S002","李慕婉", 92, 88, 95),
#             ("S003", "十三", 78, 85, 95))
# # 其次可以使用解包来操作 多变量接受内容
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total/3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.1f}") # 保留一位小数
#
# C = [s[2] for s in students]
# M = [s[3] for s in students]
# E = [s[4] for s in students]
#
# print(f"语文最高分：{max(C)}平均分：{sum(C)/len(C):.1f}最低分：{min(C)}")
# print(f"数学最高分：{max(M)}平均分：{sum(M)/len(M):.1f}最低分：{min(M)}")
# print(f"英语最高分：{max(E)}平均分：{sum(E)/len(E):.1f}最低分：{min(E)}")
""""""
# ####字典####
# # 1.字典的存储：以键值对的形式存储，其中键key不可改变是唯一的也就是不可以是set、list、dict等
# dict2 = {}
# dict()
# # 空字典的定义
# dict1 = {"a":"A", "b":"B", "c":"C", "c":"CC"}
# # 语法形式,如果重复定义则取值会取后面定义的内容
# A = dict1["a"]
# # key 对应取值，也可直接赋值修改
# # for i in dict1:
# #     print(i)
# # dict 类型无法被for呼告引用所以只能分开后遍历
def out_line(r):
    """
    对函数的解释，函数的说明文档，有利于说明和后期维护
    :param r: 参数含义
    :return: 返回值
    """
    print("____________________")
    return "r" # 返回两个值时是利用元组来接受的
# round(,) 可以使返回值的浮点数位数指定
print(out_line(8))
# 函数进阶： 三个方面，函数的变量域
# 局部变量和全局变量的不同在哪里？
# 以及在函数中如何是同命变量划为全局变量：利用global关键字
"""_______________________"""
# 函数的传参方式：位置传参，关键字传参（键 = 值，对位置没有要求）
# 函数参数的缺省默认，在形参中赋值 参数 = 默认值，其次默认值必须在非默认参数谋面中的后面
# 不定长参数，对于无法确定参数可以使用来：表达*args除了这个还有别的，即为不定长参数，这本质是一个元组，所以用的也是元组的方法
# 那么如果这是有一部分是不定长，但也有一部分是有固定的参数呢？
# 关键字不定长参数（**kwargs），这个会被封装到一个字典中，因此要用字典类的方法.get()使用
# 根据键来找对应可以使用 if 循环 和布尔判断找到相关内容
# 要求先写位置参数再写关键字参数

# 函数也可以作为参数
def add(x,y):
    return x + y
def calc(x,y,oper):
    return oper(x, y) # 定义函数,oper作为函数名指称的逻辑， 此处也就是函数的嵌套调用。
print(calc(2,5,add))

