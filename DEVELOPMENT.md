## Local development

This project uses Conda to manage its dependencies. Run the following to setup your local environment:

```shell
conda env update --file environment.yml -n sagemaker-image-builder
```

## Tests

### Unit Tests

Run the following to invoke all unit tests:

```shell
pytest test/
```

## Code Style

Install pre-commit to run code style checks before each commit:

```shell
pre-commit install
```

To run formatters for all existing files, use:

```shell
pre-commit run --all-files
```

pre-commit checks can be disabled for a particular commit with git commit -n.
