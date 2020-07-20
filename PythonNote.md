# 笔记整理-更新 2020/7/20
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

### 8. 不可变与可变-Immutable & Mutable

可变（mutable)和不可变（immutable）这个问题困扰了我很久，今天决定好好地把他理解一下！

>并不是所有的Python对象处理方式都是一样的，有的对象是可变的(mutable)，此类对象可以被改变，其余的对象则是不可变的(immutable)，它们无法被修改，并且当我们尝试更新此类对象的时候，会返回一个新的对象。知道这些对我们写Python代码有什么意义呢？我们来一探究竟。

#### 不可变（Immutable）对象类型
+ int 
+ float
+ decimal
+ complex
+ bool
+ string
+ tuple
+ range
+ frozenset
+ bytes
#### 可变（Mutable）对象类型
+ list
+ dict
+ set
+ bytearray
+ user-defined classed(unless specifically made immutable)
---
#### Case one

	>>> a = 1
	>>> id(a)
	1518038080
	>>> a = 2
	>>> id(a)
	1518038112
	
从这个例子我们可以看到，在赋值之后a的ID（内存地址空间）已经发生了变化，这与我们在以前所知的，地址空间不变而其中的值发生了变化的情况是不太相同的。我们可以这样理解，a = 1（= 相当于是引用）的含义是创建一个值为2的整形对象，再将a指向该对象的地址，多以上例的两个int对象的值并没有变。
#### Case two

	>>> a = [1,2,3]
	>>> b = (1,2,3)
	>>> a[0] = 4
	>>> print(a)
	[4, 2, 3]
	>>> b[0] = 4
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'tuple' object does not support item assignment
	>>> b = (1,2,[3])
	>>> b[2][0] = 4
	>>> print(b)
	(1, 2, [4])
	
从这个例子我们可以看到，我们改变了列表a中的一个值，因为list是可变的（mutable），同时我们看到在我们试图改变元组b的一个值时，就遭遇了错误，因为元组是属于不可变类型，一旦初始化则不可改变。但是我们要注意的是，元组也并不是绝对地不可变，如果元组中包含了mutable类的object,那么这个object的值是可以改变的。

#### Case three
Immutable

	>>> def func(x):
	...     x = 1
	...     print(x)
	...
	>>> x = 2
	>>> func(x)
	1
	>>> print(x)
	2
	
我们可以看到，immutable类型在函数执行后，自身的值并没有发生改变，即：

>传递的引用不能改变自身，只是改变了引用的指向

Mutable

	>>> def func(x):
	...     x[0] = 4
	...     print(x)
	...
	>>> x = [1]
	>>> func(x)
	[4]
	>>> print(x)
	[4]

从这个例子我们可以看到，mutable类型在函数执行后，自身的值也一起发生了改变。

>这里传递的引用可以引用自身的元素而改变自身。

> 对Case three进行总结：
> + 对于immutable类型，我们在函数参数传递是值传递。（对于函数内部来说，相当于在传递的时候，复制了一个一模一样的量，再对这个量进行操作）
> + 对于mutable类型，我们在函数参数传递则是指针传递。

### 9. 获得路径的父目录  
Pathlib
	
	>>> import pathlib
	>>> print(pathlib.Path("F:\IGG\Code\music").parent.name)
	Code

### 10.单例模式
>单例模式（Singleton Pattern）是 Java 中最简单的设计模式之一。这种类型的设计模式属于创建型模式，它提供了一种创建对象的最佳方式。

>这种模式涉及到一个单一的类，该类负责创建自己的对象，同时确保只有单个对象被创建。这个类提供了一种访问其唯一的对象的方式，可以直接访问，不需要实例化该类的对象。

>注意：

>1、单例类只能有一个实例。  
2、单例类必须自己创建自己的唯一实例。  
3、单例类必须给所有其他对象提供这一实例。

	from functools import wraps
	
	
	def singleton(cls):
	    """装饰类的装饰器"""
	    instances = {}
	
	    @wraps(cls)
	    def wrapper(*args, **kwargs):
	        if cls not in instances:
	            instances[cls] = cls(*args, **kwargs)
	        return instances[cls]
	
	    return wrapper
	
	
	@singleton
	class President:
	    """总统(单例类)"""
	    pass

