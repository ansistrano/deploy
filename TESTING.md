Testing locally with Ansible 2.x
================================

    git clone git@github.com:ansistrano/deploy.git
    cd deploy
    vagrant up
    cd test/my-app
    ansible-playbook deploy.yml -i hosts