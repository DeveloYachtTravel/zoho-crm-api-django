import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zoho_crm_api-develoyachttravel",
    version="0.0.1",
    author="it.yacht.travel@gmail.com",
    author_email="it.yacht.travel@gmail.com",
    description="Wrapper for zcrmsdk package with django with ready to use models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)