### 笔记整理
## 日常遇到的一些python常用的一些函数或者方法，做个记录。
# 1. enmurate()
>enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标，一般用在 for 循环当中：

	>>>seasons = ['Spring', 'Summer', 'Fall', 'Winter']
	>>> list(enumerate(seasons))
	[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
	>>> list(enumerate(seasons, start=1))       # 小标从 1 开始
	[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
如果是用来循环的话，常常可以使用：

	>>>seq = ['one', 'two', 'three']
	>>> for i, element in enumerate(seq):
	...     print i, element
	... 
	0 one
	1 two
	2 three
---
# 2. Windows shell中清屏操作

	import os
	os.system('cls')

	或者可以使用网上的伪清屏操作，直接写个函数，添加一百行空的东西。
---
# 3. 两个常用的查询函数help()和str()
>help() 函数用于查看函数或模块用途的详细说明。

以下实例展示了help的使用方法：
	>>>help('sys')             # 查看 sys 模块的帮助
	……显示帮助信息……
	 
	>>>help('str')             # 查看 str 数据类型的帮助
	……显示帮助信息……
	 
	>>>a = [1,2,3]
	>>>help(a)                 # 查看列表 list 帮助信息
	……显示帮助信息……
	 
	>>>help(a.append)          # 显示list的append方法的帮助
	……显示帮助信息……

>dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。

以下实例展示了dir()的使用方法：
	>>>dir()   #  获得当前模块的属性列表
	['__builtins__', '__doc__', '__name__', '__package__', 'arr', 'myslice']
	>>> dir([ ])    # 查看列表的方法
	['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
---
# 4. str() 函数将对象转化为适于人阅读的形式

以下实例展示了str()的使用方法：
	>>>s = 'RUNOOB'
	>>> str(s)
	'RUNOOB'
	>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
	>>> str(dict)
	"{'google': 'google.com', 'runoob': 'runoob.com'}"
	>>>
