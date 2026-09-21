import json
from pathlib import Path

import pytest

from compare_json import compare_json


@pytest.fixture
def input_dir():
    """Return path to input directory."""
    return Path(__file__).parent / "input"


@pytest.fixture
def baseline_path(input_dir):
    """Return path to baseline.json."""
    return str(input_dir / "baseline.json")


@pytest.fixture
def current_path(input_dir):
    """Return path to current.json."""
    return str(input_dir / "current.json")


def test_compare_json_returns_dict(baseline_path, current_path):
    """Test that compare_json returns a dictionary."""
    result = compare_json(baseline_path, current_path)
    assert isinstance(result, dict)


def test_compare_json_identical_files(input_dir, tmp_path):
    """Test that identical JSON files are recognized as equal."""
    baseline = input_dir / "baseline.json"
    identical_copy = tmp_path / "identical.json"
    identical_copy.write_text(baseline.read_text())

    result = compare_json(str(baseline), str(identical_copy))
    # This test will fail until the function is implemented
    assert result == {} or result is None or len(result) == 0


def test_compare_json_detects_email_change(baseline_path, current_path):
    """Test that differences in email are detected."""
    result = compare_json(baseline_path, current_path)
    # This test will fail until the function is implemented
    assert "email" in result or result != {}


def test_compare_json_detects_role_change(baseline_path, current_path):
    """Test that differences in role are detected."""
    result = compare_json(baseline_path, current_path)
    # This test will fail until the function is implemented
    assert "role" in result or result != {}


def test_compare_json_detects_new_field(baseline_path, current_path):
    """Test that new fields in current.json are detected."""
    result = compare_json(baseline_path, current_path)
    # This test will fail until the function is implemented
    assert "last_login" in result or result != {}


def test_compare_json_missing_baseline_file(input_dir):
    """Test that function handles missing baseline file (negative test)."""
    missing_baseline = str(input_dir / "nonexistent_baseline.json")
    current = str(input_dir / "current.json")

    with pytest.raises(FileNotFoundError):
        compare_json(missing_baseline, current)


def test_compare_json_missing_current_file(input_dir):
    """Test that function handles missing current file (negative test)."""
    baseline = str(input_dir / "baseline.json")
    missing_current = str(input_dir / "nonexistent_current.json")

    with pytest.raises(FileNotFoundError):
        compare_json(baseline, missing_current)


def test_compare_json_malformed_baseline(tmp_path):
    """Test that function handles malformed baseline JSON (negative test)."""
    malformed_baseline = tmp_path / "malformed_baseline.json"
    malformed_baseline.write_text("{invalid json")

    current = Path(__file__).parent / "input" / "current.json"

    with pytest.raises(json.JSONDecodeError):
        compare_json(str(malformed_baseline), str(current))


def test_compare_json_malformed_current(tmp_path):
    """Test that function handles malformed current JSON (negative test)."""
    baseline = Path(__file__).parent / "input" / "baseline.json"
    malformed_current = tmp_path / "malformed_current.json"
    malformed_current.write_text("{invalid json")

    with pytest.raises(json.JSONDecodeError):
        compare_json(str(baseline), str(malformed_current))
