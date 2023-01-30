#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
arr=['rock','paper','scessor']
scount=0
ucount=0
while True:
    choice=input("enter your choice:")
    a=random.choice(arr)
    if(a==choice):
        print("--------TIE GAME----------")
    elif(choice==arr[0] and a==arr[1]):
        print("--USER WON-- ")
        ucount=ucount+1
    elif(choice==arr[1] and a==arr[0]):
        print("--SYSTEM WON--")
        scount=scount+1
    elif(choice==arr[0] and a==arr[2]):
        print("--USER WON--  ")
        ucount=ucount+1
    elif(choice==arr[1] and a==arr[0]):
        print("--SYSTEM WON-- ")
        scount=scount+1
    elif(choice==arr[2] and a==arr[1]):
        print("--SYSTEM WON-- ")
        scount=scount+1
    elif(choice==arr[1] and a==arr[2]):
        print("--SYSTEM WON-- ")
        scount=scount+1
    if(scount==5):
        print("--SYSTEM WON--")
        break
    elif(ucount==5):
        print("-------USER WON WITH HIGHT WINS---------- ")
        break


# In[ ]:




