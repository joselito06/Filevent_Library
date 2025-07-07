from setuptools import setup, find_packages

setup(
    name="fileevent",
    version="0.1.0",
    description="Librería para emisión y recepción de eventos usando archivos organizados por VM y usuario.",
    author="Joselito Beriguete",
    author_email="tunombre@ejemplo.com",
    packages=find_packages(),
    install_requires=[
        "watchdog"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)