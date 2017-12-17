import os

from crudlfap.management.commands.dev import Command, CommandThread

Command.threads.append(
    CommandThread(
        name='npm-watch',
        cmd='npm start -- --watch',
        cwd=os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..')
        )
    )
)
