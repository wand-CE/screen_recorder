from screenRecorder import ScreenRecorder


if __name__ == '__main__':
    video_name = input('Digite o nome do Video a ser gravado:') or 'screen'
    video_format = input('Digite o nome do formato a ser gravado:') or 'mp4'
    screenRecorder = ScreenRecorder(video_name, video_format)
    screenRecorder.record()
