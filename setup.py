"""
Setup-Skript für die wizzycord Bibliothek
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="wizzycord",
    version="0.3.0",  # Version aktualisiert wegen neuer Funktionalität
    author="Nowaro",
    author_email="dev@nowaro.de",
    description="Eine Bibliothek zur Verwaltung von Benutzerlisten, Cog-Verwaltung und farbige Konsolenausgaben mit Discord-Integration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nowaro-official/wizzycord",
    packages=find_packages(),
    install_requires=[
        "py-cord>=2.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
