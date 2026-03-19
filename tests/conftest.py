import copy
import pytest
from src import app as app_module


@pytest.fixture(autouse=True)
def reset_activities():
    snapshot = copy.deepcopy(app_module.activities)
    yield
    app_module.activities = snapshot
