# Overlapping Segmentations

If you are annotating multiple structures in the same pixel/voxel space, you can utilize overlapping segmentations in RedBrick AI.

Any time you are using a [Segmentation Tool](segmentation-tools.md) (e.g. Brush Tool, Pen Tool, Contour Tool, etc.), you can use the options in the [Masking Panel](../visualization-and-masking.md#masking) to configure your overlapping (or overwriting) behavior.

Specifically, you can utilize various combinations of the **Editable Area** and **Modify Other Segments** menus to determine how your annotations will be overlapped or overwritten. For a more comprehensive description of these menus and their functions, please reference [the relevant documentation](../visualization-and-masking.md#editable-area).

Alternatively, please see the following short tutorial for a visual walkthrough of the differences:&#x20;

{% embed url="https://www.loom.com/share/536fa33679814e2f909e4944b1c0f8ba?sid=4b1f2781-e2c3-4904-9e02-66b3b8a0895e" %}
An overview of how to overlap segmentations
{% endembed %}

### Exporting Overlapping Segmentations

When exporting a Task with overlapping segmentations, RedBrick AI generates a unique annotation file for each segmentation.&#x20;

The following JSON block is an example of how a single Task with two overlapping annotations will be exported.

```json
projectId/
|-- TaskName
      |-- SeriesName.nii.gz // NIfTI file containing all annotations
      |-- SeriesName 
        |-- instance-1.nii.gz // NIfTI file for first overlapping segmentation
        |-- instance-2.nii.gz // NIfTI file for second overlapping segmentation
```
