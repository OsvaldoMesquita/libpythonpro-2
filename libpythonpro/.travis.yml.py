language: python
python:
 - 3.6
 - 2.7
install:
 - pip install -r requirements-dev.txt
script:
 - flake8