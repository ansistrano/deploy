Ansistrano
==========

[![CI](https://github.com/ansistrano/deploy/actions/workflows/ci.yml/badge.svg)](https://github.com/ansistrano/deploy/actions/workflows/ci.yml)
[![Total Deployments](https://img.shields.io/badge/dynamic/json.svg?label=overall&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.total&colorB=green&suffix=%20deployments)](https://ansistrano.com)
[![Year Deployments](https://img.shields.io/badge/dynamic/json.svg?label=year&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.year&colorB=green&suffix=%20deployments)](https://ansistrano.com)
[![Month Deployments](https://img.shields.io/badge/dynamic/json.svg?label=month&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.month&colorB=green&suffix=%20deployments)](https://ansistrano.com)
[![Today Deployments](https://img.shields.io/badge/dynamic/json.svg?label=today&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.today&colorB=green&suffix=%20deployments)](https://ansistrano.com)

**ansistrano.deploy** and **ansistrano.rollback** are Ansible roles to manage application deployments with a Capistrano-style workflow.

Ansistrano supports `rsync`, `rsync_direct`, `git`, `svn`, `hg`, `download`, `download_unarchive`, `s3`, `s3_unarchive`, `gcs`, and `gcs_unarchive`, plus rollback hooks and release pruning.

Quick Start
-----------

Requirements:

* Ansible on the deployer machine
* `rsync` on the target machine when using `rsync`, `rsync_direct`, `git`, or `ansistrano_current_via = rsync`

Install:

```
$ ansible-galaxy install ansistrano.deploy ansistrano.rollback
```

Update:

```
$ ansible-galaxy install --force ansistrano.deploy ansistrano.rollback
```

Documentation
-------------

Project overview:

* [History](docs/overview.md#history)
* [Project name](docs/overview.md#project-name)
* [Anonymous usage stats](docs/overview.md#ansistrano-anonymous-usage-stats)
* [Who is using Ansistrano?](docs/overview.md#who-is-using-ansistrano)
* [Features](docs/overview.md#features)
* [Main workflow](docs/overview.md#main-workflow)

Getting started:

* [Requirements](docs/getting-started.md#requirements)
* [Installation](docs/getting-started.md#installation)
* [Update](docs/getting-started.md#update)

Configuration:

* [Role variables](docs/role-variables.md#role-variables)

Deployment:

* [Deploying](docs/deployment.md#deploying)
* [Serial deployments](docs/deployment.md#serial-deployments)
* [Multistage environments](docs/deployment.md#multistage-environment-devel-preprod-prod-etc)
* [Pruning old releases](docs/deployment.md#pruning-old-releases)

Rollback and hooks:

* [Rolling back](docs/rollback.md#rolling-back)
* [Hooks: custom tasks](docs/hooks.md#hooks-custom-tasks)
* [Variables in custom tasks](docs/hooks.md#variables-in-custom-tasks)

Examples and resources:

* [Example playbook](docs/examples.md#example-playbook)
* [Sample projects](docs/examples.md#sample-projects)
* [They're talking about us](docs/community.md#theyre-talking-about-us)
* [Other resources](docs/community.md#other-resources)

Other
-----

* [Testing](TESTING.md)
* [License](LICENSE)
