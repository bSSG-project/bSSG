from setuptools import setup

setup(
    name="bSSG",
    version="0.1.0",
    py_modules=['bssggenerate', 'bssgwatch'],
    install_requires=[
        "markdown",
    ],
    entry_points={
        "console_scripts": [
            'bssg-generate = bssggenerate:main',
            'bssg-watch = bssgwatch:main'
        ]
    }
)