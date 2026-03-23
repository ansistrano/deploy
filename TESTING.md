Testing locally with Ansible
============================

    git clone git@github.com:ansistrano/deploy.git
    cd deploy
    vagrant up
    cd example/my-playbook
    ansible-playbook deploy.yml -i hosts

The repository also includes a GitHub Actions workflow in `.github/workflows/ci.yml`
that runs the legacy integration suite from `test/main.yml` on Ubuntu.

To run the same suite locally in Docker:

    ./scripts/test-in-docker.sh syntax
    ./scripts/test-in-docker.sh integration

The script builds a local image, mounts the repository into the container and
executes the existing playbooks from `test/main.yml`.

The integration suite still covers the `svn` deployment strategy. Since
GitHub.com no longer exposes repositories over Subversion, the SVN test now
creates a temporary local fixture repository with `svnadmin` and exercises the
role against a `file://` repository URL instead of relying on an external
service.
