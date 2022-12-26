def removeVowels(s):
    s1=''
    for i in s:
        if i not in 'AEIOUaeiou':
            s1+=i
    return s1
inp=input()
a=removeVowels(inp)
print("string",inp,"without vowel is",a)
