# Starter
A starter repo to get you up and running with a new project. This repo includes utilizes:

- Poetry as a package manager
- Pre-commit hooks
- CI/CD Pipeline
- Dockerfile
- Makefile
- Tests

I personally use this repo as it's a nice starting point for most new projects I start working on. Feel free to use it as well!

## Getting Started

### Prerequisites

To get started, you'll need to have the following installed on your machine:

- Python 3.11+
- Poetry
- Make

With that, you should be good to go!

### Installation

To install, you can use the cookiecutter template to create a new project. To do this, run the following command:

```bash
cookiecutter https://github.com/etav22/starter.git --checkout feat/cookiecutter
```
> Note: If you want to use the `release` step of the actions template, you will have to
> adjust the actions.yaml file and add your own secrets to the repository.

Follow the prompt and then you can get started by running the following commands:

```bash
make install
```

## Future Improvements

- Semantically version the project with [python-semantic-release](https://python-semantic-release.readthedocs.io/en/latest/) package.
