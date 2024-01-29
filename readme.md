# ClickUp Cards Integration

## Description:

Project focused on integrating ClickUp cards with Consinco Database.
The cards are registred in a csv file, where they will be read by the Pentahoo Data 
Integration and recorded in the database.

## Get started:

### Create environment files to run:

.env

    CSV_PATH='csv/data.csv'

config.json

    {
      "api_token": "",
      "url_base": "https://api.clickup.com/api/v2",
      "gdps": {
        "2024": 0,
        "2023": 0
      },
      "subtasks": false
    }

### To run on Windows with command line:

    run.bat

### To run on Linux with command line :

    chmod +x run.sh
    ./run.sh
