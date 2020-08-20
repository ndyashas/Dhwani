__all__ = ["is_supported", "print_current_support", "get_lang_mappings", "get_supported_conversions"]

import os
import yaml


def get_supported_conversions():
    """Returns all the currently supported conversions.

    :return: Returns the currently supported conversins in a dictionary
        whose keys are ISO 639-3 codes of source languages and the values are
        list containing the ISO 639-3 codes of destination languages.
        
    :rtype: Dictionary.
    """
    sc_file_basename = "supported_conversions.yaml"
    sc_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), sc_file_basename)

    with open(sc_file_path, "r", encoding="utf-8") as f:
        supported_dict = yaml.safe_load(f)

    if supported_dict is None:
        supported_dict = dict()

    return supported_dict


def is_supported(src_lang_code: str, dest_lang_code: str):
    """Checks if the given pair of languages are supported for conversion.

    :param src_lang_code: ISO 639-3 code of the source language.
    :type src_lang_code: str
    
    :param dest_lang_code: ISO 639-3 code of the destination language.
    :type src_lang_code: str
    
    :return: Boolean value for whether the source and destination language pair
        is supported.
    :rtype: Boolean

    """
    supported_dict = get_supported_conversions()

    try:
        if dest_lang_code in supported_dict[src_lang_code]:
            return True
        else:
            return False
    except:
        return False
    return False


def print_current_support():
    """Prints the currently supported mappings of supported languages.
    """
    print("The supported conversions are: ")
    supported_dict = get_supported_conversions()
    for i in supported_dict:
        print("{0} => {1}".format(i, " ".join(supported_dict[i])))
    print("\nAll language codes are as given in ISO 639-3.")


def get_lang_mappings(src_lang_code: str, dest_lang_code: str):
    """Returns the mappings from source language to destination language
    as a list.

    :param src_lang_code: ISO 639-3 code of the source language.
    :type src_lang_code: str
    
    :param dest_lang_code: ISO 639-3 code of the destination language.
    :type src_lang_code: str
    
    :return: List with each element as a dictionary, where keys need to be replaced
        by values.
    :rtype: List.

    """

    if not is_supported(src_lang_code, dest_lang_code):
        utils.print_current_support()
        raise NotImplementedError("The given conversion is not supported.")

    lang_file_base_name = src_lang_code + "_" + dest_lang_code + ".yaml"
    lang_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), lang_file_base_name)

    with open(lang_file_path, "r", encoding="utf-8") as f:
        lang_mapping_list = yaml.safe_load(f)

    # Check for empty file
    # FIXME

    return lang_mapping_list


if __name__ == "__main__":
    # Prints the currently supported mappings if this file is direclty run
    print_current_support()
