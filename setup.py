import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="pokerpy",
    version="0.0.1",
    author="Tom Dufall",
    author_email="tom@tomdufall.co.uk",
    description="A package to score and analyse poker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tomdufall/pokerpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
