# Docker image registry for the documentation site (used by CI/CD and local preview)
IMAGE=registry.gitlab.com/ip-fabric/documentation/docs

# Image tag — current production image
# Update this when building a new Docker image
TAG=9.7.0-insiders-4.53.18

# Vale linter release URL for documentation style checking
VALE_RELEASE=https://github.com/errata-ai/vale/releases/download/v3.9.1/vale_3.9.1_Linux_64-bit.tar.gz

.PHONY: mike vale serve

# Run local docs preview in Docker container (uses mkdocs.yml by default)
# Mounts current directory into the container for live editing
serve:
	docker run -it --rm -u $(shell id -u):$(shell id -g) --name mkdocs -p 8000:8000 -v $(CURDIR):/docs $(IMAGE):$(TAG)

# Create/update Python virtual environment from requirements.txt
venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

# Prepare local environment for mike (version deployment tool)
# After running, activate with: source venv/bin/activate
# Then deploy with: mike deploy --push <version>
# Note: Since mkdocs-material Insiders is now free and included in the
# community edition (v9.5+), no separate Insiders installation is needed.
# See: https://squidfunk.github.io/mkdocs-material/blog/2025/11/11/insiders-now-free-for-everyone/
mike: venv

# Run Vale linter on all documentation markdown files
# Excludes auto-generated release notes and archived content
vale: /tmp/vale/vale
	find docs temp_multirepo -name "*.md" \! -regex ".*/release_notes_low-level/.*" \! -regex ".*/previous_releases/.*" | xargs /tmp/vale/vale

# Download and extract Vale binary
/tmp/vale/vale:
	rm -rf /tmp/vale && mkdir /tmp/vale
	curl --fail -L -o /tmp/vale/vale.tar.gz "$(VALE_RELEASE)"
	tar -C /tmp/vale -zxvf /tmp/vale/vale.tar.gz

# Helper: ensure an environment variable is set (used by docker-build)
guard-%:
	@ if [ -z "${${*}}" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

# Build Docker image for docs site (all deps installed via requirements.txt)
# Tags with both version (for pinning) and latest (for CI/CD)
# Used by CI/CD pipeline and 'make serve' for local preview
docker-build: Dockerfile requirements.txt
	docker build -t $(IMAGE):$(TAG) .
	docker tag $(IMAGE):$(TAG) $(IMAGE):latest

# Push Docker image to GitLab container registry (both version tag and latest)
docker-push:
	docker push $(IMAGE):$(TAG)
	docker push $(IMAGE):latest

