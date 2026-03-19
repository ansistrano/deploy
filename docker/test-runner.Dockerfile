FROM python:3.12-slim-bookworm

ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        bash \
        ca-certificates \
        git \
        mercurial \
        openssh-client \
        rsync \
        subversion \
        sudo \
        tar \
        unzip \
    && rm -rf /var/lib/apt/lists/*

RUN python -m pip install --upgrade pip \
    && python -m pip install ansible-core

RUN ansible-galaxy collection install ansible.posix community.general

COPY docker/run-tests.sh /usr/local/bin/run-ansistrano-tests
RUN chmod +x /usr/local/bin/run-ansistrano-tests

WORKDIR /workspace/deploy

ENTRYPOINT ["/usr/local/bin/run-ansistrano-tests"]
CMD ["integration"]
