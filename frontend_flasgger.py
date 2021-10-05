from flask import Flask,request
import pickle
import numpy as np
import pandas as pd
#import flasgger
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)
pi = open('model.pkl','rb')
load = pickle.load(pi)

@app.route('/')
def welcome():
    return "Welcome all"

@app.route('/predict',methods=["Get"])
def predict_policy():
    
    """Please input the following parameters to see if
        policy will be renewed or not.
    ---
    parameters:  
      - name: Gender
        in: query
        type: number
        required: true
      - name: Age
        in: query
        type: number
        required: true
      - name: Region_Code
        in: query
        type: number
        required: true
      - name: Previously_Insured
        in: query
        type: number
        required: true
      - name: Vehicle_Age
        in: query
        type: number
        required: true
      - name: Vehicle_Damage
        in: query
        type: number
        required: true
      - name: Annual_Premium
        in: query
        type: number
        required: true
      - name: Policy_Sales_Channel
        in: query
        type: number
        required: true
      - name: Vintage
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    Gender = int(request.args.get("Gender"))
    Age = int(request.args.get("Age"))
    Region_Code = int(request.args.get("Region_Code"))
    Previously_Insured = int(request.args.get("Previously_Insured"))
    Vehicle_Age = int(request.args.get("Vehicle_Age"))
    Vehicle_Damage = int(request.args.get("Vehicle_Damage"))
    Annual_Premium = int(request.args.get("Annual_Premium"))
    Policy_Sales_Channel = int(request.args.get("Policy_Sales_Channel"))
    Vintage = int(request.args.get("Vintage"))
    ans = [[Gender,Age,Region_Code, Previously_Insured,Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage]]
#    print(ans)
#    Xnew = [[0,23,2,0,1,1,2344,2,33]]
#    xnew = np.asarray(Xnew)
    ans = np.asarray(ans)
    Response = load.predict(ans)
    
    return "The response is" + str(Response)

@app.route('/bulk',methods=["POST"])
def predict_bulk():
    """Please input the following parameters to see if
        policy will be renewed or not.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df = pd.read_csv(request.files.get("file"))
    predection = load.predict(df)
    return "The response for csv is" + str(list(predection))

    
if __name__ == '__main__':
    app.run()
