# ExternalsiteAuthorizationAllOf

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_password_set** | **bool** |  | [optional] 
**is_user_id_set** | **bool** |  | [optional] 
**password** | **str** | The password of the given username to download the image from external repository like cisco.com.   | [optional] 
**repository_type** | **str** | The repository type to which this authorization will be requested. Cisco is the only available repository today.   | [optional] [default to 'cisco']
**user_id** | **str** | The username that has permission to download the image from external repository like cisco.com.    | [optional] 
**account** | [**IamAccount**](.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


