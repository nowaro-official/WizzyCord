from setuptools import setup, find_packages

setup(
    name="wizzycord",
    version="0.1.0",
    author="Flo Kainow-code",
    author_email="flo@example.com",
    description="Eine Pycord-optimierte Bibliothek für Discord-Bots",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kainow-code/wizzycord",
    packages=find_packages(),
    install_requires=[
        "py-cord>=2.4.0",
        "aiosqlite>=0.17.0",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.9",
)
