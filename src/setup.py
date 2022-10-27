
from setuptools import find_packages
from setuptools import setup

setup(
    name="io-vizmaps",
    version="0.1.0",
    description="Map Visualization Library",
    author="IO-Aero Team",
    author_email="info@aeronetica.com",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Library",
        "License :: IO-Aero",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="Map, Visualization, QGIS",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={"io_vizmaps": ["*.pyi", "py.typed"]},
    project_urls={
        "Bug Tracker": "https://github.com/io-aero/io-vizmaps/issues",
        "Documentation": "https://io-aero.github.io/io-vizmaps/",
        "Homepage": "https://github.com/io-aero/io-vizmaps",
        "Release History": "https://io-aero.github.io/io-vizmaps/release_history/",
        "Release Notes": "https://io-aero.github.io/io-vizmaps/release_notes/",
        "Source": "https://github.com/io-aero/io-vizmaps",
    },
    python_requires=">=3.10",
    url="https://github.com/io-aero/io-vizmaps",
)