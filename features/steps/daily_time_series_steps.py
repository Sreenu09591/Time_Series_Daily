import time

from behave import *

from utils.utilities import common_utils
import requests

@given(u'End point url and required params')
def define_url_params(context):
    util=common_utils()
    context.url=util.get_url()
    context.req_params=util.get_req_params()



@when(u'user sends get request')
def get_time_series_daily(context):
    context.response=requests.get(context.url,params=context.req_params)
    context.response_json=context.response.json()
    if 'Note' in context.response_json.keys():
        print("Waiting for a minute to overcum trottle limit")
        time.sleep(60)
        context.response = requests.get(context.url, params=context.req_params)
        context.response_json = context.response.json()
    context.response_text = context.response.text




@then(u'user should get the daily time series data with status code 200')
def verify_get_time_series_daily_status(context):
    assert len(context.response_json) > 0 and context.response.status_code == 200

@then(u'verify response contains open,high,low,close,volume keys for all the days')
def verify_get_time_series_daily_response(context):

    time_series_daily_data=context.response_json["Time Series (Daily)"]
    no_of_days=len(time_series_daily_data)
    no_of_times_open_displayed=context.response_text.count('open')-1
    no_of_times_high_displayed = context.response_text.count('high')-1
    no_of_times_low_displayed = context.response_text.count('low')-1
    no_of_times_close_displayed = context.response_text.count('close')-1
    no_of_times_volume_displayed = context.response_text.count('volume')
    assert no_of_times_open_displayed == no_of_days and no_of_times_high_displayed == no_of_days and no_of_times_low_displayed == no_of_days and no_of_times_close_displayed == no_of_days and no_of_times_volume_displayed == no_of_days

@when(u'user sends get request with missing required paramaeter "{keys}"')
def get_req_with_missing_parameters(context,keys):
    context.key=keys
    context.req_params.pop(keys)
    context.response = requests.get(context.url, params=context.req_params)
    context.response_json = context.response.json()

    if 'Note' in context.response_json.keys():
        print("Waiting for a minute to overcum trottle limit")
        time.sleep(60)
        context.response = requests.get(context.url, params=context.req_params)
        context.response_json = context.response.json()
    context.response_text = context.response.text

@then(u'User should get error message in the response')
def error_message_in_the_response(context):
    if context.key == 'function':
        error_message="This API function () does not exist."
    if context.key == 'symbol':
        error_message = r"Invalid API call. Please retry or visit the documentation (https://www.alphavantage.co/documentation/) for TIME_SERIES_DAILY."
    if context.key == 'apikey':
        error_message = r"the parameter apikey is invalid or missing. Please claim your free API key on (https://www.alphavantage.co/support/#api-key). It should take less than 20 seconds."
    assert context.response_json['Error Message'] == error_message