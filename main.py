import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import MinMaxScaler
from PyQt6 import QtCore, QtGui, QtWidgets
from resultado import Ui_CuadroResultado

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

class Ui_CuadroMain(object):
    def setupUi(self, CuadroMain):
        CuadroMain.setObjectName("CuadroMain")
        CuadroMain.resize(593, 272)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icono.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        CuadroMain.setWindowIcon(icon)
        CuadroMain.setStyleSheet("background-color: rgb(57, 178, 255);")
        self.widget = QtWidgets.QWidget(parent=CuadroMain)
        self.widget.setGeometry(QtCore.QRect(10, 10, 571, 251))
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget.setObjectName("widget")

        # Inicializar los widgets de la interfaz
        self.initUI()

        self.retranslateUi(CuadroMain)
        QtCore.QMetaObject.connectSlotsByName(CuadroMain)

    def initUI(self):
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 571, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.label_2.setObjectName("label_2")
        self.lineEditAnos = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditAnos.setGeometry(QtCore.QRect(150, 30, 113, 22))
        self.lineEditAnos.setObjectName("lineEditAnos")
        self.comboBoxGenero = QtWidgets.QComboBox(parent=self.widget)
        self.comboBoxGenero.setGeometry(QtCore.QRect(150, 60, 111, 22))
        self.comboBoxGenero.setObjectName("comboBoxGenero")
        self.comboBoxGenero.addItem("")
        self.comboBoxGenero.addItem("")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 131, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditAltura = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditAltura.setGeometry(QtCore.QRect(150, 90, 113, 22))
        self.lineEditAltura.setObjectName("lineEditAltura")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(10, 120, 131, 16))
        self.label_5.setObjectName("label_5")
        self.lineEditPeso = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditPeso.setGeometry(QtCore.QRect(150, 120, 113, 22))
        self.lineEditPeso.setObjectName("lineEditPeso")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 150, 131, 16))
        self.label_6.setObjectName("label_6")
        self.lineEditSistolica = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditSistolica.setGeometry(QtCore.QRect(150, 150, 113, 22))
        self.lineEditSistolica.setObjectName("lineEditSistolica")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 141, 16))
        self.label_7.setObjectName("label_7")
        self.lineEditDiastolica = QtWidgets.QLineEdit(parent=self.widget)
        self.lineEditDiastolica.setGeometry(QtCore.QRect(150, 180, 113, 22))
        self.lineEditDiastolica.setObjectName("lineEditDiastolica")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(300, 30, 111, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(300, 80, 111, 16))
        self.label_9.setObjectName("label_9")
        self.radioButtonGluNor = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButtonGluNor.setGeometry(QtCore.QRect(300, 100, 61, 20))
        self.radioButtonGluNor.setChecked(True)
        self.radioButtonGluNor.setObjectName("radioButtonGluNor")
        self.radioButtonGluAlto = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButtonGluAlto.setGeometry(QtCore.QRect(370, 100, 51, 20))
        self.radioButtonGluAlto.setObjectName("radioButtonGluAlto")
        self.radioButtonGluMAlto = QtWidgets.QRadioButton(parent=self.widget)
        self.radioButtonGluMAlto.setGeometry(QtCore.QRect(420, 100, 71, 20))
        self.radioButtonGluMAlto.setObjectName("radioButtonGluMAlto")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(300, 130, 71, 16))
        self.label_10.setObjectName("label_10")
        self.comboBoxFumador = QtWidgets.QComboBox(parent=self.widget)
        self.comboBoxFumador.setGeometry(QtCore.QRect(410, 130, 111, 22))
        self.comboBoxFumador.setObjectName("comboBoxFumador")
        self.comboBoxFumador.addItem("")
        self.comboBoxFumador.addItem("")
        self.label_11 = QtWidgets.QLabel(parent=self.widget)
        self.label_11.setGeometry(QtCore.QRect(300, 160, 95, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.widget)
        self.label_12.setGeometry(QtCore.QRect(300, 190, 101, 16))
        self.label_12.setObjectName("label_12")
        self.pushButtonLimpiar = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonLimpiar.setGeometry(QtCore.QRect(10, 220, 75, 24))
        self.pushButtonLimpiar.setObjectName("pushButtonLimpiar")
        self.pushButtonLimpiar.clicked.connect(self.limpiarCampos)
        self.pushButtonPrediccion = QtWidgets.QPushButton(parent=self.widget)
        self.pushButtonPrediccion.setGeometry(QtCore.QRect(220, 220, 111, 24))
        self.pushButtonPrediccion.setObjectName("pushButtonPrediccion")
        self.pushButtonPrediccion.clicked.connect(self.realizarPrediccion)
        self.comboBoxAlcohol = QtWidgets.QComboBox(parent=self.widget)
        self.comboBoxAlcohol.setGeometry(QtCore.QRect(410, 160, 111, 22))
        self.comboBoxAlcohol.setObjectName("comboBoxAlcohol")
        self.comboBoxAlcohol.addItem("")
        self.comboBoxAlcohol.addItem("")
        self.comboBoxEjercicio = QtWidgets.QComboBox(parent=self.widget)
        self.comboBoxEjercicio.setGeometry(QtCore.QRect(410, 190, 111, 22))
        self.comboBoxEjercicio.setObjectName("comboBoxEjercicio")
        self.comboBoxEjercicio.addItem("")
        self.comboBoxEjercicio.addItem("")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget)
        self.widget_2.setGeometry(QtCore.QRect(300, 50, 185, 21))
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButtonColNor = QtWidgets.QRadioButton(parent=self.widget_2)
        self.radioButtonColNor.setChecked(True)
        self.radioButtonColNor.setObjectName("radioButtonColNor")
        self.horizontalLayout.addWidget(self.radioButtonColNor)
        self.radioButtonColAlto = QtWidgets.QRadioButton(parent=self.widget_2)
        self.radioButtonColAlto.setObjectName("radioButtonColAlto")
        self.horizontalLayout.addWidget(self.radioButtonColAlto)
        self.radioButtonColMAlto = QtWidgets.QRadioButton(parent=self.widget_2)
        self.radioButtonColMAlto.setObjectName("radioButtonColMAlto")
        self.horizontalLayout.addWidget(self.radioButtonColMAlto)

    def retranslateUi(self, CuadroMain):
        _translate = QtCore.QCoreApplication.translate
        CuadroMain.setWindowTitle(_translate("CuadroMain", "Predicción Cardiaca"))
        self.label.setText(_translate("CuadroMain", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Predicción Cardiaca</span></p></body></html>"))
        self.label_2.setText(_translate("CuadroMain", "Años cumplidos:"))
        self.comboBoxGenero.setItemText(0, _translate("CuadroMain", "Masculino"))
        self.comboBoxGenero.setItemText(1, _translate("CuadroMain", "Femenino"))
        self.label_3.setText(_translate("CuadroMain", "Género:"))
        self.label_4.setText(_translate("CuadroMain", "Altura (cm):"))
        self.label_5.setText(_translate("CuadroMain", "Peso (kg):"))
        self.label_6.setText(_translate("CuadroMain", "Presión Sistólica:"))
        self.label_7.setText(_translate("CuadroMain", "Presión Diastólica:"))
        self.label_8.setText(_translate("CuadroMain", "Colesterol:"))
        self.label_9.setText(_translate("CuadroMain", "Glucosa:"))
        self.radioButtonGluNor.setText(_translate("CuadroMain", "Normal"))
        self.radioButtonGluAlto.setText(_translate("CuadroMain", "Alto"))
        self.radioButtonGluMAlto.setText(_translate("CuadroMain", "Muy alto"))
        self.label_10.setText(_translate("CuadroMain", "Fumador:"))
        self.comboBoxFumador.setItemText(0, _translate("CuadroMain", "No"))
        self.comboBoxFumador.setItemText(1, _translate("CuadroMain", "Sí"))
        self.label_11.setText(_translate("CuadroMain", "Consume alcohol:"))
        self.label_12.setText(_translate("CuadroMain", "Realiza ejercicio:"))
        self.pushButtonLimpiar.setText(_translate("CuadroMain", "Limpiar"))
        self.pushButtonPrediccion.setText(_translate("CuadroMain", "Predecir"))
        self.comboBoxAlcohol.setItemText(0, _translate("CuadroMain", "No"))
        self.comboBoxAlcohol.setItemText(1, _translate("CuadroMain", "Sí"))
        self.comboBoxEjercicio.setItemText(0, _translate("CuadroMain", "No"))
        self.comboBoxEjercicio.setItemText(1, _translate("CuadroMain", "Sí"))
        self.radioButtonColNor.setText(_translate("CuadroMain", "Normal"))
        self.radioButtonColAlto.setText(_translate("CuadroMain", "Alto"))
        self.radioButtonColMAlto.setText(_translate("CuadroMain", "Muy alto"))

    def realizarPrediccion(self):
        # Recopilar datos de la interfaz
        try:
            years = int(self.lineEditAnos.text()) * 365
            gender = 2 if self.comboBoxGenero.currentIndex() == 0 else 1
            height = float(self.lineEditAltura.text())
            weight = float(self.lineEditPeso.text())
            systolic_bp = int(self.lineEditSistolica.text())
            diastolic_bp = int(self.lineEditDiastolica.text())
            cholesterol = 1 if self.radioButtonColNor.isChecked() else (2 if self.radioButtonColAlto.isChecked() else 3)
            glucose = 1 if self.radioButtonGluNor.isChecked() else (2 if self.radioButtonGluAlto.isChecked() else 3)
            smoking = 0 if self.comboBoxFumador.currentIndex() == 0 else 1
            alcohol = 0 if self.comboBoxAlcohol.currentIndex() == 0 else 1
            exercise = 0 if self.comboBoxEjercicio.currentIndex() == 0 else 1

            # Calcular el índice de masa corporal (IMC)
            bmi = weight / (height / 100) ** 2

            # Crear array de características para la predicción
            features = np.array([[years, gender, height, weight, systolic_bp, diastolic_bp, cholesterol, glucose, smoking, alcohol, exercise]])

            # Escalar las características
            features_scaled = scaler.transform(features)

             # Realizar la predicción
            prediction = model.predict(features_scaled)
            prediction_text = "Alta probabilidad de enfermedad cardíaca" if prediction[0] == 1 else "Baja probabilidad de enfermedad cardíaca"

            # Mostrar el resultado en la ventana personalizada
            self.mostrarResultado(prediction_text)
        except ValueError:
            QtWidgets.QMessageBox.warning(None, "Error", "Por favor, introduzca todos los campos correctamente.")

    def mostrarResultado(self, resultado):
        self.resultadoWindow = QtWidgets.QWidget()
        self.uiResultado = Ui_CuadroResultado()
        self.uiResultado.setupUi(self.resultadoWindow)
        self.uiResultado.labelResultado.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">{resultado}</span></p></body></html>")
        self.resultadoWindow.show()

    def limpiarCampos(self):
        self.lineEditAnos.clear()
        self.lineEditAltura.clear()
        self.lineEditPeso.clear()
        self.lineEditSistolica.clear()
        self.lineEditDiastolica.clear()
        self.comboBoxGenero.setCurrentIndex(0)
        self.radioButtonColNor.setChecked(True)
        self.radioButtonGluNor.setChecked(True)
        self.comboBoxFumador.setCurrentIndex(0)
        self.comboBoxAlcohol.setCurrentIndex(0)
        self.comboBoxEjercicio.setCurrentIndex(0)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CuadroMain = QtWidgets.QMainWindow()
    ui = Ui_CuadroMain()
    ui.setupUi(CuadroMain)
    CuadroMain.show()
    sys.exit(app.exec())