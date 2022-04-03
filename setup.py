from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Processamento_Imagens",
    version="0.0.2",
    author="José Gabriel",
    author_email="gabrielborges@gmail.com",
    description="Pacote de Processamento de Imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Gabrielborges79/ImageProcessing",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)