# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from workday_person_python_sdk.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    PEOPLE = "people"
    WORK_CONTACT_INFORMATION_CHANGES = "workContactInformationChanges"
    HOME_CONTACT_INFORMATION_CHANGES = "homeContactInformationChanges"
    PROMPT_VALUES = "Prompt Values"
    COUNTRIES = "countries"
    PHONE_VALIDATION = "phoneValidation"
