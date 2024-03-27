import typing_extensions

from workday_person_python_sdk.paths import PathValues
from workday_person_python_sdk.apis.paths.phone_validation import PhoneValidation
from workday_person_python_sdk.apis.paths.people_id_personal_information import PeopleIDPersonalInformation
from workday_person_python_sdk.apis.paths.people_id_home_addresses_subresource_id import PeopleIDHomeAddressesSubresourceID
from workday_person_python_sdk.apis.paths.countries_id import CountriesID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_web_addresses import HomeContactInformationChangesIDWebAddresses
from workday_person_python_sdk.apis.paths.people_id_additional_names_subresource_id import PeopleIDAdditionalNamesSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_phone_numbers_subresource_id import WorkContactInformationChangesIDPhoneNumbersSubresourceID
from workday_person_python_sdk.apis.paths.people_id_audio_name_pronunciation import PeopleIDAudioNamePronunciation
from workday_person_python_sdk.apis.paths.people_id_personal_information_subresource_id import PeopleIDPersonalInformationSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_instant_messengers_subresource_id import WorkContactInformationChangesIDInstantMessengersSubresourceID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id import HomeContactInformationChangesID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_phone_numbers import HomeContactInformationChangesIDPhoneNumbers
from workday_person_python_sdk.apis.paths.people_id_photos import PeopleIDPhotos
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_submit import WorkContactInformationChangesIDSubmit
from workday_person_python_sdk.apis.paths.people_id_preferred_name import PeopleIDPreferredName
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id import WorkContactInformationChangesID
from workday_person_python_sdk.apis.paths.countries_id_address_components import CountriesIDAddressComponents
from workday_person_python_sdk.apis.paths.people_id_photos_subresource_id import PeopleIDPhotosSubresourceID
from workday_person_python_sdk.apis.paths.people_id_work_instant_messengers import PeopleIDWorkInstantMessengers
from workday_person_python_sdk.apis.paths.people_id_legal_name_subresource_id import PeopleIDLegalNameSubresourceID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_email_addresses import HomeContactInformationChangesIDEmailAddresses
from workday_person_python_sdk.apis.paths.people_id_work_emails import PeopleIDWorkEmails
from workday_person_python_sdk.apis.paths.people_id_home_addresses import PeopleIDHomeAddresses
from workday_person_python_sdk.apis.paths.people_id_home_phones_subresource_id import PeopleIDHomePhonesSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_instant_messengers import WorkContactInformationChangesIDInstantMessengers
from workday_person_python_sdk.apis.paths.countries_id_name_components import CountriesIDNameComponents
from workday_person_python_sdk.apis.paths.people_id_work_instant_messengers_subresource_id import PeopleIDWorkInstantMessengersSubresourceID
from workday_person_python_sdk.apis.paths.people_id_work_addresses_subresource_id import PeopleIDWorkAddressesSubresourceID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_addresses import HomeContactInformationChangesIDAddresses
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_instant_messengers_subresource_id import HomeContactInformationChangesIDInstantMessengersSubresourceID
from workday_person_python_sdk.apis.paths.people_id_work_phones import PeopleIDWorkPhones
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_web_addresses_subresource_id import HomeContactInformationChangesIDWebAddressesSubresourceID
from workday_person_python_sdk.apis.paths.people_id_audio_name_pronunciation_subresource_id import PeopleIDAudioNamePronunciationSubresourceID
from workday_person_python_sdk.apis.paths.people_id_work_web_addresses_subresource_id import PeopleIDWorkWebAddressesSubresourceID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_phone_numbers_subresource_id import HomeContactInformationChangesIDPhoneNumbersSubresourceID
from workday_person_python_sdk.apis.paths.people_id_public_contact_information_subresource_id import PeopleIDPublicContactInformationSubresourceID
from workday_person_python_sdk.apis.paths.people_id_home_phones import PeopleIDHomePhones
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_submit import HomeContactInformationChangesIDSubmit
from workday_person_python_sdk.apis.paths.people_id import PeopleID
from workday_person_python_sdk.apis.paths.people_id_public_contact_information import PeopleIDPublicContactInformation
from workday_person_python_sdk.apis.paths.people_id_legal_name import PeopleIDLegalName
from workday_person_python_sdk.apis.paths.people import People
from workday_person_python_sdk.apis.paths.people_id_home_web_addresses import PeopleIDHomeWebAddresses
from workday_person_python_sdk.apis.paths.people_id_preferred_name_subresource_id import PeopleIDPreferredNameSubresourceID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_instant_messengers import HomeContactInformationChangesIDInstantMessengers
from workday_person_python_sdk.apis.paths.people_id_additional_names import PeopleIDAdditionalNames
from workday_person_python_sdk.apis.paths.people_id_work_addresses import PeopleIDWorkAddresses
from workday_person_python_sdk.apis.paths.people_id_work_web_addresses import PeopleIDWorkWebAddresses
from workday_person_python_sdk.apis.paths.people_id_home_emails_subresource_id import PeopleIDHomeEmailsSubresourceID
from workday_person_python_sdk.apis.paths.people_id_work_phones_subresource_id import PeopleIDWorkPhonesSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_web_addresses_subresource_id import WorkContactInformationChangesIDWebAddressesSubresourceID
from workday_person_python_sdk.apis.paths.people_id_home_instant_messengers_subresource_id import PeopleIDHomeInstantMessengersSubresourceID
from workday_person_python_sdk.apis.paths.people_id_work_emails_subresource_id import PeopleIDWorkEmailsSubresourceID
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_email_addresses_subresource_id import HomeContactInformationChangesIDEmailAddressesSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_phone_numbers import WorkContactInformationChangesIDPhoneNumbers
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_email_addresses import WorkContactInformationChangesIDEmailAddresses
from workday_person_python_sdk.apis.paths.people_id_home_web_addresses_subresource_id import PeopleIDHomeWebAddressesSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_email_addresses_subresource_id import WorkContactInformationChangesIDEmailAddressesSubresourceID
from workday_person_python_sdk.apis.paths.people_id_home_instant_messengers import PeopleIDHomeInstantMessengers
from workday_person_python_sdk.apis.paths.people_id_home_emails import PeopleIDHomeEmails
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_web_addresses import WorkContactInformationChangesIDWebAddresses
from workday_person_python_sdk.apis.paths.home_contact_information_changes_id_addresses_subresource_id import HomeContactInformationChangesIDAddressesSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_addresses_subresource_id import WorkContactInformationChangesIDAddressesSubresourceID
from workday_person_python_sdk.apis.paths.work_contact_information_changes_id_addresses import WorkContactInformationChangesIDAddresses
from workday_person_python_sdk.apis.paths.countries import Countries
from workday_person_python_sdk.apis.paths.values_name_components_hereditary import ValuesNameComponentsHereditary
from workday_person_python_sdk.apis.paths.values_name_components_religious import ValuesNameComponentsReligious
from workday_person_python_sdk.apis.paths.values_name_components_honorary import ValuesNameComponentsHonorary
from workday_person_python_sdk.apis.paths.values_name_components_royal import ValuesNameComponentsRoyal
from workday_person_python_sdk.apis.paths.values_name_components_title import ValuesNameComponentsTitle
from workday_person_python_sdk.apis.paths.values_common_phone_country_phone_codes import ValuesCommonPhoneCountryPhoneCodes
from workday_person_python_sdk.apis.paths.values_country_components_country_city import ValuesCountryComponentsCountryCity
from workday_person_python_sdk.apis.paths.values_name_components_salutation import ValuesNameComponentsSalutation
from workday_person_python_sdk.apis.paths.values_personal_information_country_populated_country import ValuesPersonalInformationCountryPopulatedCountry
from workday_person_python_sdk.apis.paths.values_name_components_social import ValuesNameComponentsSocial
from workday_person_python_sdk.apis.paths.values_name_components_professional import ValuesNameComponentsProfessional
from workday_person_python_sdk.apis.paths.values_country_components_country import ValuesCountryComponentsCountry
from workday_person_python_sdk.apis.paths.values_name_components_academic import ValuesNameComponentsAcademic
from workday_person_python_sdk.apis.paths.values_personal_information_country_allowed_country import ValuesPersonalInformationCountryAllowedCountry
from workday_person_python_sdk.apis.paths.values_country_components_country_region import ValuesCountryComponentsCountryRegion
from workday_person_python_sdk.apis.paths.values_common_phone_phone_device_types import ValuesCommonPhonePhoneDeviceTypes

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.PHONE_VALIDATION: PhoneValidation,
        PathValues.PEOPLE_ID_PERSONAL_INFORMATION: PeopleIDPersonalInformation,
        PathValues.PEOPLE_ID_HOME_ADDRESSES_SUBRESOURCE_ID: PeopleIDHomeAddressesSubresourceID,
        PathValues.COUNTRIES_ID: CountriesID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES: HomeContactInformationChangesIDWebAddresses,
        PathValues.PEOPLE_ID_ADDITIONAL_NAMES_SUBRESOURCE_ID: PeopleIDAdditionalNamesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS_SUBRESOURCE_ID: WorkContactInformationChangesIDPhoneNumbersSubresourceID,
        PathValues.PEOPLE_ID_AUDIO_NAME_PRONUNCIATION: PeopleIDAudioNamePronunciation,
        PathValues.PEOPLE_ID_PERSONAL_INFORMATION_SUBRESOURCE_ID: PeopleIDPersonalInformationSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS_SUBRESOURCE_ID: WorkContactInformationChangesIDInstantMessengersSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID: HomeContactInformationChangesID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS: HomeContactInformationChangesIDPhoneNumbers,
        PathValues.PEOPLE_ID_PHOTOS: PeopleIDPhotos,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_SUBMIT: WorkContactInformationChangesIDSubmit,
        PathValues.PEOPLE_ID_PREFERRED_NAME: PeopleIDPreferredName,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID: WorkContactInformationChangesID,
        PathValues.COUNTRIES_ID_ADDRESS_COMPONENTS: CountriesIDAddressComponents,
        PathValues.PEOPLE_ID_PHOTOS_SUBRESOURCE_ID: PeopleIDPhotosSubresourceID,
        PathValues.PEOPLE_ID_WORK_INSTANT_MESSENGERS: PeopleIDWorkInstantMessengers,
        PathValues.PEOPLE_ID_LEGAL_NAME_SUBRESOURCE_ID: PeopleIDLegalNameSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES: HomeContactInformationChangesIDEmailAddresses,
        PathValues.PEOPLE_ID_WORK_EMAILS: PeopleIDWorkEmails,
        PathValues.PEOPLE_ID_HOME_ADDRESSES: PeopleIDHomeAddresses,
        PathValues.PEOPLE_ID_HOME_PHONES_SUBRESOURCE_ID: PeopleIDHomePhonesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS: WorkContactInformationChangesIDInstantMessengers,
        PathValues.COUNTRIES_ID_NAME_COMPONENTS: CountriesIDNameComponents,
        PathValues.PEOPLE_ID_WORK_INSTANT_MESSENGERS_SUBRESOURCE_ID: PeopleIDWorkInstantMessengersSubresourceID,
        PathValues.PEOPLE_ID_WORK_ADDRESSES_SUBRESOURCE_ID: PeopleIDWorkAddressesSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES: HomeContactInformationChangesIDAddresses,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS_SUBRESOURCE_ID: HomeContactInformationChangesIDInstantMessengersSubresourceID,
        PathValues.PEOPLE_ID_WORK_PHONES: PeopleIDWorkPhones,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES_SUBRESOURCE_ID: HomeContactInformationChangesIDWebAddressesSubresourceID,
        PathValues.PEOPLE_ID_AUDIO_NAME_PRONUNCIATION_SUBRESOURCE_ID: PeopleIDAudioNamePronunciationSubresourceID,
        PathValues.PEOPLE_ID_WORK_WEB_ADDRESSES_SUBRESOURCE_ID: PeopleIDWorkWebAddressesSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS_SUBRESOURCE_ID: HomeContactInformationChangesIDPhoneNumbersSubresourceID,
        PathValues.PEOPLE_ID_PUBLIC_CONTACT_INFORMATION_SUBRESOURCE_ID: PeopleIDPublicContactInformationSubresourceID,
        PathValues.PEOPLE_ID_HOME_PHONES: PeopleIDHomePhones,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_SUBMIT: HomeContactInformationChangesIDSubmit,
        PathValues.PEOPLE_ID: PeopleID,
        PathValues.PEOPLE_ID_PUBLIC_CONTACT_INFORMATION: PeopleIDPublicContactInformation,
        PathValues.PEOPLE_ID_LEGAL_NAME: PeopleIDLegalName,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_ID_HOME_WEB_ADDRESSES: PeopleIDHomeWebAddresses,
        PathValues.PEOPLE_ID_PREFERRED_NAME_SUBRESOURCE_ID: PeopleIDPreferredNameSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS: HomeContactInformationChangesIDInstantMessengers,
        PathValues.PEOPLE_ID_ADDITIONAL_NAMES: PeopleIDAdditionalNames,
        PathValues.PEOPLE_ID_WORK_ADDRESSES: PeopleIDWorkAddresses,
        PathValues.PEOPLE_ID_WORK_WEB_ADDRESSES: PeopleIDWorkWebAddresses,
        PathValues.PEOPLE_ID_HOME_EMAILS_SUBRESOURCE_ID: PeopleIDHomeEmailsSubresourceID,
        PathValues.PEOPLE_ID_WORK_PHONES_SUBRESOURCE_ID: PeopleIDWorkPhonesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES_SUBRESOURCE_ID: WorkContactInformationChangesIDWebAddressesSubresourceID,
        PathValues.PEOPLE_ID_HOME_INSTANT_MESSENGERS_SUBRESOURCE_ID: PeopleIDHomeInstantMessengersSubresourceID,
        PathValues.PEOPLE_ID_WORK_EMAILS_SUBRESOURCE_ID: PeopleIDWorkEmailsSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES_SUBRESOURCE_ID: HomeContactInformationChangesIDEmailAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS: WorkContactInformationChangesIDPhoneNumbers,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES: WorkContactInformationChangesIDEmailAddresses,
        PathValues.PEOPLE_ID_HOME_WEB_ADDRESSES_SUBRESOURCE_ID: PeopleIDHomeWebAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES_SUBRESOURCE_ID: WorkContactInformationChangesIDEmailAddressesSubresourceID,
        PathValues.PEOPLE_ID_HOME_INSTANT_MESSENGERS: PeopleIDHomeInstantMessengers,
        PathValues.PEOPLE_ID_HOME_EMAILS: PeopleIDHomeEmails,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES: WorkContactInformationChangesIDWebAddresses,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES_SUBRESOURCE_ID: HomeContactInformationChangesIDAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES_SUBRESOURCE_ID: WorkContactInformationChangesIDAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES: WorkContactInformationChangesIDAddresses,
        PathValues.COUNTRIES: Countries,
        PathValues.VALUES_NAME_COMPONENTS_HEREDITARY: ValuesNameComponentsHereditary,
        PathValues.VALUES_NAME_COMPONENTS_RELIGIOUS: ValuesNameComponentsReligious,
        PathValues.VALUES_NAME_COMPONENTS_HONORARY: ValuesNameComponentsHonorary,
        PathValues.VALUES_NAME_COMPONENTS_ROYAL: ValuesNameComponentsRoyal,
        PathValues.VALUES_NAME_COMPONENTS_TITLE: ValuesNameComponentsTitle,
        PathValues.VALUES_COMMON_PHONE_COUNTRY_PHONE_CODES: ValuesCommonPhoneCountryPhoneCodes,
        PathValues.VALUES_COUNTRY_COMPONENTS_COUNTRY_CITY: ValuesCountryComponentsCountryCity,
        PathValues.VALUES_NAME_COMPONENTS_SALUTATION: ValuesNameComponentsSalutation,
        PathValues.VALUES_PERSONAL_INFORMATION_COUNTRY_POPULATED_COUNTRY: ValuesPersonalInformationCountryPopulatedCountry,
        PathValues.VALUES_NAME_COMPONENTS_SOCIAL: ValuesNameComponentsSocial,
        PathValues.VALUES_NAME_COMPONENTS_PROFESSIONAL: ValuesNameComponentsProfessional,
        PathValues.VALUES_COUNTRY_COMPONENTS_COUNTRY: ValuesCountryComponentsCountry,
        PathValues.VALUES_NAME_COMPONENTS_ACADEMIC: ValuesNameComponentsAcademic,
        PathValues.VALUES_PERSONAL_INFORMATION_COUNTRY_ALLOWED_COUNTRY: ValuesPersonalInformationCountryAllowedCountry,
        PathValues.VALUES_COUNTRY_COMPONENTS_COUNTRY_REGION: ValuesCountryComponentsCountryRegion,
        PathValues.VALUES_COMMON_PHONE_PHONE_DEVICE_TYPES: ValuesCommonPhonePhoneDeviceTypes,
    }
)

