def validate_attribute_string(to_validate: str, attribute: str) -> bool:
    """Validator for string attributes of classes

    Args:
        to_validate (str): value to validate
        type (str): attribute name for error message

    Returns:
        bool: True if validation was success
    """

    if not isinstance(to_validate, str):
        raise TypeError(f"Expected {attribute} of value str, instead got: ",
                        type(to_validate))
    if not to_validate:
        raise ValueError(f"{attribute} cannot be empty")

    return True
