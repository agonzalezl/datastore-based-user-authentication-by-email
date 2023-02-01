from setuptools import find_packages, setup


def get_description():
    with open("README.md") as file:
        return file.read()


setup(
    name="datastore-email-based-user-authentication",
    version="0.0.1",
    url="https://github.com/agonzalezl/datastore-email-based-user-authentication",
    author="Angel L. González",
    author_email="angel.gonzalez.lpz@gmail.com",
    description="Easy user authentication by email using GCP Datastore",
    long_description=get_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.6",
    install_requires=[
        "httpx >= 0.15.0",
    ],
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"email_authenticator": ["py.typed"]},
    include_package_data=True,
)
