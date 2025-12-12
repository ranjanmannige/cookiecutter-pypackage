#!/usr/bin/env python
import pytest, sys, glob

import {{cookiecutter.project_slug}}

"""Tests for `{{cookiecutter.project_slug}}` package."""

__author__ = "{{cookiecutter.github_username}}"
__copyright__ = "{{cookiecutter.full_name}}"
__license__ = "MIT"

# # @pytest.fixture
# # def response():
# #     """Sample pytest fixture.

# #     See more at: http://doc.pytest.org/en/latest/fixture.html

# # def test_content(response):
# #     """Sample pytest test function with the pytest fixture as an argument."""
# #     # from bs4 import BeautifulSoup
# #     # assert 'GitHub' in BeautifulSoup(response.content).title.string

def test_hello_world_simple1():
    """ 
    Test with no name, when accessed via {{cookiecutter.project_slug}}.utils
    """
    expected_return = "HELLO WORLD! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = {{cookiecutter.project_slug}}.utils.hello_world()
    assert returned_str == expected_return
#


def test_hello_world_named1():
    """ 
    Test with no name, when accessed via {{cookiecutter.project_slug}}.utils
    """
    name = 'Popeye'
    expected_return = f"HELLO {name}! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = {{cookiecutter.project_slug}}.utils.hello_world(name = name)
    assert returned_str == expected_return


def test_hello_world_simple2():
    """ 
    Test with no name, when accessed via {{cookiecutter.project_slug}} directly
    """
    expected_return = "HELLO WORLD! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = {{cookiecutter.project_slug}}.hiya()
    assert returned_str == expected_return
#


def test_hello_world_named2():
    """ 
    Test with no name, when accessed via {{cookiecutter.project_slug}} directly
    """
    name = 'Popeye'
    expected_return = f"HELLO {name}! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = {{cookiecutter.project_slug}}.hiya(name = name)
    assert returned_str == expected_return



