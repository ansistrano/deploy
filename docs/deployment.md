Deployment
==========

Deploying
---------

In order to deploy with Ansistrano, you need to perform some steps:

* Create a new `hosts` file. Check [ansible inventory documentation](http://docs.ansible.com/intro_inventory.html) if you need help. This file will identify all the hosts where to deploy to. For multistage environments check [Multistage environments](#multistage-environment-devel-preprod-prod-etc).
* Create a new playbook for deploying your app, for example, `deploy.yml`
* Set up role variables (see [Role Variables](role-variables.md#role-variables))
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

Serial deployments
------------------

To prevent different timestamps when deploying to several servers using the [`serial`](http://docs.ansible.com/playbooks_delegation.html#rolling-update-batch-size) option, you should set the `ansistrano_release_version` variable.

```ansible-playbook -i hosts -e "ansistrano_release_version=`date -u +%Y%m%d%H%M%SZ`" deploy.yml```

Multistage environment (devel, preprod, prod, etc.)
---------------------------------------------------

If you want to deploy to different environments such as devel, preprod and prod, it's recommended to create different hosts files. When done, you can specify a different host file when running the deployment playbook using the **-i** parameter. On every host file, you can specify different users, password, connection parameters, etc.

```ansible-playbook -i hosts_devel deploy.yml```

```ansible-playbook -i hosts_preprod deploy.yml```

```ansible-playbook -i hosts_prod deploy.yml```

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

