FROM python:3.11-alpine

ENV PACKAGES=/usr/local/lib/python3.11/site-packages
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /tmp

COPY docs/requirements.txt requirements.txt

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

RUN \
  pip install --no-cache-dir -r requirements.txt \
  && \
  pip install --no-cache-dir watchdog[watchmedo] \
  && \
  apk del .build \
  && \
  rm -rf /tmp/* /root/.cache \
  && \
  find "${PACKAGES}" \
  -type f \
  -path "*/__pycache__/*" \
  -exec rm -f {} \;

# Set working directory -- mount your directory here
WORKDIR /docs

# Expose MkDocs development server port
EXPOSE 8001

# Start development server by default
CMD ["mkdocs", "serve", "--config-file=/mkdocs.yml", "--dev-addr=0.0.0.0:8001", "--dirtyreload"]
