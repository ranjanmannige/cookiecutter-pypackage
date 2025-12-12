
# {{cookiecutter.full_name}}'s awesome new Python package!
.. image:: docs/images/cookie_cutter_banner.png
    :alt: CookieCutter Banner
    :width: 75%

Heading 1
=========

Material 1


Installation
============

PIP Installation
-----------------

Running the following at a command prompt (terminal) would get the job done (the '-I' is not necessary, but ensures the latest sub-version is installed):

.. code-block:: bash

    $ pip install -I {{cookiecutter.project_slug}}


GIT Installation
----------------

.. code-block:: bash

    $ git clone https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}.git
    $ cd {{cookiecutter.project_slug}}
    $ pip install .
    # For testing
    $ pip install pytest
    $ pytest


Manual Installation
-------------------

Manually download the source code (`main.zip <https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/archive/refs/heads/main.zip>`_) from the `git repository <https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}>`_. Then, same as above:

.. code-block:: bash
    
    # In stead of downloading, you can follow the next two commands (tested only on linux)
    $ wget https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_slug}}/archive/refs/heads/main.zip
    $ unzip main.zip # Should giv you a directory called "{{cookiecutter.project_slug}}-main"
    # The rest is the same as with installing using `git clone`
    $ cd {{cookiecutter.project_slug}}-main
    $ pip install .
    # For testin
    $ pip install pytest
    $ pytest


Usage
=====

In-script usage
---------------

.. code-block:: python

    import {{cookiecutter.project_slug}}
    print({{cookiecutter.project_slug}}.utils.hello_world())
    print({{cookiecutter.project_slug}}.utils.hello_world('Popeye'))
    print({{cookiecutter.project_slug}}.hiya('Popeye'))


Standalone usage
----------------

After installation, the following commands produce a variety of graphs (exampled below).

.. code-block:: bash

    $ python -m {{cookiecutter.project_slug}} --name Popeye

