import os
import sys

import pytest

from will.utils import find_module_path, load_source


def test_find_module_path_for_package():
    path = find_module_path("will.backends.analysis.nothing")

    assert os.path.isdir(path)
    assert path.endswith(os.path.join("will", "backends", "analysis"))


def test_find_module_path_raises_for_missing_module():
    with pytest.raises(ImportError):
        find_module_path("will.module_that_does_not_exist")


def test_load_source_from_file(tmp_path):
    module_name = "will_test_dynamic_module"
    module_path = tmp_path / "dynamic_module.py"
    module_path.write_text("VALUE = 'loaded'\n")

    module = load_source(module_name, str(module_path))

    assert module.VALUE == "loaded"
    assert sys.modules[module_name] is module
