
不知道为什么在目录里面跳转的md解析出的排版有问题  
如果要看正常排版的请浏览以下github链接：  
[github链接](https://github.com/WindyMen/Dashboard/blob/gh-pages/doc/BackEnd%E4%BB%A3%E7%A0%81%E8%A7%84%E8%8C%83.md)  
谢谢!  

# django编码规范  
  
## 缩进
- 统一使用Tabs进行缩进

## 行宽
每行代码尽量不超过80个字符，在命名较长的情况下不能超过120个字符。

理由：
- 方便在控制台下查看代码
- 在太长的情况下不容易debug

## 引号
- 自然语言使用双引号
  - 例如错误信息，并且还是Unicode编码，使用u"..."
  - 正则表达式， 使用原生的双引号:r"/<int:pk>"
- 机器标识使用单引号''
  - 例如dict里面的key：{name: 'XiaoMing'}
- 文档字符串使用三个引号"""..."""

## 空行
- 模块级函数和类定义之间空两行
- 类成员函数之间空一行

```
class model(models.Model):


	def __init__(self):
		pass
		
	def __str__(self):
		pass
```

- 可以使用多个空行分隔多组相关的函数
- 函数中可以使用空行分隔出逻辑相关的代码

## 编码
- 文件使用UTF-8编码，在保存文件时确保一次使用的编码方式，否则在不同机器下会有乱码
- 文件头部加入以下的标识(python3以上版本不需要)

```
#-- coding:utf-8 --
```

## import 语句
- import语句应该分行书写

```
正确的写法
import sys
import os

错误的写法
import sys, os

正确的写法
from django.http import HttpResponse, JsonResponse
```

- import语句应该使用absolute import

```
正确的写法
from rest_framework import status

错误的写法
from ..model import views
```

- import语句应该放在文件头部，置于模块说明及docstring之后，于全局变量之前
- import语句应该按照顺序排列，每组之间用一个空行分隔

```
#自身模块的导入
from mymodel import views
import settings

#http模块的导入
from django.http import HttpResponse, JsonResponse, Http404
#...
```

- 导入其他模块的类定义时，可以使用相对导入

```
from mymodel import models
```

- 如果发生命名冲突，则可使用命名空间

```
import models
import mymodel.models

models.a()
mymodel.models.a()
```

## 空格
- 在二元运算符两边各空一格[=, -, +=, ==, >.......]

```
i = i + 1
x = x * 2 - 1
if a > 2
```

- 函数的参数列表中，逗号,之后要有空格
```
def function(parm1, parm2, parm3):
	pass
```

- 函数的参数列表中，默认值等号两边不要添加空格  

```
def function(parm1=1, parm2=2, parm3=3):
	pass
	
不推荐写法:
def function(parm1 = 1, parm2 = 2, parm3 = 3):
	pass
```

- 左括号之后，右括号之间不要加多余的空格

```
serializer = Serializer(model, context={'request': request})

不推荐的写法：
serializer = Serializer(model, context={'request': request} )
```

- 字典对象的左括号之前不要有多余的空格
```
推荐写法：
dict['key'] = 'key'

不推荐写法
dict ['key'] = 'key'
```

- 不要为对齐赋值语句而使用额外的空格（应该不会有人这样）

```
不推荐写法：
x    = 1
y    = 2
test =3
```

## 换行
python支持括号内的换行。有两种情况
1. 第二行缩进到括号的起始处

```
foo = function_name(parm1, parm2, 
		  parm3, parm4)
```

2. 第二行缩进2个tabs，适用于起始括号就换行的情形

```
def function_name(
		parm1, parm2, parm3
	        parm4, ...):
	pass
```

- 使用反斜杠\换行，二元运算符 + . 等应出现在行末；长字符串也可以用此法换行

```
print ('Hello, '\
	'my baby.')
```

- 禁止复合语句，即一行中包含多个语句：

```
禁止的用法：
func1();func2();
#python也习惯是不用分号作为结尾
```

- if/for/while一定要换行：

```
if None:
	do_sth()
	
不推荐写法：
if None: do_sth()
```

## 注释
### 块注释
- “#”号后空一格，段落件用空行分开（同样需要“#”号）

```
# 块注释
#
# 块注释
```

### 行注释
- 至少使用两个空格和语句分开，注意不要使用无意义的注释

```
# 正确的写法
x = x + 1  # 边框加粗一个像素

# 不推荐写法：
x = x + 1# x加1
```

### docstring
- docstring的规范在 PEP 257 中有详细描述，其中最其本的两点：
	1. 所有的公共模块、函数、类、方法，都应该写docstring。私有方法不一定需要，但应该在def后提供一个块注释来说明。
	2. docstring的结束"""应该独占一行，除非此docstring只有一行。

```
"""content
it is a content.
"""

"""content"""
```

### 命名规范
- 应避免使用小写字母l(L)，大写字母O(o)或I(i)单独作为一个变量的名称，以区分数字1和0;
- 包和模块使用全小写命名，尽量不要使用下划线
- 类名使用CamelCase命名风格，内部类可用一个下划线开头
- 函数使用下划线分隔的小写命名
- 当参数名称和Python保留字冲突，可在最后添加一个下划线，而不是使用缩写或自造的词
- 常量使用以下划线分隔的大写命名

```
GLOBEL_VAR = 100

Class ClassName:
	
	
	def fun_name(self, parm1):
		pass
```
