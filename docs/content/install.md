{option:title=Installation Guide}

bSSG is still in early development and the installation process has not yet been refined for end users. bSSG is not recommended for production use at this stage. If you still wish to use it, the instructions for installation are below:

## Dependencies
You will need Python 3, Python-Markdown, and Watchdog to run this. On Windows, `setup.py` will automatically install these dependencies for you. On Linux, it is recommended to install the dependencies through your package manager, usually in a package called `python-markdown` and `python-watchdog` or similar.

## Installation
Download or `git clone` the [bSSG repository](https://github.com/bssg-project/bSSG). Install bSSG by using `python setup.py install`. For Linux users, it is recommended to install the program dependencies through your package manager rather than through pip, see above. Once they are installed, run `python setup.py install`.