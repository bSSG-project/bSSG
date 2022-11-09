from setuptools import setup

setup(
    name="bSSG",
    version="0.1.0",
    install_requires=[
        "markdown",
        "watchdog"
    ],
    packages=['bSSG'],
    entry_points={
        "console_scripts": [
            'bssg-generate = bssggenerate:main',
            'bssg-watch = bssgwatch:main'
        ]
    }
)