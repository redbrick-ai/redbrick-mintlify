# Export Structure

RedBrick AI offers several ways to structure exports based on the needs of your annotation workflow.&#x20;

These variations in export directly impact the contents of the subdirectory that is generated when exporting your annotation files (or, optionally, images) from RedBrick AI, and occasionally the `tasks.json` file as well.

Please see the following walkthrough for example structures, explanations, and other clarifications regarding export structures.

***

## Standard Export

For the purposes of this documentation, a standard export is any RedBrick AI export that **does not include** [**overlapping segmentations**](../../annotation-and-viewer/segmentation/overlapping-segmentations.md) **or** [**variant export parameters**](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.export.Export.export_tasks) such as `semantic_mask` or `binary_mask`.&#x20;

### Single Series

For Tasks with a single Series or object (e.g. a single 2D DICOM X-ray), RedBrick AI generates a **single NIfTI file** upon export.&#x20;

Each file contains all of the individual annotations associated with a particular Series as defined by the `segmentMap`, which can be found in the `tasks.json` file.

```json
projectId/
|-- segmentations
      |-- Task_001 // Folder with the name of the Task (i.e. "Datapoint" on the Data Page)
            |-- SeriesName.nii.gz
```

### Multi-Series

For Tasks with multiple Series, RedBrick AI generates a **single NIfTI file per Series** upon export.&#x20;

Each file contains all of the individual annotations associated with a particular Series as defined by the `segmentMap`, which can be found in the `tasks.json` file.

```json
projectId/
|-- segmentations
      |-- Task_001 // Folder with the name of the Task (i.e. "Datapoint" on the Data Page)
            |-- Series_001.nii.gz
            |-- Series_002.nii.gz
            |-- Series_003.nii.gz
```

***

## Overlapping Segmentations

For Tasks with overlapping segmentations, RedBrick AI generates the following for each Series:

* an **aggregated annotation file** containing all of the annotations in the Series;
* a **subdirectory** that has the same name as the Series;
* within the subdirectory, an **individual annotation file** for each segmentation;

Please note that the annotation files in the subdirectory are generated **incrementally based on the order in which annotations were created by the labeler**.

```json
projectId/
|-- segmentations
      |-- TaskName
            |-- SeriesName.nii.gz // NIfTI file containing all annotations
            |-- SeriesName 
              |-- instance-1.nii.gz // NIfTI file for first overlapping segmentation
              |-- instance-2.nii.gz // NIfTI file for second overlapping segmentation
```

{% hint style="success" %}
**SDK Mastery:** RedBrick AI automatically enables `binary_mask` for Tasks that have overlapping segmentations.&#x20;

You can read more about the binary\_mask parameter and how it affects exports [here](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.export.Export.export_tasks).
{% endhint %}

***

## Semantic Export

If you would prefer to map your annotations directly to the corresponding Object Label of your [Taxonomy](../../dashboard/taxonomies.md#object-label-types), you can use the `semantic_mask` parameter of the Python SDK's [`export_tasks()`](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.export.Export.export_tasks) function.&#x20;

The Semantic Export enforces a direct mapping between an Object Label and the `segmentMap` value. While this does not change the structure of the export subdirectory itself, Semantic Export does bring significant changes to the `tasks.json` file generated upon export.

Please compare the two sample `segmentMap` outputs below.

{% tabs %}
{% tab title="Standard Export" %}
```json
tasks.json/
  "items": ["image-file.ima",],
  "segmentations": "./path/to/segmentation/file.nii.gz",
  "segmentMap": {
    "1": {
      // This is the first annotation the labeler created
      "category": "Glioma"
    },
    "2": {
      // This is the second annotation the labeler created
      "category": "Glioma"
    },
     "3": {
      // This is the third annotation the labeler created
      "category": "Encephalitis"
    },
    "4": {
      // This is the fourth annotation the labeler created
      "category": "Abscess"
    },
    ...
  }
```
{% endtab %}

{% tab title="Semantic Export" %}
```json
tasks.json/
  "items": ["image-file.ima",],
  "segmentations": "./path/to/segmentation/file.nii.gz",
  "segmentMap": {
    "3": {
      "category": "Glioma"
    },
    "6": {
      "category": "Abscess"
    },
     "8": {
      "category": "Encephalitis"
    },
    ...
  }
```
{% endtab %}
{% endtabs %}

### Common Questions

#### Why are the integer values different for the Semantic Export's `segmentMap`?&#x20;

When a Taxonomy is created, each Object Label is assigned an immutable and unique integer value - a **Category Number**.&#x20;

Unlike Standard Export, which generates the `segmentMap` integer incrementally based on the order the labeler created the annotations, the Semantic Export directly correlates this **Category Number** to your annotation within the NIfTI file, regardless of how the annotator did their work.

In other words (and using the example above), any **Glioma** annotation will always have a `segmentMap` value of 3 upon semantic export, any **Abscess** will always have a value of 6, and so on.

#### What if a labeler creates 2 Entities for a single Object Label and then I try to use Semantic Export?

Semantic Export will strictly enforce the principles of [semantic annotation](../../annotation-and-viewer/segmentation/#instance-vs.-semantic-segmentation) even in the presence of human error.&#x20;

If you attempt to use Semantic Export on a Task that has multiple [Entities](https://docs.redbrickai.com/annotation/creating-editing-and-deleting-annotations#creating-object-labels) associated with a single Object Label, RedBrick AI will aggregate all of the Entities into a single annotation file.&#x20;

In this case, only the Object Label Attributes of the very first Entity will be preserved.

#### What if I need to use Semantic Export on Tasks with overlapping segmentations?

The output format will be the same, but the output annotation files will be named according to their Category Number.

```
projectId/
|-- segmentations
      |-- TaskName
            |-- SeriesName.nii.gz // Annotation file containing all segmentations
            |-- SeriesName // subdirectory
              |-- category-x.nii.gz // where x = the structure's Category Number
              |-- category-y.nii.gz // where y = the structure's Category Number
```

#### What if I re-ordered the Object Labels in my Taxonomy? Does this affect the `segmentMap` for Semantic Export?

No. The Category Number is immutable for all Object Labels, regardless of how you re-order or otherwise manipulate the contents of your Taxonomy in the UI.

***

## Consensus Export

When exporting annotations from a [Consensus Project](../../project-pages/multiple-labeling/consensus/), the `tasks.json` file and the `segmentations/` directory will have a unique structure.&#x20;

Your export subdirectory will contain the annotation files for all users who generated and saved annotations on RedBrick AI. Each individual annotation file is marked with a numeric index (e.g. "\_1" at the end of the file name, and you can map this file to the corresponding user by referencing your `tasks.json` file.

```json
project_id/
├── segmentations
│   ├── Task_001
│   │   ├── seriesA_1.nii
│   │   └── seriesA_2.nii
│   └── Task_002
│       ├── seriesA_1.nii
│       └── seriesA_2.nii
└── tasks.json
```
