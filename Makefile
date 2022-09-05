IMAGE=registry.gitlab.com/autoboss/docs
TAG=8.4.2-insiders-4.22.0

serve:
	docker run -it --rm --name mkdocs -p 8000:8000 -v $(CURDIR):/docs $(IMAGE):$(TAG)

guard-%:
	@ if [ -z "${${*}}" ]; then \
		echo "Environment variable $* not set"; \
		exit 1; \
	fi

docker-build: guard-GL_DEPLOY_USER guard-GL_DEPLOY_TOKEN Dockerfile requirements.txt
	docker build -t $(IMAGE):$(TAG) --build-arg GL_DEPLOY_USER="${GL_DEPLOY_USER}" --build-arg GL_DEPLOY_TOKEN="${GL_DEPLOY_TOKEN}" --build-arg MATERIAL_TAG="$(TAG)" .
	docker tag $(IMAGE):$(TAG) $(IMAGE):latest

docker-push:
	docker push $(IMAGE):$(TAG)
	docker push $(IMAGE):latest
