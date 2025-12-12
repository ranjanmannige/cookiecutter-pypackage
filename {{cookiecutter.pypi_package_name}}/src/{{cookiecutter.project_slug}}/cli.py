"""Console script for backmap. 

This section provides a more detailed description of what the module does,
its main functionalities, and any important context or background information.
It can span multiple paragraphs.


Usage: python -m backmap --pdbfn <filename/dirname> <other options>

Args:
    pdbfn: Location of a PDB file or a directory containing PDB file(s). 
        Single file can contain multiple structures separated by the MODEL term.
    output-dir: Where the generated figures will be stored. If absent, a 
        report dir will be placed in the PDBs parent directory.                                                     
    no-write: Don't write figures to the report directory. [default: True]                      
    no-show: Don't show figures while the app is running. [default: True]                      
    signed: Use the signed Ramachandran plot. [default: False]                                                 
    colortype: Graph coloring options (options: ['Chirality ', 'SecondaryStructure']).
        [default: Chirality]                                                
    help: Print the available options.
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


@app.command(epilog="Made with :heart: by [blue]Ranjan Mannige[/blue]")
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
