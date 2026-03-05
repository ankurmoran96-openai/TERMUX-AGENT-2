from setuptools import setup, find_packages

setup(
    name="brahmos-core",
    version="4.5.0",
    author="@Ankxrrrr",
    description="The ultimate autonomous system orchestrator.",
    packages=["tools"],
    py_modules=["main", "config"],
    install_requires=[
        "colorama",
        "requests",
        "beautifulsoup4",
        "googlesearch-python",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "brahmos=main:main",
        ],
    },
)
