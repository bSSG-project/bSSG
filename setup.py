from setuptools import setup

setup(
    name="bSSG",
    version="0.1.0",
    package_dir={"bssg": "src"},
    install_requires=[
        "markdown",
        "watchdog"
    ],
    entry_points={
        "console_scripts": [
            'bssg-generate = bssg.bssggenerate:main',
            'bssg-watch = bssg.bssgwatch:main'
        ]
    }
)