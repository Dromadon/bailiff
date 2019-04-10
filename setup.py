from setuptools import setup, find_packages

setup(name="bailiff",
      version="1.1.0",
      install_requires=["boto3==1.7.14",
                        "slackclient==1.2.1",
                        "tabulate==0.8.2",
                        "requests==2.18.4"],
      packages=find_packages(exclude=("tests*", "secrets", "package", "deploy")),
      extras_require={"tests": ["pytest", "pytest-mock"]})