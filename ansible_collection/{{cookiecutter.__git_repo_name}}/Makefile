# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.3
#

.PHONY: all info coverage pytest black yamllint check-security check-vuln pip-export checkov ansible-lint

info:
	@echo "make options"
	@echo "    ansible-lint      To run ansible lint"
	@echo "    black             To format code with black"
	@echo "    coverage          To run coverage and display ASCII and output to htmlcov"
	@echo "    pytest            To run pytest with verbose option"
	@echo "    yamllint          To lint yaml"
	@echo "    check-vuln        To check for vulnerabilities in the dependencies"
	@echo "    check-security    To check for vulnerabilities in the code"
	@echo "    checkov           To check for vulnerabilities using checkov"
{% if cookiecutter.package_manager == 'uv' %}	@echo "    pip-export          To export the requirements to requirements.txt and requirements-dev.txt"{% endif %}

{% if cookiecutter.package_manager == 'pip' %}

all: black ansible-lint yamllint checkov coverage check-security check-vuln

coverage:
	@pytest --cov --cov-report=html -vvv

pytest:
	@pytest --cov -vvv

black:
	@black plugins/
	@black tests/

yamllint:
	@yamllint ./

check-vuln:
	@pip-audit -r requirements.txt

check-security:
	@bandit -c pyproject.toml -r .

checkov:
	@checkov --config-file .checkov.yml

ansible-lint:
	@ansible-lint

{% elif cookiecutter.package_manager == 'uv' %}

all: black ansible-lint yamllint checkov coverage check-security

coverage:
	@uv run pytest --cov --cov-report=html -vvv

pytest:
	@uv run pytest --cov -vvv

black:
	@uv run black plugins/
	@uv run black tests/

yamllint:
	@uv run yamllint ./

check-security:
	@uv run bandit -c pyproject.toml -r .

checkov:
	@uv run checkov --config-file .checkov.yml

ansible-lint:
	@uv run ansible-lint

pip-export:
	@uv export --no-dev --no-emit-project --no-editable > requirements.txt
	@uv export --no-emit-project --no-editable > requirements-dev.txt

{% endif %}
