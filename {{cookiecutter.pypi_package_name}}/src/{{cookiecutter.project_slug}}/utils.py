"""Utility functions important for loading and processing PDB files. 
Functions following ``calculate_dihedral_angle()`` are probably not very 
interesting to most."""


def hello_world(name=None):
    """Print a greeting to stdout.

    Args:
        name (str | None): Name to greet. Prints a generic greeting when omitted.

    Returns:
        None
    """
    printme = "HELLO WORLD! THIS IS {{cookiecutter.project_slug}}!"
    if not name is None:
        printme = f"HELLO {name}! THIS IS {{cookiecutter.project_slug}}!"
    #
    print(printme)
    return printme
