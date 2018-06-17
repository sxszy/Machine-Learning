# 笔记整理
## 日常遇到的一些python常用的一些函数或者方法，做个记录。
### 1. enumerate()
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

### 2. Windows shell中清屏操作

	import os
	os.system('cls')

或者可以使用网上的伪清屏操作，直接写个函数，添加一百行空的东西。

### 3. 两个常用的查询函数help()和str()
>help() 函数用于查看函数或模块用途的详细说明。

以下实例展示了help的使用方法：

	>>>help('sys')             
	……显示帮助信息……
	 
	>>>help('str')             
	……显示帮助信息……
	 
	>>>a = [1,2,3]
	>>>help(a)                
	……显示帮助信息……
	 
	>>>help(a.append)     
	……显示帮助信息……

>dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法__dir__()，该方法将被调用。如果参数不包含__dir__()，该方法将最大限度地收集参数信息。

以下实例展示了dir()的使用方法：

	>>>dir()   
	['__builtins__', '__doc__', '__name__', '__package__', 'arr', 'myslice']
	>>> dir([ ])    

### 4. str() 
>str()函数将对象转化为适于人阅读的形式

以下实例展示了str()的使用方法：

	>>>s = 'RUNOOB'
	>>> str(s)
	'RUNOOB'
	>>> dict = {'runoob': 'runoob.com', 'google': 'google.com'};
	>>> str(dict)
	"{'google': 'google.com', 'runoob': 'runoob.com'}"
	>>>

### 5. reload()
>reload() 用于重新载入之前载入的模块

以下实例展示了reload()的使用方法：

	>>>from imp import reload
	>>>reload(...)

### 5. resample()
>Pandas中的resample，重新采样，是对原样本重新处理的一个方法，是一个对常规时间序列数据重新采样和频率转换的便捷的方法

以下实例展示了resample()的使用方法：

	>>> index = pd.date_range('1/1/2000', periods=9, freq='T')
	>>> series = pd.Series(range(9), index=index)
	>>> series
	2000-01-01 00:00:00    0
	2000-01-01 00:01:00    1
	2000-01-01 00:02:00    2
	2000-01-01 00:03:00    3
	2000-01-01 00:04:00    4
	2000-01-01 00:05:00    5
	2000-01-01 00:06:00    6
	2000-01-01 00:07:00    7
	2000-01-01 00:08:00    8
	Freq: T, dtype: int64

