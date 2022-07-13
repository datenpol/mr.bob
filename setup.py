import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = open("README.md").read()

setup(
    name="mrbob",  #
    version="0.1.4",
    description="Bob renders directory structure templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datenpol/mr.bob",
    author="Ahmed Aly",
    author_email="ahmed.aly@datenpol.at",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="template, development",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=[
        "setuptools",
        "six",
        "ordereddict",
        "importlib",
        "Jinja2",
        "argparse"
    ],
    entry_points={
        "console_scripts": [
            "mrbob=mrbob.cli:main",
        ],
    },
    project_urls={  # Optional
        "Bug Reports": "https://github.com/datenpol/mr.bob/issues",
        "Source": "https://github.com/datenpol/mr.bob/",
    },
)
