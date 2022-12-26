def extract_vowel(s):
    temp_vowel=''
    temp_digit=''
    temp_speciapcharecters=''
    temp_consonents=''
   
    for i in s:
        #print("i=",i)
        if i in 'AEIOUaeiou ' :
            temp_vowel+=i
            #print("i:",i,"temp_vowel:",temp_vowel)
        elif  i in '123346788365':
            temp_digit+=i 
            #print("i:",i,"temp_digit:",temp_digit)
        elif  i in 'qwrtypsdfghjklzxcvbnm':   
             temp_consonents+=i
             #print("i:",i,"temp_consonents:",temp_consonents)
        
        else:
            temp_speciapcharecters+=i

            #print("i:",i,"temp_speciapcharecters:",temp_speciapcharecters)
        a=[]
        a.append(temp_vowel)
        a.append(temp_digit)
        a.append(temp_consonents)
        a.append(temp_speciapcharecters)
        
    #return temp_vowel
    #return temp_digit
    #return temp_consonents
    #return temp_speciapcharecters
inp=input()
a=extract_vowel(inp)
print("vowel:",a[0])
print("consonents:",a[1])
print("speciapcharecters:",a[3])
print("ndigit:",a[2])
