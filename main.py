from sanic import Sanic, response
from sanic.exceptions import NotFound
from ML_model import predict_col11, train_col11

app = Sanic(__name__)


train_col11()

@app.post('/api/predict')
async def predict_stress(req):
  values = req.json
  if len(values) < 8:
    return response.json({"status": "error", "massage": "All fields must be answered! "}, status=400)
  print("request values: ", values)
  prediction = predict_col11(values['age'], values['gender'], values['Specialization'], values['workHours'], values['patientPerDay'], values['overtimeWorkInterest'], values['overtimeWorkPaid'], values['sector'])
  print('prediction says:', prediction)
  return response.json({"status": "success", "massage": prediction}, status=200) 


app.static('/', './dist')

@app.exception(NotFound)
async def ignore_404s(req, err):

  return await response.file('./dist/index.html')

if __name__ == "__main__":
  app.run(port=8000)