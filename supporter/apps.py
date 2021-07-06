import os

from django.apps import AppConfig


class SupporterConfig(AppConfig):
    name = 'supporter'
    path_to_music = "supporter\\static\\rest_musics\\"
    path_to_video = "supporter\\static\\video\\"
    path_to_env = "Helper\\.env"
    if not os.path.exists(path_to_music):
        os.mkdir(path_to_music)
    if not os.path.exists(path_to_video):
        os.mkdir(path_to_video)
    if not os.path.exists(path_to_env):
        open(path_to_env, 'a').close()
