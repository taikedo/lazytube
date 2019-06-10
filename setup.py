from setuptools import setup, find_packages

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="lazytube",
    version="0.1.0",
    description="generate minimal text-heavy videos",
    long_description=readme,
    author="Logan O'Hara",
    author_email="taikedo@protonmail.com",
    url="https://github.com/taikedo/lazytube",
    license=license,
    packages=find_packages()
)
