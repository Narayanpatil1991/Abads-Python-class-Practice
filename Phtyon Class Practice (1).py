#!/usr/bin/env python
# coding: utf-8

# In[21]:


def Feedback(x):
    if x > 0 and x <= 2:
        print("feedback is not good")
        
    elif x ==3:
        
            print("feedback is good")
     
            
    elif x > 3 and x <= 4:
        print("feedback is very good")
        
    elif x > 4 and x <= 5:
        print("feedback is Excellent")
        
    else:
        print("score greater than 5")

num = int(input("enter no: "))
Feedback(num)


# In[ ]:





# #### 
