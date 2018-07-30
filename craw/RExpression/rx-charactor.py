+
'+'的作用是将前面一个字符或一个子表达式重复一遍或者多遍。

.
'.'代表任何一个字符，包括它本身

*
'*'跟在其他符号后面表达可以匹配到它0次或多次
reg=r"https*://"
s可有可无

?
'?'代表懒惰匹配，非贪婪匹配（默认贪婪）
{a,b}(代表a<=匹配次数<=b)
reg="sa{1,2}b"  #匹配"sab" "saab"
import re

s = r"chuxiuhong@hit.edu.cn"
reg = r"@.+?\."		#我想匹配到@后面一直到“.”之间的，在这里是hit,否则为["@hit.edu."]
com = re.compile(reg)
rel=re.findall(com,s)
print(rel)
# ['@hit.']


[]
"[]"代表匹配里面的字符中的任意一个
[^]代表排除内部字符

import re
s = "lalala<hTml>hello</Html>heiheihei"
reg = "<[Hh][Tt][Mm][Ll]>.+?</[Hh][Tt][Mm][Ll]>"
com = re.compile(reg)
rel = re.findall(com,s)
print(rel) 
# ['<hTml>hello</Html>']


import re

s = r"mat cat hat pat"
reg = r"[^pm]at"		#这代表除了p,m以外都匹配
com = re.compile(reg)
rel=re.findall(com,s)
print(rel)
# ['cat', 'hat']

"""
正则表达式	代表的匹配字符
[0-9]	0123456789任意之一
[a-z]	小写字母任意之一
[A-Z]	大写字母任意之一
\d	等同于[0-9]
\D	等同于[^0-9]匹配非数字
\w	等同于[a-z0-9A-Z_]匹配大小写字母、数字和下划线
\W	等同于[^a-z0-9A-Z_]等同于上一条取非
"""

"""
元字符	说明
.	代表任意字符
|	逻辑或操作符
[ ]	匹配内部的任一字符或子表达式
[^]	对字符集和取非
-	定义一个区间
\	对下一字符取非（通常是普通变特殊，特殊变普通）
*	匹配前面的字符或者子表达式0次或多次
*?	惰性匹配上一个
+	匹配前一个字符或子表达式一次或多次
+?	惰性匹配上一个
?	匹配前一个字符或子表达式0次或1次重复
{n}	匹配前一个字符或子表达式
{m,n}	匹配前一个字符或子表达式至少m次至多n次
{n,}	匹配前一个字符或者子表达式至少n次
{n,}?	前一个的惰性匹配
^	匹配字符串的开头
\A	匹配字符串开头
$	匹配字符串结束
[\b]	退格字符
\c	匹配一个控制字符
\d	匹配任意数字
\D	匹配数字以外的字符
\t	匹配制表符
\w	匹配任意数字字母下划线
\W	不匹配数字字母下划线
"""