# https://flask.palletsprojects.com/en/3.0.x/tutorial/database/ [REFER HERE]

import click

from flask import current_app, g


def get_db():
    print("Getting DB")


def close_db(e=None):
    print("Closing DB")


def init_db():
    db = get_db()
    print("Initializing the DB")


@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)