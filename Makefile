SHELL := /bin/bash
.PHONY: deploy deploy_key package
deploy:
	source secrets/secrets.sh; \
	cd deploy/topology/; \
	terraform apply -auto-approve;

deploy_key:
	source secrets/secrets.sh; \
	cd deploy/kms/; \
	terraform apply -auto-approve;

destroy:
	source secrets/secrets.sh; \
	cd deploy/topology/; \
	terraform destroy -auto-approve;

destroy_key:
	source secrets/secrets.sh; \
	cd deploy/kms/; \
	terraform destroy -auto-approve;

package:
	mkdir -p /tmp/bailiff_package/; \
	cp -r bailiff/* /tmp/bailiff_package/; \
	cp -r venv/lib/python3.6/site-packages/* /tmp/bailiff_package/; \
	pushd /tmp/bailiff_package/; \
	zip package.zip *; \
	popd; \
	cp /tmp/bailiff_package/package.zip package/package.zip; \
	rm -r /tmp/bailiff_package/;
