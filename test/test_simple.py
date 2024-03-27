# coding: utf-8

"""
    person

    The Person REST APIs enable you to access information about the worker person, including country-specific configuration information about name components.

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

import unittest

import os
from pprint import pprint
from workday_person_python_sdk import WorkdayPerson

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        workdayperson = WorkdayPerson(
        
            client_id = 'YOUR_CLIENT_ID',
            client_secret = 'YOUR_CLIENT_SECRET',
        )
        self.assertIsNotNone(workdayperson)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
