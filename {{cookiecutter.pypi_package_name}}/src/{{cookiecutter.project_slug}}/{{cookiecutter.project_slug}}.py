"""Main module. Example usage: ``{{cookiecutter.project_slug}}.hiya()``, which is equal to ``{{cookiecutter.project_slug}}.{{cookiecutter.project_slug}}.hiya()``"""

from . import utils

def hiya(name=None):
    """Greet the user by delegating to ``utils.hello_world``.

    Args:
        name (str | None): Optional name to personalize the greeting.

    Returns:
        str: Greeting message emitted by ``utils.hello_world``.
    """
    return utils.hello_world(name=name)

if __name__ == "__main__":
    print('Please use "python -m {{cookiecutter.project_slug}}" for the standalone version of {{cookiecutter.project_slug}}.')
