CSV DB
------------


![alt text](https://badgen.net/badge/python/3.10/cyan?icon=pypi)


## Description
Proyecto académico desarrollado para la asignatura de "Python"

## Packaging

To package the project, we will use the 'setuptools' library, which is a standard tool for packaging Python projects. We will create a 'setup.py' file in the root directory of the project with the necessary configuration to generate a wheel distribution.

```
python setup.py bdist_wheel --dist-dir=/output_path
```

## Distribution

As this is a project developed for academic purposes, the distribution of the project will be done manually uploading the generated '.whl' file to the Colab working environment.
Inside the working directory '/content' in Colab, we will create a 'packages' directory where we will upload the generated artefacts.

## Usage

To install our package on the Colab notebook, we need to tell pip not to look for the package in PyPI or any other artifact repository, but to look for it in the path '/content/packages' in the Colab framework.

```
pip install cei_template --find-links=/content/packages
```

Once the package is installed, we can import it and start using it.

```
import cei_template
```

### Usage Example

```
```

## Credits

### Owner
- Your Name <your_mail@cei.es>
