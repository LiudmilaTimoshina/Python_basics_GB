#1 Написать скрипт, создающий стартер (заготовку) для проекта

import os.path

project_path = 'my_project'
paths = ['settings', 'mainapp', 'adminapp', 'authapp']

for d in paths:
    os.makedirs(os.path.join(os.curdir, project_path, d), exist_ok=True)
