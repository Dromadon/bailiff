SHELL := /bin/bash
.PHONY: deploy deploy_key package
deploy: check-env
	source secrets/secrets.sh; \
	source secrets/slack.sh; \
	cd deploy/; \
	./wrapper.sh apply $(ENV) topology

deploy_key: check-env
	source secrets/secrets.sh; \
	cd deploy/; \
	./wrapper.sh apply $(ENV) kms

destroy: check-env
	source secrets/secrets.sh; \
	cd deploy/
	./wrapper.sh destroy $(ENV) topology

destroy_key: check-env
	source secrets/secrets.sh; \
	cd deploy/; \
	./wrapper.sh destroy $(ENV) kms

package:
	mkdir -p /tmp/bailiff_package/; \
	cp -r bailiff/* /tmp/bailiff_package/; \
	cp -r venv/lib/python3.6/site-packages/* /tmp/bailiff_package/; \
	pushd /tmp/bailiff_package/; \
	zip -r package.zip *; \
	popd; \
	cp /tmp/bailiff_package/package.zip package/package.zip; \
	rm -r /tmp/bailiff_package/;

check-env:
ifndef ENV
  $(error ENV is undefined)
endif