path_to_api = PathToApi(
    {
        PathValues.PHONE_VALIDATION: PhoneValidation,
        PathValues.PEOPLE_ID_PERSONAL_INFORMATION: PeopleIDPersonalInformation,
        PathValues.PEOPLE_ID_HOME_ADDRESSES_SUBRESOURCE_ID: PeopleIDHomeAddressesSubresourceID,
        PathValues.COUNTRIES_ID: CountriesID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES: HomeContactInformationChangesIDWebAddresses,
        PathValues.PEOPLE_ID_ADDITIONAL_NAMES_SUBRESOURCE_ID: PeopleIDAdditionalNamesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS_SUBRESOURCE_ID: WorkContactInformationChangesIDPhoneNumbersSubresourceID,
        PathValues.PEOPLE_ID_AUDIO_NAME_PRONUNCIATION: PeopleIDAudioNamePronunciation,
        PathValues.PEOPLE_ID_PERSONAL_INFORMATION_SUBRESOURCE_ID: PeopleIDPersonalInformationSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS_SUBRESOURCE_ID: WorkContactInformationChangesIDInstantMessengersSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID: HomeContactInformationChangesID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS: HomeContactInformationChangesIDPhoneNumbers,
        PathValues.PEOPLE_ID_PHOTOS: PeopleIDPhotos,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_SUBMIT: WorkContactInformationChangesIDSubmit,
        PathValues.PEOPLE_ID_PREFERRED_NAME: PeopleIDPreferredName,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID: WorkContactInformationChangesID,
        PathValues.COUNTRIES_ID_ADDRESS_COMPONENTS: CountriesIDAddressComponents,
        PathValues.PEOPLE_ID_PHOTOS_SUBRESOURCE_ID: PeopleIDPhotosSubresourceID,
        PathValues.PEOPLE_ID_WORK_INSTANT_MESSENGERS: PeopleIDWorkInstantMessengers,
        PathValues.PEOPLE_ID_LEGAL_NAME_SUBRESOURCE_ID: PeopleIDLegalNameSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES: HomeContactInformationChangesIDEmailAddresses,
        PathValues.PEOPLE_ID_WORK_EMAILS: PeopleIDWorkEmails,
        PathValues.PEOPLE_ID_HOME_ADDRESSES: PeopleIDHomeAddresses,
        PathValues.PEOPLE_ID_HOME_PHONES_SUBRESOURCE_ID: PeopleIDHomePhonesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS: WorkContactInformationChangesIDInstantMessengers,
        PathValues.COUNTRIES_ID_NAME_COMPONENTS: CountriesIDNameComponents,
        PathValues.PEOPLE_ID_WORK_INSTANT_MESSENGERS_SUBRESOURCE_ID: PeopleIDWorkInstantMessengersSubresourceID,
        PathValues.PEOPLE_ID_WORK_ADDRESSES_SUBRESOURCE_ID: PeopleIDWorkAddressesSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES: HomeContactInformationChangesIDAddresses,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS_SUBRESOURCE_ID: HomeContactInformationChangesIDInstantMessengersSubresourceID,
        PathValues.PEOPLE_ID_WORK_PHONES: PeopleIDWorkPhones,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES_SUBRESOURCE_ID: HomeContactInformationChangesIDWebAddressesSubresourceID,
        PathValues.PEOPLE_ID_AUDIO_NAME_PRONUNCIATION_SUBRESOURCE_ID: PeopleIDAudioNamePronunciationSubresourceID,
        PathValues.PEOPLE_ID_WORK_WEB_ADDRESSES_SUBRESOURCE_ID: PeopleIDWorkWebAddressesSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS_SUBRESOURCE_ID: HomeContactInformationChangesIDPhoneNumbersSubresourceID,
        PathValues.PEOPLE_ID_PUBLIC_CONTACT_INFORMATION_SUBRESOURCE_ID: PeopleIDPublicContactInformationSubresourceID,
        PathValues.PEOPLE_ID_HOME_PHONES: PeopleIDHomePhones,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_SUBMIT: HomeContactInformationChangesIDSubmit,
        PathValues.PEOPLE_ID: PeopleID,
        PathValues.PEOPLE_ID_PUBLIC_CONTACT_INFORMATION: PeopleIDPublicContactInformation,
        PathValues.PEOPLE_ID_LEGAL_NAME: PeopleIDLegalName,
        PathValues.PEOPLE: People,
        PathValues.PEOPLE_ID_HOME_WEB_ADDRESSES: PeopleIDHomeWebAddresses,
        PathValues.PEOPLE_ID_PREFERRED_NAME_SUBRESOURCE_ID: PeopleIDPreferredNameSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_INSTANT_MESSENGERS: HomeContactInformationChangesIDInstantMessengers,
        PathValues.PEOPLE_ID_ADDITIONAL_NAMES: PeopleIDAdditionalNames,
        PathValues.PEOPLE_ID_WORK_ADDRESSES: PeopleIDWorkAddresses,
        PathValues.PEOPLE_ID_WORK_WEB_ADDRESSES: PeopleIDWorkWebAddresses,
        PathValues.PEOPLE_ID_HOME_EMAILS_SUBRESOURCE_ID: PeopleIDHomeEmailsSubresourceID,
        PathValues.PEOPLE_ID_WORK_PHONES_SUBRESOURCE_ID: PeopleIDWorkPhonesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES_SUBRESOURCE_ID: WorkContactInformationChangesIDWebAddressesSubresourceID,
        PathValues.PEOPLE_ID_HOME_INSTANT_MESSENGERS_SUBRESOURCE_ID: PeopleIDHomeInstantMessengersSubresourceID,
        PathValues.PEOPLE_ID_WORK_EMAILS_SUBRESOURCE_ID: PeopleIDWorkEmailsSubresourceID,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES_SUBRESOURCE_ID: HomeContactInformationChangesIDEmailAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_PHONE_NUMBERS: WorkContactInformationChangesIDPhoneNumbers,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES: WorkContactInformationChangesIDEmailAddresses,
        PathValues.PEOPLE_ID_HOME_WEB_ADDRESSES_SUBRESOURCE_ID: PeopleIDHomeWebAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_EMAIL_ADDRESSES_SUBRESOURCE_ID: WorkContactInformationChangesIDEmailAddressesSubresourceID,
        PathValues.PEOPLE_ID_HOME_INSTANT_MESSENGERS: PeopleIDHomeInstantMessengers,
        PathValues.PEOPLE_ID_HOME_EMAILS: PeopleIDHomeEmails,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_WEB_ADDRESSES: WorkContactInformationChangesIDWebAddresses,
        PathValues.HOME_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES_SUBRESOURCE_ID: HomeContactInformationChangesIDAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES_SUBRESOURCE_ID: WorkContactInformationChangesIDAddressesSubresourceID,
        PathValues.WORK_CONTACT_INFORMATION_CHANGES_ID_ADDRESSES: WorkContactInformationChangesIDAddresses,
        PathValues.COUNTRIES: Countries,
        PathValues.VALUES_NAME_COMPONENTS_HEREDITARY: ValuesNameComponentsHereditary,
        PathValues.VALUES_NAME_COMPONENTS_RELIGIOUS: ValuesNameComponentsReligious,
        PathValues.VALUES_NAME_COMPONENTS_HONORARY: ValuesNameComponentsHonorary,
        PathValues.VALUES_NAME_COMPONENTS_ROYAL: ValuesNameComponentsRoyal,
        PathValues.VALUES_NAME_COMPONENTS_TITLE: ValuesNameComponentsTitle,
        PathValues.VALUES_COMMON_PHONE_COUNTRY_PHONE_CODES: ValuesCommonPhoneCountryPhoneCodes,
        PathValues.VALUES_COUNTRY_COMPONENTS_COUNTRY_CITY: ValuesCountryComponentsCountryCity,
        PathValues.VALUES_NAME_COMPONENTS_SALUTATION: ValuesNameComponentsSalutation,
        PathValues.VALUES_PERSONAL_INFORMATION_COUNTRY_POPULATED_COUNTRY: ValuesPersonalInformationCountryPopulatedCountry,
        PathValues.VALUES_NAME_COMPONENTS_SOCIAL: ValuesNameComponentsSocial,
        PathValues.VALUES_NAME_COMPONENTS_PROFESSIONAL: ValuesNameComponentsProfessional,
        PathValues.VALUES_COUNTRY_COMPONENTS_COUNTRY: ValuesCountryComponentsCountry,
        PathValues.VALUES_NAME_COMPONENTS_ACADEMIC: ValuesNameComponentsAcademic,
        PathValues.VALUES_PERSONAL_INFORMATION_COUNTRY_ALLOWED_COUNTRY: ValuesPersonalInformationCountryAllowedCountry,
        PathValues.VALUES_COUNTRY_COMPONENTS_COUNTRY_REGION: ValuesCountryComponentsCountryRegion,
        PathValues.VALUES_COMMON_PHONE_PHONE_DEVICE_TYPES: ValuesCommonPhonePhoneDeviceTypes,
    }
)
