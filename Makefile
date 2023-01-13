IMAGE=registry.gitlab.com/ip-fabric/documentation/docs
TAG=9.0.4-insiders-4.27.1

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

guard-%:
	@ if [ -z "${${*}}" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

insiders-tag:
	git ls-remote -t --sort="version:refname" git@gitlab.com:ip-fabric/documentation/mkdocs-material-insiders-mirror.git | sed -e 's#refs/tags/##' | tail -2

docker-build: guard-GL_DEPLOY_USER guard-GL_DEPLOY_TOKEN Dockerfile requirements.txt
	docker build -t $(IMAGE):$(TAG) --build-arg GL_DEPLOY_USER="${GL_DEPLOY_USER}" --build-arg GL_DEPLOY_TOKEN="${GL_DEPLOY_TOKEN}" --build-arg MATERIAL_TAG="$(TAG)" .
	docker tag $(IMAGE):$(TAG) $(IMAGE):latest

docker-push:
	docker push $(IMAGE):$(TAG)
	docker push $(IMAGE):latest
