# coding: utf-8

"""
    person

    The Person REST APIs enable you to access information about the worker person, including country-specific configuration information about name components.

    The version of the OpenAPI document: v4
    Generated by: https://konfigthis.com
"""

from workday_person_python_sdk.paths.work_contact_information_changes_id_addresses.post import CreateAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_email_addresses.post import CreateEmailAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_instant_messengers.post import CreateInstantMessenger
from workday_person_python_sdk.paths.work_contact_information_changes_id_phone_numbers.post import CreatePhoneNumber
from workday_person_python_sdk.paths.work_contact_information_changes_id_web_addresses.post import CreateStagedWebAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_addresses_subresource_id.get import GetAddressAsStaged
from workday_person_python_sdk.paths.work_contact_information_changes_id_addresses.get import GetAddressesStaged
from workday_person_python_sdk.paths.work_contact_information_changes_id_email_addresses_subresource_id.get import GetEmailAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id.get import GetEventInfo
from workday_person_python_sdk.paths.work_contact_information_changes_id_phone_numbers_subresource_id.get import GetPhoneNumber
from workday_person_python_sdk.paths.work_contact_information_changes_id_phone_numbers.get import GetPhoneNumbers
from workday_person_python_sdk.paths.work_contact_information_changes_id_email_addresses.get import GetStagedEmailAddresses
from workday_person_python_sdk.paths.work_contact_information_changes_id_instant_messengers_subresource_id.get import GetStagedInstantMessenger
from workday_person_python_sdk.paths.work_contact_information_changes_id_instant_messengers.get import GetStagedInstantMessengers
from workday_person_python_sdk.paths.work_contact_information_changes_id_web_addresses_subresource_id.get import GetWebAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_web_addresses.get import GetWebAddressesStaged
from workday_person_python_sdk.paths.work_contact_information_changes_id_addresses_subresource_id.delete import RemoveAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_email_addresses_subresource_id.delete import RemoveEmailAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_instant_messengers_subresource_id.delete import RemoveInstantMessenger
from workday_person_python_sdk.paths.work_contact_information_changes_id_phone_numbers_subresource_id.delete import RemovePhoneNumber
from workday_person_python_sdk.paths.work_contact_information_changes_id_web_addresses_subresource_id.delete import RemoveWebAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_submit.post import Submit
from workday_person_python_sdk.paths.work_contact_information_changes_id_addresses_subresource_id.put import UpdateAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id.patch import UpdateAlternateWorkLocation
from workday_person_python_sdk.paths.work_contact_information_changes_id_email_addresses_subresource_id.patch import UpdateEmailAddress
from workday_person_python_sdk.paths.work_contact_information_changes_id_instant_messengers_subresource_id.patch import UpdateInstantMessenger
from workday_person_python_sdk.paths.work_contact_information_changes_id_phone_numbers_subresource_id.patch import UpdatePhoneNumber
from workday_person_python_sdk.paths.work_contact_information_changes_id_web_addresses_subresource_id.patch import UpdateWebAddress
from workday_person_python_sdk.apis.tags.work_contact_information_changes_api_raw import WorkContactInformationChangesApiRaw


class WorkContactInformationChangesApi(
    CreateAddress,
    CreateEmailAddress,
    CreateInstantMessenger,
    CreatePhoneNumber,
    CreateStagedWebAddress,
    GetAddressAsStaged,
    GetAddressesStaged,
    GetEmailAddress,
    GetEventInfo,
    GetPhoneNumber,
    GetPhoneNumbers,
    GetStagedEmailAddresses,
    GetStagedInstantMessenger,
    GetStagedInstantMessengers,
    GetWebAddress,
    GetWebAddressesStaged,
    RemoveAddress,
    RemoveEmailAddress,
    RemoveInstantMessenger,
    RemovePhoneNumber,
    RemoveWebAddress,
    Submit,
    UpdateAddress,
    UpdateAlternateWorkLocation,
    UpdateEmailAddress,
    UpdateInstantMessenger,
    UpdatePhoneNumber,
    UpdateWebAddress,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: WorkContactInformationChangesApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = WorkContactInformationChangesApiRaw(api_client)