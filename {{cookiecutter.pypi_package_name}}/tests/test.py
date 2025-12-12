#!/usr/bin/env python
import pytest, sys, glob
#from matplotlib.figure import Figure # to assert the returning of a proper figure
import matplotlib.pyplot as plt
import matplotlib as mpl # currently imported to compare returned axes object to mpl.axes.Axes
import matplotlib.figure

import backmap

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
    Test with no name, when accessed via backmap.utils
    """
    expected_return = "HELLO WORLD! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = backmap.utils.hello_world()
    assert returned_str == expected_return
#


def test_hello_world_named1():
    """ 
    Test with no name, when accessed via backmap.utils
    """
    name = 'Popeye'
    expected_return = f"HELLO {name}! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = backmap.utils.hello_world(name = name)
    assert returned_str == expected_return


def test_hello_world_simple2():
    """ 
    Test with no name, when accessed via backmap.utils
    """
    expected_return = "HELLO WORLD! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = backmap.hiya()
    assert returned_str == expected_return
#


def test_hello_world_named2():
    """ 
    Test with no name, when accessed via backmap
    """
    name = 'Popeye'
    expected_return = f"HELLO {name}! THIS IS {{cookiecutter.project_slug}}!"
    returned_str = backmap.hiya(name = name)
    assert returned_str == expected_return



