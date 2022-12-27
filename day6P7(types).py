Python 3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> coord=(3,5)
>>> abc=(2,9)
>>> type(coord)
<class 'tuple'>
>>> type(abc)
<class 'tuple'>
>>> abc[0]
2
>>> print('x:{0[0]}; y:{0[1];abc:{1[1]},{1[1]}'.format(coord,abc))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print('x:{0[0]}; y:{0[1];abc:{1[1]},{1[1]}'.format(coord,abc))
ValueError: unmatched '{' in format spec
>>> print('x:{0[0]}; y:{0[1]};abc:{1[1]},{1[1]}'.format(coord,abc))
x:3; y:5;abc:9,9
>>> print('x:{0[0]}; y:{0[1]};abc:{1[0]},{1[1]}'.format(coord,abc))
x:3; y:5;abc:2,9
