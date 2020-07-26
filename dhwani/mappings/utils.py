import os
import yaml


def get_supported_conversions():
    """Returns all the currently supported conversions.

    :return: Returns the currently supported conversins in a dictionary
        whose keys are ISO 639-3 codes of source languages and the values are
        list containing the ISO 639-3 codes of destination languages.
        
    :rtype: Dictionary.
    """
    with open(
        os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "supported_conversions.yaml"
        ),
        "r",
        encoding="utf-8",
    ) as f:
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


if __name__ == "__main__":
    # Prints the currently supported mappings if this file is direclty run
    print_current_support()
