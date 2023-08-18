.DEFAULT_GOAL:=help

.PHONY: help
help: ## This help text
	@awk 'BEGIN {FS = ":.*##"; printf "Usage: make \033[36m<target>\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { while (match($$2, /`[^`]*`/)) { part = substr($$2, 1, RSTART - 1); highlighted = "\033[1;33m" substr($$2, RSTART + 1, RLENGTH - 2) "\033[0m"; rest = substr($$2, RSTART + RLENGTH); $$2 = part highlighted rest } printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

NFT_API_LIBRARY_CONFIG_FILE		?= nf_tower_api_library_generator_config.yml
NFT_API_SCHEMA_FILE				?= nf_tower_openapi_schema.yml
NFT_API_SCHEMA_URL				?= https://tower.nf/openapi/nextflow-tower-api-latest.yml
PY_VERSION						:= 3.9
PYPI_INDEX						?= https://pypi.org/simple
PY_VENV							?= venv
REQUIREMENTS_FILE				?= requirements.txt
SOURCE_CODE_DIR					?= nf_tower_sdk

.PHONY: init
init: clean requirements nf-tower-sdk ## Install project dependencies.
	pre-commit install

.PHONY: venv
venv: ## Creates python virtual env with project dependencies.
	python$(PY_VERSION) -m venv $(PY_VENV)
	source $(PY_VENV)/bin/activate && \
	python -m pip install --upgrade pip -i $(PYPI_INDEX) && \
	pip install -r $(REQUIREMENTS_FILE) -i $(PYPI_INDEX) && \
	pip install .

.PHONY: requirements
requirements: clean ## Install all python dependencies.
	python -m pip install --upgrade pip -i $(PYPI_INDEX)
	pip install -r $(REQUIREMENTS_FILE) -i $(PYPI_INDEX)

.PHONY: nf-tower-sdk
nf-tower-sdk: clean ## Install project as python package.
	python -m pip install --upgrade pip -i $(PYPI_INDEX)
	pip install .

.PHONY: nft-api-library
nft-api-library: ## Generates Nextflow Tower API library using openapi-python-client.
	cd $(SOURCE_CODE_DIR) && \
	openapi-python-client generate --path ../$(NFT_API_SCHEMA_FILE) --config ../$(NFT_API_LIBRARY_CONFIG_FILE)

.PHONY: update-api-library
update-api-library: ## Update Nextflow Tower OpenAPI library.
	cd $(SOURCE_CODE_DIR) && \
	openapi-python-client update --path ../$(NFT_API_SCHEMA_FILE) --config ../$(NFT_API_LIBRARY_CONFIG_FILE)

.PHONY: download-api-schema
download-api-schema: ## Updates `nf_tower_openapi_schema.yml` file.
	curl $(NFT_API_SCHEMA_URL) --output $(NFT_API_SCHEMA_FILE)

.PHONY: clean
clean: ## Cleanup build and test objects.
	rm -f .coverage coverage.xml
	rm -rf build .pytest_cache $(SOURCE_CODE_DIR).egg-info
	make clean_pycache

.PHONY: clean_pycache
clean_pycache:	## Cleanup any python and pytest caches.
	find . | grep -E "(__pycache__|\.pyc)" | xargs rm -rf
	find . | grep -E "(.pytest_cache)" | xargs rm -rf

.PHONY: test
test: clean nf-tower-sdk ## Install dependencies and run unit tests with pytest.
	pip install .[test]
	pytest
