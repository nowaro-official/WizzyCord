from setuptools import setup, find_packages

setup(
    name="wizzycord",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "py-cord>=2.0.0"
    ],
    author="kainow-code",
    author_email="ihre.email@example.com",  # Sie können diese E-Mail-Adresse nach Bedarf ändern
    description="Eine Python-Bibliothek für einfaches Pycord-Bot-Cog-Management",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kainow-code/wizzycord",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
