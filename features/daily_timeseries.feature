# Created by Sreenivasulu Suuda at 11/27/2020
Feature: Validate daily time series data
  # This feature is used to validate daily time series data

  Scenario: Validate daily time series data with required params
    # To verify user is receiving valid data when queried get call with all required paramaeters
    Given End point url and required params
    When user sends get request
    Then user should get the daily time series data with status code 200

  Scenario: Verify response contains values for open,high,low,close,volume keys for all the days
    # To verify response contains open high low close volume keys for all the days.
    Given End point url and required params
    When user sends get request
    Then verify response contains open,high,low,close,volume keys for all the days

  Scenario Outline: Verify user can't access data if any of the required parameter is missing
    #To verify all required parameters are required to get valid response.
    Given End point url and required params
    When user sends get request with missing required paramaeter "<keys>"
    Then User should get error message in the response

    Examples:
    |keys|
    |function|
    |symbol  |
    |apikey  |