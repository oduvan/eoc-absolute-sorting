from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "absolute_sorting"
    FUNCTION_NAMES = {
        "python_3": "absolute_sorting",
        "js_node": "absoluteSorting"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''def cover(func, data):
    result = func(tuple(data))
    if not isinstance(result, (list, tuple)):
        raise TypeError("The result should be a list or a tuple")
    return result
'''
    }