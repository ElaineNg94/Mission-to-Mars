#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, redirect, url_for
from flask_pymongo import PyMongo
import scraping


# In[ ]:


app = Flask(__name__)


# In[ ]:


# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)


# In[ ]:


# define route for the HTML page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)


# In[ ]:


# add next route to our code
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update({}, mars_data, upsert=True)
   return redirect('/', code=302)


# In[ ]:


# use this to update our database (10.5.1)
# .update(query_parameter, data, options)
# mars.update({}, mars_data, upsert=True)


# In[ ]:


# tell Flask to run
if __name__ == "__main__":
   app.run()


# In[ ]:





# In[ ]:





# In[ ]:




