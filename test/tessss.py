from os.path import dirname, join
from unittest import TestSuite, TestLoader, TextTestRunner

suite = TestSuite()
loader_test = TestLoader().discover()
suite.addTest(loader_test)