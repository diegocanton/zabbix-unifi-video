#!/usr/bin/env python3


# Suprimindo os warnings
import warnings
warnings.filterwarnings("ignore")

import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

class NvrCamDiscovery:
    def __init__(self):
        self.nvr_url = os.getenv('NVR_URL')
        self.api_key = os.getenv('API_KEY')

    def ipcams(self):
        url = "{}/api/2.0/camera?apiKey={}".format(self.nvr_url, self.api_key)
        response = requests.get(url, verify=False)
        nvr_data = response.json()
        cam_names = {'data': []}

        for cam in nvr_data['data']:
            if cam['managed'] == True:
                cam_names['data'].append({'{#CAMNAME}': cam['name'], '{#CAMUID}': cam['uuid']})

        return json.dumps(cam_names)

if __name__ == "__main__":
    nvr = NvrCamDiscovery()
    print(nvr.ipcams())
