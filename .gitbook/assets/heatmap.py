# pip install redbrick-sdk==2.17.7b1

from typing import List

import redbrick
from redbrick.types.task import InputTask


ORG_ID = "ORG_ID"
PROJECT_ID = "PROJECT_ID"
API_KEY = "API_KEY"
URL = "https://preview.redbrickai.com"

project = redbrick.get_project(ORG_ID, PROJECT_ID, API_KEY, URL)

points: List[InputTask] = [
    {
        "name": "sdk-public",
        "series": [
            {
                "items": [
                    "/path/to/image/inst1.dcm",
                    "/path/to/image/inst2.dcm",
                    "/path/to/image/inst3.dcm",
                ],
                "heatMaps": [
                    {"name": "heatmap 1", "item": "/path/to/heatmap1.nii.gz"},
                    {"name": "heatmap 2", "item": "/path/to/heatmap2.nii.gz"},
                ],
            }
        ],
    }
]

project.upload.create_datapoints(redbrick.StorageMethod.REDBRICK, points)
