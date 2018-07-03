SHELL := /bin/bash
.PHONY: deploy deploy_key package
deploy: check-env
	if [ $(ENV) = "prod" ]; then \
		source config/prod.sh; \
	else \
		source config/dev.sh; \
	fi; \
	source secrets/secrets.sh; \
	source secrets/slack.sh; \
	cd deploy/topology/; \
	terraform init -backend-config="key=topology-$(ENV)" -backend-config="bucket=bailiff" -backend-config="region=eu-west-1"; \
	terraform apply -auto-approve;

deploy_key: check-env
	source secrets/secrets.sh; \
	cd deploy/kms/; \
	terraform init; \
	terraform apply -auto-approve;

destroy: check-env
	if [ $(ENV) = "prod" ]; then \
		source config/prod.sh; \
	else \
		source config/dev.sh; \
	fi; \
	source secrets/secrets.sh; \
	source secrets/slack.sh; \
	cd deploy/topology/; \
	terraform init -backend-config="key=topology-$(ENV)" -backend-config="bucket=bailiff" -backend-config="region=eu-west-1"; \
	terraform destroy

destroy_key: check-env
	source secrets/secrets.sh; \
	cd deploy/kms/; \
	terraform init; \
	terraform destroy

package: check-env
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
