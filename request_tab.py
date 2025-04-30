# request_tab.py
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox,
    QTextEdit, QPushButton, QHBoxLayout, QMessageBox,
    QTreeView, QSplitter, QAbstractItemView
)
from PyQt6.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt6.QtCore import Qt
from utils import get_example_by_method
import json
import requests


class RequestTab(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        font = QFont("Segoe UI", 10)

        self.url_input = QLineEdit()
        self.url_input.setPlaceholderText("https://httpbin.org/post")
        self.url_input.setFont(font)

        self.method_box = QComboBox()
        self.method_box.addItems(["GET", "POST", "PUT", "DELETE"])
        self.method_box.setFont(font)

        self.header_edit = QTextEdit()
        self.header_edit.setFont(QFont("Consolas", 10))

        self.body_edit = QTextEdit()
        self.body_edit.setFont(QFont("Consolas", 10))

        self.response_tree = QTreeView()
        self.response_tree.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.response_model = QStandardItemModel()
        self.response_tree.setModel(self.response_model)

        # 버튼
        self.send_button = QPushButton("\ud1b5\uc2e0 \ubcf4\ub0b4\uae30")
        self.example_button = QPushButton("\uc608\uc2dc \ubcf4\uae30")
        self.example_button.clicked.connect(self.load_example_data_by_method)
        self.send_button.clicked.connect(self.send_request)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.send_button)
        button_layout.addWidget(self.example_button)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("\U0001f517 URL:"))
        layout.addWidget(self.url_input)
        layout.addWidget(QLabel("Method:"))
        layout.addWidget(self.method_box)
        layout.addWidget(QLabel("Headers (JSON):"))
        layout.addWidget(self.header_edit)
        layout.addWidget(QLabel("Body (JSON):"))
        layout.addWidget(self.body_edit)
        layout.addLayout(button_layout)
        layout.addWidget(QLabel("\ud68c\uc2e0 JSON Tree:"))
        layout.addWidget(self.response_tree)

        self.setLayout(layout)

    def to_dict(self):
        return {
            "url": self.url_input.text(),
            "method": self.method_box.currentText(),
            "headers": self.header_edit.toPlainText(),
            "body": self.body_edit.toPlainText()
        }

    def from_dict(self, data):
        self.url_input.setText(data.get("url", ""))
        self.method_box.setCurrentText(data.get("method", "GET"))
        self.header_edit.setPlainText(data.get("headers", ""))
        self.body_edit.setPlainText(data.get("body", ""))

    def load_example_data_by_method(self):
        method = self.method_box.currentText()
        data = get_example_by_method(method)
        self.from_dict(data)

    def send_request(self):
        url = self.url_input.text().strip()
        method = self.method_box.currentText().strip()
        headers_str = self.header_edit.toPlainText().strip()
        body_str = self.body_edit.toPlainText().strip()

        try:
            headers = json.loads(headers_str) if headers_str else {}
        except json.JSONDecodeError:
            QMessageBox.warning(self, "헤더 오류", "헤더는 유효한 JSON 형식이어야 합니다.")
            return

        try:
            body = json.loads(body_str) if body_str else {}
        except json.JSONDecodeError:
            QMessageBox.warning(self, "본문 오류", "본문은 유효한 JSON 형식이어야 합니다.")
            return

        try:
            if method == "GET":
                response = requests.get(url, headers=headers)
            elif method == "POST":
                response = requests.post(url, headers=headers, json=body)
            elif method == "PUT":
                response = requests.put(url, headers=headers, json=body)
            elif method == "DELETE":
                response = requests.delete(url, headers=headers)
            else:
                raise ValueError("지원하지 않는 메서드입니다.")

            try:
                response_json = response.json()
                self.display_json_tree(response_json)
            except:
                self.response_model.clear()
                self.response_model.setHorizontalHeaderLabels(["응답이 JSON 형식이 아닙니다."])

        except Exception as e:
            QMessageBox.critical(self, "요청 오류", str(e))

    def display_json_tree(self, data, parent=None):
        if parent is None:
            self.response_model.clear()
            self.response_model.setHorizontalHeaderLabels(["Key", "Value"])
            parent = self.response_model.invisibleRootItem()

        if isinstance(data, dict):
            for key, value in data.items():
                key_item = QStandardItem(str(key))
                if isinstance(value, (dict, list)):
                    value_item = QStandardItem("")
                    key_item.appendRow([value_item])
                    self.display_json_tree(value, key_item)
                else:
                    value_item = QStandardItem(str(value))
                parent.appendRow([key_item, value_item])
        elif isinstance(data, list):
            for index, item in enumerate(data):
                key_item = QStandardItem(f"[{index}]")
                if isinstance(item, (dict, list)):
                    value_item = QStandardItem("")
                    key_item.appendRow([value_item])
                    self.display_json_tree(item, key_item)
                else:
                    value_item = QStandardItem(str(item))
                parent.appendRow([key_item, value_item])
