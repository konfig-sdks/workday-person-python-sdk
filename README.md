<div align="left">

[![Visit Workday](./header.png)](https://workday.com)

# Workday<a id="workday"></a>

The Person REST APIs enable you to access information about the worker person, including country-specific configuration information about name components.


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`workdayperson.prompt_values.get_allowed_country_data`](#workdaypersonprompt_valuesget_allowed_country_data)
  * [`workdayperson.prompt_values.get_country_phone_codes`](#workdaypersonprompt_valuesget_country_phone_codes)
  * [`workdayperson.prompt_values.get_hereditary_values`](#workdaypersonprompt_valuesget_hereditary_values)
  * [`workdayperson.prompt_values.get_instances`](#workdaypersonprompt_valuesget_instances)
  * [`workdayperson.prompt_values.get_instances_0`](#workdaypersonprompt_valuesget_instances_0)
  * [`workdayperson.prompt_values.get_instances_1`](#workdaypersonprompt_valuesget_instances_1)
  * [`workdayperson.prompt_values.get_instances_2`](#workdaypersonprompt_valuesget_instances_2)
  * [`workdayperson.prompt_values.get_instances_3`](#workdaypersonprompt_valuesget_instances_3)
  * [`workdayperson.prompt_values.get_instances_4`](#workdaypersonprompt_valuesget_instances_4)
  * [`workdayperson.prompt_values.get_instances_5`](#workdaypersonprompt_valuesget_instances_5)
  * [`workdayperson.prompt_values.get_options`](#workdaypersonprompt_valuesget_options)
  * [`workdayperson.prompt_values.get_options_0`](#workdaypersonprompt_valuesget_options_0)
  * [`workdayperson.prompt_values.get_options_1`](#workdaypersonprompt_valuesget_options_1)
  * [`workdayperson.prompt_values.get_phone_device_types`](#workdaypersonprompt_valuesget_phone_device_types)
  * [`workdayperson.prompt_values.get_title_components`](#workdaypersonprompt_valuesget_title_components)
  * [`workdayperson.prompt_values.list_country_data`](#workdaypersonprompt_valueslist_country_data)
  * [`workdayperson.countries.get_address_components`](#workdaypersoncountriesget_address_components)
  * [`workdayperson.countries.get_collection_information`](#workdaypersoncountriesget_collection_information)
  * [`workdayperson.countries.get_info`](#workdaypersoncountriesget_info)
  * [`workdayperson.countries.get_name_components`](#workdaypersoncountriesget_name_components)
  * [`workdayperson.home_contact_information_changes.create_email_address`](#workdaypersonhome_contact_information_changescreate_email_address)
  * [`workdayperson.home_contact_information_changes.create_instant_messenger`](#workdaypersonhome_contact_information_changescreate_instant_messenger)
  * [`workdayperson.home_contact_information_changes.create_new_address`](#workdaypersonhome_contact_information_changescreate_new_address)
  * [`workdayperson.home_contact_information_changes.create_phone_number`](#workdaypersonhome_contact_information_changescreate_phone_number)
  * [`workdayperson.home_contact_information_changes.create_web_address`](#workdaypersonhome_contact_information_changescreate_web_address)
  * [`workdayperson.home_contact_information_changes.get_address_as_staged`](#workdaypersonhome_contact_information_changesget_address_as_staged)
  * [`workdayperson.home_contact_information_changes.get_addresses_staged`](#workdaypersonhome_contact_information_changesget_addresses_staged)
  * [`workdayperson.home_contact_information_changes.get_email_address`](#workdaypersonhome_contact_information_changesget_email_address)
  * [`workdayperson.home_contact_information_changes.get_event_information`](#workdaypersonhome_contact_information_changesget_event_information)
  * [`workdayperson.home_contact_information_changes.get_instant_messenger`](#workdaypersonhome_contact_information_changesget_instant_messenger)
  * [`workdayperson.home_contact_information_changes.get_phone_numbers`](#workdaypersonhome_contact_information_changesget_phone_numbers)
  * [`workdayperson.home_contact_information_changes.get_staged_email_addresses`](#workdaypersonhome_contact_information_changesget_staged_email_addresses)
  * [`workdayperson.home_contact_information_changes.get_staged_instant_messengers`](#workdaypersonhome_contact_information_changesget_staged_instant_messengers)
  * [`workdayperson.home_contact_information_changes.get_staged_phone_number`](#workdaypersonhome_contact_information_changesget_staged_phone_number)
  * [`workdayperson.home_contact_information_changes.get_web_address`](#workdaypersonhome_contact_information_changesget_web_address)
  * [`workdayperson.home_contact_information_changes.get_web_addresses_staged`](#workdaypersonhome_contact_information_changesget_web_addresses_staged)
  * [`workdayperson.home_contact_information_changes.remove_address`](#workdaypersonhome_contact_information_changesremove_address)
  * [`workdayperson.home_contact_information_changes.remove_email_address`](#workdaypersonhome_contact_information_changesremove_email_address)
  * [`workdayperson.home_contact_information_changes.remove_instant_messenger`](#workdaypersonhome_contact_information_changesremove_instant_messenger)
  * [`workdayperson.home_contact_information_changes.remove_phone_number`](#workdaypersonhome_contact_information_changesremove_phone_number)
  * [`workdayperson.home_contact_information_changes.remove_web_address`](#workdaypersonhome_contact_information_changesremove_web_address)
  * [`workdayperson.home_contact_information_changes.submit_change`](#workdaypersonhome_contact_information_changessubmit_change)
  * [`workdayperson.home_contact_information_changes.update_address`](#workdaypersonhome_contact_information_changesupdate_address)
  * [`workdayperson.home_contact_information_changes.update_email_address`](#workdaypersonhome_contact_information_changesupdate_email_address)
  * [`workdayperson.home_contact_information_changes.update_instant_messenger`](#workdaypersonhome_contact_information_changesupdate_instant_messenger)
  * [`workdayperson.home_contact_information_changes.update_phone_number`](#workdaypersonhome_contact_information_changesupdate_phone_number)
  * [`workdayperson.home_contact_information_changes.update_web_address`](#workdaypersonhome_contact_information_changesupdate_web_address)
  * [`workdayperson.people.get_additional_name`](#workdaypersonpeopleget_additional_name)
  * [`workdayperson.people.get_additional_names`](#workdaypersonpeopleget_additional_names)
  * [`workdayperson.people.get_by_id`](#workdaypersonpeopleget_by_id)
  * [`workdayperson.people.get_home_address`](#workdaypersonpeopleget_home_address)
  * [`workdayperson.people.get_home_addresses`](#workdaypersonpeopleget_home_addresses)
  * [`workdayperson.people.get_home_email`](#workdaypersonpeopleget_home_email)
  * [`workdayperson.people.get_home_emails`](#workdaypersonpeopleget_home_emails)
  * [`workdayperson.people.get_home_instant_messenger_username`](#workdaypersonpeopleget_home_instant_messenger_username)
  * [`workdayperson.people.get_home_instant_messengers`](#workdaypersonpeopleget_home_instant_messengers)
  * [`workdayperson.people.get_home_phone`](#workdaypersonpeopleget_home_phone)
  * [`workdayperson.people.get_home_phones`](#workdaypersonpeopleget_home_phones)
  * [`workdayperson.people.get_home_web_address`](#workdaypersonpeopleget_home_web_address)
  * [`workdayperson.people.get_home_web_addresses`](#workdaypersonpeopleget_home_web_addresses)
  * [`workdayperson.people.get_legal_name`](#workdaypersonpeopleget_legal_name)
  * [`workdayperson.people.get_legal_name_0`](#workdaypersonpeopleget_legal_name_0)
  * [`workdayperson.people.get_name_pronunciation`](#workdaypersonpeopleget_name_pronunciation)
  * [`workdayperson.people.get_name_pronunciations`](#workdaypersonpeopleget_name_pronunciations)
  * [`workdayperson.people.get_person_by_id`](#workdaypersonpeopleget_person_by_id)
  * [`workdayperson.people.get_personal_info`](#workdaypersonpeopleget_personal_info)
  * [`workdayperson.people.get_personal_info_0`](#workdaypersonpeopleget_personal_info_0)
  * [`workdayperson.people.get_personal_photo`](#workdaypersonpeopleget_personal_photo)
  * [`workdayperson.people.get_personal_photos`](#workdaypersonpeopleget_personal_photos)
  * [`workdayperson.people.get_preferred_name`](#workdaypersonpeopleget_preferred_name)
  * [`workdayperson.people.get_preferred_name_0`](#workdaypersonpeopleget_preferred_name_0)
  * [`workdayperson.people.get_public_contact_information`](#workdaypersonpeopleget_public_contact_information)
  * [`workdayperson.people.get_public_contact_information_0`](#workdaypersonpeopleget_public_contact_information_0)
  * [`workdayperson.people.get_work_address`](#workdaypersonpeopleget_work_address)
  * [`workdayperson.people.get_work_addresses`](#workdaypersonpeopleget_work_addresses)
  * [`workdayperson.people.get_work_email`](#workdaypersonpeopleget_work_email)
  * [`workdayperson.people.get_work_emails`](#workdaypersonpeopleget_work_emails)
  * [`workdayperson.people.get_work_instant_messenger_username`](#workdaypersonpeopleget_work_instant_messenger_username)
  * [`workdayperson.people.get_work_instant_messenger_usernames`](#workdaypersonpeopleget_work_instant_messenger_usernames)
  * [`workdayperson.people.get_work_phone`](#workdaypersonpeopleget_work_phone)
  * [`workdayperson.people.get_work_phones`](#workdaypersonpeopleget_work_phones)
  * [`workdayperson.people.get_work_web_address`](#workdaypersonpeopleget_work_web_address)
  * [`workdayperson.people.get_work_web_addresses`](#workdaypersonpeopleget_work_web_addresses)
  * [`workdayperson.phone_validation.validate_phone_number`](#workdaypersonphone_validationvalidate_phone_number)
  * [`workdayperson.work_contact_information_changes.create_address`](#workdaypersonwork_contact_information_changescreate_address)
  * [`workdayperson.work_contact_information_changes.create_email_address`](#workdaypersonwork_contact_information_changescreate_email_address)
  * [`workdayperson.work_contact_information_changes.create_instant_messenger`](#workdaypersonwork_contact_information_changescreate_instant_messenger)
  * [`workdayperson.work_contact_information_changes.create_phone_number`](#workdaypersonwork_contact_information_changescreate_phone_number)
  * [`workdayperson.work_contact_information_changes.create_staged_web_address`](#workdaypersonwork_contact_information_changescreate_staged_web_address)
  * [`workdayperson.work_contact_information_changes.get_address_as_staged`](#workdaypersonwork_contact_information_changesget_address_as_staged)
  * [`workdayperson.work_contact_information_changes.get_addresses_staged`](#workdaypersonwork_contact_information_changesget_addresses_staged)
  * [`workdayperson.work_contact_information_changes.get_email_address`](#workdaypersonwork_contact_information_changesget_email_address)
  * [`workdayperson.work_contact_information_changes.get_event_info`](#workdaypersonwork_contact_information_changesget_event_info)
  * [`workdayperson.work_contact_information_changes.get_phone_number`](#workdaypersonwork_contact_information_changesget_phone_number)
  * [`workdayperson.work_contact_information_changes.get_phone_numbers`](#workdaypersonwork_contact_information_changesget_phone_numbers)
  * [`workdayperson.work_contact_information_changes.get_staged_email_addresses`](#workdaypersonwork_contact_information_changesget_staged_email_addresses)
  * [`workdayperson.work_contact_information_changes.get_staged_instant_messenger`](#workdaypersonwork_contact_information_changesget_staged_instant_messenger)
  * [`workdayperson.work_contact_information_changes.get_staged_instant_messengers`](#workdaypersonwork_contact_information_changesget_staged_instant_messengers)
  * [`workdayperson.work_contact_information_changes.get_web_address`](#workdaypersonwork_contact_information_changesget_web_address)
  * [`workdayperson.work_contact_information_changes.get_web_addresses_staged`](#workdaypersonwork_contact_information_changesget_web_addresses_staged)
  * [`workdayperson.work_contact_information_changes.remove_address`](#workdaypersonwork_contact_information_changesremove_address)
  * [`workdayperson.work_contact_information_changes.remove_email_address`](#workdaypersonwork_contact_information_changesremove_email_address)
  * [`workdayperson.work_contact_information_changes.remove_instant_messenger`](#workdaypersonwork_contact_information_changesremove_instant_messenger)
  * [`workdayperson.work_contact_information_changes.remove_phone_number`](#workdaypersonwork_contact_information_changesremove_phone_number)
  * [`workdayperson.work_contact_information_changes.remove_web_address`](#workdaypersonwork_contact_information_changesremove_web_address)
  * [`workdayperson.work_contact_information_changes.submit`](#workdaypersonwork_contact_information_changessubmit)
  * [`workdayperson.work_contact_information_changes.update_address`](#workdaypersonwork_contact_information_changesupdate_address)
  * [`workdayperson.work_contact_information_changes.update_alternate_work_location`](#workdaypersonwork_contact_information_changesupdate_alternate_work_location)
  * [`workdayperson.work_contact_information_changes.update_email_address`](#workdaypersonwork_contact_information_changesupdate_email_address)
  * [`workdayperson.work_contact_information_changes.update_instant_messenger`](#workdaypersonwork_contact_information_changesupdate_instant_messenger)
  * [`workdayperson.work_contact_information_changes.update_phone_number`](#workdaypersonwork_contact_information_changesupdate_phone_number)
  * [`workdayperson.work_contact_information_changes.update_web_address`](#workdaypersonwork_contact_information_changesupdate_web_address)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Workday&serviceName=Person&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from workday_person_python_sdk import WorkdayPerson, ApiException

workdayperson = WorkdayPerson(
)

try:
    get_allowed_country_data_response = workdayperson.prompt_values.get_allowed_country_data(
        limit=1,
        offset=1,
        person="string_example",
    )
    print(get_allowed_country_data_response)
except ApiException as e:
    print("Exception when calling PromptValuesApi.get_allowed_country_data: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python

import asyncio
from pprint import pprint
from workday_person_python_sdk import WorkdayPerson, ApiException

workdayperson = WorkdayPerson(
)

async def main():
    try:
        get_allowed_country_data_response = await workdayperson.prompt_values.aget_allowed_country_data(
            limit=1,
            offset=1,
            person="string_example",
        )
        print(get_allowed_country_data_response)
    except ApiException as e:
        print("Exception when calling PromptValuesApi.get_allowed_country_data: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)

asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from workday_person_python_sdk import WorkdayPerson, ApiException

workdayperson = WorkdayPerson(
)

try:
    get_allowed_country_data_response = workdayperson.prompt_values.raw.get_allowed_country_data(
        limit=1,
        offset=1,
        person="string_example",
    )
    pprint(get_allowed_country_data_response.body)
    pprint(get_allowed_country_data_response.body["total"])
    pprint(get_allowed_country_data_response.body["data"])
    pprint(get_allowed_country_data_response.headers)
    pprint(get_allowed_country_data_response.status)
    pprint(get_allowed_country_data_response.round_trip_time)
except ApiException as e:
    print("Exception when calling PromptValuesApi.get_allowed_country_data: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `workdayperson.prompt_values.get_allowed_country_data`<a id="workdaypersonprompt_valuesget_allowed_country_data"></a>

The set of countries a person is allowed to populated with country specific data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_allowed_country_data_response = workdayperson.prompt_values.get_allowed_country_data(
    limit=1,
    offset=1,
    person="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### person: `str`<a id="person-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/personalInformationCountry/allowedCountry` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_country_phone_codes`<a id="workdaypersonprompt_valuesget_country_phone_codes"></a>

Exposes prompting for country phone codes, which are used during the collection of phone numbers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_country_phone_codes_response = workdayperson.prompt_values.get_country_phone_codes(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/commonPhone/countryPhoneCodes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_hereditary_values`<a id="workdaypersonprompt_valuesget_hereditary_values"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_hereditary_values_response = workdayperson.prompt_values.get_hereditary_values(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/hereditary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_instances`<a id="workdaypersonprompt_valuesget_instances"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_response = workdayperson.prompt_values.get_instances(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/religious` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_instances_0`<a id="workdaypersonprompt_valuesget_instances_0"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_0_response = workdayperson.prompt_values.get_instances_0(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/honorary` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_instances_1`<a id="workdaypersonprompt_valuesget_instances_1"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_1_response = workdayperson.prompt_values.get_instances_1(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/countryComponents/countryCity` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_instances_2`<a id="workdaypersonprompt_valuesget_instances_2"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_2_response = workdayperson.prompt_values.get_instances_2(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/social` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_instances_3`<a id="workdaypersonprompt_valuesget_instances_3"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_3_response = workdayperson.prompt_values.get_instances_3(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/countryComponents/country` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_instances_4`<a id="workdaypersonprompt_valuesget_instances_4"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_4_response = workdayperson.prompt_values.get_instances_4(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/academic` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_instances_5`<a id="workdaypersonprompt_valuesget_instances_5"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instances_5_response = workdayperson.prompt_values.get_instances_5(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/countryComponents/countryRegion` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_options`<a id="workdaypersonprompt_valuesget_options"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_options_response = workdayperson.prompt_values.get_options(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/royal` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_options_0`<a id="workdaypersonprompt_valuesget_options_0"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_options_0_response = workdayperson.prompt_values.get_options_0(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/salutation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_options_1`<a id="workdaypersonprompt_valuesget_options_1"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_options_1_response = workdayperson.prompt_values.get_options_1(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/professional` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_phone_device_types`<a id="workdaypersonprompt_valuesget_phone_device_types"></a>

Exposes prompting for phone device types, which are used during the collection of phone numbers.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_phone_device_types_response = workdayperson.prompt_values.get_phone_device_types(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/commonPhone/phoneDeviceTypes` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.get_title_components`<a id="workdaypersonprompt_valuesget_title_components"></a>

Retrieves instances that can be used as values for other endpoint parameters in this service.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_title_components_response = workdayperson.prompt_values.get_title_components(
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/nameComponents/title` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.prompt_values.list_country_data`<a id="workdaypersonprompt_valueslist_country_data"></a>

The set of countries a person has populated with country specific data.

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_country_data_response = workdayperson.prompt_values.list_country_data(
    limit=1,
    offset=1,
    person="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default and maximum is 1000.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### person: `str`<a id="person-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`MULTIPLEINSTANCEMODELREFERENCE`](./workday_person_python_sdk/pydantic/multipleinstancemodelreference.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/values/personalInformationCountry/populatedCountry` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.countries.get_address_components`<a id="workdaypersoncountriesget_address_components"></a>

Retrieves the allowed address components and their configuration for the Country and a given Address Configuration Format.

Secured by: REST API Public

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_address_components_response = workdayperson.countries.get_address_components(
    id="ID_example",
    address_configuration_format="string_example",
    current_address="string_example",
    limit=1,
    offset=1,
    use_western_script=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### address_configuration_format: `str`<a id="address_configuration_format-str"></a>

The Address Configuration Format to return values for.  Required. Failure to provide this will result in no address components being returned. Available values are: - DEFAULT_AREAS - RECRUITING_FORMAT

##### current_address: `str`<a id="current_address-str"></a>

The existing address being updated.  Required when you use Default Format and a Country using Local Script to get component data for an existing address. Failure to provide this when appropriate may result in incorrect address component data being returned.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### use_western_script: `bool`<a id="use_western_script-bool"></a>

Enables Local Script components for Countries using Local Script in Default Format. Optional. When applicable, setting this value to true will enable Local Script components and enforce Western Components as optional. Local Components that are requireable will be enforced as required.

#### 🔄 Return<a id="🔄-return"></a>

[`CountriesGetAddressComponentsResponse`](./workday_person_python_sdk/pydantic/countries_get_address_components_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries/{ID}/addressComponents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.countries.get_collection_information`<a id="workdaypersoncountriesget_collection_information"></a>

Retrieves a collection of information about countries, including their alpha codes, and whether or not they are enabled for address lookup.

Secured by: REST API Public

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_collection_information_response = workdayperson.countries.get_collection_information(
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`CountriesGetCollectionInformationResponse`](./workday_person_python_sdk/pydantic/countries_get_collection_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.countries.get_info`<a id="workdaypersoncountriesget_info"></a>

Retrieves information about a country, including their alpha codes, and whether or not they are enabled for address lookup.

Secured by: REST API Public

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_info_response = workdayperson.countries.get_info(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`PersonCountryViewDefinitionF206795ea40e1000040cc6f5da4f002a`](./workday_person_python_sdk/pydantic/person_country_view_definition_f206795ea40e1000040cc6f5da4f002a.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.countries.get_name_components`<a id="workdaypersoncountriesget_name_components"></a>

Retrieves a collection of configuration information about name components. The Maintain Name Components by Country task enables administrators to configure the allowed and required name components for a country. 

You must specify the required nameConfigurationFormat query parameter.

Secured by: REST API Public

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_name_components_response = workdayperson.countries.get_name_components(
    id="ID_example",
    current_name="string_example",
    limit=1,
    name_configuration_format="string_example",
    offset=1,
    use_western_script=True,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### current_name: `str`<a id="current_name-str"></a>

The Workday ID of the person's current name being updated.  Required when you use Default Format and a Country using Local Script to get component data for an existing name. Failure to provide this when appropriate may result in incorrect name component data being returned.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### name_configuration_format: `str`<a id="name_configuration_format-str"></a>

The Name Configuration Format for which to return values.  Required. Failure to provide this will result in no name components being returned. Available values are: - RECRUITING_FORMAT - The name components specific to Recruiting. - OTHER_FUNCTIONAL_AREAS - The name components for all other functional areas in Workday. Example: nameConfigurationFormat=Name_Configuration_Format_ID=OTHER_FUNCTIONAL_AREAS

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### use_western_script: `bool`<a id="use_western_script-bool"></a>

If true, this method returns the set of allowed and required name components that uses Western Script.  The default is false.

#### 🔄 Return<a id="🔄-return"></a>

[`CountriesGetNameComponentsResponse`](./workday_person_python_sdk/pydantic/countries_get_name_components_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/countries/{ID}/nameComponents` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.create_email_address`<a id="workdaypersonhome_contact_information_changescreate_email_address"></a>

Creates a new email address staged by the parent business process event.

Secured by: Person Data: Home Email, Self-Service: Home Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_address_response = workdayperson.home_contact_information_changes.create_email_address(
    body={
        "email_address": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    email_address="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### email_address: `str`<a id="email_address-str"></a>

The email address.

##### usage: `Usage6333dee5ac2010000c8653405aaa0038`<a id="usage-usage6333dee5ac2010000c8653405aaa0038"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/type/email_address_reference0918d433e86b100018119edc1b8f00f7.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/pydantic/email_address_reference0918d433e86b100018119edc1b8f00f7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/emailAddresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.create_instant_messenger`<a id="workdaypersonhome_contact_information_changescreate_instant_messenger"></a>

Creates a new instant messenger staged by the parent business process event.

Secured by: Person Data: Home Instant Messenger, Self-Service: Home Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_instant_messenger_response = workdayperson.home_contact_information_changes.create_instant_messenger(
    body={
        "user_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    type=None,
    user_name="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### type: `TypeDe08a6c876a810000cb2e3dd8853001a`<a id="type-typede08a6c876a810000cb2e3dd8853001a"></a>

##### user_name: `str`<a id="user_name-str"></a>

The instant messenger account username.

##### usage: `UsageDe08a6c876a810000cb2e3d738be0019`<a id="usage-usagede08a6c876a810000cb2e3d738be0019"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/type/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/pydantic/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/instantMessengers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.create_new_address`<a id="workdaypersonhome_contact_information_changescreate_new_address"></a>

Creates a new address staged by the parent business process event.

Secured by: Person Data: Home Address, Self-Service: Home Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_new_address_response = workdayperson.home_contact_information_changes.create_new_address(
    body={
        "city_subdivision2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "effective": "2024-03-23T07:00:00.000Z",
        "address_line3": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "postal_code": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "number_days_wfh": 1,
        "address_line2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line3_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    city_subdivision2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line9="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line8_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    effective="2024-03-23T07:00:00.000Z",
    address_line3="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    postal_code="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    number_days_wfh=1,
    address_line2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line7="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line5="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line9_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line3_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_city=None,
    address_line7_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country=None,
    country_region=None,
    address_line5_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    address_line8="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### city_subdivision2_local: `str`<a id="city_subdivision2_local-str"></a>

City Subdivision 2 - Local

##### address_line9: `str`<a id="address_line9-str"></a>

Address Line 9

##### city_subdivision1_local: `str`<a id="city_subdivision1_local-str"></a>

City Subdivision 1 - Local

##### address_line8_local: `str`<a id="address_line8_local-str"></a>

Local Address Line 8

##### address_line6: `str`<a id="address_line6-str"></a>

Address Line 6

##### effective: `date`<a id="effective-date"></a>

The date this business process takes effect.

##### address_line3: `str`<a id="address_line3-str"></a>

Address Line 3

##### postal_code: `str`<a id="postal_code-str"></a>

Postal Code

##### number_days_wfh: `int`<a id="number_days_wfh-int"></a>

Number of Days WFH

##### address_line2_local: `str`<a id="address_line2_local-str"></a>

Local Address Line 2

##### city_local: `str`<a id="city_local-str"></a>

City - Local

##### address_line6_local: `str`<a id="address_line6_local-str"></a>

Local Address Line 6

##### address_line1: `str`<a id="address_line1-str"></a>

Address Line 1

##### city_subdivision1: `str`<a id="city_subdivision1-str"></a>

City Subdivision 1

##### region_subdivision2: `str`<a id="region_subdivision2-str"></a>

Region Subdivision 2

##### city: `str`<a id="city-str"></a>

City

##### address_line4_local: `str`<a id="address_line4_local-str"></a>

Local Address Line 4

##### region_subdivision1: `str`<a id="region_subdivision1-str"></a>

Region Subdivision 1

##### address_line7: `str`<a id="address_line7-str"></a>

Address Line 7

##### address_line2: `str`<a id="address_line2-str"></a>

Address Line 2

##### address_line5: `str`<a id="address_line5-str"></a>

Address Line 5

##### address_line9_local: `str`<a id="address_line9_local-str"></a>

Local Address Line 9

##### address_line3_local: `str`<a id="address_line3_local-str"></a>

Local Address Line 3

##### country_city: `CountryCity81f66ab16f7510005c53d89089074844`<a id="country_city-countrycity81f66ab16f7510005c53d89089074844"></a>

##### address_line7_local: `str`<a id="address_line7_local-str"></a>

Local Address Line 7

##### address_line1_local: `str`<a id="address_line1_local-str"></a>

Local Address Line 1

##### country: `Country81f66ab16f7510005c53d8fd5f5b4852`<a id="country-country81f66ab16f7510005c53d8fd5f5b4852"></a>

##### country_region: `CountryRegion81f66ab16f7510005c53d8be2fe44847`<a id="country_region-countryregion81f66ab16f7510005c53d8be2fe44847"></a>

##### address_line5_local: `str`<a id="address_line5_local-str"></a>

Local Address Line 5

##### region_subdivision1_local: `str`<a id="region_subdivision1_local-str"></a>

Region Subdivision 1 - Local

##### address_line4: `str`<a id="address_line4-str"></a>

Address Line 4

##### usage: `Usage81f66ab16f7510005c53d917926f4857`<a id="usage-usage81f66ab16f7510005c53d917926f4857"></a>

##### address_line8: `str`<a id="address_line8-str"></a>

Address Line 8

##### city_subdivision2: `str`<a id="city_subdivision2-str"></a>

City Subdivision 2

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HomeAddressReference81f66ab16f7510005c53d881876e4843`](./workday_person_python_sdk/type/home_address_reference81f66ab16f7510005c53d881876e4843.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HomeAddressReference81f66ab16f7510005c53d881876e4843`](./workday_person_python_sdk/pydantic/home_address_reference81f66ab16f7510005c53d881876e4843.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/addresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.create_phone_number`<a id="workdaypersonhome_contact_information_changescreate_phone_number"></a>

Creates a new phone number staged by the parent business process event.

Secured by: Person Data: Home Phone, Self-Service: Home Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_phone_number_response = workdayperson.home_contact_information_changes.create_phone_number(
    body={
        "extension": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "complete_phone_number": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    extension="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    complete_phone_number="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_phone_code=None,
    device_type=None,
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### extension: `str`<a id="extension-str"></a>

The phone extension.

##### complete_phone_number: `str`<a id="complete_phone_number-str"></a>

The complete phone number.

##### country_phone_code: `CountryPhoneCode1089da0ab90910000f7089365467088c`<a id="country_phone_code-countryphonecode1089da0ab90910000f7089365467088c"></a>

##### device_type: `DeviceType1089da0ab90910000f7089256c7b0888`<a id="device_type-devicetype1089da0ab90910000f7089256c7b0888"></a>

##### usage: `Usage1089da0ab90910000f70892f2de3088a`<a id="usage-usage1089da0ab90910000f70892f2de3088a"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/type/phone_reference1089da0ab90910000f70891a998b0887.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/pydantic/phone_reference1089da0ab90910000f70891a998b0887.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/phoneNumbers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.create_web_address`<a id="workdaypersonhome_contact_information_changescreate_web_address"></a>

Creates a new web address staged by the parent business process event.

Secured by: Person Data: Home Web Address, Self-Service: Home Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_web_address_response = workdayperson.home_contact_information_changes.create_web_address(
    body={
        "url": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    usage=None,
    url="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### usage: `UsageE357ae6d466510000ce25a08bfe401b3`<a id="usage-usagee357ae6d466510000ce25a08bfe401b3"></a>

##### url: `str`<a id="url-str"></a>

The complete URL address for the web address.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/type/web_address_reference_e357ae6d466510000ce259f323be01b0.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/pydantic/web_address_reference_e357ae6d466510000ce259f323be01b0.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/webAddresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_address_as_staged`<a id="workdaypersonhome_contact_information_changesget_address_as_staged"></a>

Retrieve an existing address as it exists when staged by the parent business process.

Secured by: Person Data: Home Address, Self-Service: Home Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_address_as_staged_response = workdayperson.home_contact_information_changes.get_address_as_staged(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeAddressReference81f66ab16f7510005c53d881876e4843`](./workday_person_python_sdk/pydantic/home_address_reference81f66ab16f7510005c53d881876e4843.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/addresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_addresses_staged`<a id="workdaypersonhome_contact_information_changesget_addresses_staged"></a>

Retrieve all addresses staged for update by the parent business process

Secured by: Person Data: Home Address, Self-Service: Home Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_addresses_staged_response = workdayperson.home_contact_information_changes.get_addresses_staged(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

##### used_for: `str`<a id="used_for-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`HomeContactInformationChangesGetAddressesStagedResponse`](./workday_person_python_sdk/pydantic/home_contact_information_changes_get_addresses_staged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_email_address`<a id="workdaypersonhome_contact_information_changesget_email_address"></a>

Retrieve an existing email address as it exists when staged by the parent business process.

Secured by: Person Data: Home Email, Self-Service: Home Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_address_response = workdayperson.home_contact_information_changes.get_email_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/pydantic/email_address_reference0918d433e86b100018119edc1b8f00f7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/emailAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_event_information`<a id="workdaypersonhome_contact_information_changesget_event_information"></a>

Returns basic information about the home contact change event.

Secured by: Change Home Contact Information (REST Service), Person Data: Home Contact Information, Self-Service: Home Contact Information

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_information_response = workdayperson.home_contact_information_changes.get_event_information(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`ChangeContactInformationEvent765b18aa13af1000064a10bf37b800ed`](./workday_person_python_sdk/pydantic/change_contact_information_event765b18aa13af1000064a10bf37b800ed.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_instant_messenger`<a id="workdaypersonhome_contact_information_changesget_instant_messenger"></a>

Retrieve an existing instant messenger as it exists when staged by the parent business process.

Secured by: Person Data: Home Instant Messenger, Self-Service: Home Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_instant_messenger_response = workdayperson.home_contact_information_changes.get_instant_messenger(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/pydantic/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/instantMessengers/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_phone_numbers`<a id="workdaypersonhome_contact_information_changesget_phone_numbers"></a>

Retrieve all phone numbers staged for update by the parent business process

Secured by: Person Data: Home Phone, Self-Service: Home Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_phone_numbers_response = workdayperson.home_contact_information_changes.get_phone_numbers(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary phone numbers.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public phone numbers.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeContactInformationChangesGetPhoneNumbersResponse`](./workday_person_python_sdk/pydantic/home_contact_information_changes_get_phone_numbers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/phoneNumbers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_staged_email_addresses`<a id="workdaypersonhome_contact_information_changesget_staged_email_addresses"></a>

Retrieve all email addresses staged for update by the parent business process

Secured by: Person Data: Home Email, Self-Service: Home Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staged_email_addresses_response = workdayperson.home_contact_information_changes.get_staged_email_addresses(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary email addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public email addresses.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeContactInformationChangesGetStagedEmailAddressesResponse`](./workday_person_python_sdk/pydantic/home_contact_information_changes_get_staged_email_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/emailAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_staged_instant_messengers`<a id="workdaypersonhome_contact_information_changesget_staged_instant_messengers"></a>

Retrieve all instant messengers staged for update by the parent business process

Secured by: Person Data: Home Instant Messenger, Self-Service: Home Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staged_instant_messengers_response = workdayperson.home_contact_information_changes.get_staged_instant_messengers(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary instant messenger account usernames.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public instant messenger account usernames.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeContactInformationChangesGetStagedInstantMessengersResponse`](./workday_person_python_sdk/pydantic/home_contact_information_changes_get_staged_instant_messengers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/instantMessengers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_staged_phone_number`<a id="workdaypersonhome_contact_information_changesget_staged_phone_number"></a>

Retrieve an existing phone number as it exists when staged by the parent business process.

Secured by: Person Data: Home Phone, Self-Service: Home Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staged_phone_number_response = workdayperson.home_contact_information_changes.get_staged_phone_number(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/pydantic/phone_reference1089da0ab90910000f70891a998b0887.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/phoneNumbers/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_web_address`<a id="workdaypersonhome_contact_information_changesget_web_address"></a>

Retrieve an existing web address as it exists when staged by the parent business process.

Secured by: Person Data: Home Web Address, Self-Service: Home Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_web_address_response = workdayperson.home_contact_information_changes.get_web_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/pydantic/web_address_reference_e357ae6d466510000ce259f323be01b0.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/webAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.get_web_addresses_staged`<a id="workdaypersonhome_contact_information_changesget_web_addresses_staged"></a>

Retrieve all web addresses staged for update by the parent business process

Secured by: Person Data: Home Web Address, Self-Service: Home Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_web_addresses_staged_response = workdayperson.home_contact_information_changes.get_web_addresses_staged(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary web addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public web addresses.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`HomeContactInformationChangesGetWebAddressesStagedResponse`](./workday_person_python_sdk/pydantic/home_contact_information_changes_get_web_addresses_staged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/webAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.remove_address`<a id="workdaypersonhome_contact_information_changesremove_address"></a>

Remove the specified address. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Home Address, Self-Service: Home Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.home_contact_information_changes.remove_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/addresses/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.remove_email_address`<a id="workdaypersonhome_contact_information_changesremove_email_address"></a>

Remove the specified email address. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Home Email, Self-Service: Home Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.home_contact_information_changes.remove_email_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/emailAddresses/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.remove_instant_messenger`<a id="workdaypersonhome_contact_information_changesremove_instant_messenger"></a>

Remove the specified instant messenger. If this instant messenger existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Home Instant Messenger, Self-Service: Home Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.home_contact_information_changes.remove_instant_messenger(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/instantMessengers/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.remove_phone_number`<a id="workdaypersonhome_contact_information_changesremove_phone_number"></a>

Remove the specified phone number. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Home Phone, Self-Service: Home Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.home_contact_information_changes.remove_phone_number(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/phoneNumbers/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.remove_web_address`<a id="workdaypersonhome_contact_information_changesremove_web_address"></a>

Remove the specified web address. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Home Web Address, Self-Service: Home Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.home_contact_information_changes.remove_web_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/webAddresses/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.submit_change`<a id="workdaypersonhome_contact_information_changessubmit_change"></a>

Submits the specified home contact information change ID. 

To submit the Home Contact Change event and initiate the Home Contact Change business process, specify an empty request body: {}.
To save for later, specify this request body:
{
    "businessProcessParameters": {
        "action":{
            "id": "d9e41a8c446c11de98360015c5e6daf6"
        }
    }
}

The action id value is the Workday ID of the Save for Later action. If you submit this endpoint with the Save for Later action, you can no longer edit nor resubmit the Home Contact Change event using the REST APIs. The user with correct permissions can edit and submit the saved Home Contact Change event in the Workday UI.

Secured by: Change Home Contact Information (REST Service)

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_change_response = workdayperson.home_contact_information_changes.submit_change(
    body={
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    business_process_parameters=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### business_process_parameters: `BusinessProcessParameters83f6f6b7c38d100009c7ad91dd414a16`<a id="business_process_parameters-businessprocessparameters83f6f6b7c38d100009c7ad91dd414a16"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeContactInformationEvent765b18aa13af1000064a10bf37b800ed`](./workday_person_python_sdk/type/change_contact_information_event765b18aa13af1000064a10bf37b800ed.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeContactInformationEvent765b18aa13af1000064a10bf37b800ed`](./workday_person_python_sdk/pydantic/change_contact_information_event765b18aa13af1000064a10bf37b800ed.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.update_address`<a id="workdaypersonhome_contact_information_changesupdate_address"></a>

Update an existing address that is staged for update by the parent business process event.

Secured by: Person Data: Home Address, Self-Service: Home Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_address_response = workdayperson.home_contact_information_changes.update_address(
    body={
        "city_subdivision2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "effective": "2024-03-23T07:00:00.000Z",
        "address_line3": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "postal_code": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "number_days_wfh": 1,
        "address_line2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line3_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    city_subdivision2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line9="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line8_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    effective="2024-03-23T07:00:00.000Z",
    address_line3="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    postal_code="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    number_days_wfh=1,
    address_line2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line7="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line5="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line9_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line3_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_city=None,
    address_line7_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country=None,
    country_region=None,
    address_line5_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    address_line8="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### city_subdivision2_local: `str`<a id="city_subdivision2_local-str"></a>

City Subdivision 2 - Local

##### address_line9: `str`<a id="address_line9-str"></a>

Address Line 9

##### city_subdivision1_local: `str`<a id="city_subdivision1_local-str"></a>

City Subdivision 1 - Local

##### address_line8_local: `str`<a id="address_line8_local-str"></a>

Local Address Line 8

##### address_line6: `str`<a id="address_line6-str"></a>

Address Line 6

##### effective: `date`<a id="effective-date"></a>

The date this business process takes effect.

##### address_line3: `str`<a id="address_line3-str"></a>

Address Line 3

##### postal_code: `str`<a id="postal_code-str"></a>

Postal Code

##### number_days_wfh: `int`<a id="number_days_wfh-int"></a>

Number of Days WFH

##### address_line2_local: `str`<a id="address_line2_local-str"></a>

Local Address Line 2

##### city_local: `str`<a id="city_local-str"></a>

City - Local

##### address_line6_local: `str`<a id="address_line6_local-str"></a>

Local Address Line 6

##### address_line1: `str`<a id="address_line1-str"></a>

Address Line 1

##### city_subdivision1: `str`<a id="city_subdivision1-str"></a>

City Subdivision 1

##### region_subdivision2: `str`<a id="region_subdivision2-str"></a>

Region Subdivision 2

##### city: `str`<a id="city-str"></a>

City

##### address_line4_local: `str`<a id="address_line4_local-str"></a>

Local Address Line 4

##### region_subdivision1: `str`<a id="region_subdivision1-str"></a>

Region Subdivision 1

##### address_line7: `str`<a id="address_line7-str"></a>

Address Line 7

##### address_line2: `str`<a id="address_line2-str"></a>

Address Line 2

##### address_line5: `str`<a id="address_line5-str"></a>

Address Line 5

##### address_line9_local: `str`<a id="address_line9_local-str"></a>

Local Address Line 9

##### address_line3_local: `str`<a id="address_line3_local-str"></a>

Local Address Line 3

##### country_city: `CountryCity81f66ab16f7510005c53d89089074844`<a id="country_city-countrycity81f66ab16f7510005c53d89089074844"></a>

##### address_line7_local: `str`<a id="address_line7_local-str"></a>

Local Address Line 7

##### address_line1_local: `str`<a id="address_line1_local-str"></a>

Local Address Line 1

##### country: `Country81f66ab16f7510005c53d8fd5f5b4852`<a id="country-country81f66ab16f7510005c53d8fd5f5b4852"></a>

##### country_region: `CountryRegion81f66ab16f7510005c53d8be2fe44847`<a id="country_region-countryregion81f66ab16f7510005c53d8be2fe44847"></a>

##### address_line5_local: `str`<a id="address_line5_local-str"></a>

Local Address Line 5

##### region_subdivision1_local: `str`<a id="region_subdivision1_local-str"></a>

Region Subdivision 1 - Local

##### address_line4: `str`<a id="address_line4-str"></a>

Address Line 4

##### usage: `Usage81f66ab16f7510005c53d917926f4857`<a id="usage-usage81f66ab16f7510005c53d917926f4857"></a>

##### address_line8: `str`<a id="address_line8-str"></a>

Address Line 8

##### city_subdivision2: `str`<a id="city_subdivision2-str"></a>

City Subdivision 2

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`HomeAddressReference81f66ab16f7510005c53d881876e4843`](./workday_person_python_sdk/type/home_address_reference81f66ab16f7510005c53d881876e4843.py)
#### 🔄 Return<a id="🔄-return"></a>

[`HomeAddressReference81f66ab16f7510005c53d881876e4843`](./workday_person_python_sdk/pydantic/home_address_reference81f66ab16f7510005c53d881876e4843.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/addresses/{subresourceID}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.update_email_address`<a id="workdaypersonhome_contact_information_changesupdate_email_address"></a>

Partially update an existing email address that is staged for update by the parent business process event.

Secured by: Person Data: Home Email, Self-Service: Home Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_address_response = workdayperson.home_contact_information_changes.update_email_address(
    body={
        "email_address": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    email_address="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### email_address: `str`<a id="email_address-str"></a>

The email address.

##### usage: `Usage6333dee5ac2010000c8653405aaa0038`<a id="usage-usage6333dee5ac2010000c8653405aaa0038"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/type/email_address_reference0918d433e86b100018119edc1b8f00f7.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/pydantic/email_address_reference0918d433e86b100018119edc1b8f00f7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/emailAddresses/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.update_instant_messenger`<a id="workdaypersonhome_contact_information_changesupdate_instant_messenger"></a>

Partially update an existing instant messenger that is staged for update by the parent business process event.

Secured by: Person Data: Home Instant Messenger, Self-Service: Home Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_instant_messenger_response = workdayperson.home_contact_information_changes.update_instant_messenger(
    body={
        "user_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    type=None,
    user_name="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### type: `TypeDe08a6c876a810000cb2e3dd8853001a`<a id="type-typede08a6c876a810000cb2e3dd8853001a"></a>

##### user_name: `str`<a id="user_name-str"></a>

The instant messenger account username.

##### usage: `UsageDe08a6c876a810000cb2e3d738be0019`<a id="usage-usagede08a6c876a810000cb2e3d738be0019"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/type/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/pydantic/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/instantMessengers/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.update_phone_number`<a id="workdaypersonhome_contact_information_changesupdate_phone_number"></a>

Partially update an existing phone number that is staged for update by the parent business process event.

Secured by: Person Data: Home Phone, Self-Service: Home Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_number_response = workdayperson.home_contact_information_changes.update_phone_number(
    body={
        "extension": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "complete_phone_number": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    extension="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    complete_phone_number="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_phone_code=None,
    device_type=None,
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### extension: `str`<a id="extension-str"></a>

The phone extension.

##### complete_phone_number: `str`<a id="complete_phone_number-str"></a>

The complete phone number.

##### country_phone_code: `CountryPhoneCode1089da0ab90910000f7089365467088c`<a id="country_phone_code-countryphonecode1089da0ab90910000f7089365467088c"></a>

##### device_type: `DeviceType1089da0ab90910000f7089256c7b0888`<a id="device_type-devicetype1089da0ab90910000f7089256c7b0888"></a>

##### usage: `Usage1089da0ab90910000f70892f2de3088a`<a id="usage-usage1089da0ab90910000f70892f2de3088a"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/type/phone_reference1089da0ab90910000f70891a998b0887.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/pydantic/phone_reference1089da0ab90910000f70891a998b0887.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/phoneNumbers/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.home_contact_information_changes.update_web_address`<a id="workdaypersonhome_contact_information_changesupdate_web_address"></a>

Partially update an existing web address that is staged for update by the parent business process event.

Secured by: Person Data: Home Web Address, Self-Service: Home Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_web_address_response = workdayperson.home_contact_information_changes.update_web_address(
    body={
        "url": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    usage=None,
    url="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### usage: `UsageE357ae6d466510000ce25a08bfe401b3`<a id="usage-usagee357ae6d466510000ce25a08bfe401b3"></a>

##### url: `str`<a id="url-str"></a>

The complete URL address for the web address.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/type/web_address_reference_e357ae6d466510000ce259f323be01b0.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/pydantic/web_address_reference_e357ae6d466510000ce259f323be01b0.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/homeContactInformationChanges/{ID}/webAddresses/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_additional_name`<a id="workdaypersonpeopleget_additional_name"></a>

Retrieves an additional name for the person with the specified ID.

Secured by: Person Data:  Name, Self-Service: Name

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_additional_name_response = workdayperson.people.get_additional_name(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`Name33e26848dc0010002f1ae76d63ec0061`](./workday_person_python_sdk/pydantic/name33e26848dc0010002f1ae76d63ec0061.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/additionalNames/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_additional_names`<a id="workdaypersonpeopleget_additional_names"></a>

Retrieves all additional names for the person with the specified ID.

Secured by: Person Data:  Name, Self-Service: Name

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_additional_names_response = workdayperson.people.get_additional_names(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetAdditionalNamesResponse`](./workday_person_python_sdk/pydantic/people_get_additional_names_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/additionalNames` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_by_id`<a id="workdaypersonpeopleget_by_id"></a>

Retrieves a person with the specified ID. You can use the returned ID from GET /people or GET /workers as the ID of the person whose information you want to retrieve.

Secured by: REST API Public

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = workdayperson.people.get_by_id(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`PersonRepresentationE451ce2c8b48100007c312f3f72700b3`](./workday_person_python_sdk/pydantic/person_representation_e451ce2c8b48100007c312f3f72700b3.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_address`<a id="workdaypersonpeopleget_home_address"></a>

Retrieves a home address for the person with the specified ID.

Secured by: Person Data: Home Address, Self-Service: Home Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_address_response = workdayperson.people.get_home_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`AddressReference9c3ab7b846e4100009e5ec55fa530024`](./workday_person_python_sdk/pydantic/address_reference9c3ab7b846e4100009e5ec55fa530024.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_addresses`<a id="workdaypersonpeopleget_home_addresses"></a>

Retrieves all home addresses for the person with the specified ID.

Secured by: Person Data: Home Address, Self-Service: Home Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_addresses_response = workdayperson.people.get_home_addresses(
    id="ID_example",
    effective="1970-01-01",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### effective: `date`<a id="effective-date"></a>

The effective date of the person's addresses using the yyyy-mm-dd format.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public addresses.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetHomeAddressesResponse`](./workday_person_python_sdk/pydantic/people_get_home_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_email`<a id="workdaypersonpeopleget_home_email"></a>

Retrieve a home email address for the person with the specified ID.

Secured by: Person Data: Home Email, Self-Service: Home Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_email_response = workdayperson.people.get_home_email(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`EmailReference9c3ab7b846e41000327e788d9664012a`](./workday_person_python_sdk/pydantic/email_reference9c3ab7b846e41000327e788d9664012a.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeEmails/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_emails`<a id="workdaypersonpeopleget_home_emails"></a>

Retrieve all home email addresses for the person with the specified ID.

Secured by: Person Data: Home Email, Self-Service: Home Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_emails_response = workdayperson.people.get_home_emails(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary email addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public email addresses.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetHomeEmailsResponse`](./workday_person_python_sdk/pydantic/people_get_home_emails_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeEmails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_instant_messenger_username`<a id="workdaypersonpeopleget_home_instant_messenger_username"></a>

Retrieves a home instant messenger account username for the person with the specified ID.

Secured by: Person Data: Home Instant Messenger, Self-Service: Home Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_instant_messenger_username_response = workdayperson.people.get_home_instant_messenger_username(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerAccount33e26848dc00100036f723337ebb0132`](./workday_person_python_sdk/pydantic/instant_messenger_account33e26848dc00100036f723337ebb0132.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeInstantMessengers/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_instant_messengers`<a id="workdaypersonpeopleget_home_instant_messengers"></a>

Retrieves all home instant messenger account usernames for the person with the specified ID.

Secured by: Person Data: Home Instant Messenger, Self-Service: Home Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_instant_messengers_response = workdayperson.people.get_home_instant_messengers(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary instant messenger account usernames.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public instant messenger usernames.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetHomeInstantMessengersResponse`](./workday_person_python_sdk/pydantic/people_get_home_instant_messengers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeInstantMessengers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_phone`<a id="workdaypersonpeopleget_home_phone"></a>

Retrieves a home phone number for the person with the specified ID.

Secured by: Person Data: Home Phone, Self-Service: Home Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_phone_response = workdayperson.people.get_home_phone(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd`](./workday_person_python_sdk/pydantic/phone_reference_df014bc8b5fa10000af0fe7cb0ab00dd.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homePhones/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_phones`<a id="workdaypersonpeopleget_home_phones"></a>

Retrieves all home phone numbers for the person with the specified ID.

Secured by: Person Data: Home Phone, Self-Service: Home Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_phones_response = workdayperson.people.get_home_phones(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary phone numbers.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public phone numbers.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetHomePhonesResponse`](./workday_person_python_sdk/pydantic/people_get_home_phones_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homePhones` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_web_address`<a id="workdaypersonpeopleget_home_web_address"></a>

Retrieves a home web address for the person with the specified ID.

Secured by: Person Data: Home Web Address, Self-Service: Home Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_web_address_response = workdayperson.people.get_home_web_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`WebAddress33e26848dc0010003893a0202ced0165`](./workday_person_python_sdk/pydantic/web_address33e26848dc0010003893a0202ced0165.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeWebAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_home_web_addresses`<a id="workdaypersonpeopleget_home_web_addresses"></a>

Retrieves all home web addresses for the person with the specified ID.

Secured by: Person Data: Home Web Address, Self-Service: Home Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_home_web_addresses_response = workdayperson.people.get_home_web_addresses(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary web addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public web addresses.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetHomeWebAddressesResponse`](./workday_person_python_sdk/pydantic/people_get_home_web_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/homeWebAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_legal_name`<a id="workdaypersonpeopleget_legal_name"></a>

Retrieves the legal name for the person with the specified ID.

Secured by: Person Data: Legal Name, Self-Service: Legal Name

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_legal_name_response = workdayperson.people.get_legal_name(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`Name33e26848dc0010002f1ae76d63ec0061`](./workday_person_python_sdk/pydantic/name33e26848dc0010002f1ae76d63ec0061.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/legalName/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_legal_name_0`<a id="workdaypersonpeopleget_legal_name_0"></a>

Retrieves the legal name for the person with the specified ID.

Secured by: Person Data: Legal Name, Self-Service: Legal Name

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_legal_name_0_response = workdayperson.people.get_legal_name_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetLegalNameResponse`](./workday_person_python_sdk/pydantic/people_get_legal_name_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/legalName` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_name_pronunciation`<a id="workdaypersonpeopleget_name_pronunciation"></a>

Retrieves a Audio Name Pronunciation of a Person

Secured by: Person Data: Name Pronunciation

Scope: Personal Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_name_pronunciation_response = workdayperson.people.get_name_pronunciation(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`MediaDownload5d5f0fb1184b10000b16f0e5c20f0000`](./workday_person_python_sdk/pydantic/media_download5d5f0fb1184b10000b16f0e5c20f0000.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/audioNamePronunciation/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_name_pronunciations`<a id="workdaypersonpeopleget_name_pronunciations"></a>

Retrieves all Audio Name Pronunciations of a Person

Secured by: Person Data: Name Pronunciation

Scope: Personal Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_name_pronunciations_response = workdayperson.people.get_name_pronunciations(
    id="ID_example",
    current_audio=True,
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### current_audio: `bool`<a id="current_audio-bool"></a>

Download only the currently active audio

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetNamePronunciationsResponse`](./workday_person_python_sdk/pydantic/people_get_name_pronunciations_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/audioNamePronunciation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_person_by_id`<a id="workdaypersonpeopleget_person_by_id"></a>

Retrieves a person of the specified ID.
You can use the returned ID from GET /people or GET /workers as the ID of the person whose information you want to retrieve.
When the person has any person information, for example:home addresses, a hyperlink to the resource of the information will be included in the response.

Secured by: REST API Public

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_person_by_id_response = workdayperson.people.get_person_by_id(
    limit=1,
    offset=1,
    universal_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### universal_id: `str`<a id="universal_id-str"></a>

The Universal ID of the person you want to retrieve.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetPersonByIdResponse`](./workday_person_python_sdk/pydantic/people_get_person_by_id_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_personal_info`<a id="workdaypersonpeopleget_personal_info"></a>

Retrieves all personal information for the person with the specified ID.

Secured by: Person Data: Personal Information, Self-Service: Personal Information

Scope: Personal Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_personal_info_response = workdayperson.people.get_personal_info(
    id="ID_example",
    country="string_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### country: `str`<a id="country-str"></a>

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetPersonalInfoResponse`](./workday_person_python_sdk/pydantic/people_get_personal_info_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/personalInformation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_personal_info_0`<a id="workdaypersonpeopleget_personal_info_0"></a>

Retrieves personal information for the person with the specified ID.

Secured by: Person Data: Personal Information, Self-Service: Personal Information

Scope: Personal Data

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_personal_info_0_response = workdayperson.people.get_personal_info_0(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`PersonalInformation414c4cee7d91100023fe329d6f900018`](./workday_person_python_sdk/pydantic/personal_information414c4cee7d91100023fe329d6f900018.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/personalInformation/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_personal_photo`<a id="workdaypersonpeopleget_personal_photo"></a>

Retrieves a personal photo for the person with the specified ID.

Secured by: Person Data: Personal Photo, Self-Service: Personal Photo

Scope: Personal Data

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_personal_photo_response = workdayperson.people.get_personal_photo(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`PersonPhoto6b9baf67ce60100007d43c79e7a30011`](./workday_person_python_sdk/pydantic/person_photo6b9baf67ce60100007d43c79e7a30011.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/photos/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_personal_photos`<a id="workdaypersonpeopleget_personal_photos"></a>

Retrieves all personal photos for the person with the specified ID.

Secured by: Person Data: Personal Photo, Self-Service: Personal Photo

Scope: Personal Data

Contains attachment(s)

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_personal_photos_response = workdayperson.people.get_personal_photos(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetPersonalPhotosResponse`](./workday_person_python_sdk/pydantic/people_get_personal_photos_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/photos` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_preferred_name`<a id="workdaypersonpeopleget_preferred_name"></a>

Retrieves the preferred name for the person with the specified ID.

Secured by: Person Data: Preferred Name, Self-Service: Preferred Name

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_preferred_name_response = workdayperson.people.get_preferred_name(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetPreferredNameResponse`](./workday_person_python_sdk/pydantic/people_get_preferred_name_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/preferredName` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_preferred_name_0`<a id="workdaypersonpeopleget_preferred_name_0"></a>

Retrieves the preferred name for the person with the specified ID.

Secured by: Person Data: Preferred Name, Self-Service: Preferred Name

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_preferred_name_0_response = workdayperson.people.get_preferred_name_0(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`Name33e26848dc0010002f1ae76d63ec0061`](./workday_person_python_sdk/pydantic/name33e26848dc0010002f1ae76d63ec0061.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/preferredName/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_public_contact_information`<a id="workdaypersonpeopleget_public_contact_information"></a>

Retrieves public contact information for the person with the specified ID.

Secured by: REST API Public

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_public_contact_information_response = workdayperson.people.get_public_contact_information(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`PersonPublicRepresentationD8f2aecf3d63100016a77ab413a20235`](./workday_person_python_sdk/pydantic/person_public_representation_d8f2aecf3d63100016a77ab413a20235.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/publicContactInformation/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_public_contact_information_0`<a id="workdaypersonpeopleget_public_contact_information_0"></a>

Retrieves all public contact information for the person with the specified ID.

Secured by: REST API Public

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_public_contact_information_0_response = workdayperson.people.get_public_contact_information_0(
    id="ID_example",
    limit=1,
    offset=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetPublicContactInformationResponse`](./workday_person_python_sdk/pydantic/people_get_public_contact_information_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/publicContactInformation` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_address`<a id="workdaypersonpeopleget_work_address"></a>

Retrieves a work address for the person with the specified ID.

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_address_response = workdayperson.people.get_work_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`AddressReference9c3ab7b846e4100009e5ec55fa530024`](./workday_person_python_sdk/pydantic/address_reference9c3ab7b846e4100009e5ec55fa530024.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_addresses`<a id="workdaypersonpeopleget_work_addresses"></a>

Retrieves all work addresses for the person with the specified ID.

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_addresses_response = workdayperson.people.get_work_addresses(
    id="ID_example",
    effective="1970-01-01",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### effective: `date`<a id="effective-date"></a>

The effective date of the person's addresses using the yyyy-mm-dd format.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public addresses.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetWorkAddressesResponse`](./workday_person_python_sdk/pydantic/people_get_work_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_email`<a id="workdaypersonpeopleget_work_email"></a>

Retrieves a work email address for the person with the specified ID.

Secured by: Person Data: Work Email, Self-Service: Work Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_email_response = workdayperson.people.get_work_email(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`EmailReference9c3ab7b846e41000327e788d9664012a`](./workday_person_python_sdk/pydantic/email_reference9c3ab7b846e41000327e788d9664012a.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workEmails/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_emails`<a id="workdaypersonpeopleget_work_emails"></a>

Retrieves all work email addresses for the person with the specified ID.

Secured by: Person Data: Work Email, Self-Service: Work Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_emails_response = workdayperson.people.get_work_emails(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary email addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public email addresses.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetWorkEmailsResponse`](./workday_person_python_sdk/pydantic/people_get_work_emails_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workEmails` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_instant_messenger_username`<a id="workdaypersonpeopleget_work_instant_messenger_username"></a>

Retrieves a work instant messenger account username for the person with the specified ID.

Secured by: Person Data: Work Instant Messenger, Self-Service: Work Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_instant_messenger_username_response = workdayperson.people.get_work_instant_messenger_username(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerAccount33e26848dc00100036f723337ebb0132`](./workday_person_python_sdk/pydantic/instant_messenger_account33e26848dc00100036f723337ebb0132.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workInstantMessengers/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_instant_messenger_usernames`<a id="workdaypersonpeopleget_work_instant_messenger_usernames"></a>

Retrieves all work instant messenger account usernames for the person with the specified ID.

Secured by: Person Data: Work Instant Messenger, Self-Service: Work Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_instant_messenger_usernames_response = workdayperson.people.get_work_instant_messenger_usernames(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary instant messenger account usernames.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public instant messenger usernames.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetWorkInstantMessengerUsernamesResponse`](./workday_person_python_sdk/pydantic/people_get_work_instant_messenger_usernames_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workInstantMessengers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_phone`<a id="workdaypersonpeopleget_work_phone"></a>

Retrieves a work phone number for the person with the specified ID.

Secured by: Person Data: Work Phone, Self-Service: Work Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_phone_response = workdayperson.people.get_work_phone(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReferenceDf014bc8b5fa10000af0fe7cb0ab00dd`](./workday_person_python_sdk/pydantic/phone_reference_df014bc8b5fa10000af0fe7cb0ab00dd.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workPhones/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_phones`<a id="workdaypersonpeopleget_work_phones"></a>

Retrieves all work phone numbers for the person with the specified ID.

Secured by: Person Data: Work Phone, Self-Service: Work Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_phones_response = workdayperson.people.get_work_phones(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary phone numbers.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public phone numbers.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetWorkPhonesResponse`](./workday_person_python_sdk/pydantic/people_get_work_phones_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workPhones` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_web_address`<a id="workdaypersonpeopleget_work_web_address"></a>

Retrieves a work web address for the person with the specified ID.

Secured by: Person Data: Work Web Address, Self-Service: Work Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_web_address_response = workdayperson.people.get_work_web_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`WebAddress33e26848dc0010003893a0202ced0165`](./workday_person_python_sdk/pydantic/web_address33e26848dc0010003893a0202ced0165.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workWebAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.people.get_work_web_addresses`<a id="workdaypersonpeopleget_work_web_addresses"></a>

Retrieves all work web addresses for the person with the specified ID.

Secured by: Person Data: Work Web Address, Self-Service: Work Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_work_web_addresses_response = workdayperson.people.get_work_web_addresses(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary web addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public web addresses.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`PeopleGetWorkWebAddressesResponse`](./workday_person_python_sdk/pydantic/people_get_work_web_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/people/{ID}/workWebAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.phone_validation.validate_phone_number`<a id="workdaypersonphone_validationvalidate_phone_number"></a>

Validates the specified completePhoneNumber in the request body.
The completePhoneNumber field is required in the request body.

If the specified completePhoneNumber is valid, this method returns the 201 response status. If the specified completePhoneNumber is invalid, this method returns the 400 response status with a validation error message. 

This method assumes the Allowed Phone Validations for the country of the phone is enabled on the Tenant Setup - Global configuration.
If the tenant configuration has disabled the Allowed Phone Validations for the associated country, the validation returns as valid.

Secured by: REST API Public

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
validate_phone_number_response = workdayperson.phone_validation.validate_phone_number(
    body={
        "complete_phone_number": "+19259519000",
    },
    device_type=None,
    complete_phone_number="+19259519000",
    country_phone_code=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### device_type: `DeviceTypeDb1991f2fb091000169c5e28fc0400bb`<a id="device_type-devicetypedb1991f2fb091000169c5e28fc0400bb"></a>

##### complete_phone_number: `str`<a id="complete_phone_number-str"></a>

The complete phone number.

##### country_phone_code: `CountryPhoneCodeDb1991f2fb091000169c5e0cb7c200b9`<a id="country_phone_code-countryphonecodedb1991f2fb091000169c5e0cb7c200b9"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PhoneNumberValidationDb1991f2fb091000169c5dfa023800b8`](./workday_person_python_sdk/type/phone_number_validation_db1991f2fb091000169c5dfa023800b8.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PhoneNumberValidationDb1991f2fb091000169c5dfa023800b8`](./workday_person_python_sdk/pydantic/phone_number_validation_db1991f2fb091000169c5dfa023800b8.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/phoneValidation` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.create_address`<a id="workdaypersonwork_contact_information_changescreate_address"></a>

Creates a new address staged by the parent business process event.

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_address_response = workdayperson.work_contact_information_changes.create_address(
    body={
        "address_line3": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line3_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "postal_code": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "effective": "2024-03-23T07:00:00.000Z",
        "city_subdivision2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    address_line3="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line8_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country=None,
    address_line9="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line8="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line5_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line3_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    postal_code="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line9_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line7_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_region=None,
    address_line5="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    region_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line7="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    effective="2024-03-23T07:00:00.000Z",
    city_subdivision2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_city=None,
    city_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### address_line3: `str`<a id="address_line3-str"></a>

Address Line 3

##### address_line8_local: `str`<a id="address_line8_local-str"></a>

Local Address Line 8

##### region_subdivision2: `str`<a id="region_subdivision2-str"></a>

Region Subdivision 2

##### city_local: `str`<a id="city_local-str"></a>

City - Local

##### city_subdivision1_local: `str`<a id="city_subdivision1_local-str"></a>

City Subdivision 1 - Local

##### address_line6_local: `str`<a id="address_line6_local-str"></a>

Local Address Line 6

##### address_line4_local: `str`<a id="address_line4_local-str"></a>

Local Address Line 4

##### region_subdivision1_local: `str`<a id="region_subdivision1_local-str"></a>

Region Subdivision 1 - Local

##### country: `CountryC1bb9f46f65210002d2fa329fe6700b4`<a id="country-countryc1bb9f46f65210002d2fa329fe6700b4"></a>

##### address_line9: `str`<a id="address_line9-str"></a>

Address Line 9

##### address_line4: `str`<a id="address_line4-str"></a>

Address Line 4

##### city_subdivision1: `str`<a id="city_subdivision1-str"></a>

City Subdivision 1

##### address_line8: `str`<a id="address_line8-str"></a>

Address Line 8

##### address_line1: `str`<a id="address_line1-str"></a>

Address Line 1

##### address_line5_local: `str`<a id="address_line5_local-str"></a>

Local Address Line 5

##### address_line6: `str`<a id="address_line6-str"></a>

Address Line 6

##### city: `str`<a id="city-str"></a>

City

##### address_line3_local: `str`<a id="address_line3_local-str"></a>

Local Address Line 3

##### postal_code: `str`<a id="postal_code-str"></a>

Postal Code

##### address_line9_local: `str`<a id="address_line9_local-str"></a>

Local Address Line 9

##### address_line2: `str`<a id="address_line2-str"></a>

Address Line 2

##### address_line1_local: `str`<a id="address_line1_local-str"></a>

Local Address Line 1

##### address_line7_local: `str`<a id="address_line7_local-str"></a>

Local Address Line 7

##### country_region: `CountryRegionC1bb9f46f65210002d2fa322479a00b2`<a id="country_region-countryregionc1bb9f46f65210002d2fa322479a00b2"></a>

##### address_line5: `str`<a id="address_line5-str"></a>

Address Line 5

##### usage: `UsageC1bb9f46f65210002d2fa2e7babe00a8`<a id="usage-usagec1bb9f46f65210002d2fa2e7babe00a8"></a>

##### region_subdivision1: `str`<a id="region_subdivision1-str"></a>

Region Subdivision 1

##### address_line7: `str`<a id="address_line7-str"></a>

Address Line 7

##### effective: `date`<a id="effective-date"></a>

The date this business process takes effect.

##### city_subdivision2_local: `str`<a id="city_subdivision2_local-str"></a>

City Subdivision 2 - Local

##### address_line2_local: `str`<a id="address_line2_local-str"></a>

Local Address Line 2

##### country_city: `CountryCityC1bb9f46f65210002d2fa2bb24a300a1`<a id="country_city-countrycityc1bb9f46f65210002d2fa2bb24a300a1"></a>

##### city_subdivision2: `str`<a id="city_subdivision2-str"></a>

City Subdivision 2

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkAddressReferenceC1bb9f46f65210002d2fa259a1c10095`](./workday_person_python_sdk/type/work_address_reference_c1bb9f46f65210002d2fa259a1c10095.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkAddressReferenceC1bb9f46f65210002d2fa259a1c10095`](./workday_person_python_sdk/pydantic/work_address_reference_c1bb9f46f65210002d2fa259a1c10095.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/addresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.create_email_address`<a id="workdaypersonwork_contact_information_changescreate_email_address"></a>

Creates a new email address staged by the parent business process event.

Secured by: Person Data: Work Email, Self-Service: Work Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_email_address_response = workdayperson.work_contact_information_changes.create_email_address(
    body={
        "email_address": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    email_address="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### email_address: `str`<a id="email_address-str"></a>

The email address.

##### usage: `Usage6333dee5ac2010000c8653405aaa0038`<a id="usage-usage6333dee5ac2010000c8653405aaa0038"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/type/email_address_reference0918d433e86b100018119edc1b8f00f7.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/pydantic/email_address_reference0918d433e86b100018119edc1b8f00f7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/emailAddresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.create_instant_messenger`<a id="workdaypersonwork_contact_information_changescreate_instant_messenger"></a>

Creates a new instant messenger staged by the parent business process event.

Secured by: Person Data: Work Instant Messenger, Self-Service: Work Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_instant_messenger_response = workdayperson.work_contact_information_changes.create_instant_messenger(
    body={
        "user_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    type=None,
    user_name="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### type: `TypeDe08a6c876a810000cb2e3dd8853001a`<a id="type-typede08a6c876a810000cb2e3dd8853001a"></a>

##### user_name: `str`<a id="user_name-str"></a>

The instant messenger account username.

##### usage: `UsageDe08a6c876a810000cb2e3d738be0019`<a id="usage-usagede08a6c876a810000cb2e3d738be0019"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/type/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/pydantic/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/instantMessengers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.create_phone_number`<a id="workdaypersonwork_contact_information_changescreate_phone_number"></a>

Creates a new phone number staged by the parent business process event.

Secured by: Person Data: Work Phone, Self-Service: Work Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_phone_number_response = workdayperson.work_contact_information_changes.create_phone_number(
    body={
        "extension": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "complete_phone_number": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    extension="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    complete_phone_number="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_phone_code=None,
    device_type=None,
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### extension: `str`<a id="extension-str"></a>

The phone extension.

##### complete_phone_number: `str`<a id="complete_phone_number-str"></a>

The complete phone number.

##### country_phone_code: `CountryPhoneCode1089da0ab90910000f7089365467088c`<a id="country_phone_code-countryphonecode1089da0ab90910000f7089365467088c"></a>

##### device_type: `DeviceType1089da0ab90910000f7089256c7b0888`<a id="device_type-devicetype1089da0ab90910000f7089256c7b0888"></a>

##### usage: `Usage1089da0ab90910000f70892f2de3088a`<a id="usage-usage1089da0ab90910000f70892f2de3088a"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/type/phone_reference1089da0ab90910000f70891a998b0887.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/pydantic/phone_reference1089da0ab90910000f70891a998b0887.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/phoneNumbers` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.create_staged_web_address`<a id="workdaypersonwork_contact_information_changescreate_staged_web_address"></a>

Creates a new web address staged by the parent business process event.

Secured by: Person Data: Work Web Address, Self-Service: Work Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_staged_web_address_response = workdayperson.work_contact_information_changes.create_staged_web_address(
    body={
        "url": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    usage=None,
    url="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### usage: `UsageE357ae6d466510000ce25a08bfe401b3`<a id="usage-usagee357ae6d466510000ce25a08bfe401b3"></a>

##### url: `str`<a id="url-str"></a>

The complete URL address for the web address.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/type/web_address_reference_e357ae6d466510000ce259f323be01b0.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/pydantic/web_address_reference_e357ae6d466510000ce259f323be01b0.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/webAddresses` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_address_as_staged`<a id="workdaypersonwork_contact_information_changesget_address_as_staged"></a>

Retrieve an existing address as it exists when staged by the parent business process.

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_address_as_staged_response = workdayperson.work_contact_information_changes.get_address_as_staged(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkAddressReferenceC1bb9f46f65210002d2fa259a1c10095`](./workday_person_python_sdk/pydantic/work_address_reference_c1bb9f46f65210002d2fa259a1c10095.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/addresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_addresses_staged`<a id="workdaypersonwork_contact_information_changesget_addresses_staged"></a>

Retrieve all addresses staged for update by the parent business process

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_addresses_staged_response = workdayperson.work_contact_information_changes.get_addresses_staged(
    id="ID_example",
    limit=1,
    offset=1,
    public_only=True,
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### public_only: `bool`<a id="public_only-bool"></a>

##### used_for: `str`<a id="used_for-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactInformationChangesGetAddressesStagedResponse`](./workday_person_python_sdk/pydantic/work_contact_information_changes_get_addresses_staged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/addresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_email_address`<a id="workdaypersonwork_contact_information_changesget_email_address"></a>

Retrieve an existing email address as it exists when staged by the parent business process.

Secured by: Person Data: Work Email, Self-Service: Work Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_email_address_response = workdayperson.work_contact_information_changes.get_email_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/pydantic/email_address_reference0918d433e86b100018119edc1b8f00f7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/emailAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_event_info`<a id="workdaypersonwork_contact_information_changesget_event_info"></a>

Returns basic information about the work contact change event, as well as the Alternate Work Location staged by the event, if there is one.

Secured by: Change Work Contact Information (REST Service), Person Data: Work Contact Information, Self-Service: Work Contact Information

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_event_info_response = workdayperson.work_contact_information_changes.get_event_info(
    id="ID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactChangeEventViewBdfa2c83ea5e10002b70a7e9f69e5d67`](./workday_person_python_sdk/pydantic/work_contact_change_event_view_bdfa2c83ea5e10002b70a7e9f69e5d67.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_phone_number`<a id="workdaypersonwork_contact_information_changesget_phone_number"></a>

Retrieve an existing phone number as it exists when staged by the parent business process.

Secured by: Person Data: Work Phone, Self-Service: Work Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_phone_number_response = workdayperson.work_contact_information_changes.get_phone_number(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/pydantic/phone_reference1089da0ab90910000f70891a998b0887.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/phoneNumbers/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_phone_numbers`<a id="workdaypersonwork_contact_information_changesget_phone_numbers"></a>

Retrieve all phone numbers staged for update by the parent business process

Secured by: Person Data: Work Phone, Self-Service: Work Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_phone_numbers_response = workdayperson.work_contact_information_changes.get_phone_numbers(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary phone numbers.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public phone numbers.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactInformationChangesGetPhoneNumbersResponse`](./workday_person_python_sdk/pydantic/work_contact_information_changes_get_phone_numbers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/phoneNumbers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_staged_email_addresses`<a id="workdaypersonwork_contact_information_changesget_staged_email_addresses"></a>

Retrieve all email addresses staged for update by the parent business process

Secured by: Person Data: Work Email, Self-Service: Work Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staged_email_addresses_response = workdayperson.work_contact_information_changes.get_staged_email_addresses(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary email addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public email addresses.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactInformationChangesGetStagedEmailAddressesResponse`](./workday_person_python_sdk/pydantic/work_contact_information_changes_get_staged_email_addresses_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/emailAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_staged_instant_messenger`<a id="workdaypersonwork_contact_information_changesget_staged_instant_messenger"></a>

Retrieve an existing instant messenger as it exists when staged by the parent business process.

Secured by: Person Data: Work Instant Messenger, Self-Service: Work Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staged_instant_messenger_response = workdayperson.work_contact_information_changes.get_staged_instant_messenger(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/pydantic/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/instantMessengers/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_staged_instant_messengers`<a id="workdaypersonwork_contact_information_changesget_staged_instant_messengers"></a>

Retrieve all instant messengers staged for update by the parent business process

Secured by: Person Data: Work Instant Messenger, Self-Service: Work Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_staged_instant_messengers_response = workdayperson.work_contact_information_changes.get_staged_instant_messengers(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary instant messenger account usernames.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public instant messenger account usernames.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactInformationChangesGetStagedInstantMessengersResponse`](./workday_person_python_sdk/pydantic/work_contact_information_changes_get_staged_instant_messengers_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/instantMessengers` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_web_address`<a id="workdaypersonwork_contact_information_changesget_web_address"></a>

Retrieve an existing web address as it exists when staged by the parent business process.

Secured by: Person Data: Work Web Address, Self-Service: Work Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_web_address_response = workdayperson.work_contact_information_changes.get_web_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🔄 Return<a id="🔄-return"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/pydantic/web_address_reference_e357ae6d466510000ce259f323be01b0.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/webAddresses/{subresourceID}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.get_web_addresses_staged`<a id="workdaypersonwork_contact_information_changesget_web_addresses_staged"></a>

Retrieve all web addresses staged for update by the parent business process

Secured by: Person Data: Work Web Address, Self-Service: Work Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_web_addresses_staged_response = workdayperson.work_contact_information_changes.get_web_addresses_staged(
    id="ID_example",
    limit=1,
    offset=1,
    primary_only=True,
    public_only=True,
    usage_type="string_example",
    used_for="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### limit: `int`<a id="limit-int"></a>

The maximum number of objects in a single response. The default is 20. The maximum is 100.

##### offset: `int`<a id="offset-int"></a>

The zero-based index of the first object in a response collection. The default is 0. Use offset with the limit parameter to control paging of a response collection. Example: If limit is 5 and offset is 9, the response returns a collection of 5 objects starting with the 10th object.

##### primary_only: `bool`<a id="primary_only-bool"></a>

If true, returns only the IDs of the person's primary web addresses.

##### public_only: `bool`<a id="public_only-bool"></a>

If true, returns only the IDs of the person's public web addresses.

##### usage_type: `str`<a id="usage_type-str"></a>

Specifies usage type, such as home or work. Only used if the service provides access to multiple usage types from the same endpoint.

##### used_for: `str`<a id="used_for-str"></a>

Specifies usage behavior, such as mailing, billing, or shipping. Optional.

#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactInformationChangesGetWebAddressesStagedResponse`](./workday_person_python_sdk/pydantic/work_contact_information_changes_get_web_addresses_staged_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/webAddresses` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.remove_address`<a id="workdaypersonwork_contact_information_changesremove_address"></a>

Remove the specified address. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.work_contact_information_changes.remove_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/addresses/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.remove_email_address`<a id="workdaypersonwork_contact_information_changesremove_email_address"></a>

Remove the specified email address. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Work Email, Self-Service: Work Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.work_contact_information_changes.remove_email_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/emailAddresses/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.remove_instant_messenger`<a id="workdaypersonwork_contact_information_changesremove_instant_messenger"></a>

Remove the specified instant messenger. If this instant messenger existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Work Instant Messenger, Self-Service: Work Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.work_contact_information_changes.remove_instant_messenger(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/instantMessengers/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.remove_phone_number`<a id="workdaypersonwork_contact_information_changesremove_phone_number"></a>

Remove the specified phone number. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Work Phone, Self-Service: Work Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.work_contact_information_changes.remove_phone_number(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/phoneNumbers/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.remove_web_address`<a id="workdaypersonwork_contact_information_changesremove_web_address"></a>

Remove the specified web address. If this address existed before the start of the current business process, it won't be removed from the target Person until the parent business process completes.

Secured by: Person Data: Work Web Address, Self-Service: Work Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
workdayperson.work_contact_information_changes.remove_web_address(
    id="ID_example",
    subresource_id="subresourceID_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/webAddresses/{subresourceID}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.submit`<a id="workdaypersonwork_contact_information_changessubmit"></a>

Submits the specified work contact information change ID. 

To submit the Work Contact Change event and initiate the Work Contact Change business process, specify an empty request body: {}.
To save for later, specify this request body:
{
    "businessProcessParameters": {
        "action":{
            "id": "d9e41a8c446c11de98360015c5e6daf6"
        }
    }
}

The action id value is the Workday ID of the Save for Later action. If you submit this endpoint with the Save for Later action, you can no longer edit nor resubmit the Work Contact Change event using the REST APIs. The user with correct permissions can edit and submit the saved Work Contact Change event in the Workday UI.

Secured by: Change Work Contact Information (REST Service)

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
submit_response = workdayperson.work_contact_information_changes.submit(
    body={
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    business_process_parameters=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### business_process_parameters: `BusinessProcessParameters83f6f6b7c38d100009c7ad91dd414a16`<a id="business_process_parameters-businessprocessparameters83f6f6b7c38d100009c7ad91dd414a16"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`ChangeContactInformationEvent765b18aa13af1000064a10bf37b800ed`](./workday_person_python_sdk/type/change_contact_information_event765b18aa13af1000064a10bf37b800ed.py)
#### 🔄 Return<a id="🔄-return"></a>

[`ChangeContactInformationEvent765b18aa13af1000064a10bf37b800ed`](./workday_person_python_sdk/pydantic/change_contact_information_event765b18aa13af1000064a10bf37b800ed.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/submit` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.update_address`<a id="workdaypersonwork_contact_information_changesupdate_address"></a>

Update an existing address that is staged for update by the parent business process event.

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_address_response = workdayperson.work_contact_information_changes.update_address(
    body={
        "address_line3": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line4": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line8": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line6": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line3_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "postal_code": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line9_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line1_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line5": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "region_subdivision1": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line7": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "effective": "2024-03-23T07:00:00.000Z",
        "city_subdivision2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "address_line2_local": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "city_subdivision2": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    address_line3="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line8_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    region_subdivision1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country=None,
    address_line9="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line4="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line8="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line5_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line6="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    city="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line3_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    postal_code="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line9_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line1_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line7_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_region=None,
    address_line5="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    region_subdivision1="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line7="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    effective="2024-03-23T07:00:00.000Z",
    city_subdivision2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    address_line2_local="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_city=None,
    city_subdivision2="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### address_line3: `str`<a id="address_line3-str"></a>

Address Line 3

##### address_line8_local: `str`<a id="address_line8_local-str"></a>

Local Address Line 8

##### region_subdivision2: `str`<a id="region_subdivision2-str"></a>

Region Subdivision 2

##### city_local: `str`<a id="city_local-str"></a>

City - Local

##### city_subdivision1_local: `str`<a id="city_subdivision1_local-str"></a>

City Subdivision 1 - Local

##### address_line6_local: `str`<a id="address_line6_local-str"></a>

Local Address Line 6

##### address_line4_local: `str`<a id="address_line4_local-str"></a>

Local Address Line 4

##### region_subdivision1_local: `str`<a id="region_subdivision1_local-str"></a>

Region Subdivision 1 - Local

##### country: `CountryC1bb9f46f65210002d2fa329fe6700b4`<a id="country-countryc1bb9f46f65210002d2fa329fe6700b4"></a>

##### address_line9: `str`<a id="address_line9-str"></a>

Address Line 9

##### address_line4: `str`<a id="address_line4-str"></a>

Address Line 4

##### city_subdivision1: `str`<a id="city_subdivision1-str"></a>

City Subdivision 1

##### address_line8: `str`<a id="address_line8-str"></a>

Address Line 8

##### address_line1: `str`<a id="address_line1-str"></a>

Address Line 1

##### address_line5_local: `str`<a id="address_line5_local-str"></a>

Local Address Line 5

##### address_line6: `str`<a id="address_line6-str"></a>

Address Line 6

##### city: `str`<a id="city-str"></a>

City

##### address_line3_local: `str`<a id="address_line3_local-str"></a>

Local Address Line 3

##### postal_code: `str`<a id="postal_code-str"></a>

Postal Code

##### address_line9_local: `str`<a id="address_line9_local-str"></a>

Local Address Line 9

##### address_line2: `str`<a id="address_line2-str"></a>

Address Line 2

##### address_line1_local: `str`<a id="address_line1_local-str"></a>

Local Address Line 1

##### address_line7_local: `str`<a id="address_line7_local-str"></a>

Local Address Line 7

##### country_region: `CountryRegionC1bb9f46f65210002d2fa322479a00b2`<a id="country_region-countryregionc1bb9f46f65210002d2fa322479a00b2"></a>

##### address_line5: `str`<a id="address_line5-str"></a>

Address Line 5

##### usage: `UsageC1bb9f46f65210002d2fa2e7babe00a8`<a id="usage-usagec1bb9f46f65210002d2fa2e7babe00a8"></a>

##### region_subdivision1: `str`<a id="region_subdivision1-str"></a>

Region Subdivision 1

##### address_line7: `str`<a id="address_line7-str"></a>

Address Line 7

##### effective: `date`<a id="effective-date"></a>

The date this business process takes effect.

##### city_subdivision2_local: `str`<a id="city_subdivision2_local-str"></a>

City Subdivision 2 - Local

##### address_line2_local: `str`<a id="address_line2_local-str"></a>

Local Address Line 2

##### country_city: `CountryCityC1bb9f46f65210002d2fa2bb24a300a1`<a id="country_city-countrycityc1bb9f46f65210002d2fa2bb24a300a1"></a>

##### city_subdivision2: `str`<a id="city_subdivision2-str"></a>

City Subdivision 2

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkAddressReferenceC1bb9f46f65210002d2fa259a1c10095`](./workday_person_python_sdk/type/work_address_reference_c1bb9f46f65210002d2fa259a1c10095.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkAddressReferenceC1bb9f46f65210002d2fa259a1c10095`](./workday_person_python_sdk/pydantic/work_address_reference_c1bb9f46f65210002d2fa259a1c10095.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/addresses/{subresourceID}` `put`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.update_alternate_work_location`<a id="workdaypersonwork_contact_information_changesupdate_alternate_work_location"></a>

Update the Alternate Work Location staged by this business process event.   Any Home or Work address for the target Person is valid for use as an Alternate Work Location.

Secured by: Person Data: Work Address, Self-Service: Work Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_alternate_work_location_response = workdayperson.work_contact_information_changes.update_alternate_work_location(
    body={
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    alternate_work_location=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### alternate_work_location: `AlternateWorkLocationD72a8353f91e1000169a83b894e7046e`<a id="alternate_work_location-alternateworklocationd72a8353f91e1000169a83b894e7046e"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WorkContactChangeEventD72a8353f91e1000169a839c31a0046d`](./workday_person_python_sdk/type/work_contact_change_event_d72a8353f91e1000169a839c31a0046d.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WorkContactChangeEventD72a8353f91e1000169a839c31a0046d`](./workday_person_python_sdk/pydantic/work_contact_change_event_d72a8353f91e1000169a839c31a0046d.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.update_email_address`<a id="workdaypersonwork_contact_information_changesupdate_email_address"></a>

Partially update an existing email address that is staged for update by the parent business process event.

Secured by: Person Data: Work Email, Self-Service: Work Email

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_email_address_response = workdayperson.work_contact_information_changes.update_email_address(
    body={
        "email_address": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    email_address="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### email_address: `str`<a id="email_address-str"></a>

The email address.

##### usage: `Usage6333dee5ac2010000c8653405aaa0038`<a id="usage-usage6333dee5ac2010000c8653405aaa0038"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/type/email_address_reference0918d433e86b100018119edc1b8f00f7.py)
#### 🔄 Return<a id="🔄-return"></a>

[`EmailAddressReference0918d433e86b100018119edc1b8f00f7`](./workday_person_python_sdk/pydantic/email_address_reference0918d433e86b100018119edc1b8f00f7.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/emailAddresses/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.update_instant_messenger`<a id="workdaypersonwork_contact_information_changesupdate_instant_messenger"></a>

Partially update an existing instant messenger that is staged for update by the parent business process event.

Secured by: Person Data: Work Instant Messenger, Self-Service: Work Instant Messenger

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_instant_messenger_response = workdayperson.work_contact_information_changes.update_instant_messenger(
    body={
        "user_name": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    type=None,
    user_name="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    usage=None,
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### type: `TypeDe08a6c876a810000cb2e3dd8853001a`<a id="type-typede08a6c876a810000cb2e3dd8853001a"></a>

##### user_name: `str`<a id="user_name-str"></a>

The instant messenger account username.

##### usage: `UsageDe08a6c876a810000cb2e3d738be0019`<a id="usage-usagede08a6c876a810000cb2e3d738be0019"></a>

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/type/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)
#### 🔄 Return<a id="🔄-return"></a>

[`InstantMessengerReferenceDe08a6c876a810000cb2e38a1d2a0016`](./workday_person_python_sdk/pydantic/instant_messenger_reference_de08a6c876a810000cb2e38a1d2a0016.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/instantMessengers/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.update_phone_number`<a id="workdaypersonwork_contact_information_changesupdate_phone_number"></a>

Partially update an existing phone number that is staged for update by the parent business process event.

Secured by: Person Data: Work Phone, Self-Service: Work Phone

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_phone_number_response = workdayperson.work_contact_information_changes.update_phone_number(
    body={
        "extension": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "complete_phone_number": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
        "descriptor": "Lorem ipsum dolor sit ame",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    extension="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    complete_phone_number="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    country_phone_code=None,
    device_type=None,
    usage=None,
    descriptor="Lorem ipsum dolor sit ame",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### extension: `str`<a id="extension-str"></a>

The phone extension.

##### complete_phone_number: `str`<a id="complete_phone_number-str"></a>

The complete phone number.

##### country_phone_code: `CountryPhoneCode1089da0ab90910000f7089365467088c`<a id="country_phone_code-countryphonecode1089da0ab90910000f7089365467088c"></a>

##### device_type: `DeviceType1089da0ab90910000f7089256c7b0888`<a id="device_type-devicetype1089da0ab90910000f7089256c7b0888"></a>

##### usage: `Usage1089da0ab90910000f70892f2de3088a`<a id="usage-usage1089da0ab90910000f70892f2de3088a"></a>

##### descriptor: `str`<a id="descriptor-str"></a>

A preview of the instance

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/type/phone_reference1089da0ab90910000f70891a998b0887.py)
#### 🔄 Return<a id="🔄-return"></a>

[`PhoneReference1089da0ab90910000f70891a998b0887`](./workday_person_python_sdk/pydantic/phone_reference1089da0ab90910000f70891a998b0887.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/phoneNumbers/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `workdayperson.work_contact_information_changes.update_web_address`<a id="workdaypersonwork_contact_information_changesupdate_web_address"></a>

Partially update an existing web address that is staged for update by the parent business process event.

Secured by: Person Data: Work Web Address, Self-Service: Work Web Address

Scope: Contact Information

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
update_web_address_response = workdayperson.work_contact_information_changes.update_web_address(
    body={
        "url": "Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    },
    id="ID_example",
    subresource_id="subresourceID_example",
    usage=None,
    url="Lorem ipsum dolor sit amet, cum choro singulis consectetuer ut, ubique iisque contentiones ex duo. Quo lorem etiam eu.",
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

The Workday ID of the resource.

##### subresource_id: `str`<a id="subresource_id-str"></a>

The Workday ID of the subresource.

##### usage: `UsageE357ae6d466510000ce25a08bfe401b3`<a id="usage-usagee357ae6d466510000ce25a08bfe401b3"></a>

##### url: `str`<a id="url-str"></a>

The complete URL address for the web address.

##### id: `str`<a id="id-str"></a>

Id of the instance

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/type/web_address_reference_e357ae6d466510000ce259f323be01b0.py)
#### 🔄 Return<a id="🔄-return"></a>

[`WebAddressReferenceE357ae6d466510000ce259f323be01b0`](./workday_person_python_sdk/pydantic/web_address_reference_e357ae6d466510000ce259f323be01b0.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/workContactInformationChanges/{ID}/webAddresses/{subresourceID}` `patch`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
