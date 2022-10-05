from setuptools import setup

setup(
    name="bSSG",
    version="0.1.0",
    package_dir={"": "src"},
    install_requires=[
        "markdown",
        "watchdog"
    ],
    entry_points={
        "console_scripts": [
            'bssg-generate = bssggenerate:main',
            'bssg-watch = bssgwatch:main'
        ]
    }
)