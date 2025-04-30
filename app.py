# app.py
import os
import sys
import time
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTabWidget, QFileDialog, QMenuBar, QSplashScreen
)
from PyQt6.QtGui import QIcon, QAction, QPixmap
from request_tab import RequestTab
from utils import save_request_to_file, load_request_from_file

class HttpTesterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zapi - Lightning-fast API Tester")
        self.setMinimumSize(900, 700)

        # 아이콘 경로 처리
        if hasattr(sys, "_MEIPASS"):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.dirname(__file__)

        icon_path = os.path.join(base_path, "icon", "zapi_icon.ico")
        self.setWindowIcon(QIcon(icon_path))

        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        self.init_menu()
        self.new_tab()

    def init_menu(self):
        menubar = self.menuBar()
        file_menu = menubar.addMenu("파일")

        save_action = QAction("요청 저장", self)
        save_action.triggered.connect(self.save_request)
        file_menu.addAction(save_action)

        load_action = QAction("요청 불러오기", self)
        load_action.triggered.connect(self.load_request)
        file_menu.addAction(load_action)

        new_tab_action = QAction("새 요청 탭", self)
        new_tab_action.triggered.connect(self.new_tab)
        file_menu.addAction(new_tab_action)

    def new_tab(self):
        tab = RequestTab()
        index = self.tabs.addTab(tab, "📝 요청")
        self.tabs.setCurrentIndex(index)

    def save_request(self):
        current_tab = self.tabs.currentWidget()
        if not isinstance(current_tab, RequestTab):
            return

        data = current_tab.to_dict()
        path, _ = QFileDialog.getSaveFileName(self, "요청 저장", "", "요청 파일 (*.req.json)")
        if path:
            if not path.endswith(".req.json"):
                path += ".req.json"
            save_request_to_file(data, path)

    def load_request(self):
        path, _ = QFileDialog.getOpenFileName(self, "요청 불러오기", "", "요청 파일 (*.req.json)")
        if path:
            try:
                data = load_request_from_file(path)
                current_tab = self.tabs.currentWidget()
                if isinstance(current_tab, RequestTab):
                    current_tab.from_dict(data)
            except Exception as e:
                print(f"불러오기 실패: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if hasattr(sys, "_MEIPASS"):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(__file__)

    icon_path = os.path.join(base_path, "icon", "zapi_icon.ico")
    splash_path = os.path.join(base_path, "icon", "splash_dark_small.png")

    app.setWindowIcon(QIcon(icon_path))

    splash_pix = QPixmap(splash_path)
    splash = QSplashScreen(splash_pix)
    splash.show()
    app.processEvents()
    time.sleep(1.5)

    window = HttpTesterApp()
    splash.finish(window)
    window.show()

    sys.exit(app.exec())
