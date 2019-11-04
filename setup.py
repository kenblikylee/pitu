import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pitu",
    version="0.3.0",
    author="kenblikylee",
    author_email="kenblikylee@126.com",
    description="python 开源命令行P图工具。",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kenblikylee/pitu.git",
    packages=setuptools.find_packages(),
    license='MIT',
    install_requires=[
        'Pillow>=6.1.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'pitu = pitu.cli:main'
        ]
    },
    python_requires='>=3.6',
)
