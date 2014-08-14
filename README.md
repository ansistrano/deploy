Ansistrano: ansistrano.deploy and ansistrano.rollback roles
===========================================================

**ansistrano.deploy** and **ansistrano.rollback** are Ansible roles to easily manage the deployment process for
scripting applications such as PHP, Python and Ruby. It's an Ansible port for Capistrano.

```
-- /var/www/my-app.com
|-- current -> /var/www/my-app.com/releases/20100512131539
|-- releases
|   |-- 20100512131539
|   |-- 20100509150741
|   |-- 20100509145325
|-- shared
```

History
-------

[Capistrano](http://capistranorb.com/) is a remote server automation tool and it's currently in Version 3.
[Version 2.0](https://github.com/capistrano/capistrano/tree/legacy-v2) was originally thought in order to deploy RoR
applications. With additional plugins, you we're able to deploy non Rails applications such as PHP and Python, with
different deployment strategies, stages and much more. I loved Capistrano v2. I have used it a lot. I developed
a plugin for it.

Capistrano 2 was a great tool and it works really well. However, right now is not maintained anymore because the
original team is working in v3. This new version does not have the same features so is less powerful and flexible and
other new tools are becoming easier to use in order to deploy applications, such as Ansible.

So, I have decided to stop using Capistrano because v2 is not maintained, v3 does not have features enough, and I
can do everything Capistrano was doing with Ansible.

Features
--------

- Fast rollback
- Custom path deployment
- Keep releases deployed up to a custom limit
- Pushing release strategy

Enable `cleanUpAfterDeploy` parameter and set the `maxNumberOfReleases` to the total number of
releases you want to keep. In continuous delivery environments, the number of

Requirements
------------

None

Installation
------------

```
    $ ansible-galaxy install ansistrano.deploy ansistrano.rollback
```

Role Variables
--------------

```yaml
- vars:
  deployTo: Path where application will be deployed on server.
  deployFrom: "/Users/buenosvinos/Development/ansible"
  deployTo: "/var/www/atrapalo.com"
  versionDir: "releases"
  currentDir: "current"
  cleanUpAfterDeploy: False
  maxNumberOfReleases: 10
  preAndPostTasksFolder: "./custom-tasks"
```

Dependencies
------------

None

Example Playbook
-------------------------

In Ansible, a Role cannot be use alone, so you will need to Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
# deploy.
- hosts: servers
    roles:
        - { role: ansistrano.deploy }
```

License
-------

MIT
