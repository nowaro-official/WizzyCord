from setuptools import setup, find_packages

setup(
    name="wizzycord",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Fügen Sie hier eventuelle Abhängigkeiten hinzu
    ],
    author="kainow-code",
    author_email="ihre.email@example.com",
    description="Eine Python-Bibliothek namens WizzyCord",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kainow-code/wizzycord",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)