#!/usr/bin/env python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Server, Manager

from api.app import create_app, db
from api.commands import (
    GenerateApiSpecCommand, RunCallbackSpreaderProcessorCommand, RunCallbackDeliveryProcessorCommand
)
from api.conf import DevelopmentConfig

app = create_app(config_object=DevelopmentConfig())
manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command("runserver", Server())
manager.add_command('db', MigrateCommand)
manager.add_command('generate_swagger', GenerateApiSpecCommand)
manager.add_command('run_callback_spreader', RunCallbackSpreaderProcessorCommand)
manager.add_command('run_callback_delivery', RunCallbackDeliveryProcessorCommand)

if __name__ == "__main__":
    manager.run()
