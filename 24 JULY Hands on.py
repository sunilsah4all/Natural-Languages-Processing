#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Task 1 - Lexicons
#1. Stopwords:
from nltk.corpus import stopwords
stopwords.words('english')


# In[2]:


#2 CMU Wordlist
import nltk
entries=nltk.corpus.cmudict.entries()
len(entries)


# In[5]:


print(entries[:50])


# In[6]:


#3 Wordnet
from nltk.corpus import wordnet as wn
wn.synsets('motorcar')


# In[8]:


wn.synset('car.n.01').lemma_names()


# In[9]:


wn.synsets('good')


# In[11]:


wn.synset('dependable.s.04').lemma_names()


# In[12]:


#Task 2: STEMMING
import nltk
from nltk.stem import PorterStemmer
stemmerporter=PorterStemmer()
stemmerporter.stem('happiness')


# In[15]:


import nltk
from nltk.stem import LancasterStemmer
stemmerlan=LancasterStemmer()
stemmerlan.stem('happiness')


# In[17]:


#Regexp
from nltk.stem import RegexpStemmer
stemmerregexp=RegexpStemmer('ing')
stemmerregexp.stem('singing')


# In[18]:


import nltk
from nltk.stem import SnowballStemmer
SnowballStemmer.languages
frenchstemmer=SnowballStemmer('french')
frenchstemmer.stem('manges')


# In[2]:


from nltk.stem import PorterStemmer
stemmer=PorterStemmer()
texteg="He loves programming but he often asks me - is programming and coding same?"
texteg=[stemmer.stem(token) for token in texteg.split(" ")]
print(" ".join(texteg))


# In[ ]:




