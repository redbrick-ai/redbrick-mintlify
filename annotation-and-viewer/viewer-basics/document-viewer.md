# Document Viewer

As of v1.1.4, RedBrick AI allows users to upload text reports to Tasks.&#x20;

For purposes of data I/O, viewing, and navigation, each document is treated as a Series and occupies its own viewport.

<figure><img src="../../.gitbook/assets/CleanShot 2024-09-24 at 16.29.09@2x.png" alt=""><figcaption><p>An example text report alongside a CT scan</p></figcaption></figure>

## Uploading Documents to RedBrick AI

All documents must be uploaded programmatically and must be `.txt` files.

Please see the following JSON as an example:

```json
// example Items List

[
  {
    "name": "Task Name",
    "series": [
      {
        "name": "Series Name"
        "items": [
          "file/path/to/images/1.2.156.14702.dcm",
        ]
      },
      {
        "items": [
          "file/path/to/report.txt"
        ]
      }
    ]
  }
]
```
