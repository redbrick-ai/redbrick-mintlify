# Import Data & Annotations

You can easily import large amounts of data from the command line interface. Before following this guide, make sure to [set up credentials for the CLI](./).

## Importing locally stored images

### Upload using an items file

To upload images that are stored in a non-conventional folder structure, you can define the structure using an [items](../../importing-data/import-cloud-data/creating-an-items-list.md) JSON file and upload it like this.

```bash
$ redbrick upload path/to/items.json
```

***

If you don't want to use an items file for upload, ensure your data is stored within the correct folder structure [defined in our documentation](../../importing-data/uploading-data-to-redbrick.md). You can only upload a single data type in one upload operation. See the [supported file types here](../../importing-data/uploading-data-to-redbrick.md).

```bash
$ redbrick upload path/to/data/ --type DICOM3D
```

You can see all available [types in the CLI upload reference documentation](https://redbrick-sdk.readthedocs.io/en/stable/cli.html#Positional%20Arguments\_repeat8).

### Group images by study

To group your images by study, see [here for examples](../../importing-data/uploading-data-to-redbrick.md), input the following:&#x20;

```bash
$ redbrick upload path/to/data/ --as-study
```

### Upload video frames

To upload a [video by uploading individual frames](../../importing-data/uploading-data-to-redbrick.md#video-frames), input the following:

```
$ redbrick upload path/to/videoframes/ --as-frames --type VIDEOFRAMES
```

## Importing externally stored images

To import data that is stored externally (e.g., in an AWS s3 bucket), you must specify the storage ID. You can find your storage solution's unique Storage ID in the _Storage tab_ of the RedBrick AI platform.

<div data-full-width="true">

<figure><img src="../../.gitbook/assets/CleanShot 2023-12-27 at 15.15.27@2x.png" alt=""><figcaption><p>Click on the field in order to copy the value to your clipboard.</p></figcaption></figure>

</div>

Prepare an [Items List](../../importing-data/import-cloud-data.md#items-list) containing references to your externally stored files.

```bash
$ redbrick upload items.json --storage STORAGEID # replace STORAGEID with your Storage ID
```

## Import annotations

To import annotations with your data, you must first create an items JSON file [following the import annotations guide](../importing-annotations-guide.md).

{% content-ref url="../importing-annotations-guide.md" %}
[importing-annotations-guide.md](../importing-annotations-guide.md)
{% endcontent-ref %}

### Import locally stored annotations & images

```bash
$ redbrick upload path/to/items.json # items.json must have local file paths.
```

### Import locally stored annotations with externally stored images

The following command will upload your (locally stored) annotation files and your image files (stored in `STORAGEID`):

```bash
$ redbrick upload path/to/items.json --storage STORAGEID
```

### Import externally stored annotations & images

If your annotation files are also stored externally, you can run the following command:&#x20;

```
$ redbrick upload path/to/items.json --storage STORAGEID --label-storage LABELSTORAGEID
```
