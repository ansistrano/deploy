Role Variables
==============

```yaml
vars:
  ansistrano_deploy_from: "{{ playbook_dir }}/" # Where my local project is (relative or absolute path)
  ansistrano_deploy_to: "/var/www/my-app" # Base path to deploy to.
  ansistrano_version_dir: "releases" # Releases folder name
  ansistrano_shared_dir: "shared" # Shared folder name
  ansistrano_current_dir: "current" # Softlink name. You should rarely changed it.
  ansistrano_current_via: "symlink" # Deployment strategy who code should be deployed to current path. Options are symlink or rsync
  ansistrano_keep_releases: 0 # Releases to keep after a new deployment. See "Pruning old releases".

  # Arrays of directories and files to be shared.
  # The following arrays of directories and files will be symlinked to the current release directory after the 'update-code' step and its callbacks
  # Notes:
  # * Paths are relative to the shared directory (no starting /)
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
  ansistrano_git_identity_key_shred: true # Shred identity key by default but can be overloaded to false if you encounter the following issue (https://github.com/ansistrano/deploy/issues/357)
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

  # Note for maintainers: GitHub.com no longer serves repositories over the SVN
  # protocol. The integration suite uses a temporary local `file://` SVN
  # repository fixture instead of GitHub for this strategy.

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

