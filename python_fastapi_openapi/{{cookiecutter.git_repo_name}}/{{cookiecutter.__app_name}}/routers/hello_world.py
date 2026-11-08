"""
Hello World Example # FIXME: This is an example you should delete it
"""

from pathlib import Path
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
)

templates_path = Path(__file__).parent.parent.joinpath("templates").resolve().as_posix()
templates = Jinja2Templates(directory=templates_path)


@router.get('/hello', response_class=HTMLResponse, response_model=None,
            description='Hello World', name='Hello World', include_in_schema=False)
async def get_hello(request: Request) -> templates.TemplateResponse:
    """Function to display the Hello World

    :param request: The request from the user

    :returns: The webpage
    """
    error = None

    try:
        pass

    except Exception as err:  # pylint: disable=broad-except
        error = f'{err}'

    data = {
        'page': 'Hello World from {{ cookiecutter.git_repo_name }}',
        'error': error
    }
    return templates.TemplateResponse(request=request, name='index.jinja2', context={'request': request, 'data': data})


@router.get('/hello-error', response_class=HTMLResponse, response_model=None,
            description='Hello World', name='Hello World', include_in_schema=False)
async def get_hello_error(request: Request) -> templates.TemplateResponse:
    """Function to display the Hello World

    :param request: The request from the user

    :returns: The webpage
    """
    error = 'OH NO THERE WAS SOME ERROR!!'

    try:
        pass

    except Exception as err:  # pylint: disable=broad-except
        error = f'{err}'

    data = {
        'page': 'Hello World Error from {{ cookiecutter.git_repo_name }}',
        'error': error
    }
    return templates.TemplateResponse(request=request, name='index.jinja2', context={'request': request, 'data': data})
