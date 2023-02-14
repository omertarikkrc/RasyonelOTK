import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout, QWidget
from PyQt5.QtGui import QTextCursor

class ChatWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a text edit widget for displaying the chat messages
        self.sohbet = QTextEdit(self)
        self.sohbet.setReadOnly(True)

        # Create a line edit widget for entering new messages
        self.kullanici_input = QLineEdit(self)

        # Create a label for displaying the status
        #self.status_label = QLabel(self)

        # Create a vertical layout for the chat messages
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.sohbet)
        v_layout.addWidget(self.kullanici_input)
        #v_layout.addWidget(self.status_label)

        # Create a horizontal layout for the window
        h_layout = QHBoxLayout()
        h_layout.addLayout(v_layout)

        # Create a central widget to hold the layouts
        central_widget = QWidget(self)
        central_widget.setLayout(h_layout)
        self.setCentralWidget(central_widget)

        # Connect the returnPressed signal of the line edit widget to the sendMessage method
        #self.kullanici_input.returnPressed.connect(self.sendMessage)
        self.instanttext = self.kullanici_input.text()

        # Set the window title
        self.setWindowTitle("Abee Chat")
        self.show()
        self.temp_text = ""


    """def sendMessage(self):
        # Get the text from the line edit widget
        text = self.kullanici_input.text()

        # Append the text to the text edit widget
        self.sohbet.append(text)

        # Clear the line edit widget
        self.kullanici_input.clear()

        # Move the cursor to the end of the text edit widget
        cursor = self.sohbet.textCursor()
        cursor.movePosition(QTextCursor.End)
        self.sohbet.setTextCursor(cursor)
"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_window = ChatWindow()
    sys.exit(app.exec_())
