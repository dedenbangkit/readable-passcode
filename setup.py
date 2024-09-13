from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="readable_passcode",
    version="1.0.0",
    author="Deden",
    author_email="mail@dedenbangkit.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.8 :: Only",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    description="Generate human-readable passcodes with memory optimization",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={
        "Documentation": "https://github.com/dedenbangkit/readable-passcode",
        "Bug Reports": "https://github.com/dedenbangkit/readable-passcode/issues",
        "Source Code": "https://github.com/dedenbangkit/readable-passcode",
    },
    url="https://github.com/dedenbangkit/readable-passcode",
    include_package_data=True,
    install_requires=[],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    package_data={
        "readable_passcode": ["words.txt"],
    },
    entry_points={
        "console_scripts": [
            "readable-passcode=readable_passcode.readable_passcode:main",
        ],
    },
    extras_require={
        "dev": ["check-manifest"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
