from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QLabel, QPushButton

app = QApplication([])
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("BMI")
        self.setFixedSize(210, 200)

        self.weightLineEdit = QLineEdit(self)
        self.button = QPushButton("=", self)
        self.weightLabel = QLabel("Weight(kg):", self)
        self.heightLabel = QLabel("Height(cm):", self)
        self.heightLineEdit = QLineEdit(self)
        self.bmiLabel = QLabel("BMI:", self)
        self.statusLabel = QLabel("Status:", self)

        self.weightLineEdit.move(90, 50)
        self.weightLabel.move(10, 50)

        self.heightLabel.move(10, 90)
        self.heightLineEdit.move(90, 90)
        self.heightLineEdit.setFixedWidth(100)

        self.bmiLabel.move(10, 150)
        self.bmiLabel.setFixedWidth(200)
        self.statusLabel.move(10, 175)

        self.button.move(90, 125)
        self.button.setFixedHeight(20)

        self.button.clicked.connect(self.BMI)

    def BMI(self):
        try:
            self.weight = self.weightLineEdit.text()
            self.height = self.heightLineEdit.text()

            self.weight = int(self.weight)
            self.height = int(self.height)

            self.height_in_m = self.height / 100
            self.squared_height_in_m = self.height_in_m * self.height_in_m
            self.bmi_number = self.weight / self.squared_height_in_m
            self.bmi_number = round(self.bmi_number, 1)
            if self.bmi_number < 18.5:
                self.bmiLabel.setText(f"BMI: {self.bmi_number}")
                self.statusLabel.setText("Status: Underweight")
            if self.bmi_number <= 24.9:
                if self.bmi_number >= 18.5:
                    self.bmiLabel.setText(f"BMI: {self.bmi_number}")
                    self.statusLabel.setText("Status: Normal")
            if self.bmi_number >= 25:
                if self.bmi_number <= 29.9:
                    self.bmiLabel.setText(f"BMI: {self.bmi_number}")
                    self.statusLabel.setText("Status: Overweight")
            if self.bmi_number > 29.9:
                if self.bmi_number <= 34.9:
                    self.bmiLabel.setText(f"BMI: {self.bmi_number}")
                    self.statusLabel.setText("Status: Obese")
            if self.bmi_number > 35:
                if self.bmi_number <= 39.9:
                    self.bmiLabel.setText(f"BMI: {self.bmi_number}")
                    self.statusLabel.setText("Status: Morbid Obese")
            if self.bmi_number >= 40:
                self.bmiLabel.setText(f"BMI: {self.bmi_number}")
                self.statusLabel.setText("Status: Super Obese")
        except ValueError:
            self.bmiLabel.setText("BMI: We Need Proper Input!!!")

        self.show()

    

window = MainWindow()
window.show()
app.exec_()