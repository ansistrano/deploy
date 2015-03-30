Ansistrano
==========

**ansistrano.deploy** and **ansistrano.rollback** are Ansible roles to easily manage the deployment process for
scripting applications such as PHP, Python and Ruby. It's an Ansible port for Capistrano.

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
can do everything Capistrano was doing with Ansible. If you are looking for alternatives, check Fabric or Chef Solo.

Requirements
------------

* Ansible in your deployer machine

Installation
------------

```
$ ansible-galaxy install carlosbuenosvinos.ansistrano-deploy carlosbuenosvinos.ansistrano-rollback
```

Features
--------

- Fast rollback (with ansistrano.rollback role)
- Custom path deployment
- Keep releases deployed up to a custom limit
- Pushing release strategy

Main workflow
-------------
This role deploys applications following the Capistrano flow.
* Code update: Uploads the code into the servers
* Symlink: After deploying the new release into your servers, changes the `current` softlink to new the release
* Cleanup: Removes any old version based in the `ansistrano_keep_releases` parameter

Custom tasks
------------
You will typically need to restart your webserver after the `Symlink` step, or download your dependencies before `Code update` or even do it in production before the `Symlink`. So, in order to perform your custom tasks you have some hooks that ansistrano will execute before and after each of the main 3 steps. By default, ansistrano will try to find some files in `./custom-tasks` path.

```
-- /my-local-machine/my-app.com
|-- hosts
|-- deploy-with-capistrano.yml
|-- custom-tasks
|   |-- before-code-update.yml
|   |-- after-code-update.yml
|   |-- before-symlink.yml
|   |-- after-symlink.yml
|   |-- before-cleanup.yml
|   |-- after-cleanup.yml
```

For example, in order to restart apache after `Symlink` step, we'll add in the `after-symlink.yml`

```
- name: Restart Apache
  service: name=httpd state=restarted
```

You can specify a custom folder to your custom tasks using the `ansistrano_custom_tasks_path`.

Deploying
---------

* Create a new hosts file. Check [ansible inventory documentation](http://docs.ansible.com/intro_inventory.html) if you
need help.
* Create a new fresh deploy-with-ansistrano.yml
* Include carlosbuenosvinos.ansible-deploy role
* Tune parameteres
* ```ansible-playbook -i your_hosts_file deploy-with-ansistrano.yml```

If everything has been set up properly, this command will create the following approximate directory structure on
your server.

```
-- /var/www/my-app.com
|-- current -> /var/www/my-app.com/releases/20100509145325
|-- releases
|   |-- 20100509145325
|-- shared
```

```
-- /var/www/my-app.com
|-- current -> /var/www/my-app.com/releases/20100509150741
|-- releases
|   |-- 20100509150741
|   |-- 20100509145325
|-- shared
```

```
-- /var/www/my-app.com
|-- current -> /var/www/my-app.com/releases/20100512131539
|-- releases
|   |-- 20100512131539
|   |-- 20100509150741
|   |-- 20100509145325
|-- shared
```

Pruning old releases
--------------------

In continuous delivery environments, the number of releases that you could possibly have in production is really high.
Maybe you have tons of space and you don't mind, but it's common to keep just a custom number of releases.

After the deployment, if you want to remove old releases just set the `ansistrano_keep_releases` variable to the total number
of releases you want to keep.

Role Variables
--------------

```yaml
- vars:
  ansistrano_deploy_from: "/home/carlosbuenosvinos/my-project" # Where my local project is
  ansistrano_deploy_to: "/var/www/atrapalo.com" # Base path to deploy to.
  ansistrano_version_dir: "releases" # Releases folder name
  ansistrano_keep_releases: 10 # Releases to keep after a new deployment. See "Pruning old releases".
  ansistrano_custom_tasks_path: "{{ playbook_dir }}/config/deploy/custom-tasks" # Path to find custom pre and post tasks for each deployment step.
  ansistrano_current_dir: "current" # Softlink name. You should rarely changed it.
  ansistrano_git_repo: git@github.com:USERNAME/REPO.git # Location of the git repository
  ansistrano_git_branch: master # Branch to use when deploying
  ansistrano_deploy_via: "rsync" # Method used to deliver the code to the server. Options are copy, rsync or git
```

Dependencies
------------

None

Example Playbook
-------------------------

In Ansible, a Role cannot be use alone, so you will need to Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yaml
---
- name: Deploy my super WebApp with Ansistrano
  hosts: all
  vars:
    ansistrano_deploy_via: copy
  roles:
    - { role: carlosbuenosvinos.ansistrano-deploy }
```

```ansible-playbook -i hosts deploy-with-ansistrano.yml```

```
PLAY [Deploy Dots. Game with Ansistrano] **************************************

GATHERING FACTS ***************************************************************
ok: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Ensure deployment base path exists] ***
ok: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Ensure releases folder exists] ***
ok: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Ensure shared elements folder exists] ***
ok: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Ensure shared copy for rsync improvement exists (in rsync case)] ***
skipping: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Get release timestamp] ***********
changed: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Get release path] ****************
changed: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Get releases path] ***************
changed: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Get shared path (in rsync case)] ***
skipping: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Rsync application files to remote shared copy (in rsync case)] ***
skipping: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Deploy existing code to servers] ***
skipping: [web1]

TASK: [carlosbuenosvinos.ansistrano-deploy | Deploy existing code to remote servers] ***
...
```

License
-------

MIT

Other resources
---------------
[Thoughts on deploying with Ansible](http://www.future500.nl/articles/2014/07/thoughts-on-deploying-with-ansible/)
