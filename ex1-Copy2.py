#!/usr/bin/env python
# coding: utf-8

# In[1]:


#farenheit to celcius
f=float(input("enter the temp in farenhite"))
c=(f-32)*5/9
print("temp in celcius",c,"C")


# In[4]:


#area and circumference of the circle
r=float(input("enter the radius"))
pi=3.14
area=pi*r*r
cir=2*pi*r
print("area of the circle is::",area,"\n circumference of circle is::",cir)


# In[6]:


#average of the three number
x=int(input("eneter the first number"))
y=int(input("enter the second number"))
z=int(input("enter the third number"))
avg=(x+y+z)/3
print("average of the number",avg)


# In[7]:


#simple interst and maturity amount
p=int(input("enter the prinicple amount"))
r=int(input("enter the rate"))
t=int(input("enter the time"))
si=(p*r*t)/100
print("simple interst",si)
m=si+p
print("maturity amount",m)


# In[9]:


#area of the triangle
a=float(input("eneter the 1st value "))
b=float(input("enter the 2nd value"))
c=float(input("enter the 3rd value"))
s=((a+b+c)/2)
area=((s*(s-a)*(s-b)*(s-c))**0.5)
print("area of the tringle",area)


# In[1]:


#km/h to m/s
x=float(input("enter number in km/h"))
y=x*0.278
print("velocity is::",y)


# In[2]:


#velocity
u=float(input("enter the intail velocity"))
a=float(input("enter the acceleration"))
t=float(input("enter the time"))
v=u+(a*t)
print("final velocity",v)


# In[3]:


#seconds in year
age=int(input("enter the age"))
seconds=age*31536000
print("you are",seconds,"seconds old.")


# In[7]:


#odd even program
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))


# In[ ]:





# In[ ]:





# In[ ]:




