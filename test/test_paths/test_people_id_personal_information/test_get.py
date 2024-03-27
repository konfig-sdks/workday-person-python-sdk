# coding: utf-8

"""
    person

    The Person REST APIs enable you to access information about the worker person, including country-specific configuration information about name components.

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

import unittest
from unittest.mock import patch

import urllib3

import workday_person_python_sdk
from workday_person_python_sdk.paths.people_id_personal_information import get
from workday_person_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestPeopleIDPersonalInformation(ApiTestMixin, unittest.TestCase):
    """
    PeopleIDPersonalInformation unit test stubs
        Retrieves a collection of personal information.
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
