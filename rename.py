from pathlib import Path
import argparse
import re

from loguru import logger


def rename_dir(new_name: str):
    original_package = "starter"
    new_name = sanitize_name(new_name)

    Path(original_package).rename(new_name)
    logger.success(f"Renamed directory {original_package} to {new_name}")


def rename_pyproject_toml(new_name: str):
    """Update the package name in pyproject.toml

    Args:
            new_name (str): The new name of the package
    """
    with open("pyproject.toml", "r") as file:
        data = file.read()

    new_name = sanitize_name(new_name)
    data = re.sub(r'"starter"', f'"{new_name}"', data)

    # Write the TOML file back out
    with open("pyproject.toml", "w") as file:
        file.write(data)

    logger.success(f"Updated pyproject.toml package name to {new_name}")


def sanitize_name(name: str):
    # Replace spaces and hyphens with underscores
    name = name.replace(" ", "_")
    name = name.replace("-", "_")
    return name


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("new_name", help="The new name of the project")

    args = parser.parse_args()
    new_name = args.new_name

    rename_dir(new_name)
    rename_pyproject_toml(new_name)
