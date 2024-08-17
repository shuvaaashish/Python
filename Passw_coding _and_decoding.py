import random

a=input('Code or Decode?:')
a=a.lower()
c=''
if(a=='code'):
    passw=input('Enter Your Password:')   
    jpt_values='qwertyuiopasdfghjklzxcvbnm,.123456780-_!@#$%^&*()?><'
    for i in range(0,len(passw)):
        ra=''.join(random.choice(jpt_values)for _ in range(3))
        b=ord(passw[i])+3
        c=f'{c}{chr(b)}{ra}'
    arc='@#$!)(&^*'
    ag=''.join(random.choices(arc, k=4))
    print(f'Your coded Password is {ag}{c}')
elif(a=='decode'):
    e=''
    coded_p=input('Enter your coded password:')
    for i in range(4,len(coded_p),4):
        d=ord(coded_p[i])-3
        e=e+chr(d)
    print(e)
else:
    print('Instructions Unclear')


