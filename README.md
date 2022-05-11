# Project Setup

[![Production Workflow](https://github.com/rod608/is218_p4/actions/workflows/prod.yml/badge.svg)](https://github.com/rod608/is218_p4/actions/workflows/prod.yml)

* [Production Deployment](https://ren9-p4-prod.herokuapp.com/)


[![Development Workflow](https://github.com/rod608/is218_p4/actions/workflows/dev.yml/badge.svg)](https://github.com/rod608/is218_p4/actions/workflows/dev.yml)

* [Developmental Deployment](https://ren9-p4-dev.herokuapp.com/)

# Project 4 Notes: 
Requirement #1: "Your project must have a log file with an entry for each time a user uploads a CSV account transaction file. "
   - COMPLETED | Embedded within transactions_upload() function within the transactions/dunderinit. The log file is myApp.log.

Requirement #2: "There must be a test to verify that the CSV file is uploaded and processed."
   - COMPLETED | Check tests/csv_verification_test.py

Requirement #3: "You must create a database record that is related to the user record for each transaction"
   - COMPLETED | Found in the Song class within db/models/dunderinit. All four requested properties for the Transaction-related datatable are included.

Requirement #4: "You must calculate a balance and have a test for this."
   - In-Progress | The balance has been added as a property of the User model. It is initially 0 and is updated when the user uploads a transaction csv file (check transactions/dunderinit)

Requirement #5: "You must have a test for login, a test for registration, a test for accessing the dashboard as a logged-in user, and a test for denying access to the dashboard, and denying access to uploading the CSV file"
   - COMPLETED | These tests can be found in tests/user_access_test.py
