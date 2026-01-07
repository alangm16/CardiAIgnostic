import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import MinMaxScaler
import tkinter as tk

# Función para limpiar los datos ingresados en los campos de entrada
def limpiar_datos():
    entry_age.delete(0, tk.END)
    entry_gender.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    entry_weight.delete(0, tk.END)
    entry_ap_hi.delete(0, tk.END)
    entry_ap_lo.delete(0, tk.END)
    entry_cholesterol.delete(0, tk.END)
    entry_gluc.delete(0, tk.END)
    entry_smoke.delete(0, tk.END)
    entry_alco.delete(0, tk.END)
    entry_active.delete(0, tk.END)

# Función para mostrar el resultado en una nueva ventana
def mostrar_resultado(resultado):
    ventana_resultado = tk.Toplevel()
    ventana_resultado.title("Resultado")
    ventana_resultado.iconbitmap('icono.ico')

    resultado_label = tk.Label(ventana_resultado, text=resultado)
    resultado_label.pack()

    cerrar_button = tk.Button(ventana_resultado, text="Cerrar", command=ventana_resultado.destroy)
    cerrar_button.pack()

# Paso 1: Cargar los datos en un DataFrame de pandas
data = pd.read_csv('cardio_train.csv')

# Paso 2: Preprocesar los datos
X = data.drop(['id', 'cardio'], axis=1)  # Excluir las columnas 'id' y 'cardio'
y = data['cardio']

scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Paso 3: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Paso 4: Crear una instancia del modelo de regresión logística y ajustarla a los datos de entrenamiento
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Crear una función para realizar la predicción y mostrar el resultado
def predecir():
    age = int(entry_age.get())
    gender = int(entry_gender.get())
    height = float(entry_height.get())
    weight = float(entry_weight.get())
    ap_hi = int(entry_ap_hi.get())
    ap_lo = int(entry_ap_lo.get())
    cholesterol = int(entry_cholesterol.get())
    gluc = int(entry_gluc.get())
    smoke = int(entry_smoke.get())
    alco = int(entry_alco.get())
    active = int(entry_active.get())

    # Escalar los datos de entrada
    input_data = scaler.transform([[age, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, alco, active]])

    # Realizar la predicción en los datos de entrada
    prediction = model.predict(input_data)

   # Mostrar el resultado de la predicción en una nueva ventana
    if prediction[0] == 1:
        resultado = "La persona presenta una enfermedad cardiaca."
    else:
        resultado = "La persona no presenta una enfermedad cardiaca."

    mostrar_resultado(resultado)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Predicción de enfermedad cardiaca")

# Establecer el ícono de la aplicación
ventana.iconbitmap('icono.ico')

# Crear los campos de entrada
label_age = tk.Label(ventana, text="Edad en días:")
label_age.pack()
entry_age = tk.Entry(ventana)
entry_age.pack()

label_gender = tk.Label(ventana, text="Género (1: mujer, 2: hombre):")
label_gender.pack()
entry_gender = tk.Entry(ventana)
entry_gender.pack()

# Agregar más campos de entrada para los demás atributos...
label_height = tk.Label(ventana, text="Ingrese la altura en cm: ")
label_height.pack()
entry_height = tk.Entry(ventana)
entry_height.pack()

label_weight = tk.Label(ventana, text="Ingrese el peso en kg: ")
label_weight.pack()
entry_weight = tk.Entry(ventana)
entry_weight.pack()

label_ap_hi = tk.Label(ventana, text="Ingrese la presión arterial sistólica: ")
label_ap_hi.pack()
entry_ap_hi = tk.Entry(ventana)
entry_ap_hi.pack()

label_ap_lo = tk.Label(ventana, text="Ingrese la presión arterial diastólica: ")
label_ap_lo.pack()
entry_ap_lo = tk.Entry(ventana)
entry_ap_lo.pack()

label_cholesterol = tk.Label(ventana, text="Ingrese el nivel de colesterol (1: normal, 2: por encima de lo normal, 3: muy por encima de lo normal): ")
label_cholesterol.pack()
entry_cholesterol = tk.Entry(ventana)
entry_cholesterol.pack()

label_gluc = tk.Label(ventana, text="Ingrese el nivel de glucosa (1: normal, 2: por encima de lo normal, 3: muy por encima de lo normal): ")
label_gluc.pack()
entry_gluc = tk.Entry(ventana)
entry_gluc.pack()

label_smoke = tk.Label(ventana, text="¿Es fumador? (0: no, 1: si): ")
label_smoke.pack()
entry_smoke = tk.Entry(ventana)
entry_smoke.pack()

label_alco = tk.Label(ventana, text="¿Consume alcohol? (0: no, 1: si): ")
label_alco.pack()
entry_alco = tk.Entry(ventana)
entry_alco.pack()

label_active = tk.Label(ventana, text="¿Realiza actividad física regularmente? (0: no, 1: si): ")
label_active.pack()
entry_active = tk.Entry(ventana)
entry_active.pack()

# Crear el botón de predicción
predict_button = tk.Button(ventana, text="Realizar predicción", command=predecir)
predict_button.pack()

# Crear la etiqueta para mostrar el resultado de la predicción
result_label = tk.Label(ventana, text="")
result_label.pack()

# Agregar botón de limpieza
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack()

ventana.mainloop()