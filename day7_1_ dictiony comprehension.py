string='''
practice problemes
forp list com pre he nsm in python
'''
words=string.split(' ')
print(words)
words={i.strip('\n')  for i in words  }
print(words)
ans={i:len(i) for i in words}
print(ans)
