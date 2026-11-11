"""
CLI for {{cookiecutter.__app_name}}
"""
from argparse import ArgumentParser
import uvicorn


def cli_argument_parser() -> ArgumentParser:
    """Function to create the argument parser

    :returns: The argument parser
    """
    arg_parser = ArgumentParser(description='{{cookiecutter.git_repo_name}}-cli')
    subparsers = arg_parser.add_subparsers(title='commands', description='Valid commands: a single command is required',
                                           help='CLI Help', dest='a single command please see the -h option')
    subparsers.required = True

    # This is the sub parser to start the MCP with https transport
    arg_parser_http = subparsers.add_parser('http', help='Start FastMCP in http transport')
    arg_parser_http.set_defaults(which_sub='http')
    arg_parser_http.add_argument('-b', '--bind', required=False, default="127.0.0.1", help='Bind address default: 127.0.0.1')
    arg_parser_http.add_argument('-p', '--port', required=True, help='TCP Port')

    # This is the sub parser to start the MCP with stdio transport
    arg_parser_stdio = subparsers.add_parser('stdio', help='Start FastMCP in stdio transport')
    arg_parser_stdio.set_defaults(which_sub='stdio')

    return arg_parser

def cli() -> None:
    """Function to run the command line

    :returns: Nothing it is the CLI
    """
    arg_parser = None

    try:
        arg_parser = cli_argument_parser()

        args = arg_parser.parse_args()

        if args.which_sub == 'http':
            uvicorn.run('{{cookiecutter.__app_name}}:web_app',
                        host=args.bind, port=int(args.port))

        if args.which_sub == 'stdio':
            pass

    except AttributeError as error:
        print(f'\n !!! {error} !!! \n')
        if isinstance(arg_parser, ArgumentParser):
            arg_parser.print_help()

    except FileNotFoundError as error:
        print(f'\n !!! {error} !!! \n')
        if isinstance(arg_parser, ArgumentParser):
            arg_parser.print_help()

    except FileExistsError as error:
        print(f'\n !!! {error} !!! \n')
        if isinstance(arg_parser, ArgumentParser):
            arg_parser.print_help()

    except Exception as error:  # pylint: disable=broad-exception-caught
        print(f'\n !!! {error} !!! \n')
        if isinstance(arg_parser, ArgumentParser):
            arg_parser.print_help()
