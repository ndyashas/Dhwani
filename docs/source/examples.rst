Examples
========

Convert from English to Kannada
*******************************
.. code-block:: python

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
	
