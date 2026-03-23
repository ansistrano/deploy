Rollback
========

Rolling back
------------

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

