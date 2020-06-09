#!/usr/bin/env python

# Purpose: use our login function and output the token

import os
from dotenv import load_dotenv
import cisco_dnacenter.dnac.dnac_api as dnac_api


load_dotenv(verbose=True)

dnac = dnac_api.dnaCenterAPI(
    host=os.getenv("DNA_CENTER"),
    username=os.getenv("DNA_CENTER_USERNAME"),
    password=os.getenv("DNA_CENTER_PASSWORD"),
    verify=False
)

area = {
    "type": "area",
    "site": {
        "area": {
            "name": "Jeff-Test2",
            "parentName": "Global"
        }
    }
}

building = {
    "type": "building",
    "site": {
        "building": {
            "name": "jeff-bldg",
            "parentName": "Global/Jeff-Test2",
            "latitude": "38.707996",
            "longitude": "-90.440120"
        }
    }
}
floor = {
    "type": "floor",
    "site": {
        "floor": {
            "name": "jeff-bldg-floor-1",
            "parentName": "Global/Jeff-Test2/jeff-bldg",
            "rfModel": "Cubes And Walled Offices",
            "width": 200,
            "length": 500,
            "height": "10"
        }
    }
}
results = dnac.create_site(floor)

print(f"Status Code: {results.status_code}\nResult Text: {results.text}")
data = results.json()
print(data["siteId"])
