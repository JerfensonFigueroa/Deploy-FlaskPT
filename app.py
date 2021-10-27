from flask import Flask, request
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def home():
    return 'Deploy ML Tarea'

@app.route("/predecir", methods=['POST'])
def prediccion():
    json = request.get_json(force=True)
    xin = json['Datos']
    print(xin)
    yout = model.predict(xin)
    print(yout)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'Tiene enfermedad cardiaca: {}\n'.format(labels[y_out])
        
    return mensaje



pkl_filename = 'RandomForest2.pkl'
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)

labels = ['Si tiene enfermedad cardiaca', 'No tiene enfermedad cardiaca']


if __name__ == '__main__':
    app.run()

