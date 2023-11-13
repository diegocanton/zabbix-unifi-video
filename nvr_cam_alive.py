#!/usr/bin/env python3

# Suprimindo os warnings
import warnings
warnings.filterwarnings("ignore")

from dotenv import load_dotenv
load_dotenv()

import os
import sys
import requests
import json

class NvrCamAlive:
    def __init__(self):
        self.nvr_url = os.environ.get('NVR_URL')
        self.api_key = os.environ.get('API_KEY')

    def cam_alive(self, cam_uid):
        url = "{}/api/2.0/camera?apiKey={}".format(self.nvr_url, self.api_key)
        response = requests.get(url, verify=False)
        nvr_data = json.loads(response.text)

        for cam in nvr_data['data']:
            if cam['uuid'] == cam_uid:
                if cam['state'] == 'CONNECTED':
                    return '1'
                else:
                    return '0'

        return '0'

if __name__ == "__main__":
    nvr = NvrCamAlive()

    if len(sys.argv) != 2:
        print("Usage: python script.py <CAM_UID>")
        sys.exit(1)

    cam_uid = sys.argv[1]
    print(nvr.cam_alive(cam_uid))
