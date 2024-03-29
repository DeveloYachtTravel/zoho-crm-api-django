import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zoho_crm_api",
    version="1.0.7",
    author="it.yacht.travel@gmail.com",
    author_email="it.yacht.travel@gmail.com",
    description="Wrapper of zcrmsdk package for django with ready to use models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DeveloYachtTravel/zoho-crm-api-django",
    packages=setuptools.find_packages(),
    install_requires=[
        'zcrmsdk==2.0.11',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
