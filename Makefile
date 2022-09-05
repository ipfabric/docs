IMAGE=registry.gitlab.com/autoboss/docs
TAG=8.4.2

serve:
	docker run -it --rm --name mkdocs -p 8000:8000 -v $(CURDIR):/docs $(IMAGE):$(TAG)

docker-build: Dockerfile requirements.txt
	docker build -t $(IMAGE):$(TAG) .
	docker tag $(IMAGE):latest $(IMAGE):$(TAG)
	touch docker-build-stamp

docker-push: docker-build
	docker push $(IMAGE):$(TAG)
	docker push $(IMAGE):latest
