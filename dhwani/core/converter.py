import dhwani.mappings.utils as utils
import dhwani.core.core_utils.converter_utils as converter_utils


class Converter:
    """The :class:`dhwani.Converter` (implementation at :class:`dhwani.core.converter.Converter`) 
    class is the main entry point for Dhwani. You can make an object of this class and configure 
    it to perform phonetic conversion from one language to another.

    :param src_lang_code: ISO 639-3 code of the source language.
    :type src_lang_code: str
    
    :param dest_lang_code: ISO 639-3 code of the destination language.
    :type dest_lang_code: str
    
    """

    def __init__(self, src_lang_code: str, dest_lang_code: str):
        """Constuctor method
        """
        if not utils.is_supported(src_lang_code, dest_lang_code):
            utils.print_current_support()
            raise NotImplementedError("The given conversion is not supported.")

        self._src_lang_code = src_lang_code
        self._dest_lang_code = dest_lang_code

        self._lang_mappings = utils.get_lang_mappings(src_lang_code, dest_lang_code)

    def convert(self, src_text: str) -> str:
        """Converts the full source text from source language to destination
        language.

        :param src_text: The text in ``src_lang_code`` language to be converted
        :type src_text: str

        :return: The text in ``dest_lang_code`` language converted 
            from ``src_lang_code``

        :rtype: str
        """

        if type(src_text) is not str:
            raise TypeError("Source string should be of type 'str'")

        return converter_utils._convert(src_text, self._lang_mappings)
