.PHONY: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

NFT_API_LIBRARY_CONFIG_FILE		?= nf_tower_api_library_generator_config.yml
NFT_API_SCHEMA_FILE				?= nf_tower_openapi_schema.yml
NFT_API_SCHEMA_URL				?= https://tower.nf/openapi/nextflow-tower-api-latest.yml
PY_VERSION						:= 3.9
PYPI_INDEX						?= https://pypi.org/simple
PY_VENV							?= venv
REQUIREMENTS_FILE				?= requirements.txt
SOURCE_CODE_DIR					?= nf_tower_sdk

.PHONY: init
init: venv ## Setup development environment.
	pre-commit install

.PHONY: venv
venv: ## Creates python virtual env with dependencies.
	python$(PY_VERSION) -m venv $(PY_VENV)
	source $(PY_VENV)/bin/activate && \
	python -m pip install --upgrade pip -i $(PYPI_INDEX) && \
	pip install -r $(REQUIREMENTS_FILE) -i $(PYPI_INDEX) && \
	pip install .

.PHONY: requirements
requirements: ## Install python dependencies.
	python -m pip install --upgrade pip -i $(PYPI_INDEX)
	pip install -r $(REQUIREMENTS_FILE) -i $(PYPI_INDEX)

.PHONY: nft-api-library
nft-api-library: ## Generates Nextflow Tower API library using openapi-python-client.
	cd $(SOURCE_CODE_DIR) && \
	openapi-python-client generate --path ../$(NFT_API_SCHEMA_FILE) --config ../$(NFT_API_LIBRARY_CONFIG_FILE)

.PHONY: update-api-library
update-api-library: ## Update Nextflow Tower OpenAPI library.
	curl $(NFT_API_SCHEMA_URL) --output $(NFT_API_SCHEMA_FILE)
	cd $(SOURCE_CODE_DIR) && \
	openapi-python-client update --path ../$(NFT_API_SCHEMA_FILE) --config ../$(NFT_API_LIBRARY_CONFIG_FILE)

.PHONY: clean
clean: ## Cleanup build and test objects.
	rm -f .coverage coverage.xml
	rm -rf build .pytest_cache $(SOURCE_CODE_DIR).egg-info
	python -Bc "import pathlib; import shutil; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"

.PHONY: test
test: clean ## Run unit tests with pytest.
	pip install .[test]
	pytest
