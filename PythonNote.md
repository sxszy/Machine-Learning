# 笔记整理-更新 2018/6/22
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
---
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

### 6. resample()
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
	
### 7.异常处理
>当Python检测到一个错误时，解释器就无法继续执行下去，于是抛出提示信息，即为异常。

常用的方式是使用try....except...else,以下是使用方法：

	try:
	<语句>        #运行别的代码
	except <名字>：
	<语句>        #如果在try部份引发了'name'异常
	except <名字>，<数据>:
	<语句>        #如果引发了'name'异常，获得附加的数据
	else:
	<语句>        #如果没有异常发生

>try的工作原理是，当开始一个try语句后，python就在当前程序的上下文中作标记，这样当异常出现时就可以回到这里，try子句先执行，接下来会发生什么依赖于执行时是否出现异常。  
> + 如果当try后的语句执行时发生异常，python就跳回到try并执行第一个匹配该异常的except子句，异常处理完毕，控制流就通过整个try语句（除非在处理异常时又引>发新的异常）。  
> + 如果在try后的语句里发生了异常，却没有匹配的except子句，异常将被递交到上层的try，或者到程序的最上层（这样将结束程序，并打印缺省的出错信息）。  
> + 如果在try子句执行时没有发生异常，python将执行else语句后的语句（如果有else的话），然后控制流通过整个try语句。  
---
#### try-except
用以下方式try-except语句捕获所有发生的异常。但这不是一个很好的方式，我们不能通过该程序识别出具体的异常信息。因为它捕获所有的异常：

	try:
	    正常的操作
	   ......................
	except:
	    发生异常，执行这块代码
	   ......................
	else:
	    如果没有异常执行这块代码

或者：

	try:
	    正常的操作
	   ......................
	except(Exception1[, Exception2[,...ExceptionN]]]):
	   发生以上多个异常中的一个，执行这块代码
	   ......................
	else:
	    如果没有异常执行这块代码
---
#### try...finally语句的使用方法：

	try:
	<语句>
	finally:
	<语句>    #退出try时总会执行
	raise
---
#### 触发异常：

>我们可以使用raise语句自己触发异常,语句中 Exception 是异常的类型（例如，NameError）参数标准异常中任一种，args 是自已提供的异常参数。最后一个参数是可选的（在实践中很少使用），如果存在，是跟踪异常对象.

raise语法格式如下:
	
	raise [Exception [, args [, traceback]]]
---	
#### 用户自定义异常

>通过创建一个新的异常类，程序可以命名它们自己的异常。异常应该是典型的继承自Exception类，通过直接或间接的方式。

以下为与RuntimeError相关的实例,实例中创建了一个类，基类为RuntimeError，用于在异常触发时输出更多的信息。在try语句块中，用户自定义的异常后执行except块语句，变量 e 是用于创建Networkerror类的实例:

	class Networkerror(RuntimeError):
	    def __init__(self, arg):
		self.args = arg

在定义该类后可以触发异常：

	try:
	    raise Networkerror("Bad hostname")
	except Networkerror,e:
	    print e.args
