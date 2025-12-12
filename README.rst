.. image:: {{cookiecutter.pypi_package_name}}/docs/images/cookie_cutter_banner.png
    :alt: CookieCutter Banner
    :width: 75%

=======================================
Cookiecutter PyPackage (custom version)
=======================================

[Cookiecutter](https://github.com/cookiecutter/cookiecutter) template for a Python package.

V1 of readme from [https://github.com/audreyfeldroy/cookiecutter-pypackage/](github.com/audreyfeldroy/cookiecutter-pypackage/)

.. contents::

*   GitHub repo: [https://github.com/audreyfeldroy/cookiecutter-pypackage/](https://github.com/audreyfeldroy/cookiecutter-pypackage/)
*   Free software: MIT license

Features
========

*   Testing setup with pytest
*   Sphinx documentation, including creation of views for code manual and notebooks
*   GitHub Actions publishing
*   GitHub Actions testing: Setup to easily test for Python 3.10, 3.11, 3.12, and 3.13
*   Auto-release to [PyPI](https://pypi.python.org/pypi) when you push a new tag to master (optional)
*   Command line interface using Typer

Quickstart
==========

Install the latest Cookiecutter if you haven't installed it yet:

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/audreyfeldroy/cookiecutter-pypackage.git
```

Then:

*   Create a repo and put it there.
*   [Register](https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives) your project with PyPI.
*   Add the repo to your [Read the Docs](https://readthedocs.io/) account + turn on the Read the Docs service hook.
*   Release your package by pushing a new tag to master.

