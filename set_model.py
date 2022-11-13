#!/usr/bin/env python
import os
import sys

def create_apps(dir_path, model_name):
    file = open(dir_path + '/apps.py', 'w')
    default_context = "from django.apps import AppConfig\n"\
                      "\n"\
                     f"class {model_name.title()}Config(AppConfig):\n"\
                      "\tdefault_auto_field = 'django.db.models.BigAutoField'\n"\
                     f"\tname = 'api.models.{model_name}'\n"

    file.write(default_context)
    file.close()


def create_model(dir_path, model_name):
    file = open(dir_path + '/models.py', 'w')
    default_context = "from django.db import models\n"\
                      "from lib.common.model_frame import ModelFrame\n"\
                      "\n"\
                     f"class {model_name.title()}(ModelFrame):\n"\
                      "\tpass\n"\
                      "\n"\
                      "\tclass Meta:\n"\
                     f"\t\tdb_table = \"{model_name + 's'}\""

    file.write(default_context)
    file.close()

def main():
    model_name = sys.argv[-1]

    dir_path = os.getcwd() + '/api'

    if not os.path.isdir(dir_path):
        print('create api directory')
        os.makedirs(dir_path)

        print('create models directory')
        os.makedirs(dir_path + '/models')

    dir_path = dir_path + f"/models/{model_name}"

    if not os.path.isdir(dir_path):

        print('create migrates directory')
        os.makedirs(dir_path + '/migrations')
        open(dir_path + '/migrations/__init__.py', 'w')

        create_apps(dir_path, model_name)
        create_model(dir_path, model_name)
    else:
        print(f"already {model_name} is exist")

if __name__ == '__main__':
    main()
