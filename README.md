## Amazon SageMaker Image Builder

Amazon SageMaker Image Builder is a set of tools for building, releasing, and managing Docker images.

## Installation
```bash
conda create -n sagemaker-image-builder python=3.12
conda activate sagemaker-image-builder
conda env update --file environment.yml
```

## Getting started

Before using Amazon SageMaker Image Builder to build and release your docker image, you will need to prepare for your image configuration file and image build artifacts.

### Image Configuration File

This is a JSON file including a list of image configurations. It should include the following fields:
1. (Required) `image_name`: The name of the docker image.
1. (Required) `build_args`: Including a list of docker arguments being used during docker image build.
1. (Required) `env_out_filename`: Path to output file including a list of dependency Python packages.
1. (Required) `image_type`: The type of the docker image. (e.g. cpu, gpu)
1. (Optional) `image_tag_suffix`: The image tag suffix. (e.g. -cpu, -gpu)
1. (Optional) `additional_packages_env_in_file`: Path to a file including additional input packages.
1. (Optional) `pytest_flags`: Additional flags being set when running unit tests for your images.

Here is an example image config file:
```shell
[
    {
        "image_name": "sagemaker-distribution",
        "build_args": {
            "TAG_FOR_BASE_MICROMAMBA_IMAGE": "jammy-cuda-11.8.0",
            "CUDA_MAJOR_MINOR_VERSION": "11.8",
            "ENV_IN_FILENAME": "gpu.env.in",
            "ARG_BASED_ENV_IN_FILENAME": "gpu.arg_based_env.in"
        },
        "additional_packages_env_in_file": "gpu.additional_packages_env.in",
        "image_tag_suffix": "gpu",
        "env_out_filename": "gpu.env.out",
        "image_type": "gpu"
    }
]
```

### Image Build Artifacts Folder

This is a folder including image build artifacts like docker file, input package list, etc. It should include all artifacts that are required to build your image. The name of the folder needs to be `build_artifacts`, and it should contain subfolders with exact format `build_artifacts/v{major_version}/v{minor_version}/v{patch_version}`. For example, the build artifacts for image version v0.0.1 should be stored in folder `build_artifacts/v0/v0.0/v0.0.1`.

Example build artifacts for SageMaker Distribution Images: https://github.com/aws/sagemaker-distribution/tree/main/build_artifacts

### Build Your Image

After you have image config file and build artifacts folder ready, you may start to build your image by running the following command:
```shell
VERSION=<Insert image version here. example: 0.4.2>
IMAGE_CONFIG_FILE=<Path to image config file. example: image_config.json>

sagemaker-image-builder build --target-patch-version $VERSION --image-config-file $IMAGE_CONFIG_FILE

# If you want to skip tests
sagemaker-image-builder build --target-patch-version $VERSION --image-config-file $IMAGE_CONFIG_FILE --skip-tests

# If you want to override existing image
sagemaker-image-builder build --target-patch-version $VERSION --image-config-file $IMAGE_CONFIG_FILE --force


# If you want to push the built image to AWS ECR repository:
REGION=<Your AWS region>
TARGET_ECR_REPO=<AWS ECR repository link>

sagemaker-image-builder build --target-patch-version $VERSION --image-config-file $IMAGE_CONFIG_FILE --target-ecr-repo $TARGET_ECR_REPO --region $REGION
```

### Package Staleness Report

If you want to generate/view the staleness report for each of the individual packages in a given image version, then run the following command:

```
VERSION=<Insert image version here. example: 0.4.2>
sagemaker-image-builder generate-staleness-report --target-patch-version $VERSION
```

### Package Size Delta Report

If you want to generate/view the package size delta report for a given
image version comparing to a base image version, then run the following command:

```
BASE_PATCH_VERSION=<Insert base image version here. example: 1.6.1>
VERSION=<Insert target image version here. example: 1.6.2>
sagemaker-image-builder generate-size-report --base-patch-version $BASE_PATCH_VERSION --target-patch-version $VERSION
```

## Security

See [SECURITY](SECURITY.md#security-issue-notifications) for more information.

## License

This project is licensed under the Apache-2.0 License.
