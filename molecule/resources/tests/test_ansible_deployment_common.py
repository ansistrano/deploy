import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

deploy_path = pytest.deploy_path
# Make it available for all session (for all tests)
releases_path = pytest.releases_path = deploy_path + "/releases"
current_path = pytest.current_path = deploy_path + "/current"
shared_path = pytest.shared_path = deploy_path + "/shared"


def test_ansistrano_deploy_to_path_exists(host):
    d = host.file(deploy_path)

    assert d.is_directory
    assert d.user == 'admin'
    assert d.group == 'admin'


def test_ansistrano_shared_path_exists(host):
    d = host.file(shared_path)

    assert d.is_directory
    assert d.user == 'admin'
    assert d.group == 'admin'


def test_ansistrano_releases_path_exists(host):
    d = host.file(releases_path)

    assert d.is_directory
    assert d.user == 'admin'
    assert d.group == 'admin'


def test_ansistrano_current_symlink_exists(host):
    d = host.file(current_path)

    assert d.is_symlink
    assert d.user == 'admin'
    assert d.group == 'admin'


def test_ansistrano_current_folder_is_pointing_to_the_latest_version(host):
    current = host.file(current_path).linked_to
    latest = host.run("ls -1dt " + releases_path + "/* | head -n1")

    assert current == latest.stdout
    assert latest.rc == 0


def test_ansistrano_ensure_release_version_file_exists(host):
    f = host.file(current_path + "/REVISION")

    assert f.exists
    assert f.user == 'admin'
    assert f.group == 'admin'


def test_ansistrano_ensure_only_have_max_5_releases(host):
    cmd = host.run("ls -1dt " + releases_path + "/* | tail -n +6")

    assert cmd.stdout == ''
    assert cmd.rc == 0


def test_ansistrano_ensure_we_can_do_a_second_deploy(host):
    releases_count = int(
        host.check_output("ls -1dt " + releases_path + "/* | wc -l").strip())

    assert releases_count == 2