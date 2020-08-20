[![Documentation Status](https://readthedocs.org/projects/dhwani/badge/?version=latest)](https://dhwani.readthedocs.io/en/latest/?badge=latest) [![Build Status](https://travis-ci.com/ndyashas/Dhwani.svg?branch=master)](https://travis-ci.com/ndyashas/Dhwani)

# Dhwani
English to Indic language phonetic conversion engine. Read more about the project [here](https://ndyashas.github.io/projects/Dhwani.html).

## Installation
Dhwani is currently **not** stable. However, the developmental release is [avalibale at PyPI](https://pypi.org/project/dhwani/).

### Installing from PyPI
```
$ pip install dhwani
```

### Installing from sources
```
$ git clone https://github.com/ndyashas/Dhwani.git
$ cd Dhwani
$ pip install -r requirements.txt
$ pip install -e .
```
## Example
An example of converting from *English* to *Kannada* is shown here.
```python
# Import the main converter class
from dhwani import Converter

# Make  a converter object. The first argument is the
# ISO 639-3 code of the source language, and the second
# argument is the ISO 639-3 code of the destination language.
converter = Converter('eng', 'kan')

src_string = "kannaDa"

# Use the 'convert' method of converter object to get the converter
# string back.
dest_string = converter.convert(src_string)

# Print the result
# Note that the display for standard output needs to support the unicode
# characters.
print(dest_string)
# output > ಕನ್ನಡ​
```

## Currently supported conversions
* English to Kannada
* English to Devnagari
* English to Tamil
