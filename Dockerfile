# Documentation site build image
# All MkDocs plugins and mkdocs-material (formerly Insiders, now free community edition)
# are installed via requirements.txt — no private mirror or token needed.
# See: https://squidfunk.github.io/mkdocs-material/blog/2025/11/11/insiders-now-free-for-everyone/
FROM python:3.11-alpine

ENV PACKAGES=/usr/local/lib/python3.11/site-packages
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /tmp

COPY requirements.txt requirements.txt

# Install system dependencies required by mkdocs-material (cairo for social cards,
# git for git-revision-date plugin, openssh for multirepo plugin fetching private repos)
RUN \
  apk upgrade --update-cache -a \
  && \
  apk add --no-cache \
  bash \
  cairo \
  curl \
  gcompat \
  findutils \
  freetype-dev \
  git \
  git-fast-import \
  jpeg-dev \
  libgcc \
  libstdc++ \
  libxml2 \
  libxslt \
  make \
  openssh \
  zlib-dev \
  && \
  apk add --no-cache --virtual .build \
  gcc \
  libffi-dev \
  libxml2-dev \
  libxslt-dev \
  musl-dev

# Install all Python dependencies (mkdocs, material theme, plugins)
# Build-only system packages are removed after pip install to reduce image size
RUN \
  pip install --no-cache-dir -r requirements.txt \
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
# Needed because /docs is a bind-mounted volume from the host
RUN git config --global --add safe.directory /docs

# Set working directory -- mount your docs repository here
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8000

# Start development server by default (uses mkdocs.yml)
# --dirtyreload only rebuilds changed pages for faster feedback during editing
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000", "--dirtyreload"]
