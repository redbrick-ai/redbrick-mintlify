# Importing Data & Annotations

The RedBrick AI SDK allows you to programmatically import data and/or annotations with a Python script. You can import either locally or externally stored data via the SDK using the `create_datapoints` method.

{% hint style="info" %}
Please see the full reference documentation for [`create_datapoints` here](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.upload.Upload.create\_datapoints).
{% endhint %}

Perform the [standard RedBrick AI SDK setup](./#initializing-the-redbrick-sdk-in-python) to create a Project object.

```python
project = redbrick.get_project(org_id, project_id, api_key)
```

## Import locally stored images

To import locally stored data, create a list of `points` with relative file paths to your locally stored data, and use the [`redbrick.StorageMethod.REDBRICK`](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.StorageMethod) storage ID.&#x20;

```python
# create a list of file paths to your locally stored data
points = [{"items": ["path/to/data.nii"], "name": "..."}]

# perform the upload operation
project.upload.create_datapoints(
    storage_id=redbrick.StorageMethod.REDBRICK, 
    points=points
)
```

{% hint style="info" %}
The points array follows the format of the [items list](../../importing-data/import-cloud-data/creating-an-items-list.md).
{% endhint %}

## Import externally stored images

To import data stored in an external storage method such as AWS s3, be sure to use the Storage ID found on the Storage tab of your RedBrick AI account instead of `redbrick.StorageMethod.REDBRICK`.

<div data-full-width="true">

<figure><img src="../../.gitbook/assets/CleanShot 2023-12-27 at 15.15.27@2x.png" alt=""><figcaption><p>Click on the field to copy the Storage ID to your clipboard!</p></figcaption></figure>

</div>

{% hint style="info" %}
[Visit our documentation on external storage](../../importing-data/import-cloud-data.md) to learn how to integrate your own external storage like AWS s3, GCS, or Azure blob.
{% endhint %}

## Import annotations

First, please follow our guide on [preparing your items list for annotation](../importing-annotations-guide.md) import to prepare your points object correctly.

{% content-ref url="../importing-annotations-guide.md" %}
[importing-annotations-guide.md](../importing-annotations-guide.md)
{% endcontent-ref %}

### Importing locally stored annotations & images

```python
project.upload.create_datapoints(
    storage_id=redbrick.StorageMethod.REDBRICK, 
    points=points
)
```

### Importing locally stored annotations with externally stored images

```python
project.upload.create_datapoints(
    storage_id="your_storage_id", 
    label_storage_id=redbrick.StorageMethod.REDBRICK
    points=points
)
```

### Importing externally stored annotations and images

```python
project.upload.create_datapoints(
    storage_id="your_storage_id", 
    label_storage_id="your_storage_id"
    points=points
)
```
