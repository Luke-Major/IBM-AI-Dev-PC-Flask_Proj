from setuptools import setup, find_packages

setup(
    name="EmotionDetection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        # List your dependencies here
        "json",
        "requests",
        # Add any other required packages
    ],
)