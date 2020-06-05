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
# CLI Credentials
cli_creds = [{
    "credentialType": "GLOBAL",
    "username": "wwt",
    "password": "WWTwwt1!",
    "enablePassword": "WWTwwt1!",
    "comments": "Global Admin",
    "description": "Global Admin"
}]

result = dnac.create_cli_credentials(cli_creds)
print(f"Status Code: {result.status_code}\nResult Text: {result.text} ")

# SNMP Credentials
snmp_creds = [{
    "comments": "SNMP_WRITE",
    "credentialType": "GLOBAL",
    "description": "SNMP_WRITE",
    "writeCommunity": "WWTwwt1!"
}]

results = dnac.create_snmp_write_community(snmp_creds)
print(f"Status Code: {results.status_code}\nResult Text: {results.text} ")
