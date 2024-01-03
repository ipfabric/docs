FROM python:3.11-alpine

ENV PACKAGES=/usr/local/lib/python3.11/site-packages
ENV PYTHONDONTWRITEBYTECODE=1

ARG GL_DEPLOY_USER
ARG GL_DEPLOY_TOKEN
ARG MATERIAL_TAG

WORKDIR /tmp

COPY requirements.txt requirements.txt

RUN \
  apk upgrade --update-cache -a \
  && \
  apk add --no-cache \
  bash \
  cairo \
  curl \
  freetype-dev \
  git \
  git-fast-import \
  jpeg-dev \
  libxml2 \
  libxslt \
  openssh \
  zlib-dev \
  && \
  apk add --no-cache --virtual .build \
  gcc \
  libffi-dev \
  libxml2-dev \
  libxslt-dev \
  musl-dev

RUN \
  pip install --no-cache-dir -r requirements.txt \
  && \
  pip uninstall -y mkdocs-material \
  && \
  pip install --no-cache-dir \
  "git+https://${GL_DEPLOY_USER}:${GL_DEPLOY_TOKEN}@gitlab.com/ip-fabric/documentation/mkdocs-material-insiders-mirror.git@${MATERIAL_TAG}" \
  && \
  apk del .build \
  && \
  rm -rf /tmp/* /root/.cache \
  && \
  find "${PACKAGES}" \
  -type f \
  -path "*/__pycache__/*" \
  -exec rm -f {} \;

# Trust git directory, required for git >= 2.35.2
RUN git config --global --add safe.directory /docs

# Set working directory -- mount your directory here
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default
CMD ["mkdocs", "serve", "--config-file=mkdocs_insiders.yml", "--dev-addr=0.0.0.0:8000", "--dirtyreload"]
