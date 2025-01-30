# Exporting Annotations

## Overview

The RedBrick CLI allows you to easily export your Project's annotations within [a local project directory](creating-and-cloning-projects.md).&#x20;

Please note that the `export` function only fetches **newly created annotations** when run. It will not generate an annotation file for a Task if no annotation work has been completed and saved on said Task.&#x20;

For example, if you upload 100 images to your Project, annotate 80 of them and initiate an export using the CLI, the CLI will export **annotations for 80 Tasks**.&#x20;

If your team annotates 5 additional Tasks the next day and initiates an export, the CLI will only export annotations for the **5 newly annotated Tasks**, bringing the total number of annotation files in your local directory to **85**.

{% hint style="success" %}
By default, all segmentation files are exported in **NIfTI-1 format**. Please see our [Format Reference](../formats/full-format-reference.md) for more information on exported annotations and alternative formats (such as PNG or RT Struct).
{% endhint %}

***

## Export Folder Structure

RedBrick AI exports annotations in a JSON structure, accompanied by [NIfTI-1 masks](https://nifti.nimh.nih.gov/nifti-1/) for segmentations. All data will be exported within a folder named after your `project_id`, with the following structure:

```
project_id/
├── segmentations
│   ├── study01
│   │   └── series1.nii
│   └── study02
│       ├── series1.nii
│       └── series2.nii
└── tasks.json
```

### Segmentations Subdirectory

The segmentation directory will contain a single sub-directory for each task in your export. The sub-directories will be named after the task [`name`](exporting-annotations.md#name-string). A single task (depending on whether it was single series or multi-series) can have one or more segmentations.

The individual segmentation files will be in NIfTI-1 format and be [named after the user-defined series name](exporting-annotations.md#name-string-1). If no series name is provided on upload, RedBrick will assign a unique name. Corresponding meta-data ex. category names will be provided in [tasks.json](exporting-annotations.md#tasks-json).

***

## Export Annotations to a Local Directory using the CLI

{% hint style="info" %}
You can also find all of these steps, as well as pre-configured CLI commands, inside the "Export Labels" section of your Project Settings
{% endhint %}

To export your data, first ensure that your [credentials file has been properly configured](https://docs.redbrickai.com/python-sdk/cli-overview) and you have created a [local project directory](creating-and-cloning-projects.md).&#x20;

Next, navigate to the newly created Project directory.

```bash
$ cd my-project
```

Once inside your local project directory, you can initiate several types of exports. Please see some common examples below or use `redbrick export -h` to see a full list of export-related commands inside of the Terminal.

### Export Annotations for All Tasks

To export the latest state of all annotations for all Tasks (including those in Label and Review stages) run the following command.&#x20;

```bash
$ redbrick export
```

### Export Ground Truth Tasks Only

For exporting only those annotations associated with Tasks in the Ground Truth Stage.

<pre class="language-bash"><code class="lang-bash"><strong>$ redbrick export groundtruth
</strong></code></pre>

### Export Tasks and Clear Cache

For clearing your local Redbrick cache and forcing a fresh download of all annotation files within a Project.

```bash
$ redbrick export --clear-cache
```

### Export Tasks with Images

For downloading your Project's image and/or volume files along with any created annotations.&#x20;

```bash
$ redbrick export --with-files
```

### DICOM to NIfTI Conversion

If you initially uploaded DICOM images/volumes to RedBrick and would like to convert them to NIfTI upon export (ensuring that both your annotation files and images/volumes are in the same format), use the following command.

```bash
$ redbrick export --with-files --dicom-to-nifti
```

### Export Tasks from a Specific Stage

If you want to export tasks that are queued in a specific stage, for example, exporting all tasks queued in Review\_2, you can do so in the following way:

```bash
$ redbrick export --stage Review_2
```

***

## Export an Audit Trail

Generating an audit trail can be useful material for regulators interested in your quality control processes and for managing your internal QA processes.&#x20;

You can create such a report by running the following command within your [local project directory](creating-and-cloning-projects.md).

```bash
$ redbrick report
```

The exported JSON object will contain data similar to what is shown below. Each entry will represent a single task (uniquely identified by `taskId`). The `events` array contains all key events/actions performed on the task, with `events[0]` being the first event.

```json
[
  {
    "taskId": "...",
    "currentStageName": "Label",
    "events": [
      {
        "eventType": "TASK_CREATED",
        "createdAt": "...",
        "isGroundTruth": false,
        "createdBy": "..."
      },
      {
        "eventType": "TASK_ASSIGNED",
        "createdAt": "...",
        "assignee": "...",
        "stage": "Label"
      }
    ]
  }
]
```
