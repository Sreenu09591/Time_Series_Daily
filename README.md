# Time_Series_Daily

This project will run 5 test cases of Time_Series_Daily api's which is written using python behave BDD Framework.  
This repository contains Test Cases file, Automation Code files,requirements.txt file, allure exe and reports folder

# Setup and Execution

## Pre-Requisites

Python and Java shoule be available in your PC.  
Any of the editor to update/write new code.

## Follow below steps to setup this project
1.Clone this repository to a required directory.  
2.Navigate to root directory and run "pip install -r requirements.txt" to install all required libraries.

## Executing test cases.

Navigate to root directory and run "behave --no-capture -f allure_behave.formatter:AllureFormatter -o reports"

Above command will run the feature file and will display the results in the console output. It will also generate json allure reports in the reports directory.

# To view test execution reports
1.Navigate to allure-2.13.7\bin directory and run "allure serve %path to reports directory%"

Updated by sreenivasulusuuda

