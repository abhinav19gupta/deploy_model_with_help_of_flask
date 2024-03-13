#!/usr/bin/env python
# coding: utf-8

# https://anaconda.org/anaconda/flask

# In[1]:


from flask import Flask

# Instantiate the Flask app
app = Flask(__name__)

@app.route('/') # Home directory
def hello():
    return "Hello DS C34 NLP-DL track learners. Welcome to the class of Deployment"

# If you want to run this app, you must call the run()
if __name__ == '__main__':
    app.run(debug=True)

