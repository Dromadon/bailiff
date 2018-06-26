SHELL := /bin/bash
.PHONY: deploy deploy_key
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
	cd bailiff/;
