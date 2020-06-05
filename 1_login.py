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

print(dnac.session.headers)
