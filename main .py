from flask import Flask ,render_template,request
app = Flask(__name__)
import pandas as pd
import random
#from bs4 import BeautifulSoup
df=pd.read_csv("data.csv")
def recommend(df,interest):
  focus=df.groupby('Category').get_group(interest)
  li=random.choice(focus['Target'].values)
  return li
@app.route("/home",methods =["GET", "POST"])
@app.route("/",methods =["GET", "POST"])
def home():
  if request.method == "POST":
    goals= request.form.get("area_of_interest")
    if goals=="0":
      return recommend(df,'Physical Fitness	')
    if goals=="2":
      return recommend(df,'Diet')
    if goals=="3":
      return recommend(df,'Pregnancy')
    if goals=="4":
      return recommend(df,'Old Age')
  return render_template("getzing/home.html")
if __name__ == "__main__":
  app.run(debug=False,host="0.0.0.0")

