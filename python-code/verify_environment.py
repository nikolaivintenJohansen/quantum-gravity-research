"""Verify the pinned scientific Python environment and save machine-readable output."""

from __future__ import annotations

import argparse
import importlib.metadata
import json
import platform
from pathlib import Path

import matplotlib
import networkx
import numpy
import pandas
import pytest
import scipy
import sympy


PACKAGES = (
    numpy,
    scipy,
    sympy,
    matplotlib,
    networkx,
    pandas,
    pytest,
)


def build_report() -> dict[str, object]:
    """Return versions and deterministic algebraic smoke-test results."""
    x = sympy.symbols("x")
    symbolic_residual = sympy.simplify(sympy.diff(x**3, x) - 3 * x**2)
    matrix_determinant = int(round(numpy.linalg.det(numpy.array([[1, 2], [3, 4]]))))

    if symbolic_residual != 0:
        raise AssertionError(f"SymPy smoke test failed: {symbolic_residual}")
    if matrix_determinant != -2:
        raise AssertionError(f"NumPy smoke test failed: {matrix_determinant}")

    return {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "packages": {
            module.__name__: importlib.metadata.version(module.__name__)
            for module in PACKAGES
        },
        "checks": {
            "sympy_derivative_residual": str(symbolic_residual),
            "numpy_determinant": matrix_determinant,
        },
        "randomness_used": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = build_report()
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    print(rendered, end="")


if __name__ == "__main__":
    main()
