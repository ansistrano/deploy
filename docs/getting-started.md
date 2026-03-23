Getting Started
===============

Requirements
------------

In order to deploy your apps with Ansistrano, you will need:

* Ansible in your deployer machine
* `rsync` on the target machine if you are using either the `rsync`, `rsync_direct`, or `git` deployment strategy or if you are using `ansistrano_current_via = rsync`

Installation
------------

Ansistrano is an Ansible role distributed globally using [Ansible Galaxy](https://galaxy.ansible.com/). In order to install Ansistrano role you can use the following command.

```
$ ansible-galaxy install ansistrano.deploy ansistrano.rollback
```

Update
------

If you want to update the role, you need to pass **--force** parameter when installing. Please, check the following command:

```
$ ansible-galaxy install --force ansistrano.deploy ansistrano.rollback
```

