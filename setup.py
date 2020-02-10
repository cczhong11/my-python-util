import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ztc-python-util", # Replace with your own username
    version="0.0.1",
    author="Tianchen Zhong",
    author_email="me@tczhong.com",
    description="A util for myself",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cczhong11/my-python-util",
    packages=setuptools.find_packages(),
    install_requires=[
          'pytz',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)