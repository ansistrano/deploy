Examples
========

Example Playbook
----------------

In the folder, `example` you can check an example project that shows how to deploy a small application with Ansistrano.

In order to run it, you will need to have Vagrant and the ansistrano roles installed. Please check https://www.vagrantup.com for more information about Vagrant and our Installation section.

```
$ cd example/my-playbook
$ vagrant up
$ ansible-playbook -i hosts deploy.yml
```

And after running these commands, the index.html located in the `my-app` folder will be deployed to both vagrant boxes

In order to test the rollback playbook, you will need to run deploy.yml at least twice (so that there is something to rollback to). And once this is done, you only need to run

```
$ ansible-playbook -i hosts rollback.yml
```

You can check more advanced examples inside the `test` folder which are run against GitHub Actions.

Sample projects
---------------

We have added Ansistrano support for other projects we are working on.

* LastWishes: Domain-Driven Design PHP Sample App: https://github.com/dddinphp/last-wishes

As an example, see the execution log of the LastWishes deployment:

```
PLAY [Deploy last wishes app to my server] ************************************

GATHERING FACTS ***************************************************************
ok: [quepimquepam.com]

TASK: [ansistrano.deploy | Ensure deployment base path exists] ***
ok: [quepimquepam.com]

TASK: [ansistrano.deploy | Ensure releases folder exists] ***
ok: [quepimquepam.com]

TASK: [ansistrano.deploy | Ensure shared elements folder exists] ***
ok: [quepimquepam.com]

TASK: [ansistrano.deploy | Get release timestamp] ***********
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Get release path] ****************
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Get releases path] ***************
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Get shared path (in rsync case)] ***
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Rsync application files to remote shared copy (in rsync case)] ***
changed: [quepimquepam.com -> 127.0.0.1]

TASK: [ansistrano.deploy | Deploy existing code to servers] ***
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Deploy existing code to remote servers] ***
skipping: [quepimquepam.com]

TASK: [ansistrano.deploy | Update remote repository] ********
skipping: [quepimquepam.com]

TASK: [ansistrano.deploy | Export a copy of the repo] *******
skipping: [quepimquepam.com]

TASK: [ansistrano.deploy | Deploy code from to servers] *****
skipping: [quepimquepam.com]

TASK: [ansistrano.deploy | Copy release version into REVISION file] ***
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Touches up the release code] *****
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Change softlink to new release] ***
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Reload Apache] *******************
changed: [quepimquepam.com]

TASK: [ansistrano.deploy | Clean up releases] ***************
skipping: [quepimquepam.com]

PLAY RECAP ********************************************************************
quepimquepam.com           : ok=14   changed=10   unreachable=0    failed=0
```

