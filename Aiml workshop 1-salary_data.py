#!/usr/bin/env python
# coding: utf-8

# In[27]:


#Importing the dataset:

import numpy as np
import pandas as pd
d=pd.read_csv("Salary_Data.csv")
print(d)


# In[46]:


#Visualize the dataset:

import matplotlib.pyplot as plt
plt.scatter(d.YearsExperience,d.Salary,marker='.')
plt.xlabel("YearsExperience")
plt.ylabel("Salary")
plt.show()


# In[29]:


#x :- Independent variiable
#y :- Dependent Variable

x=d.iloc[:,:-1].values
y=d.iloc[:,1:].values
x


# In[30]:


y


# In[31]:


train_x=np.array(d[["YearsExperience"]])
train_y=np.array(d[["Salary"]])
print(train_x)


# In[32]:


#Splitting the dataset into Train & Test Dataset:

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=0)


# In[33]:


x_train


# In[34]:


y_train


# In[35]:


#Training the Model:

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x_train,y_train)


# In[36]:


#Testing the Model:

y_pred=model.predict(x_test)


# In[39]:


#Evaluating the Model
#Train set results 

plt.scatter(x_train,y_train,color='red')
plt.plot(x_train,model.predict(x_train),color='black')
plt.title('Salary vs YearsExperience (training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[48]:


#Test Set Results:

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_test, model.predict(x_test), color = 'black')
plt.title('Salary vs Experience (Testing set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[42]:


#Finding the accuracy - How Accurate the model is?

import numpy as np
print("Mean sum of squares (MSE): %.2f" % np.mean(((y_pred - y_test)** 2)**0.5))


# In[43]:


#New Prediction:

years_exp=float(input("Enter Years Of Experience:"))
sal=model.predict([[years_exp]])
print(sal)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




