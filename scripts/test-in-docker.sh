#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
repo_dir="$(cd "${script_dir}/.." && pwd)"

mode="${1:-integration}"
shift || true

image_name="${ANSISTRANO_TEST_IMAGE:-ansistrano-deploy-test}"

docker build -f "${repo_dir}/docker/test-runner.Dockerfile" -t "${image_name}" "${repo_dir}"

docker_run_args=(
  run
  --rm
  -e ANSIBLE_VERSION=docker
  -v "${repo_dir}:/workspace/deploy"
)

if [ -t 0 ] && [ -t 1 ]; then
  docker_run_args+=(-it)
fi

docker "${docker_run_args[@]}" "${image_name}" "${mode}" "$@"
