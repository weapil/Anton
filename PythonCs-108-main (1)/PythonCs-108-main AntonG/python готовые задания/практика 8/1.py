import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QLabel, QSlider, QVBoxLayout, QWidget, QMessageBox
)
from PyQt5.QtCore import Qt, QTimer

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Минималистичный видеоплеер')
        self.setGeometry(100, 100, 800, 600)
        self.video_capture = None
        self.timer = QTimer()
        self.is_playing = False
        self.video_length = 0
        self.label = QLabel('Выберите видеофайл', self)
        self.play_button = QPushButton('Играть/Пауза', self)
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setMinimum(0)
        self.slider.setValue(0)
        self.slider.setTracking(True)
        self.slider.valueChanged.connect(self.set_video_position)
        self.play_button.clicked.connect(self.toggle_play)
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.slider)
        layout.addWidget(self.play_button)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.select_video_file()
        self.timer.timeout.connect(self.update_frame)

    def select_video_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Выберите видеофайл", "", "Video Files (*.mp4 *.avi *.mov);;All Files (*)", options=options)
        if file_name:
            self.label.setText(file_name)
            self.video_capture = cv2.VideoCapture(file_name)
            self.video_length = int(self.video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
            self.slider.setMaximum(self.video_length)

    def toggle_play(self):
        if self.video_capture is not None:
            if self.is_playing:
                self.timer.stop()
            else:
                self.timer.start(30)  # Обновление 30 мс
            self.is_playing = not self.is_playing

    def update_frame(self):
        if self.video_capture is not None and self.is_playing:
            ret, frame = self.video_capture.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = np.array(frame)
                frame = frame[:, :, ::-1]
                h, w, ch = frame.shape
                bytes_per_line = ch * w
                q_img = QImage(frame.data, w, h, bytes_per_line, QImage.Format_RGB888)
                QPixmap.fromImage(q_img)
                current_frame = int(self.video_capture.get(cv2.CAP_PROP_POS_FRAMES))
                self.slider.setValue(current_frame)
            else:
                self.timer.stop()
                self.is_playing = False
    def set_video_position(self, position):
        if self.video_capture is not None:
            self.video_capture.set(cv2.CAP_PROP_POS_FRAMES, position)
    def closeEvent(self, event):
        if self.video_capture is not None:
            self.video_capture.release()
        event.accept()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    player = VideoPlayer()
    player.show()
    sys.exit(app.exec_())
