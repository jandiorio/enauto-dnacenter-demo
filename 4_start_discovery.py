#!/usr/bin/env python

# Purpose: use our login function and output the token

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

# Build List of credential IDs
cli = dnac.get_credential().json()
snmp = dnac.get_credential(type="SNMPV2_WRITE_COMMUNITY").json()
creds = [ cli["response"][0]["id"], snmp["response"][0]["id"] ]
print(creds)

# Discover Devices
# ================================================
# Start Discovery
with open("cisco_dnacenter/vars/existing_creds_id_discovery.json", "r") as file:
    stream = file.read()
    discovery = json.loads(stream)
    discovery["globalCredentialIdList"] = creds

result = dnac.start_discovery(discovery)
print(f"Result Code: {result} \nResult Tex: {result.text}\nResult JOSN: {result.json()}")
