# -*- coding: utf-8 -*-
"""Example  docstrings.

This module tests the generation of a cookiecutter project.

.. Python Style Guide:
    STYLEGUIDE.md
"""

import os
import re

import pytest
from binaryornot.check import is_binary
from io import open

PATTERN = '{{(\\s?cookiecutter)[.](.*?)}}'
RE_OBJ = re.compile(PATTERN)

@pytest.fixture
def context():
    return {
        'full_name': 'Test Author',
        'github_username': 'lacion',
        'app_name': 'MyTestProject',
        'project_short_description': 'A short description of the project.',
        "docker_hub_username": "lacion",
        "docker_image": "golang:latest",
        "docker_build_image": "gobuildimage",
        "use_docker": "y",
        "use_git": "y",
        "use_logrus_logging": "y",
        "use_viper_config": "y"
}

def build_files_list(root_dir: str) -> list:
    """
    Build a list containing absolute paths to the generated files.
    
    Args:
        root_dir (type): description
    
    Returns:
        list: of absolute paths to the generated files
    """
    return [
        os.path.join(dirpath, file_path)
        for dirpath, _, files in os.walk(root_dir)
        for file_path in files
    ]

def check_paths(paths):
    """
    Method to check all paths have correct substitutions, used by other tests
    cases
    
    Args:
        paths (List[str]): list of paths to check
    """
    # Assert that no match is found in any of the files
    for path in paths:
        if is_binary(path):
            continue
        for line in open(path, 'r', encoding="latin-1"):
            match = RE_OBJ.search(line)
            msg = 'cookiecutter variable not replaced in {}'
            assert match is None, msg.format(path)

def test_default_configuration(cookies, context):
    """
    function description
    
    Args:
        cookies (type): description
        context (type): description
    """
    result = cookies.bake(extra_context=context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == context['app_name']
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)

@pytest.fixture(params=['use_docker', 'use_git', 'use_logrus_logging', 'use_viper_config'])
def feature_context(request, context):
    """
    function description
    
    Args:
        request (type): description
        context (type): description
    
    Returns:
        type: description
    """
    context.update({request.param: 'n'})
    return context

def test_disable_features(cookies, feature_context):
    """
    function description
    
    Args:
        cookies (type): description
        feature_context (type): description
    """
    result = cookies.bake(extra_context=feature_context)
    assert result.exit_code == 0
    assert result.exception is None
    assert result.project.basename == feature_context['app_name']
    assert result.project.isdir()

    paths = build_files_list(str(result.project))
    assert paths
    check_paths(paths)