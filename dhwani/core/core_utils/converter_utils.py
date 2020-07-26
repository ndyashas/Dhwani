__all__ = ["_convert"]

import re


def _convert(src_text: str, lang_mappings: list) -> str:
    """The utility function which which does the heavy-lifting of
    converting the src text into dest string using the language mapping list

    :param src_text: The text in :param:`src_lang_code` language to be converted
    :type src_text: str
    
    :param lang_mappings: List with each element as a dictionary, where keys need to be replaced
        by values.
    :type lang_mappings: List

    :return: The converted text.

    :rtype: str

    """

    prev_dest_text = ""
    dest_text = src_text
    string_changed = False

    while not string_changed:
        prev_dest_text = dest_text
        try:
            for repl_pair in lang_mappings:
                pattern = list(repl_pair.keys())[0]
                repl = list(repl_pair.values())[0]
                dest_text = re.sub(pattern, repl, dest_text)

        except Exception as e:
            print("Encountered exception while converting string\nError message:{}".format(e))
            string_changed = True

        if dest_text == prev_dest_text:
            string_changed = True
            return dest_text
