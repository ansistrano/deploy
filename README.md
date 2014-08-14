Symfony2
========

Ansible role to easily deploy Symfony2 applications. It will clone a git repository, download and run composer install, and run assetic:dump when finished. The resulting directory structure is similar to what capifony creates:

```
project
    releases
        release
    shared
        web/uploads
        app/config
        app/logs
    current -> symlink to latest deployed release
```

Requirements
------------

None

Installation
------------

```
    $ ansible-galaxy install servergrove.symfony2
```


Role Variables
--------------

```yaml
- vars:
    symfony2_project_root: Path where application will be deployed on server.
    symfony2_project_name: Name of project.
    symfony2_project_repo: URL of git repository.
    symfony2_project_release: Release number, can be numeric, we recommend to set it to release date/time, 20140327100911
    symfony2_project_branch: git branch to deploy.
    symfony2_project_php_path: /usr/local/php54/bin/php
    symfony2_project_env: prod
    symfony2_project_console_opts: ''
    symfony2_project_composer_opts: '--no-dev --optimize-autoloader'
```

Dependencies
------------

None

Example Playbook
-------------------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
- hosts: servers
    roles:
        - { role: servergrove.symfony2, symfony2_project_root: /var/www/vhosts/example.com/, symfony2_project_name: demo, symfony2_project_branch: master, symfony2_project_release: 1 }
```

License
-------

MIT

Author Information
------------------

Contributions are welcome: https://github.com/servergrove/ansible-symfony2
