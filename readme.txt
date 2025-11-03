There are 3 separate test files for 3 separate flow:

- test__login verifies the login flow
- test_search verifies the job search flow and verifies if the results are visible
- test_job_apply verifies the job apply flow until we need the 'Upload Resume' box is visible

docker-compose.yml has:

Hub:
- selenium-hub

Nodes:
-chrome1
-chrome2
-chrome3

Command to Start the docker:
- docker compose up -d

Command to run all 3 tests in parallel on Grid:
- pytest n -3 tests/