import unittest
import unittest.mock
import timeout_decorator

import dhwani
import dhwani.mappings.utils as utils

_test_id_match = {
    "00": "Test that the mappings do not form any loops",
}


class Test_Dhwani_API(unittest.TestCase):
    def setUp(self):
        """Load the supported conversions
        """
        self.supported_conversions_dict = dhwani.get_supported_conversions()

    def load_src_string_from_codes(self, src_lang_code: str, dest_lang_code: str):
        mappings_list = utils.get_lang_mappings(src_lang_code, dest_lang_code)
        toret_list = [list(element.keys())[0] for element in mappings_list]
        toret = "".join(toret_list)
        return toret

    @timeout_decorator.timeout(2)  # Assumption that it wont take more than this.
    def _convert(self, converter, *args, **kwargs):
        return converter.convert(*args, **kwargs)

    def test_id_00(self):
        """Test that the mappings do not form any loops
        """

        for src_lang_code in self.supported_conversions_dict:
            for dest_lang_code in self.supported_conversions_dict[src_lang_code]:
                src_text = self.load_src_string_from_codes(
                    src_lang_code, dest_lang_code
                )

                converter = dhwani.Converter(src_lang_code, dest_lang_code)
                self.assertIsNotNone(converter.convert)

                dest_text = self._convert(converter, src_text)
