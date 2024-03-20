import logging

logging.basicConfig(level=logging.DEBUG)


def assert_strings_are_equal(expected, actual):
    result = None

    try:
        if expected == actual:
            result = 'Passed'
        else:
            logging.error("Expected value was: '{}' but was: '{}'".format(expected, actual))
            result = 'Failed'
    except TypeError as error:
        print("The value '{}' and '{}' cannot be of different datatypes".format(expected, actual))
    finally:
        return result


def assert_strings_are_not_equal(expected, actual):
    result = None

    try:
        if expected == actual:
            logging.error("'{}' and: '{}' should not be the same".format(expected, actual))
            result = 'Failed'
        else:
            result = 'Passed'
    except TypeError as error:
        print("The value '{}' and '{}' cannot be of different datatypes".format(expected, actual))
    finally:
        return result
