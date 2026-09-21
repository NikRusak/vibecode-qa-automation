import json


def compare_json(baseline_path: str, current_path: str) -> dict:
    """
    Compare two JSON files and return differences.

    Args:
        baseline_path: Path to baseline.json
        current_path: Path to current.json

    Returns:
        Dictionary with differences
    """
    with open(baseline_path, 'r') as f:
        baseline = json.load(f)

    with open(current_path, 'r') as f:
        current = json.load(f)

    return _compare_recursive(baseline, current)


def _compare_recursive(baseline, current, path="") -> dict:
    """Recursively compare two objects."""
    diff = {}

    if isinstance(baseline, dict) and isinstance(current, dict):
        # Check all keys in baseline
        for key in baseline:
            new_path = f"{path}.{key}" if path else key
            if key not in current:
                diff[new_path] = {"removed": baseline[key]}
            elif baseline[key] != current[key]:
                if isinstance(baseline[key], dict) and isinstance(current[key], dict):
                    nested_diff = _compare_recursive(baseline[key], current[key], new_path)
                    diff.update(nested_diff)
                else:
                    diff[new_path] = {"old": baseline[key], "new": current[key]}

        # Check for new keys in current
        for key in current:
            if key not in baseline:
                new_path = f"{path}.{key}" if path else key
                diff[new_path] = {"added": current[key]}

    elif baseline != current:
        diff[path] = {"old": baseline, "new": current}

    return diff
