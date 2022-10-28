rom __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.blockchain.com/v3/exchange
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.blockchain.com/v3/exchange"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration = openapi_client.Configuration(
    host = "https://api.blockchain.com/v3/exchange",
    api_key = {
        'X-API-Token': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    create_withdrawal_request = openapi_client.CreateWithdrawalRequest() # CreateWithdrawalRequest | 

    try:
        # Request a withdrawal
        api_response = api_instance.create_withdrawal(create_withdrawal_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_withdrawal: %s\n" % e)
