@ECHO OFF
REM Makefile for project needs
REM Author: Ben Trachtenberg
REM Version: 1.0.2
REM

IF "%1" == "all" (
    uv run black ansible_collection\hooks\
    uv run black ansible_collection\tests\
    uv run black go\hooks\
    uv run black go\tests\
    uv run black python_fastapi_openapi\hooks\
    uv run black python_fastapi_openapi\tests\
    uv run black python_library\hooks\
    uv run black python_library\tests\
    uv run pylint ansible_collection\hooks\
    uv run pylint go\hooks\
    uv run pylint python_fastapi_openapi\hooks\
    uv run pylint python_library\hooks\
    uv run pytest --cov --cov-report=html -vvv
    uv run bandit -c pyproject.toml -r .
    uv export --no-dev --no-emit-project --no-editable > requirements.txt
	uv export --no-emit-project --no-editable > requirements-dev.txt
    uv run pip-audit -r requirements.txt
    GOTO END
)

IF "%1" == "coverage" (
    uv run pytest --cov --cov-report=html -vvv
    GOTO END
)

IF "%1" == "pylint" (
    uv run pylint ansible_collection\hooks\
    uv run pylint go\hooks\
    uv run pylint python_fastapi_openapi\hooks\
    uv run pylint python_library\hooks\
    GOTO END
)

IF "%1" == "pytest" (
    uv run pytest --cov -vvv
    GOTO END
)

IF "%1" == "black" (
    uv run black ansible_collection\hooks\
    uv run black ansible_collection\tests\
    uv run black go\hooks\
    uv run black go\tests\
    uv run black python_fastapi_openapi\hooks\
    uv run black python_fastapi_openapi\tests\
    uv run black python_library\hooks\
    uv run black python_library\tests\
    GOTO END
)

IF "%1" == "security" (
    uv run bandit -c pyproject.toml -r .
    GOTO END
)

IF "%1" == "vulnerabilities" (
    uv run pip-audit -r requirements.txt
    GOTO END
)

IF "%1" == "pip-export" (
	uv export --no-dev --no-emit-project --no-editable > requirements.txt
	uv export --no-emit-project --no-editable > requirements-dev.txt
    GOTO END
)

@ECHO make options
@ECHO     coverage  To run coverage and display ASCII and output to htmlcov
@ECHO     black     To format the code with black
@ECHO     pylint    To run pylint
@ECHO     pytest    To run pytest with verbose option

:END
