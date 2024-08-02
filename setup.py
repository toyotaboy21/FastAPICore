from setuptools import setup, find_packages

with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setup(
    name="fastcore",
    version="0.0.1",
    packages=find_packages(),
    install_requires=install_requires,
    author="Reques6e",
    author_email="lygitormaa@gmail.com",
    description="FastCore",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/reques6e/FastAPICore",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
