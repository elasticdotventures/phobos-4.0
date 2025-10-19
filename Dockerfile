# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.11
FROM python:${PYTHON_VERSION}-slim AS phobos-base

ENV DEBIAN_FRONTEND=noninteractive \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       git \
       ca-certificates \
       wget \
       libgl1 \
       libx11-6 \
       libxi6 \
       libxxf86vm1 \
       libxrender1 \
       libxfixes3 \
       libxrandr2 \
       libxtst6 \
       libxcomposite1 \
       libxdamage1 \
       libglu1-mesa \
    && rm -rf /var/lib/apt/lists/*

# Install headless Blender runtime through the official wheels.
ARG BPY_VERSION=4.2.0
RUN pip install --no-cache-dir "bpy==${BPY_VERSION}"

WORKDIR /opt/phobos
COPY . /opt/phobos

# Install Phobos and its dependencies.
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -e .

# Expose the add-on to Blender by default.
ENV PHOBOS_SOURCE=/opt/phobos/phobos \
    BLENDER_USER_SCRIPTS=/opt/blender-user-scripts

RUN mkdir -p "${BLENDER_USER_SCRIPTS}/addons" \
    && ln -s /opt/phobos/phobos "${BLENDER_USER_SCRIPTS}/addons/phobos"

ENTRYPOINT ["phobos"]
CMD ["--help"]
