Hooks
=====

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

You can specify a custom tasks file for before and after every step using `ansistrano_before_*_tasks_file` and `ansistrano_after_*_tasks_file` role variables. See [Role Variables](role-variables.md#role-variables) for more information.

Variables in custom tasks
-------------------------

When writing your custom tasks files you may need some variables that Ansistrano makes available to you:

* ```{{ ansistrano_release_path.stdout }}```: Path to current deployment release (probably the one you are going to use the most)
* ```{{ ansistrano_releases_path }}```: Path to releases folder
* ```{{ ansistrano_shared_path }}```: Path to shared folder (where common releases assets can be stored)
* ```{{ ansistrano_release_version }}```: Relative directory name for the release (by default equals to the current timestamp in UTC timezone)

