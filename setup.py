from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Date tools to help create a calendar'
LONG_DESCRIPTION = 'A package that will help to determine the day that each year\
    and month starts on so that a calander can be created on a GUI or terminal'

# Setting up
setup(
    name="PyDtTls",
    version=VERSION,
    author="Matt Bay",
    author_email="MJBayUNL@yahoo.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['Date', 'Calendar'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)