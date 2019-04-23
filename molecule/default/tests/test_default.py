import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

current_path = pytest.current_path
archive_name = "artifact2.zip"


def test_ansistrano_downloaded_files_does_not_exists(host):
    f = host.file(current_path + "/" + archive_name)

    assert not f.exists

def test_ansistrano_database_file_exists(host):
    f = host.file(current_path + "/config/database.yml")

    assert f.exists
    assert f.user == 'admin'
    assert f.group == 'admin'

def test_ansistrano_environment_file_exists(host):
    f = host.file(current_path + "/config/environment.yml")

    assert f.exists
    assert f.user == 'admin'
    assert f.group == 'admin'

def test_ansistrano_remote_file_exists(host):
    f = host.file(current_path + "/config/cycloid.yml")

    assert f.exists
    assert f.user == 'admin'
    assert f.group == 'admin'

def test_ansistrano_public_sitemaps_path_exists(host):
    d = host.file(current_path + "/public/sitemaps")

    assert d.is_symlink
    assert d.user == 'admin'
    assert d.group == 'admin'