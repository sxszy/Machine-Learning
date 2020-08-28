# 17. 电话号码的字母组合
## 题目简述：
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

	'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv', '9':'wxyz'}

示例:

	输入："23"
	输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
    
具体代码：

**方法一**

	import itertools
	class Solution:
	    def letterCombinations(self, digits: str) -> List[str]:
	        conversion={'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv', '9':'wxyz'}
	        if len(digits)==0:
	            return [] 
	        product=['']
	        for k in digits:
	            product=[i+j for i in product for j in conversion[k]]
	        return product

**方法二**

	class Solution:
	
	    def __init__(self):
	        self.letter_dict = {"2": ["a", "b", "c"],
	                "3": ["d", "e", "f"],
	                "4": ["g", "h", "i"],
	                "5":["j", "k", "l"],
	                "6": ["m", "n", "o"],
	                "7":["p", "q", "r", "s"],
	                "8": ["t", "u", "v"],
	                "9": ["w", "x", "y", "z"]}
	
	    def letterCombinations(self, digits: str) -> List[str]:
	        if digits == "":
	            return []
	        import itertools
	        letter_input = [i for i in digits]
	        letter_input = list(map(self.look_up, letter_input))
	        return list(map(self.simple_fuc, list(itertools.product(*letter_input))))
	
	    def simple_fuc(self, l):
	        return "".join(l)
	
	    def look_up(self,s):
	        return self.letter_dict[s]