import setuptools

long_description = open("README.md").read()
required = [
    "six",
    "ordereddict",
    "importlib",
    "Jinja2",
    "argparse"
]

setuptools.setup(
    name="mr.bob",
    version="0.1.4",  # eg:1.0.0
    author="Ahmed Aly, Domen Kozar, Tom Lazar",
    author_email="ahmed.aly@datenpol.at",
    license="BSD",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    description="Bob renders directory structure templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/datenpol/mr.bob.git",
    key_words="temlates, render, mr.bob, odoo",
    install_requires=required,
    entry_points="""
      [console_scripts]
      mrbob = mrbob.cli:main
      """,
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
)
