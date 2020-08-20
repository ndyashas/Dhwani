import unittest

import dhwani

_test_id_match = {
    "00": "Sanity test for the returned supported language dictionary",
    "01": "Converter class API testing",
}


class Test_Dhwani_API(unittest.TestCase):
    def setUp(self):
        """Load the supported conversions
        """
        self.supported_conversions_dict = dhwani.get_supported_conversions()

    def test_id_00(self):
        """Sanity test for the returned supported language dictionary
        """
        self.assertIsNotNone(
            self.supported_conversions_dict,
            msg="{} returned None".format("dhwani.get_lang_mappings()"),
        )

        self.assertTrue(
            len(self.supported_conversions_dict) > 0,
            msg="No supported convertions available.",
        )

        for src_lang_code in self.supported_conversions_dict:
            self.assertIsInstance(self.supported_conversions_dict[src_lang_code], list)
            self.assertTrue(
                len(self.supported_conversions_dict[src_lang_code]) > 0,
                msg="src {} does not support convertions to any destination language".format(
                    src_lang_code
                ),
            )

    def test_id_01(self):
        """Converter class API testing
        """

        for src_lang_code in self.supported_conversions_dict:
            for dest_lang_code in self.supported_conversions_dict[src_lang_code]:
                converter = dhwani.Converter(src_lang_code, dest_lang_code)

                self.assertIsInstance(converter, dhwani.Converter)  # Needed?
                self.assertIsNotNone(converter.convert)
