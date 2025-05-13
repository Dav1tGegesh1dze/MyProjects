import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QFormLayout
)
from PyQt5.QtGui import QPainter, QPolygon, QPen
from PyQt5.QtCore import Qt, QPoint


class TrapezoidWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 400)

        # Default Values of trapezoid sizes
        self.base1 = 200
        self.base2 = 100
        self.height = 100
        self.side = 80

        self.area_label = QLabel("Area: ")
        self.perimeter_label = QLabel("Perimeter: ")

        # Input size of sides
        self.base1_input = QLineEdit(str(self.base1))
        self.base2_input = QLineEdit(str(self.base2))
        self.height_input = QLineEdit(str(self.height))
        self.side_input = QLineEdit(str(self.side))

        self.init_ui()

    def init_ui(self):
        # Buttons
        area_button = QPushButton("Calculate Area")
        perimeter_button = QPushButton("Calculate Perimeter")


        area_button.clicked.connect(self.calculate_area)
        perimeter_button.clicked.connect(self.calculate_perimeter)

        # Input layout
        form_layout = QFormLayout()
        form_layout.addRow("Base 1 (bottom):", self.base1_input)
        form_layout.addRow("Base 2 (top):", self.base2_input)
        form_layout.addRow("Side length:", self.side_input)
        form_layout.addRow("Height:", self.height_input)

        #Buttons
        button_layout = QHBoxLayout()
        button_layout.addWidget(area_button)
        button_layout.addWidget(perimeter_button)

        #Texts
        label_layout = QVBoxLayout()
        label_layout.addWidget(self.area_label)
        label_layout.addWidget(self.perimeter_label)

        layout = QVBoxLayout()
        layout.addLayout(form_layout)
        layout.addLayout(button_layout)
        layout.addLayout(label_layout)
        layout.addStretch()

        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2))


        base1 = self.base1
        base2 = self.base2
        height = self.height

        top_y = 200
        bottom_y = top_y + height
        left_x = 100
        right_x = left_x + base1

        top_left_x = left_x + (base1 - base2) // 2
        top_right_x = top_left_x + base2

        points = QPolygon([
            QPoint(top_left_x, top_y),
            QPoint(top_right_x, top_y),
            QPoint(right_x, bottom_y),
            QPoint(left_x, bottom_y)
        ])
        painter.drawPolygon(points)

    def update_values(self):
        try:
            self.base1 = int(self.base1_input.text())
            self.base2 = int(self.base2_input.text())
            self.side = int(self.side_input.text())
            self.height = int(self.height_input.text())
        except ValueError:
            self.area_label.setText("Area: Incorrect input")
            self.perimeter_label.setText("Perimeter: Incorrect input")
            return False
        return True

    def calculate_area(self):
        if self.update_values():
            area = 0.5 * (self.base1 + self.base2) * self.height
            self.area_label.setText(f"Area: {area}")
            self.update()

    def calculate_perimeter(self):
        if self.update_values():
            perimeter = self.base1 + self.base2 + 2 * self.side
            self.perimeter_label.setText(f"Perimeter: {perimeter}")
            self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TrapezoidWidget()
    window.setWindowTitle("Trapezoid Calculator")
    window.show()
    sys.exit(app.exec_())
