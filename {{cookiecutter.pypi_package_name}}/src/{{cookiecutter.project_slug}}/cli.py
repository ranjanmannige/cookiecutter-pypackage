"""Console script for {{cookiecutter.project_slug}}. 

This section provides a more detailed description of what the module does,
its main functionalities, and any important context or background information.
It can span multiple paragraphs.


Usage: python -m {{cookiecutter.project_slug}} --name "Popeye"
"""

import typer
import sys
from enum import Enum
from typing_extensions import Annotated
from rich.console import Console

from . import utils

helpme = r"""
THIS IS A CUSTOM HELP STRING

"""
if '--help' in sys.argv:
    print(helpme)

# Creating a Typer app
app = typer.Typer(add_completion=False, 
                  rich_markup_mode="rich",
                  )
console = Console()


@app.command(epilog="Made with :heart: by [blue]{{cookiecutter.full_name}}[/blue]")
def main(name:Annotated[str, typer.Option("--name", 
                                     help="""Who do you want to greet?""")],
    ):
    """Print a greeting to stdout.

    Args:
        name (str | None): Name to greet. Prints a generic greeting when omitted.

    Returns:
        None
    """
    utils.hello_world(name=name)
    #

if __name__ == "__main__":
    app()
