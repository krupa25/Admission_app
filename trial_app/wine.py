#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import pickle
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.metrics import accuracy_score
from django.views.decorators.csrf import csrf_protect


# In[2]:
@csrf_protect
def winePrediction(request):
    print(request.POST["wine"])
    X_test = request.POST["wine"]
    wine = load_wine()


    # In[3]:


    data = pd.DataFrame(data= np.c_[wine['data'], wine['target']],
                        columns= wine['feature_names'] + ['target'])


    # In[4]:


    X_train = data[:-20]
    X_test = data[-20:]

    y_train = X_train.target
    y_test = X_test.target

    X_train = X_train.drop('target',1)
    X_test = X_test.drop('target',1)


    # In[5]:


    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)


    # In[6]:


    y_pred = clf.predict(X_test)


    # In[7]:


    print("accuracy_score: %.2f"
        % accuracy_score(y_test, y_pred))


    # In[11]:

    pickle.dump(clf, open('/home/volv/ML_API/final_prediction.pickle', 'wb'))


    # In[ ]:



