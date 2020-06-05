#!/usr/bin/env python

# Author: Jeff Andiorio
# Purpose: Demonstrate working with device API in DNAC


import sys, json, os
from dotenv import load_dotenv
from pprint import pprint
import cisco_dnacenter.dnac.dnac_api as dnac_api

load_dotenv(verbose=True)

dnac = dnac_api.dnaCenterAPI(
    host=os.getenv("DNA_CENTER"),
    username=os.getenv("DNA_CENTER_USERNAME"),
    password=os.getenv("DNA_CENTER_PASSWORD"),
    verify=False
)

# Add Device
with open("cisco_dnacenter/vars/add_device.json", "r") as file:
    stream = file.read()
    payload = json.loads(stream)
    print(payload)

results = dnac.add_device(payload)
print(results, results.text, results.json())
t = dnac.task_checker(results.json()["response"]["taskId"])
print(t, t.text, t.json())


# Get Device List
devices = dnac.get_devices()
pprint(devices)

# assign devices to a site
# Requires a site_id and a payload
site_id = dnac.get_site_id_by_name("Global/Jeff-Test2/jeff-bldg/jeff-bldg-floor-1")
devices = {"device": [
    {"ip": "10.253.176.159"}
]}
result = dnac.assign_device_to_site(site_id, devices)
print(result, result.text, result.json())
