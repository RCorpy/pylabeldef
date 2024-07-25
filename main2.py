import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget, QListWidgetItem, QPushButton
from PyQt5.QtWidgets import QAbstractItemView  # Importar QAbstractItemView

class MultiSelectExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Configurar la ventana principal
        self.setWindowTitle('Selector Múltiple en PyQt5')
        self.setGeometry(100, 100, 300, 200)

        # Crear un layout vertical
        layout = QVBoxLayout()

        # Crear un QListWidget y habilitar la selección múltiple
        self.list_widget = QListWidget()
        self.list_widget.setSelectionMode(QAbstractItemView.MultiSelection)  # Usar QAbstractItemView.MultiSelection

        # Agregar elementos a QListWidget
        items = ['Elemento 1', 'Elemento 2', 'Elemento 3', 'Elemento 4', 'Elemento 5']
        for item in items:
            list_item = QListWidgetItem(item)
            self.list_widget.addItem(list_item)

        # Crear un botón para obtener los elementos seleccionados
        btn = QPushButton('Obtener Selección')
        btn.clicked.connect(self.get_selected_items)

        # Agregar el QListWidget y el botón al layout
        layout.addWidget(self.list_widget)
        layout.addWidget(btn)

        # Establecer el layout en la ventana principal
        self.setLayout(layout)

    def get_selected_items(self):
        selected_items = self.list_widget.selectedItems()
        selected_texts = [item.text() for item in selected_items]
        print("Elementos seleccionados:", selected_texts)

# Inicializar la aplicación
app = QApplication(sys.argv)
ex = MultiSelectExample()
ex.show()
sys.exit(app.exec_())