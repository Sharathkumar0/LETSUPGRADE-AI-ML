#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask

app = Flask(__name__)

@app.route('/')

def home():
    return 'Hi sharath kumar, How are you?'
if __name__ == '__main__':
    app.run(debug=True)

