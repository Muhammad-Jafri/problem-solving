from setuptools import setup, find_packages

setup(
    name="problem-solving",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["pydantic"],
    author="Your Name",
    author_email="your.email@example.com",
    description="A package for solving various problems",
    keywords="problem, solving, ai",
    url="https://github.com/yourusername/problem-solving",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
)
