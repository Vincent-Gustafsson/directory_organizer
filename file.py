import shutil
import time
import os

directory = 'C:/Users/Vincent/Downloads'

image_extensions = ('.png', '.jpg', '.gif')
video_extensions = ('.mp4', '.mov', '.avi')
exe_zip_extensions = ('.exe', '.rar', '.zip')
audio_extensions = ('.wav', '.mp3', '.ogg', '.flac')

dir_names = ['videos', 'audio', 'exe_zip', 'images', 'other']

def create_directories(dir, dir_names):
    for dir_name in dir_names:
        if dir_name not in os.listdir(dir):
            os.mkdir(dir + '/' + dir_name)


def downloads_organizer(dir):
    for file in os.listdir(dir):
        if os.path.isfile(directory + '/' + file):
            src_path = dir + '/' + file

            if file.endswith(image_extensions):
                dest_path =  dir + '/images/' + file
                shutil.move(src_path, dest_path)
            
            elif file.endswith(video_extensions):
                dest_path =  dir + '/videos/' + file
                shutil.move(src_path, dest_path)
            
            elif file.endswith(exe_zip_extensions):
                dest_path =  dir + '/exe_zip/' + file
                shutil.move(src_path, dest_path)

            elif file.endswith(audio_extensions):
                dest_path =  dir + '/audio/' + file
                shutil.move(src_path, dest_path)

            else:
                dest_path =  dir + '/other/' + file
                shutil.move(src_path, dest_path)


if __name__ == "__main__":
    try:
        create_directories(directory, dir_names)
        while True:
            downloads_organizer(directory)
            time.sleep(10)

    except KeyboardInterrupt:
        print('interrupted!')