#!/usr/bin/env bash
set -euo pipefail

mode="${1:-integration}"
shift || true

repo_dir="/workspace/deploy"
inventory_file="/tmp/ansistrano-inventory"

ln -sfn "${repo_dir}" /workspace/local-ansistrano
mkdir -p /etc/ansible/roles
ln -sfn "${repo_dir}" /etc/ansible/roles/role_under_test
printf 'localhost ansible_connection=local\n' > "${inventory_file}"

cd "${repo_dir}/test"
export ANSIBLE_CONFIG="${repo_dir}/ansible.cfg"
export ANSIBLE_VERSION="${ANSIBLE_VERSION:-docker}"

case "${mode}" in
  syntax)
    exec ansible-playbook -i "${inventory_file}" --syntax-check main.yml "$@"
    ;;
  integration)
    exec ansible-playbook -i "${inventory_file}" --connection=local --become -e update_cache=1 -v main.yml "$@"
    ;;
  *)
    echo "Usage: run-ansistrano-tests [syntax|integration] [extra ansible-playbook args...]" >&2
    exit 2
    ;;
esac
