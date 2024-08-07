import pytest


@pytest.fixture
def local_image_version(request) -> str:
    return request.config.getoption("--local-image-version")
