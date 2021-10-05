from flask import Flask,request
import pickle
import numpy as np

app = Flask(__name__)
pi = open('model.pkl','rb')
load = pickle.load(pi)

@app.route('/')
def welcome():
    return "Welcome all"

@app.route('/predict')
def predict_policy():
    Gender = request.args.get("Gender")
    Age = request.args.get("Age")
    Region_Code = request.args.get("Region_Code")
    Previously_Insured = request.args.get("Previously_Insured")
    Vehicle_Age = request.args.get("Vehicle_Age")
    Vehicle_Damage = request.args.get("Vehicle_Damage")
    Annual_Premium = request.args.get("Annual_Premium")
    Policy_Sales_Channel = request.args.get("Policy_Sales_Channel")
    Vintage = request.args.get("Vintage")
    ans = [[Gender,Age,Region_Code,
                               Previously_Insured,Vehicle_Age,
                               Vehicle_Damage,Annual_Premium,
                               Policy_Sales_Channel,Vintage]]
    Xnew = [[0,23,2,0,1,1,2344,2,33]]
    xnew = np.asarray(Xnew)
    ans = np.asarray(ans)
    Response = load.predict(xnew)
    
    return "The response is" + str(Response)

@app.route('/bulk',method=["POST])
def predict_bulk():
    df = pd.read_csv(r'test.csv')
    predection = load.predict(df)
    return "The response for csv is" + str(list(predection))

    
if __name__ == '__main__':
    app.run()