# python setup.py sdist bdist_wheel
from setuptools import setup

setup(
    name="bikesharing",
    version="0.1",
    description="AIMLOPS Bike Sharing Project",
    long_description="AIMLOPS Module 3 Mini Project 2",
    install_requires=[
        "numpy",
        "pandas",
        "pydantic",
        "scikit-learn",
        "strictyaml",
        "ruamel.yaml",
        "joblib",
        "pytest",
    ],
    packages=["bikeshare_model"],
    package_dir={"bikeshare_model": "Application/bikeshare_model"},
    package_data={
        "bikeshare_model": [
            "*.yml",
            "VERSION",
            "trained_models/bike_share__model_output_v0.0.1.pkl",
        ]
    },
    include_package_data=True,
)
