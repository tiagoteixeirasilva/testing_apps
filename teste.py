#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Imports
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
from scipy.cluster.hierarchy import linkage, fcluster
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
import pandas_profiling
from pandas_profiling import ProfileReport
import streamlit as st


# In[2]:


st.write("""
# My first app
Hello *world!*
""")


# In[ ]:




