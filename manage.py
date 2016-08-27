#!/usr/bin/env python
from __future__ import print_function
import os

from flask_script import Manager
from flask_migrate import MigrateCommand, Migrate

from server.apps import create_app
from server.models import db


base_dir = os.path.dirname(os.path.realpath(__file__))
config_file = os.path.join(base_dir, 'config.py')

application = create_app(default_config=config_file)
Migrate(application, db)
manager = Manager(application)


def manage_app(app, app_manager):
    app_manager.init_app(app)


@manager.command
def runserver(port=5000, host='0.0.0.0', init=False):
    port = int(port)
    application.run(host=host, port=port)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
