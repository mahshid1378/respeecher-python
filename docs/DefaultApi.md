# respeecher.DefaultApi

All URIs are relative to *https://api.respeecher.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_calibration**](DefaultApi.md#create_calibration) | **POST** /api/calibration | Create a new Calibration
[**create_folder**](DefaultApi.md#create_folder) | **POST** /api/folders | Create a folder
[**create_note**](DefaultApi.md#create_note) | **POST** /api/notes | Create a note associated with a recording
[**create_order**](DefaultApi.md#create_order) | **POST** /api/v2/orders | Create a conversion order
[**create_original_recording**](DefaultApi.md#create_original_recording) | **POST** /api/recordings | Create an original recording
[**create_project**](DefaultApi.md#create_project) | **POST** /api/projects | Create a new project
[**create_tts_recording**](DefaultApi.md#create_tts_recording) | **POST** /api/v2/recordings/tts | Create an original text-to-speech recording
[**delete_api_key**](DefaultApi.md#delete_api_key) | **DELETE** /api/api-key | Delete the API key associated with your account
[**delete_calibration**](DefaultApi.md#delete_calibration) | **DELETE** /api/calibration/{calibration_id} | Delete a calibration
[**delete_folder**](DefaultApi.md#delete_folder) | **DELETE** /api/folders/{folder_id} | Delete a folder
[**delete_note**](DefaultApi.md#delete_note) | **DELETE** /api/notes | Delete a note
[**delete_project**](DefaultApi.md#delete_project) | **DELETE** /api/projects/{project_id} | Delete a project
[**delete_recording**](DefaultApi.md#delete_recording) | **DELETE** /api/recordings/{recording_id} | Delete a recording
[**enable_calibration**](DefaultApi.md#enable_calibration) | **PUT** /api/calibration/{calibration_id}/enable | Set a calibration as the default enabled calibration
[**export_project**](DefaultApi.md#export_project) | **GET** /api/projects/{project_id}/export | Export a project
[**favorite_voice**](DefaultApi.md#favorite_voice) | **POST** /api/v2/voices/favorite/{voice_id} | Mark a voice as a favorite
[**generate_api_key**](DefaultApi.md#generate_api_key) | **POST** /api/api-key | Generate a new API key
[**get_accent_samples**](DefaultApi.md#get_accent_samples) | **GET** /api/v2/accents/samples | Get samples available for an accent
[**get_account_statistics**](DefaultApi.md#get_account_statistics) | **GET** /api/stats | Get the statistics for your account
[**get_calibration**](DefaultApi.md#get_calibration) | **GET** /api/calibration/{calibration_id} | Get a calibration by its ID
[**get_credits**](DefaultApi.md#get_credits) | **GET** /api/credits | Get the credits available to your account
[**get_folder_by_id**](DefaultApi.md#get_folder_by_id) | **GET** /api/folders/{folder_id} | Get a folder by its ID
[**get_folders_statistics**](DefaultApi.md#get_folders_statistics) | **POST** /api/stats/folders | Get statistics for a list of folders
[**get_project_by_url**](DefaultApi.md#get_project_by_url) | **GET** /api/projects/by-url | Get a project by its URL
[**get_projects_statistics**](DefaultApi.md#get_projects_statistics) | **GET** /api/stats/projects | Get statistics for a list of projects
[**get_recording_by_id**](DefaultApi.md#get_recording_by_id) | **GET** /api/recordings/{recording_id} | Get a recording by its ID
[**list_calibrations**](DefaultApi.md#list_calibrations) | **GET** /api/calibration | Get a list of calibrations associated with your account
[**list_conversions**](DefaultApi.md#list_conversions) | **GET** /api/recordings/conversions | Get a list of the conversions for an original recording
[**list_folders**](DefaultApi.md#list_folders) | **GET** /api/folders | Get a list of the folders in a project
[**list_original_recordings**](DefaultApi.md#list_original_recordings) | **GET** /api/recordings/originals | Get a list of the original recordings in a folder
[**list_projects**](DefaultApi.md#list_projects) | **GET** /api/projects | Get a list of your projects
[**list_recordings**](DefaultApi.md#list_recordings) | **GET** /api/recordings | Get a list of recordings for a specified folder or project
[**list_tts_voices**](DefaultApi.md#list_tts_voices) | **GET** /api/tts-voices | Get a list of the available TTS voices
[**list_voices**](DefaultApi.md#list_voices) | **GET** /api/v2/voices | Get a list of the voices available
[**login**](DefaultApi.md#login) | **POST** /api/login | Log in to an account and start a new session
[**logout**](DefaultApi.md#logout) | **POST** /api/logout | End your session
[**rename_folder**](DefaultApi.md#rename_folder) | **PATCH** /api/folders/{folder_id} | Rename a folder
[**retry_order_v2**](DefaultApi.md#retry_order_v2) | **POST** /api/v2/orders/retry/{recording_id} | Retry a conversion order for a specific original
[**search_voices**](DefaultApi.md#search_voices) | **GET** /api/v2/voices/search | Search for a voice by its name
[**set_voice_settings**](DefaultApi.md#set_voice_settings) | **POST** /api/v2/voices/settings | Set the settings for a voice
[**update_note**](DefaultApi.md#update_note) | **PUT** /api/notes | Update a note
[**update_project**](DefaultApi.md#update_project) | **PATCH** /api/projects/{project_id} | Change the name of a project
[**update_recording**](DefaultApi.md#update_recording) | **PATCH** /api/recordings/{recording_id} | Update a recording

# **create_calibration**
> CalibrationResponse create_calibration(name, data)

Create a new Calibration

Currently the supported audio formats are wav, ogg, mp3 or flac.

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
name = 'name_example' # str | 
data = 'data_example' # str | 

try:
    # Create a new Calibration
    api_response = api_instance.create_calibration(name, data)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_calibration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **data** | **str**|  | 

### Return type

[**CalibrationResponse**](CalibrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_folder**
> Folder create_folder(body)

Create a folder

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.FolderRequest() # FolderRequest | 

try:
    # Create a folder
    api_response = api_instance.create_folder(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FolderRequest**](FolderRequest.md)|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_note**
> NoteResponse create_note(body)

Create a note associated with a recording

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.NoteRequest() # NoteRequest | 

try:
    # Create a note associated with a recording
    api_response = api_instance.create_note(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteRequest**](NoteRequest.md)|  | 

### Return type

[**NoteResponse**](NoteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order**
> list[Order] create_order(body)

Create a conversion order

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.OrderRequest() # OrderRequest | 

try:
    # Create a conversion order
    api_response = api_instance.create_order(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OrderRequest**](OrderRequest.md)|  | 

### Return type

[**list[Order]**](Order.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_original_recording**
> Recording create_original_recording(data, parent_folder_id, microphone, label)

Create an original recording

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
data = 'data_example' # str | 
parent_folder_id = 'parent_folder_id_example' # str | 
microphone = 'microphone_example' # str | 
label = 'label_example' # str | 

try:
    # Create an original recording
    api_response = api_instance.create_original_recording(data, parent_folder_id, microphone, label)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_original_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data** | **str**|  | 
 **parent_folder_id** | **str**|  | 
 **microphone** | **str**|  | 
 **label** | **str**|  | 

### Return type

[**Recording**](Recording.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_project**
> ProjectResponse create_project(body)

Create a new project

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.ProjectRequest() # ProjectRequest | 

try:
    # Create a new project
    api_response = api_instance.create_project(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectRequest**](ProjectRequest.md)|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tts_recording**
> Recording create_tts_recording(body)

Create an original text-to-speech recording

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.TTSRecordingRequest() # TTSRecordingRequest | 

try:
    # Create an original text-to-speech recording
    api_response = api_instance.create_tts_recording(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_tts_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TTSRecordingRequest**](TTSRecordingRequest.md)|  | 

### Return type

[**Recording**](Recording.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_api_key**
> delete_api_key()

Delete the API key associated with your account

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))

try:
    # Delete the API key associated with your account
    api_instance.delete_api_key()
except ApiException as e:
    print("Exception when calling DefaultApi->delete_api_key: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_calibration**
> CalibrationResponse delete_calibration(calibration_id)

Delete a calibration

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
calibration_id = 'calibration_id_example' # str | 

try:
    # Delete a calibration
    api_response = api_instance.delete_calibration(calibration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_calibration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calibration_id** | **str**|  | 

### Return type

[**CalibrationResponse**](CalibrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder**
> list[InlineResponse2004] delete_folder(folder_id)

Delete a folder

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
folder_id = 'folder_id_example' # str | 

try:
    # Delete a folder
    api_response = api_instance.delete_folder(folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**list[InlineResponse2004]**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_note**
> NoteResponse delete_note(body)

Delete a note

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.NoteDeleteRequest() # NoteDeleteRequest | 

try:
    # Delete a note
    api_response = api_instance.delete_note(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteDeleteRequest**](NoteDeleteRequest.md)|  | 

### Return type

[**NoteResponse**](NoteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_project**
> InlineResponse2004 delete_project(project_id)

Delete a project

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
project_id = 'project_id_example' # str | 

try:
    # Delete a project
    api_response = api_instance.delete_project(project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**InlineResponse2004**](InlineResponse2004.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_recording**
> delete_recording(recording_id)

Delete a recording

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
recording_id = 'recording_id_example' # str | The ID of the recording to delete

try:
    # Delete a recording
    api_instance.delete_recording(recording_id)
except ApiException as e:
    print("Exception when calling DefaultApi->delete_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| The ID of the recording to delete | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_calibration**
> list[CalibrationResponse] enable_calibration(calibration_id)

Set a calibration as the default enabled calibration

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
calibration_id = 'calibration_id_example' # str | 

try:
    # Set a calibration as the default enabled calibration
    api_response = api_instance.enable_calibration(calibration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->enable_calibration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calibration_id** | **str**|  | 

### Return type

[**list[CalibrationResponse]**](CalibrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_project**
> str export_project(project_id, starred_only=starred_only)

Export a project

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
project_id = 'project_id_example' # str | 
starred_only = true # bool |  (optional)

try:
    # Export a project
    api_response = api_instance.export_project(project_id, starred_only=starred_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->export_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **starred_only** | **bool**|  | [optional] 

### Return type

**str**

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/zip

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **favorite_voice**
> Voice favorite_voice(body, voice_id)

Mark a voice as a favorite

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.FavoriteVoiceIdBody() # FavoriteVoiceIdBody | 
voice_id = 'voice_id_example' # str | 

try:
    # Mark a voice as a favorite
    api_response = api_instance.favorite_voice(body, voice_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->favorite_voice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FavoriteVoiceIdBody**](FavoriteVoiceIdBody.md)|  | 
 **voice_id** | **str**|  | 

### Return type

[**Voice**](Voice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_api_key**
> InlineResponse200 generate_api_key(body)

Generate a new API key

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.ApiApikeyBody() # ApiApikeyBody | 

try:
    # Generate a new API key
    api_response = api_instance.generate_api_key(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->generate_api_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiApikeyBody**](ApiApikeyBody.md)|  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accent_samples**
> AccentSamplesResponse get_accent_samples(accent_id)

Get samples available for an accent

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
accent_id = 'accent_id_example' # str | 

try:
    # Get samples available for an accent
    api_response = api_instance.get_accent_samples(accent_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_accent_samples: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accent_id** | **str**|  | 

### Return type

[**AccentSamplesResponse**](AccentSamplesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_account_statistics**
> AccountStatistics get_account_statistics()

Get the statistics for your account

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))

try:
    # Get the statistics for your account
    api_response = api_instance.get_account_statistics()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_account_statistics: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountStatistics**](AccountStatistics.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calibration**
> CalibrationResponse get_calibration(calibration_id)

Get a calibration by its ID

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
calibration_id = 'calibration_id_example' # str | 

try:
    # Get a calibration by its ID
    api_response = api_instance.get_calibration(calibration_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_calibration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calibration_id** | **str**|  | 

### Return type

[**CalibrationResponse**](CalibrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_credits**
> InlineResponse2003 get_credits()

Get the credits available to your account

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))

try:
    # Get the credits available to your account
    api_response = api_instance.get_credits()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_credits: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2003**](InlineResponse2003.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_by_id**
> Folder get_folder_by_id(folder_id)

Get a folder by its ID

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
folder_id = 'folder_id_example' # str | 

try:
    # Get a folder by its ID
    api_response = api_instance.get_folder_by_id(folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_folder_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folders_statistics**
> FoldersStatisticsResponse get_folders_statistics(body)

Get statistics for a list of folders

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.FoldersStatisticsRequest() # FoldersStatisticsRequest | 

try:
    # Get statistics for a list of folders
    api_response = api_instance.get_folders_statistics(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_folders_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FoldersStatisticsRequest**](FoldersStatisticsRequest.md)|  | 

### Return type

[**FoldersStatisticsResponse**](FoldersStatisticsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_project_by_url**
> ProjectResponse get_project_by_url(project_url)

Get a project by its URL

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
project_url = 'project_url_example' # str | 

try:
    # Get a project by its URL
    api_response = api_instance.get_project_by_url(project_url)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_project_by_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_url** | **str**|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_projects_statistics**
> list[ProjectsStatisticsResponse] get_projects_statistics(project_ids=project_ids)

Get statistics for a list of projects

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
project_ids = 'project_ids_example' # str | Comma-separated list of project IDs to fetch statistics for. (optional)

try:
    # Get statistics for a list of projects
    api_response = api_instance.get_projects_statistics(project_ids=project_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_projects_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_ids** | **str**| Comma-separated list of project IDs to fetch statistics for. | [optional] 

### Return type

[**list[ProjectsStatisticsResponse]**](ProjectsStatisticsResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_recording_by_id**
> Recording get_recording_by_id(recording_id)

Get a recording by its ID

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
recording_id = 'recording_id_example' # str | The ID of the recording to fetch

try:
    # Get a recording by its ID
    api_response = api_instance.get_recording_by_id(recording_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_recording_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**| The ID of the recording to fetch | 

### Return type

[**Recording**](Recording.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_calibrations**
> list[CalibrationResponse] list_calibrations()

Get a list of calibrations associated with your account

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))

try:
    # Get a list of calibrations associated with your account
    api_response = api_instance.list_calibrations()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_calibrations: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CalibrationResponse]**](CalibrationResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_conversions**
> RecordingListResponse list_conversions(original_id, limit=limit, offset=offset, direction=direction)

Get a list of the conversions for an original recording

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
original_id = 'original_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
direction = 'direction_example' # str |  (optional)

try:
    # Get a list of the conversions for an original recording
    api_response = api_instance.list_conversions(original_id, limit=limit, offset=offset, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_conversions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **original_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**RecordingListResponse**](RecordingListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders**
> FolderListResponse list_folders(project_id, limit=limit, offset=offset, direction=direction)

Get a list of the folders in a project

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
project_id = 'project_id_example' # str | 
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
direction = 'direction_example' # str |  (optional)

try:
    # Get a list of the folders in a project
    api_response = api_instance.list_folders(project_id, limit=limit, offset=offset, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_folders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**FolderListResponse**](FolderListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_original_recordings**
> RecordingListResponse list_original_recordings()

Get a list of the original recordings in a folder

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))

try:
    # Get a list of the original recordings in a folder
    api_response = api_instance.list_original_recordings()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_original_recordings: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RecordingListResponse**](RecordingListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects**
> ProjectListResponse list_projects(limit=limit, offset=offset, sort=sort, direction=direction, owner=owner)

Get a list of your projects

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
limit = 56 # int | The maximum number of projects to list. (optional)
offset = 56 # int | The number of projects to offset the list by. (optional)
sort = 'sort_example' # str | Sort by name, created_at or last_recording_at. (optional)
direction = 'direction_example' # str | Order projects by asc or desc. (optional)
owner = 'owner_example' # str | List projects for a specific owner ID. (optional)

try:
    # Get a list of your projects
    api_response = api_instance.list_projects(limit=limit, offset=offset, sort=sort, direction=direction, owner=owner)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_projects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of projects to list. | [optional] 
 **offset** | **int**| The number of projects to offset the list by. | [optional] 
 **sort** | **str**| Sort by name, created_at or last_recording_at. | [optional] 
 **direction** | **str**| Order projects by asc or desc. | [optional] 
 **owner** | **str**| List projects for a specific owner ID. | [optional] 

### Return type

[**ProjectListResponse**](ProjectListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_recordings**
> RecordingListResponse list_recordings(project_id=project_id, folder_id=folder_id, limit=limit, offset=offset, direction=direction)

Get a list of recordings for a specified folder or project

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
project_id = 'project_id_example' # str |  (optional)
folder_id = 'folder_id_example' # str |  (optional)
limit = 56 # int |  (optional)
offset = 56 # int |  (optional)
direction = 'direction_example' # str |  (optional)

try:
    # Get a list of recordings for a specified folder or project
    api_response = api_instance.list_recordings(project_id=project_id, folder_id=folder_id, limit=limit, offset=offset, direction=direction)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_recordings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | [optional] 
 **folder_id** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **direction** | **str**|  | [optional] 

### Return type

[**RecordingListResponse**](RecordingListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tts_voices**
> list[TTSVoice] list_tts_voices()

Get a list of the available TTS voices

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))

try:
    # Get a list of the available TTS voices
    api_response = api_instance.list_tts_voices()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_tts_voices: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[TTSVoice]**](TTSVoice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_voices**
> VoicesListResponse list_voices(limit=limit, offset=offset, sort=sort, direction=direction, visibility=visibility, species=species, gender=gender, age_group=age_group, pitch_group=pitch_group, nationality=nationality)

Get a list of the voices available

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
limit = 25 # int | Limits the number of voices returned in the response. Defaults to 25. (optional) (default to 25)
offset = 0 # int | Offsets the list of voices to paginate through results. Defaults to 0. (optional) (default to 0)
sort = 'sort_example' # str | Sorts the voices by a specified attribute (e.g., name, pitch, rating, or created_at). (optional)
direction = 'direction_example' # str | Specifies the direction of sorting. Can be 'asc' for ascending or 'desc' for descending. (optional)
visibility = 'visibility_example' # str | Filters voices by their visibility status (e.g., public, paid, private, or kids). (optional)
species = 'species_example' # str | Filters voices by species category (e.g., human, animal, or other). (optional)
gender = 'gender_example' # str | Filters voices by gender (e.g., male or female). (optional)
age_group = 'age_group_example' # str | Filters voices by age group (e.g., child, young, adult, or senior). (optional)
pitch_group = 'pitch_group_example' # str | Filters voices by pitch group (e.g., low, mid, or high). (optional)
nationality = 'nationality_example' # str | Filters voices by nationality. (optional)

try:
    # Get a list of the voices available
    api_response = api_instance.list_voices(limit=limit, offset=offset, sort=sort, direction=direction, visibility=visibility, species=species, gender=gender, age_group=age_group, pitch_group=pitch_group, nationality=nationality)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_voices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of voices returned in the response. Defaults to 25. | [optional] [default to 25]
 **offset** | **int**| Offsets the list of voices to paginate through results. Defaults to 0. | [optional] [default to 0]
 **sort** | **str**| Sorts the voices by a specified attribute (e.g., name, pitch, rating, or created_at). | [optional] 
 **direction** | **str**| Specifies the direction of sorting. Can be &#x27;asc&#x27; for ascending or &#x27;desc&#x27; for descending. | [optional] 
 **visibility** | **str**| Filters voices by their visibility status (e.g., public, paid, private, or kids). | [optional] 
 **species** | **str**| Filters voices by species category (e.g., human, animal, or other). | [optional] 
 **gender** | **str**| Filters voices by gender (e.g., male or female). | [optional] 
 **age_group** | **str**| Filters voices by age group (e.g., child, young, adult, or senior). | [optional] 
 **pitch_group** | **str**| Filters voices by pitch group (e.g., low, mid, or high). | [optional] 
 **nationality** | **str**| Filters voices by nationality. | [optional] 

### Return type

[**VoicesListResponse**](VoicesListResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> InlineResponse2001 login(body)

Log in to an account and start a new session

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.ApiLoginBody() # ApiLoginBody | 

try:
    # Log in to an account and start a new session
    api_response = api_instance.login(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiLoginBody**](ApiLoginBody.md)|  | 

### Return type

[**InlineResponse2001**](InlineResponse2001.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> InlineResponse2002 logout()

End your session

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))

try:
    # End your session
    api_response = api_instance.logout()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **rename_folder**
> Folder rename_folder(body, folder_id)

Rename a folder

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.FoldersFolderIdBody() # FoldersFolderIdBody | 
folder_id = 'folder_id_example' # str | 

try:
    # Rename a folder
    api_response = api_instance.rename_folder(body, folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->rename_folder: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**FoldersFolderIdBody**](FoldersFolderIdBody.md)|  | 
 **folder_id** | **str**|  | 

### Return type

[**Folder**](Folder.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **retry_order_v2**
> retry_order_v2(recording_id)

Retry a conversion order for a specific original

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
recording_id = 'recording_id_example' # str | 

try:
    # Retry a conversion order for a specific original
    api_instance.retry_order_v2(recording_id)
except ApiException as e:
    print("Exception when calling DefaultApi->retry_order_v2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recording_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_voices**
> list[Voice] search_voices(name, limit=limit)

Search for a voice by its name

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
name = 'name_example' # str | 
limit = 56 # int |  (optional)

try:
    # Search for a voice by its name
    api_response = api_instance.search_voices(name, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->search_voices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | 
 **limit** | **int**|  | [optional] 

### Return type

[**list[Voice]**](Voice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_voice_settings**
> Voice set_voice_settings(body)

Set the settings for a voice

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.VoiceSettingsRequest() # VoiceSettingsRequest | 

try:
    # Set the settings for a voice
    api_response = api_instance.set_voice_settings(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->set_voice_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VoiceSettingsRequest**](VoiceSettingsRequest.md)|  | 

### Return type

[**Voice**](Voice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_note**
> NoteResponse update_note(body)

Update a note

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.NoteRequest() # NoteRequest | 

try:
    # Update a note
    api_response = api_instance.update_note(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_note: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**NoteRequest**](NoteRequest.md)|  | 

### Return type

[**NoteResponse**](NoteResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project**
> ProjectResponse update_project(body, project_id)

Change the name of a project

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.ProjectsProjectIdBody() # ProjectsProjectIdBody | 
project_id = 'project_id_example' # str | 

try:
    # Change the name of a project
    api_response = api_instance.update_project(body, project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_project: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectsProjectIdBody**](ProjectsProjectIdBody.md)|  | 
 **project_id** | **str**|  | 

### Return type

[**ProjectResponse**](ProjectResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_recording**
> Recording update_recording(body, recording_id)

Update a recording

### Example
```python
from __future__ import print_function
import time
import respeecher
from respeecher.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = respeecher.Configuration()
configuration.api_key['api-key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: CookieAuth
configuration = respeecher.Configuration()
configuration.api_key['X-Csrf-Token'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Csrf-Token'] = 'Bearer'

# create an instance of the API class
api_instance = respeecher.DefaultApi(respeecher.ApiClient(configuration))
body = respeecher.RecordingsRecordingIdBody() # RecordingsRecordingIdBody | 
recording_id = 'recording_id_example' # str | The ID of the recording to update

try:
    # Update a recording
    api_response = api_instance.update_recording(body, recording_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_recording: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordingsRecordingIdBody**](RecordingsRecordingIdBody.md)|  | 
 **recording_id** | **str**| The ID of the recording to update | 

### Return type

[**Recording**](Recording.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [CookieAuth](../README.md#CookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

