from setuptools import setup, find_packages

setup(
    name="fastapicore",
    version="0.0.1",
    packages=find_packages(),
    install_requires=['pyjwt==2.7.0', 'fastapi>=0.110.0', 'aiohttp>=3.8.6'],
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
