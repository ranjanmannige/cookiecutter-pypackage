"""Utility functions."""


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
