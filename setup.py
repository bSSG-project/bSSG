from setuptools import setup

setup(
    name="bSSG",
    version="0.1.0",
    package_dir={"bSSG": "src"},
    install_requires=[
        "markdown",
        "watchdog"
    ],
    entry_points={
        "console_scripts": [
            'bssg-generate = bSSG.bssggenerate:main',
            'bssg-watch = bSSG.bssgwatch:main'
        ]
    }
)