### 11.线程安全？Rlock?
线程安全是多线程编程时的计算机程序代码中的一个概念。在拥有共享数据的多条线程并行执行的程序中，线程安全的代码会通过同步机制保证各个线程都可以正常且正确的执行，不会出现数据污染等意外情况。[教程链接](https://python-parallel-programmning-cookbook.readthedocs.io/zh_CN/latest/chapter2/07_Thread_synchronization_with_RLock.html)  

### 12.抽象类
总结：用abc模块装饰后，在实例化的时候就会报错，那么当我们代码很长的时候，就可以早一点预知错误，所以以后在接口类类似问题中用这个模块
接口继承实质上是要求“做出一个良好的抽象，这个抽象规定了一个兼容接口，使得外部调用者无需关心具体细节，
可一视同仁的处理实现了特定接口的所有对象”——这在程序设计上，叫做归一化。

### 13.什么是实例方法、静态方法和类方法？
实例方法：就是实例化之后可以调用的方法，默认第一个参数为self
类方法：类里面需要传入cls参数，无需创建实例对象调用
静态方法：无需传入self参数或者是cls参数

### 14.对象复制（普通赋值，深复制/浅拷贝/）
python赋值：是简单的对象引用，指向了同一个地址
浅拷贝：拷贝父对象，不会拷贝对象内部的子对象，如切片操作，copy操作等，如果浅复制的对象是不可变对象，id值相同，如果对象是可变对象，则产生一个“不完全新”的对象（1.内部无复杂子对象，则相互不影响2.有复杂子对象，则原对象值改变也会影响到新拷贝里面的值）
深拷贝：完全拷贝父对象及其子对象，拷贝了所有元素，是个全新对象，不再与原有对象有任何联系

### 15.python垃圾回收
>Python使用了自动化内存管理，这种管理机制以引用计数为基础，同时也引入了标记-清除和分代收集两种机制为辅的策略。  

导致引用计数+1的情况：

+ 对象被创建，例如a = 23
+ 对象被引用，例如b = a
+ 对象被作为参数，传入到一个函数中，例如f(a)
+ 对象作为一个元素，存储在容器中，例如list1 = [a, a]

导致引用计数-1的情况：

+ 对象的别名被显式销毁，例如del a
+ 对象的别名被赋予新的对象，例如a = 24
+ 一个对象离开它的作用域，例如f函数执行完毕时，f函数中的局部变量（全局变量不会）
+ 对象所在的容器被销毁，或从容器中删除对象

引用计数可能会导致循环引用问题，而循环引用会导致内存泄露，如下面的代码所示。为了解决这个问题，Python中引入了**“标记-清除”**和**“分代收集”**。在创建一个对象的时候，对象被放在第一代中，如果在第一代的垃圾检查中对象存活了下来，该对象就会被放到第二代中，同理在第二代的垃圾检查中对象存活下来，该对象就会被放到第三代中。

以下情况会导致垃圾回收：

+ 调用gc.collect()
+ gc模块的计数器达到阀值
+ 程序退出

如果循环引用中两个对象都定义了__del__方法，gc模块不会销毁这些不可达对象，因为gc模块不知道应该先调用哪个对象的__del__方法，这个问题在Python 3.6中得到了解决。

### 16.魔法属性和方法
魔法属性和方法：查看书，比如__slots__，__new__等自带的属性和方法


### 17.元编程和元类
对象是通过类创建的，类是通过元类创建的，元类提供了创建类的元信息。所有的类都直接或间接的继承自object，所有的元类都直接或间接的继承自type。

	# 用例子实现单例模式
	import threading
	
	
	class SingletonMeta(type):
	    """自定义元类"""
	
	    def __init__(cls, *args, **kwargs):
	        cls.__instance = None
	        cls.__lock = threading.RLock()
	        super().__init__(*args, **kwargs)
	
	    def __call__(cls, *args, **kwargs):
	        if cls.__instance is None:
	            with cls.__lock:
	                if cls.__instance is None:
	                    cls.__instance = super().__call__(*args, **kwargs)
	        return cls.__instance
	
	
	class President(metaclass=SingletonMeta):
	    """总统(单例类)"""
	    
	    pass

### 18.面向对象设计原则

+ 单一职责原则 （SRP）- 一个类只做该做的事情（类的设计要高内聚）
+ 开闭原则 （OCP）- 软件实体应该对扩展开发对修改关闭
+ 依赖倒转原则（DIP）- 面向抽象编程（在弱类型语言中已经被弱化）
+ 里氏替换原则（LSP） - 任何时候可以用子类对象替换掉父类对象
+ 接口隔离原则（ISP）- 接口要小而专不要大而全（Python中没有接口的概念）
+ 合成聚合复用原则（CARP） - 优先使用强关联关系而不是继承关系复用代码
+ 最少知识原则（迪米特法则，LoD）- 不要给没有必然联系的对象发消息

### 19.生成器

	def fib(num):
	    """生成器"""
	    a, b = 0, 1
	    for _ in range(num):
	        a, b = b, a + b
	        yield a

### 20.并发编程
>Python中实现并发编程的三种方案：多线程、多进程和异步I/O。并发编程的好处在于可以提升程序的执行效率以及改善用户体验；坏处在于并发的程序不容易开发和调试，同时对其他程序来说它并不友好。

>多线程：Python中提供了Thread类并辅以Lock、Condition、Event、Semaphore和Barrier。Python中有GIL来防止多个线程同时执行本地字节码，这个锁对于CPython是必须的，因为CPython的内存管理并不是线程安全的，因为GIL(全局解释器锁)的存在多线程并不能发挥CPU的多核特性。  

	"""
	面试题：进程和线程的区别和联系？
	进程 - 操作系统分配内存的基本单位 - 一个进程可以包含一个或多个线程
	线程 - 操作系统分配CPU的基本单位
	并发编程（concurrent programming）
	1. 提升执行性能 - 让程序中没有因果关系的部分可以并发的执行
	2. 改善用户体验 - 让耗时间的操作不会造成程序的假死
	"""
	import glob
	import os
	import threading
	
	from PIL import Image
	
	PREFIX = 'thumbnails'
	
	
	def generate_thumbnail(infile, size, format='PNG'):
	    """生成指定图片文件的缩略图"""
		file, ext = os.path.splitext(infile)
		file = file[file.rfind('/') + 1:]
		outfile = f'{PREFIX}/{file}_{size[0]}_{size[1]}.{ext}'
		img = Image.open(infile)
		img.thumbnail(size, Image.ANTIALIAS)
		img.save(outfile, format)
	
	
	def main():
	    """主函数"""
		if not os.path.exists(PREFIX):
			os.mkdir(PREFIX)
		for infile in glob.glob('images/*.png'):
			for size in (32, 64, 128):
	            # 创建并启动线程
				threading.Thread(
					target=generate_thumbnail, 
					args=(infile, (size, size))
				).start()
				
	
	if __name__ == '__main__':
		main()


>**重点：多线程和多进程的比较。**

>以下情况需要使用多线程：

>程序需要维护许多共享的状态（尤其是可变状态），Python中的列表、字典、集合都是线程安全的，所以使用线程而不是进程维护共享状态的代价相对较小。
程序会花费大量时间在I/O操作上，没有太多并行计算的需求且不需占用太多的内存。
以下情况需要使用多进程：

>程序执行计算密集型任务（如：字节码操作、数据处理、科学计算）。
程序的输入可以并行的分成块，并且可以将运算结果合并。
程序在内存使用方面没有任何限制且不强依赖于I/O操作（如：读写文件、套接字等）。

多进程：多进程可以有效的解决GIL的问题，实现多进程主要的类是Process，其他辅助的类跟threading模块中的类似，进程间共享数据可以使用管道、套接字等，在multiprocessing模块中有一个Queue类，它基于管道和锁机制提供了多个进程共享的队列。下面是官方文档上关于多进程和进程池的一个示例。

	"""
	多进程和进程池的使用
	多线程因为GIL的存在不能够发挥CPU的多核特性
	对于计算密集型任务应该考虑使用多进程
	time python3 example22.py
	real    0m11.512s
	user    0m39.319s
	sys     0m0.169s
	使用多进程后实际执行时间为11.512秒，而用户时间39.319秒约为实际执行时间的4倍
	这就证明我们的程序通过多进程使用了CPU的多核特性，而且这台计算机配置了4核的CPU
	"""
	import concurrent.futures
	import math
	
	PRIMES = [
	    1116281,
	    1297337,
	    104395303,
	    472882027,
	    533000389,
	    817504243,
	    982451653,
	    112272535095293,
	    112582705942171,
	    112272535095293,
	    115280095190773,
	    115797848077099,
	    1099726899285419
	] * 5
	
	
	def is_prime(n):
	    """判断素数"""
	    if n % 2 == 0:
	        return False
	
	    sqrt_n = int(math.floor(math.sqrt(n)))
	    for i in range(3, sqrt_n + 1, 2):
	        if n % i == 0:
	            return False
	    return True
	
	
	def main():
	    """主函数"""
	    with concurrent.futures.ProcessPoolExecutor() as executor:
	        for number, prime in zip(PRIMES, executor.map(is_prime, PRIMES)):
	            print('%d is prime: %s' % (number, prime))
	
	
	if __name__ == '__main__':
	    main()

### 21.异步处理
>异步处理：从调度程序的任务队列中挑选任务，该调度程序以交叉的形式执行这些任务，我们并不能保证任务将以某种顺序去执行，因为执行顺序取决于队列中的一项任务是否愿意将CPU处理时间让位给另一项任务。异步任务通常通过多任务协作处理的方式来实现，由于执行时间和顺序的不确定，因此需要通过回调式编程或者future对象来获取任务执行的结果。Python 3通过asyncio模块和await和async关键字（在Python 3.7中正式被列为关键字）来支持异步处理。

	"""
	异步I/O - async / await
	"""
	import asyncio
	
	
	def num_generator(m, n):
	    """指定范围的数字生成器"""
	    yield from range(m, n + 1)
	
	# 我们可以使用async修饰将普通函数和生成器函数包装成异步函数和异步生成器，await语法只能出现在通过async修饰的函数中，否则会报SyntaxError错误。
	async def prime_filter(m, n):
	    """素数过滤器"""
	    primes = []
	    for i in num_generator(m, n):
	        flag = True
	        for j in range(2, int(i ** 0.5 + 1)):
	            if i % j == 0:
	                flag = False
	                break
	        if flag:
	            print('Prime =>', i)
	            primes.append(i)
			# 在协程函数中，可以通过await语法来挂起自身的协程，并等待另一个协程完成直到返回结果：
	        await asyncio.sleep(0.001)
	    return tuple(primes)
	
	
	async def square_mapper(m, n):
	    """平方映射器"""
	    squares = []
	    for i in num_generator(m, n):
	        print('Square =>', i * i)
	        squares.append(i * i)
	
	        await asyncio.sleep(0.001)
	    return squares
	
	
	def main():
	    """主函数"""
		# get_event_loop（）获取当前事件循环
	    loop = asyncio.get_event_loop()
		#  gather并发运行序列中的可等待对象
	    future = asyncio.gather(prime_filter(2, 100), square_mapper(1, 100))
		# add_done_callback添加一个回调，这里是打印结果
	    future.add_done_callback(lambda x: print(x.result()))
		# 运行直至future实例完成
	    loop.run_until_complete(future)
	    loop.close()
	
	
	if __name__ == '__main__':
	    main()

>**重点：异步I/O与多进程的比较。**

>当程序不需要真正的并发性或并行性，而是更多的依赖于异步处理和回调时，asyncio就是一种很好的选择。如果程序中有大量的等待与休眠时，也应该考虑asyncio，它很适合编写没有实时数据处理需求的Web应用服务器。