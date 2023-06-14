import pathlib

from setuptools import find_packages, setup

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

setup(
    name="pys-django-issue-tracker",
    version="1.0.0",
    author="Pysquad",
    author_email="vh@pysquad.com",
    description="Django Issue tracker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pys-info/pys-issue-tracker",
    install_requires=[line.strip() for line in open("requirements.txt")],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 3.0",
        "Framework :: Django :: 3.1",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Django :: 4.2",
    ],
    keywords="django, issue, tracker, development",
    packages=find_packages(exclude=("example")),
    python_requires=">=3.5",
    project_urls={
        "Bug Reports": "",
        "Funding": "",
        "Say Thanks!": "",
        "Source": "https://github.com/pys-info/pys-issue-tracker",
    },
)
