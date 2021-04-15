from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="riot-games-api",
    version="1.0.3",
    author="Kirill Shikhalev",
    author_email="esbraff@yandex.ru",
    description="Riot Games API wrapper for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/esbraff/riot_games_api",
    project_urls={
        "Bug Tracker": "https://github.com/esbraff/riot_games_api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "requests>=2.5.0",
        "pydantic~=1.8.1",
        "humps~=0.2.2",
    ],
    python_requires=">=3.6",
)
