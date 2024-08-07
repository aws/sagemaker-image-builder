from setuptools import setup

INSTALL_REQUIRES = [
    "boto3",
    "conda",
    # "docker-py", # commented because docker-py is not updated on pypi since 2016 - causes an older version to be installed.
    "pytest",
    "semver",
]

TESTS_REQUIRE = [
    "pytest",
    "pytest-mock",
    "pytest-xdist",
    "autoflake",
    "pre-commit",
]

EXTRAS_REQUIRE = {
    "tests": TESTS_REQUIRE,
}

setup(
    name="sagemaker-image-builder",
    version="0.0.1.dev",
    description="A tool that follows semver to automate new releases of docker images.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="SageMaker",
    packages=[
        "sagemaker_image_builder"
    ],
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    zip_safe=False,
    entry_points={
        "console_scripts": [
            "sagemaker-image-builder = sagemaker_image_builder.main:main",
        ]
    },
)
