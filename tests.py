# Usage: pytest tests.py

import pytest
from unittest.mock import mock_open, patch
from postgres_to_sqlite import open_file, remove, replace, add, convert

# Test for open_file function
def test_open_file_success():
    m = mock_open(read_data="some content")
    with patch("builtins.open", m):
        result = open_file("fake_filepath")
    assert result == "some content"

def test_open_file_failure():
    with pytest.raises(FileNotFoundError):
        open_file("nonexistent_filepath")

# Test for remove function
def test_remove():
    content = """SET something
    other thing"""
    assert remove(content, "SET") == "    other thing"

# Test for replace function
def test_replace():
    assert replace("replace true with t", "true", "t") == "replace t with t"

# Tests for add function
def test_add_top():
    assert add("content", "top", True) == "top\ncontent"

def test_add_bottom():
    assert add("content", "bottom", False) == "content\nbottom"

# Test for convert function
@patch("postgres_to_sqlite.open_file")
@patch("postgres_to_sqlite.remove")
@patch("postgres_to_sqlite.replace")
@patch("postgres_to_sqlite.add")
def test_convert(mock_add, mock_replace, mock_remove, mock_open_file):
    mock_open_file.return_value = "content"
    mock_remove.return_value = "removed content"
    mock_replace.return_value = "replaced content"
    mock_add.return_value = "added content"

    assert convert("fake_filepath") == "added content"
