from flask.cli import AppGroup
from .users import seed_users, undo_users
from .reviews import seed_review, undo_seed_review
from .review_images import seed_review_image, undo_seed_review_images
from .businesses import seed_business, undo_seed_business
from .business_images import seed_business_image, undo_seed_business_image
from app.models.db import db, environment, SCHEMA

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')


# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    if environment == 'production':
        # Before seeding in production, you want to run the seed undo
        # command, which will  truncate all tables prefixed with
        # the schema name (see comment in users.py undo_users function).
        # Make sure to add all your other model's undo functions below
        undo_seed_business_image()
        undo_seed_review_images()
        undo_seed_review()
        undo_seed_business()
        undo_users()
    seed_users()
    seed_business()
    seed_review()
    seed_business_image()
    seed_review_image()
    # Add other seed functions here


# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_users()
    undo_seed_business()
    undo_seed_review()
    undo_seed_business_image()
    undo_seed_review_images()
    # Add other undo functions here
