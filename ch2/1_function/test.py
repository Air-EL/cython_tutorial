import demo

print(demo.foo("3.14159"))  # 答案约等于0

# 按照上面的输入 "3.14159" 会有以下报错
"""
Traceback (most recent call last):
  File "e:\Cython\test.py", line 3, in <module>
    print(demo.foo("3.1415"))  # 答案约等于0
  File "demo.pyx", line 5, in demo.foo
    def foo(char *s):
TypeError: expected bytes, str found
"""
# 改为下面的输入 b"3.14159" ，以字节序列的形式（二进制形式）来输入
# print(demo.foo(b"3.14159"))  # 答案约等于0
# 输出 9.265358966049026e-05
