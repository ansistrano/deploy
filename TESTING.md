Testing locally with Ansible 2.x
================================

    git clone git@github.com:ansistrano/deploy.git
    cd deploy
    vagrant up
    cd example/my-playbook
    ansible-playbook deploy.yml -i hosts