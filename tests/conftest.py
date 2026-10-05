from collections.abc import Iterator

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app, follow_redirects=False)


@pytest.fixture(autouse=True)
def restore_activity_participants() -> Iterator[None]:
    original_participants = {
        name: list(details["participants"])
        for name, details in activities.items()
    }

    yield

    for name, participants in original_participants.items():
        activities[name]["participants"][:] = participants
