# -*- coding: utf-8 -*-
from ..parsers.abstract import AbstractRouter
from pathlib import PurePath

def test_AbstractRouter():
    file_extension = ".py"
    current_paths = AbstractRouter(
        project_path="./tests/tests_data/",
        file_extension=file_extension,
    ).router()

    expected_paths = {
        file_extension: [
            PurePath('submodule/3_module.py'),
            PurePath('submodule/__init__.py'),
            PurePath('1_module.py'),
            PurePath('2_module.py'),
            PurePath('__init__.py'),
        ]
    }

    assert current_paths == expected_paths