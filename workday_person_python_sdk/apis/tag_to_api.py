import typing_extensions

from workday_person_python_sdk.apis.tags import TagValues
from workday_person_python_sdk.apis.tags.people_api import PeopleApi
from workday_person_python_sdk.apis.tags.work_contact_information_changes_api import WorkContactInformationChangesApi
from workday_person_python_sdk.apis.tags.home_contact_information_changes_api import HomeContactInformationChangesApi
from workday_person_python_sdk.apis.tags.prompt_values_api import PromptValuesApi
from workday_person_python_sdk.apis.tags.countries_api import CountriesApi
from workday_person_python_sdk.apis.tags.phone_validation_api import PhoneValidationApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.PEOPLE: PeopleApi,
        TagValues.WORK_CONTACT_INFORMATION_CHANGES: WorkContactInformationChangesApi,
        TagValues.HOME_CONTACT_INFORMATION_CHANGES: HomeContactInformationChangesApi,
        TagValues.PROMPT_VALUES: PromptValuesApi,
        TagValues.COUNTRIES: CountriesApi,
        TagValues.PHONE_VALIDATION: PhoneValidationApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.PEOPLE: PeopleApi,
        TagValues.WORK_CONTACT_INFORMATION_CHANGES: WorkContactInformationChangesApi,
        TagValues.HOME_CONTACT_INFORMATION_CHANGES: HomeContactInformationChangesApi,
        TagValues.PROMPT_VALUES: PromptValuesApi,
        TagValues.COUNTRIES: CountriesApi,
        TagValues.PHONE_VALIDATION: PhoneValidationApi,
    }
)
