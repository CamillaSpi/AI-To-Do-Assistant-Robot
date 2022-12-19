import os
from pathlib import Path
import pytest
import json
import sqlalchemy as sa

from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Tracker

REF_PATH = os.path.dirname(os.path.abspath(__file__))

EMPTY_TRACKER = Tracker.from_dict(json.load(open(REF_PATH + "/data/empty_tracker.json")))
SESSION_START = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_session_start.json"))
)
VIEW_CATEGORIES = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_view_categories.json"))
)
VIEW_ACTIVITIES = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_view_activities.json"))
)
VIEW_ACTIVITIES = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_view_activities.json"))
)
SET_STATUS_ACTIVITY = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_set_status_activity.json"))
)
SET_REMINDER_SLOT = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_set_reminder_slot.json"))
)
RESET_SLOT = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_reset_slot.json"))
)
REMOVE_ITEM = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_remove_item.json"))
)
REMOVE_CATEGORY = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_remove_category.json"))
)
REMINDER_ITEM = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_reminder_item.json"))
)
RECOGNZE_USER = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_recognize_user.json"))
)
REACT_TO_REMINDER = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_react_to_reminder.json"))
)
MODIFY_CATEGORY = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_modify_category.json"))
)
MODIFY_ACTIVTY = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_modify_activity.json"))
)
CLEAN_ALL_COMLETED = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_clean_all_completed.json"))
)
ASK_CATEGORY_OLD = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_ask_category_old.json"))
)
ASK_ACTIVITY_OLD = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_ask_activity_old.json"))
)
ASK_ACTIVITY_NEW = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_ask_activity_new.json"))
)
ADD_ITEM = Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_add_item.json"))
)
ASK_ADD_CATEGORY= Tracker.from_dict(
    json.load(open(REF_PATH + "/data/action_add_category.json"))
)
# DATABASE_URL = os.environ.setdefault("DATABASE_URL", "postgresql:///postgres")


@pytest.fixture
def dispatcher():
    return CollectingDispatcher()


@pytest.fixture
def domain():
    return dict()


# @pytest.fixture
# def session():
#     engine = sa.create_engine(DATABASE_URL)
#     db_session = sessionmaker(bind=engine)()

#     try:
#         yield db_session
#     finally:
#         db_session.close()
#         Base.metadata.drop_all(engine)