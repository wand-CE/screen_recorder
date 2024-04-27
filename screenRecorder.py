import os
import cv2
import keyboard
import pyautogui
import numpy as np

class ScreenRecorder:
    def __init__(self, video_name='screen', video_format='mp4'):
        self.video_name = video_name
        self.video_format = f".{video_format}"
        self.fps = 30
        self.tamanho_tela = tuple(pyautogui.size())
        self.codec = cv2.VideoWriter_fourcc(*"XVID")

    def record(self):
        self.remove_name_conflict()
        video = cv2.VideoWriter(self.return_video_path(), self.codec, self.fps, self.tamanho_tela)

        print('Gravando tela("ESC" para sair)')
        while True:
            frame = pyautogui.screenshot()
            frame = np.array(frame)

            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

            video.write(frame)

            if keyboard.is_pressed("esc"):
                break

        video.release()
        cv2.destroyAllWindows()

        print(f"Video gravado com sucesso em {self.return_video_path()}")

    def remove_name_conflict(self):
        os.makedirs('videos', exist_ok=True)

        complete_name = self.video_name + self.video_format
        index = 1
        while complete_name in os.listdir('videos'):
            print(complete_name)
            complete_name = f"{self.video_name}_{index}{self.video_format}"
            index += 1

        self.video_name = complete_name

    def return_video_path(self):
        return os.path.join(os.getcwd(), 'videos', self.video_name)
