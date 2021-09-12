#!/usr/bin/env python
# coding: utf-8

# In[37]:


import warnings
warnings.simplefilter('ignore')


# In[38]:


from flask import Flask, request, render_template
import pickle


# In[39]:


app = Flask(__name__)


# In[40]:


model = pickle.load(open('Model pkl','rb'))


# In[41]:


@app.route('/')
def home():
    return render_template('https://raw.githubusercontent.com/ingledarshan/AIML-B2/main/templates/index.html')


# In[42]:


@app.route('/predict',methods=['POST'])

def predict():
    int_features = [ int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = round(prediction[0],2)
    
    return render_template('https://raw.githubusercontent.com/ingledarshan/AIML-B2/main/templates/index.html',prediction_text='Employee salary should be {}'.format(output))


# In[43]:


if __name__ == '__main__':
    app.run(debug=True)

