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
from datetime import datetime

class NvrCamLastRecord:
    def __init__(self):
        self.nvr_url = os.environ.get('NVR_URL')
        self.api_key = os.environ.get('API_KEY')

    def cam_last_record(self, cam_uid):
        if not self.nvr_url or not self.api_key:
            print("Error: NVR_URL or API_KEY not set in the environment.")
            return '0'

        url = "{}/api/2.0/camera?apiKey={}".format(self.nvr_url, self.api_key)
        response = requests.get(url, verify=False)
        nvr_data = json.loads(response.text)

        for cam in nvr_data.get('data', []):
            if cam['uuid'] == cam_uid:
                last_recording_time = int(cam.get('lastRecordingStartTime', 0))
                current_time = int(datetime.now().timestamp() * 1000)
                return int((current_time - last_recording_time) / (60 * 1000))  # em minutos

        return '0'

if __name__ == "__main__":
    nvr = NvrCamLastRecord()

    if len(sys.argv) != 2:
        print("Usage: python script.py <CAM_UID>")
        sys.exit(1)

    cam_uid = sys.argv[1]
    print(nvr.cam_last_record(cam_uid))
