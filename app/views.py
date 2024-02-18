import os
import joblib
from django.shortcuts import render, redirect

try:
   model = os.path.join(os.path.dirname(__file__), 'model/model.joblib')
except FileNotFoundError as err:
   pass

def index(request):
    return render(request, 'template/index.html')

def predict(request):
    if request.method == 'POST':
       text = request.POST['text']
       
       if text.strip() != '':
          with open(model, 'rb') as model_algorithm:
            algorithm = joblib.load(model_algorithm)
            
            prediction = algorithm.best_estimator_.predict([text])

            return render(request, 'template/result.html', {'result': prediction[0]})
       else:
          return render(request, 'template/index.html', {'error': '* Please fill out this field.'})
    return redirect('/')