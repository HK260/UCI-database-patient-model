#!/usr/bin/env python
# coding: utf-8

# In[1]:


import joblib

def load_model():
    return joblib.load('best_random_forest_model.pkl')  # Adjust the path to your model file if necessary

