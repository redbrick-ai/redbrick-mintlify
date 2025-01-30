# Annotation mirroring

It is common to have multiple series that show the same anatomy with different scanner directions or scanner settings.&#x20;

The segmentation mirroring feature allows you to "mirror" the segmentations from a single volume onto another volume. This allows you to compare and contrast information from different scans to modify the same segmentation file.&#x20;

{% embed url="https://www.loom.com/share/722a414d86e947d582d2790270e2b251" %}
Segmentation mirroring demonstration
{% endembed %}

### Activating and using

To activate, load up a task with more than one 3D series, and select "Mirror labels to all volumes." This option will not be available if your task only has a single series.

<figure><img src="../../.gitbook/assets/image (1) (2).png" alt=""><figcaption><p>Activating label mirroring</p></figcaption></figure>

Once activated, you can now edit any segmentation labels from the series that you are mirroring in the same way as any other segmentation label.

### Notes, warnings, and limitations

* This feature will only be effective if your data is properly registered. We use the header information of your DICOM and NIfTI files to align the data in three dimensions. If your series are not properly aligned, the mirroring will also be incorrectly aligned.
* While using label mirroring, 2D tools will not be available, only 3D variants.
