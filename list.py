Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var= '1'
>>> new_var=int(var)+1
>>> print new_var
2
>>> var= 'abc'
>>> var=1
>>> page_num=1
>>> print "第", page_num, "页"
第 1 页
>>> print type(page_num)
<type 'int'>
>>> print "第" + page_num + "页"

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print "第" + page_num + "页"
TypeError: cannot concatenate 'str' and 'int' objects
>>> print "第" + str(page_num) + "页"
第1页
>>> import random
>>> random.Random()
<random.Random object at 0x0000000002F01C58>
>>> random.choice("['a', 'b', 'c']")
'b'
>>> random.choice("['a', 'b', 'c']")
' '
>>>  random.choice("['a', 'b', 'c']")
 
  File "<pyshell#14>", line 2
    random.choice("['a', 'b', 'c']")
    ^
IndentationError: unexpected indent
>>> random.choice("['a', 'b', 'c']")
"'"
>>> random.choice(['a', 'b', 'c'])
'a'
>>> list1 = ['physics', 'chemistry', 1997, 2000];
>>> list1[0]
'physics'
>>> list1[0:1]
['physics']
>>> list1[0:2]
['physics', 'chemistry']
>>> list2 = [1, 2, 3, 4, 5 ];
>>> list1 * list2

Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    list1 * list2
TypeError: can't multiply sequence by non-int of type 'list'
>>> list2 = [1, 2, 3, 4, 5 ];
>>> list1 + list2
['physics', 'chemistry', 1997, 2000, 1, 2, 3, 4, 5]
>>> list1 * 2
['physics', 'chemistry', 1997, 2000, 'physics', 'chemistry', 1997, 2000]
>>> list1 = [2,3]
>>> list1 * 2
[2, 3, 2, 3]
>>> if 3 in [1, 2, 3]:
	print "OK"

	
OK
>>> 
