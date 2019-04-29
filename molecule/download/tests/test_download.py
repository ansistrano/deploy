import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

current_path = pytest.current_path
archive_name = "artifact1.zip"


def test_ansistrano_downloaded_files_does_not_exists(host):
    f = host.file(current_path + "/" + archive_name)

    assert not f.exists