import unittest

from tests import test_ethereum_utils, test_import


def suite():
    modules = [
        test_ethereum_utils, test_import,
    ]
    test_suite = unittest.TestSuite()
    for module in modules:
        test_suite.addTest(unittest.TestLoader().loadTestsFromModule(module))
    return test_suite
