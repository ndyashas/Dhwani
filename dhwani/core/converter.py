import dhwani.mappings.utils as utils

class Converter:
    """The Converter class is the main entry point for Dhwani. You can
    make an object of this class and configure it to perform phonetic conversion
    from one language to another.

    :param src_lang_code: ISO 639-3 code of the source language.
    :type src_lang_code: str
    
    :param dest_lang_code: ISO 639-3 code of the destination language.
    :type src_lang_code: str
    
    :param disable_source_caching: Disables buffering of the source language text
        useful if you want the source langauge text back.
    :type src_lang_code: bool, optional
    

    """

    def __init__(self, src_lang_code:str, dest_lang_code:str, disable_source_caching:bool=True):
        """Constuctor method
        """
        if not utils.is_supported(src_lang_code, dest_lang_code):
            utils.print_current_support()
            raise NotImplementedError("The given conversion is not supported.")

        self._src_lang_code = src_lang_code
        self._dest_lang_code = dest_lang_code

        self._disable_source_caching = disable_source_caching
        self._current_buffer = ""
        
        
    @property
    def current_buffer(self):
        return self._current_buffer
        
    
    def convert(self, src_text:str):
        """Converts the full source text from source language to destination
        language.
        """
        raise NotImplementedError("The conversion function has not yet been implemented.")
