from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

app = QApplication([])
window = QWidget()

layout = QVBoxLayout()
layout.addWidget(QPushButton("One"))
layout.addWidget(QPushButton("Two"))
layout.addWidget(QPushButton("Three"))
layout.addWidget(QPushButton("Four"))
layout.addWidget(QPushButton("Five"))

window.setLayout(layout)
window.show()
app.exec_()