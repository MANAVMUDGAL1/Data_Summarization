
from flask import Flask , render_template, url_for, request
import requests


app=Flask(__name__)
@app.route('/',methods=['GET','POST'])


def index():
    return render_template('index.html')

@app.route("/Summarize",methods=["GET","POST"])    
def Summarize():
    if request.method =="POST":
        API_URL = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        headers = {"Authorization": "Bearer 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"}
    
        data=request.form["data"]

        maxL=int(request.form["maxL"])
        minL=maxL//4
        

        def query(payload):

          response = requests.post(API_URL, headers=headers, json=payload)
          # print(response.status_code)
          # print(response.text)
          return response.json()
        
        
        output = query({
        "inputs": data,
        "parameters":{"min_length":minL,"max_length":maxL},
        })[0]



        return render_template('index.html',result=output["summary_text"])
    
    else:
        return render_template('index.html')
from flask import Flask , render_template, url_for, request
import requests

if __name__ == '__main__':
    app.run(debug=True)