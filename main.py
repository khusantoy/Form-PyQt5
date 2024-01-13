from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QPushButton,
    QSpinBox,
    QRadioButton,
    QComboBox,
    QFormLayout,
    QLabel,
    QHBoxLayout,
    QVBoxLayout
)

class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("So'rovnoma")
        self.setFixedSize(400, 450)
        self.setStyleSheet("""
            font-family: Arial;
            font-size: 18px;
        """)

        self.input_name = QLineEdit(self)
        self.input_name.setFixedHeight(40)
        self.input_name.setPlaceholderText("Ismni kiriting")

        self.input_surname = QLineEdit(self)
        self.input_surname.setFixedHeight(40)
        self.input_surname.setPlaceholderText("Familiyani kiriting")

        self.spinbox_age = QSpinBox(self)
        self.spinbox_age.setMinimum(15)  #min age
        self.spinbox_age.setMaximum(50)  #max age
        self.spinbox_age.setFixedHeight(40)

        self.radio_male = QRadioButton('Erkak', self)
        self.radio_female = QRadioButton('Ayol', self)

        self.combobox_cities = QComboBox(self)
        self.combobox_cities.addItems(['Toshkent shahri', 'Andijon', 'Buxoro', "Farg'ona", 'Jizzax', 'Namangan', 'Navoiy', 'Qashqadaryo', 'Samarqand', 'Sirdaryo', 'Surxondaroy', 'Toshkent viloyati', 'Xorazm', "Qoraqalpog'iston"])
        self.combobox_cities.setFixedHeight(40)


        self.input_number = QLineEdit(self)
        self.input_number.setFixedHeight(40)
        self.input_number.setPlaceholderText("Telefon raqamni kiriting")
        self.input_faculty = QLineEdit(self)
        self.input_faculty.setFixedHeight(40)
        self.input_faculty.setPlaceholderText("Fakultetni kiriting")

        self.combobox_class = QComboBox(self)
        self.combobox_class.addItems(['1', '2', '3', '4'])
        self.combobox_class.setFixedHeight(40)

        self.btn_save = QPushButton(self)
        self.btn_save.setText("Ma'lumotlarni saqlash")
        self.btn_save.setFixedHeight(40)
        self.btn_save.setStyleSheet("""
            QPushButton {
                border: 2px solid #084298;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #0D6EFD;
                color: #FFF;
            }
        """)

        layout = QFormLayout()
        layout.addRow("Ism:", self.input_name)
        layout.addRow("Familiya:", self.input_surname)
        layout.addRow("Yosh:", self.spinbox_age)
        layout.addRow("Jinsi:", self.radio_male)
        layout.addRow("", self.radio_female)
        layout.addRow("Manzil:", self.combobox_cities)
        layout.addRow("Telefon raqam:\n(99...)", self.input_number)
        layout.addRow("Fakultet", self.input_faculty)
        layout.addRow("Kurs:", self.combobox_class)
        layout.addRow(self.btn_save)

        self.setLayout(layout)

        self.show()

        self.btn_save.clicked.connect(self.save)

    def save(self):
        name = self.input_name.text()
        surname = self.input_surname.text()
        age = self.spinbox_age.value()
        radio = 'Erkak' if self.radio_male.isChecked() else 'Ayol'
        region = self.combobox_cities.currentText()
        number = self.input_number.text()
        faculty = self.input_faculty.text()
        level = self.combobox_class.currentText()

        if name and surname and age and radio and region and number and faculty and level and number.isdigit():
            file_name = f"{name}_{surname}.txt"
            with open(file_name, 'w') as file:
                file.write(f'Ism: {name}\nFamiliya: {surname}\nYosh: {age}\nJins: {radio}\nManzil: {region}\nTelefon raqam: {number}\nFakultet: {faculty}\nKurs: {level}')
            self.close()
        else:
            self.win = ErrorWindow()


class ErrorWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Ogohlantirish!")
        self.setFixedSize(350, 100)
        self.setStyleSheet("""
            font-family: Arial;
            font-size: 18px;
            font-weight: bold;
            color: #FFF;
            background-color: #DC3545;
        """)

        self.error = QLabel(self)
        self.error.setText("⚠️ Xatolik")
        self.error.setAlignment(Qt.AlignCenter)

        self.h_box = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.h_box.addWidget(self.error)
        self.v_box.addLayout(self.h_box)

        self.setLayout(self.v_box)

        self.show()

app = QApplication([])
win = Window()
app.exec_()