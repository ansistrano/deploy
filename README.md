Ansistrano
==========

[![Build Status](https://travis-ci.com/ansistrano/deploy.svg?branch=master)](https://travis-ci.com/ansistrano/deploy)
[![Total Deployments](https://img.shields.io/badge/dynamic/json.svg?label=overall&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.total&colorB=green&suffix=%20deployments)](https://ansistrano.com)
[![Year Deployments](https://img.shields.io/badge/dynamic/json.svg?label=year&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.year&colorB=green&suffix=%20deployments)](https://ansistrano.com)
[![Month Deployments](https://img.shields.io/badge/dynamic/json.svg?label=month&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.month&colorB=green&suffix=%20deployments)](https://ansistrano.com)
[![Today Deployments](https://img.shields.io/badge/dynamic/json.svg?label=today&uri=https%3A%2F%2Fansistrano.com%2Finfo&query=deployments.today&colorB=green&suffix=%20deployments)](https://ansistrano.com)

**ansistrano.deploy** and **ansistrano.rollback** are Ansible roles to easily manage the deployment process for scripting applications such as PHP, Python and Ruby. It's an Ansible port for Capistrano.

- [Ansistrano](#ansistrano)
  - [History](#history)
  - [Project name](#project-name)
  - [Ansistrano anonymous usage stats](#ansistrano-anonymous-usage-stats)
  - [Who is using Ansistrano?](#who-is-using-ansistrano)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Update](#update)
  - [Features](#features)
  - [Main workflow](#main-workflow)
  - [Role Variables](#role-variables)
  - [Deploying](#deploying)
  - [Rolling back](#rolling-back)
  - [Hooks: Custom tasks](#hooks-custom-tasks)
  - [Variables in custom tasks](#variables-in-custom-tasks)
  - [Pruning old releases](#pruning-old-releases)
  - [Example Playbook](#example-playbook)
  - [Sample projects](#sample-projects)
  - [They're talking about us](#theyre-talking-about-us)
  - [License](#license)
  - [Other resources](#other-resources)

History
-------

[Capistrano](http://capistranorb.com/) is a remote server automation tool and it's currently in Version 3. [Version 2.0](https://github.com/capistrano/capistrano/tree/legacy-v2) was originally thought in order to deploy RoR applications. With additional plugins, you were able to deploy non Rails applications such as PHP and Python, with different deployment strategies, stages and much more. I loved Capistrano v2. I have used it a lot. I developed a plugin for it.

Capistrano 2 was a great tool and it still works really well. However, it is not maintained anymore since the original team is working in v3. This new version does not have the same set of features so it is less powerful and flexible. Besides that, other new tools are becoming easier to use in order to deploy applications, such as Ansible.

So, I have decided to stop using Capistrano because v2 is not maintained, v3 does not have enough features, and I can do everything Capistrano was doing with Ansible. If you are looking for alternatives, check Fabric or Chef Solo.

Project name
------------

Ansistrano comes from Ansible + Capistrano, easy, isn't it?

Ansistrano anonymous usage stats
--------------------------------

There is an optional step in Ansistrano that sends a HTTP request to our servers. Unfortunately, the metrics we can get from Ansible Galaxy are limited so this is one of the few ways we have to measure how many active users we really have.

We only use this data for usage statistics but anyway, if you are not comfortable with this, you can disable this extra step by setting `ansistrano_allow_anonymous_stats` to false in your playbooks.

Who is using Ansistrano?
------------------------

Is Ansistrano ready to be used? Here are some companies currently using it:

* [ABA English](http://www.abaenglish.com/)
* [Another Place Productions](http://www.anotherplaceproductions.com)
* [Aptvision](https://www.aptvision.com)
* [ARTACK WebLab](https://www.artack.ch)
* [Atrápalo](http://www.atrapalo.com)
* [Beroomers](https://www.beroomers.com)
* [CMP Group](http://www.teamcmp.com)
* [Cabissimo](https://www.cabissimo.com)
* [Camel Secure](https://camelsecure.com)
* [Cherry Hill](https://chillco.com)
* [Claranet France](http://www.claranet.fr/)
* [Clearpoint](http://www.clearpoint.co.nz)
* [Clever Age](https://www.clever-age.com)
* [CridaDemocracia](https://cridademocracia.org)
* [Cycloid](http://www.cycloid.io)
* [Daemonit](https://daemonit.com)
* [Deliverea](https://www.deliverea.com/)
* [DevOps Barcelona Conference](https://devops.barcelona/)
* [EnAlquiler](http://www.enalquiler.com/)
* [Euromillions.com](http://euromillions.com/)
* [Finizens](https://finizens.com/)
* [FloraQueen](https://www.floraqueen.com/)
* [Fluxus](http://www.fluxus.io/)
* [Geocalia](https://geocalia.com/)
* [Gstock](http://www.g-stock.es)
* [HackSoft](https://hacksoft.io/)
* [HackConf](https://hackconf.bg/en/)
* [Hexanet](https://www.hexanet.fr)
* [HiringThing](https://www.hiringthing.com/)
* [Holaluz](https://www.holaluz.com)
* [Hosting4devs](https://hosting4devs.com)
* [Jolicode](http://jolicode.com/)
* [Kidfund](http://link.kidfund.us/github "Kidfund")
* [Lumao SAS](https://lumao.eu)
* [mailXpert](https://www.mailxpert.ch)
* [MEDIA.figaro](http://media.figaro.fr)
* [Moss](https://moss.sh)
* [Nice&Crazy](http://www.niceandcrazy.com)
* [Nodo Ámbar](http://www.nodoambar.com/)
* [Oferplan](http://oferplan.com/)
* [Ofertix](http://www.ofertix.com)
* [Òmnium Cultural](https://www.omnium.cat)
* [OpsWay Software Factory](http://opsway.com)
* [Parkimeter](https://parkimeter.com)
* [PHP Barcelona Conference](https://php.barcelona/)
* [Scoutim](https://scoutim.com)
* [Socialnk](https://socialnk.com/)
* [Spotahome](https://www.spotahome.com)
* [Suntransfers](http://www.suntransfers.com)
* [TechPump](http://www.techpump.com/)
* [Tienda Online VirginMobile](https://cambiate.virginmobile.cl)
* [The Cocktail](https://the-cocktail.com/)
* [Timehook](https://timehook.io)
* [TMTFactory](https://tmtfactory.com)
* [UNICEF Comité Español](https://www.unicef.es)
* [Ulabox](https://www.ulabox.com)
* [Uvinum](http://www.uvinum.com)
* [VirginMobile Chile](https://empresas.virginmobile.cl)
* [Wavecontrol](http://monitoring.wavecontrol.com/ca/public/demo/)
* [WAVE Meditation](https://wavemeditation.com/)
* [Yubl](https://yubl.me/)

If you are also using it, please let us know via a PR to this document.

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

Features
--------

* Rollback in seconds (with ansistrano.rollback role)
* Customize your deployment with hooks before and after critical steps
* Save disk space keeping a maximum fixed releases in your hosts
* Choose between SCP, RSYNC, GIT, SVN, HG, HTTP Download or S3 GET deployment strategies (optional unarchive step included)

Main workflow
-------------

Ansistrano deploys applications following the Capistrano flow.

* Setup phase: Creates the folder structure to hold your releases
* Code update phase: Puts the new release into your hosts
* Symlink phase: After deploying the new release into your hosts, this step changes the `current` softlink to new the release
* Cleanup phase: Removes any old version based in the `ansistrano_keep_releases` parameter (see "Role Variables")

![Ansistrano Flow](https://raw.githubusercontent.com/ansistrano/deploy/master/docs/ansistrano-flow.png)

Role Variables
--------------

```yaml
vars:
  ansistrano_deploy_from: "{{ playbook_dir }}/" # Where my local project is (relative or absolute path)
  ansistrano_deploy_to: "/var/www/my-app" # Base path to deploy to.
  ansistrano_version_dir: "releases" # Releases folder name
  ansistrano_current_dir: "current" # Softlink name. You should rarely changed it.
  ansistrano_current_via: "symlink" # Deployment strategy who code should be deployed to current path. Options are symlink or rsync
  ansistrano_keep_releases: 0 # Releases to keep after a new deployment. See "Pruning old releases".

  # Arrays of directories and files to be shared.
  # The following arrays of directories and files will be symlinked to the current release directory after the 'update-code' step and its callbacks
  # Notes:
  # * Paths are relative to the /shared directory (no starting /)
  # * If your items are in a subdirectory, write the entire path to each shared directory
  #
  # Example:
  # ansistrano_shared_paths:
  #   - path/to/first-dir
  #   - path/next-dir
  # ansistrano_shared_files:
  #   - my-file.txt
  #   - path/to/file.txt
  ansistrano_shared_paths: []
  ansistrano_shared_files: []


  # Shared paths and basedir shared files creation.
  # By default the shared paths directories and base directories for shared files are created automatically if not exists. But in some scenarios those paths could be symlinks to another directories in the filesystem, and the deployment process would fails. With these variables you can disable the involved tasks. If you have two or three shared paths, and don't need creation only for some of them, you always could disable the automatic creation and add a custom task in a hook.
  ansistrano_ensure_shared_paths_exist: yes
  ansistrano_ensure_basedirs_shared_files_exist: yes
  
  # Deployment strategy - method used to deliver code. Options are copy, download, git, rsync, rsync_direct, svn, or s3. 
  ansistrano_deploy_via: rsync 
  # Copy, download and s3 have an optional step to unarchive the downloaded file which can be used by adding _unarchive. 
  # The rsync_direct strategy omits a file copy on the target offering a slight speed increase if you are deploying to shared hosts, are experiancing bad file-performance, or serve static assets from the same host you deploy your app to and rsync many files.
  # You can check all the options inside tasks/update-code folder!
  
  ansistrano_allow_anonymous_stats: yes

  # Variables used in the rsync/rsync_direct deployment strategy
  ansistrano_rsync_extra_params: "" # Extra parameters to use when deploying with rsync in a single string. Although Ansible allows an array this can cause problems if we try to add multiple --include args as it was reported in https://github.com/ansistrano/deploy/commit/e98942dc969d4e620313f00f003a7ea2eab67e86
  ansistrano_rsync_set_remote_user: yes # See [ansible synchronize module](http://docs.ansible.com/ansible/synchronize_module.html). Options are yes, no.
  ansistrano_rsync_path: "" # See [ansible synchronize module](http://docs.ansible.com/ansible/synchronize_module.html). By default is "sudo rsync", it can be overwriten with (example): "sudo -u user rsync".
  ansistrano_rsync_use_ssh_args: no # See [ansible synchronize module](http://docs.ansible.com/ansible/synchronize_module.html). If set yes, use the ssh_args specified in ansible.cfg.

  # Variables used in the Git deployment strategy
  ansistrano_git_repo: git@github.com:USERNAME/REPO.git # Location of the git repository
  ansistrano_git_branch: master # What version of the repository to check out. This can be the full 40-character SHA-1 hash, the literal string HEAD, a branch name, or a tag name
  ansistrano_git_repo_tree: "" # If specified the subtree of the repository to deploy
  ansistrano_git_identity_key_path: "" # If specified this file is copied over and used as the identity key for the git commands, path is relative to the playbook in which it is used
  ansistrano_git_identity_key_remote_path: "" # If specified this file on the remote server is used as the identity key for the git commands, remote path is absolute
  # Optional variables, omitted by default
  ansistrano_git_refspec: ADDITIONAL_GIT_REFSPEC # Additional refspec to be used by the 'git' module. Uses the same syntax as the 'git fetch' command.
  ansistrano_git_ssh_opts: "-o StrictHostKeyChecking=no" # Additional ssh options to be used in Git
  ansistrano_git_depth: 1 # Additional history truncated to the specified number or revisions
  ansistrano_git_executable: /opt/local/bin/git # Path to git executable to use. If not supplied, the normal mechanism for resolving binary paths will be used.

  # Variables used in the SVN deployment strategy
  # Please note there was a bug in the subversion module in Ansible 1.8.x series (https://github.com/ansible/ansible-modules-core/issues/370) so it is only supported from Ansible 1.9
  ansistrano_svn_repo: https://svn.company.com/project # Location of the svn repository
  ansistrano_svn_branch: trunk # What branch from the repository to check out.
  ansistrano_svn_revision: HEAD # What revision from the repository to check out.
  ansistrano_svn_username: user # SVN authentication username
  ansistrano_svn_password: Pa$$word # SVN authentication password
  ansistrano_svn_environment: {} # Dict with environment variables for svn tasks (https://docs.ansible.com/ansible/playbooks_environment.html)

  # Variables used in the HG deployment strategy
  ansistrano_hg_repo: https://USERNAME@bitbucket.org/USERNAME/REPO # Location of the hg repo
  ansistrano_hg_branch: default # Any branch identifier that works with hg -r, so named branch, bookmark, commit hash...

  # Variables used in the download deployment strategy
  ansistrano_get_url: https://github.com/someproject/somearchive.tar.gz
  ansistrano_download_force_basic_auth: false # no default as this is only supported from Ansible 2.0
  ansistrano_download_headers: "" # no default as this is only supported from Ansible 2.0

  # Variables used in the S3 deployment strategy
  ansistrano_s3_bucket: s3bucket
  ansistrano_s3_object: s3object.tgz # Add the _unarchive suffix to the ansistrano_deploy_via if your object is a package (ie: s3_unarchive)
  ansistrano_s3_region: eu-west-1
  ansistrano_s3_rgw: false # must be Ansible >= 2.2. use Ceph RGW for S3 compatible cloud providers
  ansistrano_s3_url: http://rgw.example.com # when use Ceph RGW, set url
  # Optional variables, omitted by default
  ansistrano_s3_aws_access_key: YOUR_AWS_ACCESS_KEY
  ansistrano_s3_aws_secret_key: YOUR_AWS_SECRET_KEY
  ansistrano_s3_ignore_nonexistent_bucket: false
  
  # Variables used in the GCS deployment strategy
  ansistrano_gcs_bucket: gcsbucket
  ansistrano_gcs_object: gcsobject.tgz # Add the _unarchive suffix to the ansistrano_deploy_via if your object is a package (ie: s3_unarchive)
  ansistrano_gcs_region: eu-west-1 # https://cloud.google.com/storage/docs/bucket-locations
  # Optional variables, omitted by default
  ansistrano_gcs_access_key: YOUR_GCS_ACCESS_KEY # navigate to Cloud console > Storage > Settings > Interoperability
  ansistrano_gcs_secret_key: YOUR_GCS_SECRET_KEY

  # Hooks: custom tasks if you need them
  ansistrano_before_setup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-before-setup-tasks.yml"
  ansistrano_after_setup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-after-setup-tasks.yml"
  ansistrano_before_update_code_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-before-update-code-tasks.yml"
  ansistrano_after_update_code_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-after-update-code-tasks.yml"
  ansistrano_before_symlink_shared_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-before-symlink-shared-tasks.yml"
  ansistrano_after_symlink_shared_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-after-symlink-shared-tasks.yml"
  ansistrano_before_symlink_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-before-symlink-tasks.yml"
  ansistrano_after_symlink_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-after-symlink-tasks.yml"
  ansistrano_before_cleanup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-before-cleanup-tasks.yml"
  ansistrano_after_cleanup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-after-cleanup-tasks.yml"
```

`{{ playbook_dir }}` is an Ansible variable that holds the path to the current playbook.

Deploying
---------

In order to deploy with Ansistrano, you need to perform some steps:

* Create a new `hosts` file. Check [ansible inventory documentation](http://docs.ansible.com/intro_inventory.html) if you need help. This file will identify all the hosts where to deploy to. For multistage environments check [Multistage environments](#multistage-environment-devel-preprod-prod-etc).
* Create a new playbook for deploying your app, for example, `deploy.yml`
* Set up role variables (see [Role Variables](#role-variables))
* Include the `ansistrano.deploy` role as part of a play
* Run the deployment playbook

```ansible-playbook -i hosts deploy.yml```

If everything has been set up properly, this command will create the following approximate directory structure on your server. Check how the hosts folder structure would look like after one, two and three deployments.

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

### Serial deployments

To prevent different timestamps when deploying to several servers using the [`serial`](http://docs.ansible.com/playbooks_delegation.html#rolling-update-batch-size) option, you should set the `ansistrano_release_version` variable.

```ansible-playbook -i hosts -e "ansistrano_release_version=`date -u +%Y%m%d%H%M%SZ`" deploy.yml```


Rolling back
-----------

In order to rollback with Ansistrano, you need to set up the deployment and run the rollback playbook.

```ansible-playbook -i hosts rollback.yml```

If you try to rollback with zero or one releases deployed, an error will be raised and no actions performed.

Variables you can tune in rollback role are less than in deploy one:

```yaml
vars:
  ansistrano_deploy_to: "/var/www/my-app" # Base path to deploy to.
  ansistrano_version_dir: "releases" # Releases folder name
  ansistrano_current_dir: "current" # Softlink name. You should rarely changed it.
  ansistrano_rollback_to_release: "" # If specified, the application will be rolled back to this release version; previous release otherwise.
  ansistrano_remove_rolled_back: yes # You can change this setting in order to keep the rolled back release in the server for later inspection
  ansistrano_allow_anonymous_stats: yes

  # Hooks: custom tasks if you need them
  ansistrano_rollback_before_setup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-rollback-before-setup-tasks.yml"
  ansistrano_rollback_after_setup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-rollback-after-setup-tasks.yml"
  ansistrano_rollback_before_symlink_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-rollback-before-symlink-tasks.yml"
  ansistrano_rollback_after_symlink_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-rollback-after-symlink-tasks.yml"
  ansistrano_rollback_before_cleanup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-rollback-before-cleanup-tasks.yml"
  ansistrano_rollback_after_cleanup_tasks_file: "{{ playbook_dir }}/<your-deployment-config>/my-rollback-after-cleanup-tasks.yml"
```

Multistage environment (devel, preprod, prod, etc.)
---------------------------------------------------

If you want to deploy to different environments such as devel, preprod and prod, it's recommended to create different hosts files. When done, you can specify a different host file when running the deployment playbook using the **-i** parameter. On every host file, you can specify different users, password, connection parameters, etc.

```ansible-playbook -i hosts_devel deploy.yml```

```ansible-playbook -i hosts_preprod deploy.yml```

```ansible-playbook -i hosts_prod deploy.yml```

Hooks: Custom tasks
-------------------

You will typically need to reload your webserver after the `Symlink` step, or download your dependencies before `Code update` or even do it in production before the `Symlink`. So, in order to perform your custom tasks you have some hooks that Ansistrano will execute before and after each of the main 3 steps. **This is the main benefit against other similar deployment roles.**

```
-- /my-local-machine/my-app.com
|-- hosts
|-- deploy.yml
|-- my-custom-tasks
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
  service: name=httpd state=reloaded
```

* **Q: Where would you add sending email notification after a deployment?**
* **Q: (for PHP and Symfony developers) Where would you clean the cache?**

You can specify a custom tasks file for before and after every step using `ansistrano_before_*_tasks_file` and `ansistrano_after_*_tasks_file` role variables. See "Role Variables" for more information.

Variables in custom tasks
-------------------------

When writing your custom tasks files you may need some variables that Ansistrano makes available to you:

* ```{{ ansistrano_release_path.stdout }}```: Path to current deployment release (probably the one you are going to use the most)
* ```{{ ansistrano_releases_path }}```: Path to releases folder
* ```{{ ansistrano_shared_path }}```: Path to shared folder (where common releases assets can be stored)
* ```{{ ansistrano_release_version }}```: Relative directory name for the release (by default equals to the current timestamp in UTC timezone)

Pruning old releases
--------------------

In continuous delivery environments, you will possibly have a high number of releases in production. Maybe you have tons of space and you don't mind, but it's common practice to keep just a custom number of releases.

After the deployment, if you want to remove old releases just set the `ansistrano_keep_releases` variable to the total number of releases you want to keep.

Let's see three deployments with an `ansistrano_keep_releases: 2` configuration:

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
|-- shared
```

See how the release `20100509145325` has been removed.

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

You can check more advanced examples inside the test folder which are run against Travis-CI

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

They're talking about us
------------------------

* [Pablo Godel - Deploying Symfony - Symfony Cat 2016](https://youtu.be/K2bBhrkmpSg?t=26m)
* [https://www.artansoft.com/2016/05/deploy-de-proyectos-php-ansistrano/](https://www.artansoft.com/2016/05/deploy-de-proyectos-php-ansistrano/)
* [http://alexmoreno.net/ansistrano-deploying-drupal-ansible](http://alexmoreno.net/ansistrano-deploying-drupal-ansible)
* [http://www.ricardclau.com/2015/10/deploying-php-applications-with-ansistrano/](http://www.ricardclau.com/2015/10/deploying-php-applications-with-ansistrano/)
* [http://es.slideshare.net/OrestesCA/ansible-intro-ansible-barcelona-user-group-june-2015](http://es.slideshare.net/OrestesCA/ansible-intro-ansible-barcelona-user-group-june-2015)
* [http://carlosbuenosvinos.com/deploying-symfony-and-php-apps-with-ansistrano/](http://carlosbuenosvinos.com/deploying-symfony-and-php-apps-with-ansistrano/)
* [https://www.youtube.com/watch?v=CPz5zPzzMZE](https://www.youtube.com/watch?v=CPz5zPzzMZE)
* [https://github.com/cbrunnkvist/ansistrano-symfony-deploy](https://github.com/cbrunnkvist/ansistrano-symfony-deploy)
* [https://www.reddit.com/r/ansible/comments/2ezzz5/rapid_rollback_with_ansible/](https://www.reddit.com/r/ansible/comments/2ezzz5/rapid_rollback_with_ansible/)
* [Cookiecutting Ansible for Django](https://hacksoft.io/blog/cookiecutting-django-ansible/)
* [Deploying PHP applications with Ansible, Ansible Vault and Ansistrano](https://www.oliverdavies.uk/talks/deploying-php-ansible-ansistrano)

License
-------

MIT

Other resources
---------------

* [Thoughts on deploying with Ansible](http://www.future500.nl/articles/2014/07/thoughts-on-deploying-with-ansible/)
* [Docker image](https://hub.docker.com/r/lavoweb/ansistrano/)
