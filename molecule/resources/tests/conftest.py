import pytest

# Make it available for all session (for all tests)
pytest.releases_path = pytest.deploy_path + "/releases"
pytest.current_path = pytest.deploy_path + "/current"
pytest.shared_path = pytest.deploy_path + "/shared"