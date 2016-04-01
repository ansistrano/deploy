Testing
=======

    git clone git@github.com:ansistrano/deploy.git
    cd deploy
    vagrant up
    cd example/my-app
    ansible-playbook deploy.yml -i hosts