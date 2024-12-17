IMAGE=registry.gitlab.com/ip-fabric/documentation/docs
VALE_RELEASE=https://github.com/errata-ai/vale/releases/download/v3.9.1/vale_3.9.1_Linux_64-bit.tar.gz
TAG=9.5.49-insiders-4.53.14

.PHONY: mike vale serve

serve:
	docker run -it --rm -u $(shell id -u):$(shell id -g) --name mkdocs -p 8000:8000 -v $(CURDIR):/docs $(IMAGE):$(TAG)

venv: venv/touchfile

venv/touchfile: requirements.txt
	test -d venv || python3 -m venv venv
	. venv/bin/activate; pip install -Ur requirements.txt
	touch venv/touchfile

mike: venv
	. venv/bin/activate && pip uninstall -y mkdocs-material
	. venv/bin/activate && pip install "git+ssh://git@gitlab.com/ip-fabric/documentation/mkdocs-material-insiders-mirror.git@${TAG}"

vale: /tmp/vale/vale
	find docs temp_multirepo -name "*.md" \! -regex ".*/release_notes_low-level/.*" \! -regex ".*/previous_releases/.*" | xargs /tmp/vale/vale

/tmp/vale/vale:
	rm -rf /tmp/vale && mkdir /tmp/vale
	curl --fail -L -o /tmp/vale/vale.tar.gz "$(VALE_RELEASE)"
	tar -C /tmp/vale -zxvf /tmp/vale/vale.tar.gz

guard-%:
	@ if [ -z "${${*}}" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

insiders-tag:
	git ls-remote -t --sort="version:refname" git@gitlab.com:ip-fabric/documentation/mkdocs-material-insiders-mirror.git | grep -v 'master' | sed -e 's#refs/tags/##' | tail -2

docker-build: guard-GL_DEPLOY_USER guard-GL_DEPLOY_TOKEN Dockerfile requirements.txt
	docker build -t $(IMAGE):$(TAG) --build-arg GL_DEPLOY_USER="${GL_DEPLOY_USER}" --build-arg GL_DEPLOY_TOKEN="${GL_DEPLOY_TOKEN}" --build-arg MATERIAL_TAG="$(TAG)" .
	docker tag $(IMAGE):$(TAG) $(IMAGE):latest

docker-push:
	docker push $(IMAGE):$(TAG)
	docker push $(IMAGE):latest

