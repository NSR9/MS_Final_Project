# Proposed Changes


Before
The repo version on the branch sprint_dev is squashed and merged on to master untiil now. That version has the Image Fetcher and Pre-processing stages of the pipeline. 

After
Branched onto this new branch called "chay/addingPredictionStage" sourcing from "sprint_dev" which has following changes:
* Created a config.ini file.
* Built my_utils folder which has image fetcher and pre-processing script. 
* Modified the plv_module_pipeline.py
* Modularized the code for image_fetcher and preprocessing scripts


# Jira Stories

- [LAB-293](https://oregonstate-innovationlab.atlassian.net/browse/LAB-293?atlOrigin=eyJpIjoiYzEwOTRmNTE2MTI5NDZjMTk3MWI0NGZiNGUwMWVjZTQiLCJwIjoiaiJ9)

# Checklist

[1] This has been tested
[1] Self-documenting code
[1] Code is linted

# Instructions to review
Here are the steps:
* Clone the repository.
* Change directory using "cd ms_final_project"
* Install the required packages by running "pip install -r requirements.txt"
* then run "python3 plv_module1_pipeline.py"
