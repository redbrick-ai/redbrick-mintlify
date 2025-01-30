# Importing Annotations Guide

You can import all annotation types that are supported in RedBrick AI, including segmentations, classifications, bounding boxes, and more. Imported annotations will appear automatically on your annotator's interface.

{% hint style="warning" %}
Annotations and images must be imported together at the start.&#x20;

If you want to add annotations programmatically to images that have already been uploaded, [please use the programmatic label & review](sdk-overview/programmatic-label-and-review.md).
{% endhint %}

{% hint style="warning" %}
Annotation import is only supported through the SDK and CLI.&#x20;

That is, you cannot use the [direct upload UI](../importing-data/uploading-data-to-redbrick.md) to import annotations, and you must use the items list with the SDK/CLI to provide the required metadata along with annotations.
{% endhint %}

To import images along with segmentations, you must provide us with:

1. Images in any supported format and NIftI segmentation files.
2. [An items list](importing-annotations-guide.md#items-list-for-importing-segmentations) that provides a mapping of:
   * Segmentation files to volumes so that segmentations are applied to correct images.
   * Values within segmentation file to taxonomy categories.

{% hint style="success" %}
Once you've prepared the [items list in the format defined below](importing-annotations-guide.md#items-list-for-importing-segmentations), you can import the images and annotations using the [`create_datapoints` SDK method](sdk-overview/importing-data-and-annotations.md) or [CLI `upload` method](cli-overview/import-data-and-annotations.md).
{% endhint %}

## Items list for importing segmentations

You can find the [full format reference here](formats/full-format-reference.md#items-list-and-tasks.json). In this section, we will focus on importing segmentations. In the examples below, pay attention to the following fields:&#x20;

1. `segmentations`: The segmentation files to be applied to the task.
2. `segmentMap`: Map the values present in the segmentation files to their corresponding taxonomy categories.

### I: One segmentation file per task

<pre class="language-json" data-line-numbers><code class="lang-json">{
    "name": "...", 
    "series": [
        {
            "items": ["instance-01.dcm", "instance-02.dcm", ...],
            "segmentations": "segmentation.nii.gz",
            
            <a data-footnote-ref href="#user-content-fn-1">// Read more about "segmentMap"</a>
            "segmentMap": {
                "1": "category-a", 
                "2": "category-b"
            }
        }
    ]
}
</code></pre>

### II: Multiple segmentation files per task

Sometimes, segmentations for a single volume are stored in multiple segmentation files, but these segmentation files are not binary masks. In this case, follow the format below.

<pre class="language-json5"><code class="lang-json5">{
    "name": "...", 
    "series": [
        {
            "items": ["instance-01.dcm", "instance-02.dcm", ...],
            
            <a data-footnote-ref href="#user-content-fn-2">// Read more about "segmentations"</a>
            "segmentations": ["segmentation-1.nii.gz", "segmentation-2.nii.gz"]
            
            <a data-footnote-ref href="#user-content-fn-3">// Read more about "segmentMap"</a>
            "segmentMap": {
                "1": "category-a", 
                "2": "category-b"
            }
        }
    ]
}
</code></pre>

### Common mistakes for I and II.&#x20;

{% hint style="warning" %}
* The values 1 and 2 must be present in either `segmentation-1.nii.gz` or `segmentation-2.nii.gz.`
* Values in `segmentation-1.nii.gz` & `segmentation-2.nii.gz` that are not in `segmentMap`will not map to any taxonomy category. This will result in uneditable, view-only annotations.
* All values in `segmentation.nii.gz` that are not in `segmentMap` will not be mapped to any taxonomy category in the editor.
{% endhint %}

### III: Multiple binary segmentation files per task

A common pattern is to store each segmentation instance in a separate NIfTI file as a binary mask. In the example below, all non-zero values in `segmentation-1.nii.gz` are meant to correspond to the taxonomy category `category-a`.&#x20;

<pre class="language-json"><code class="lang-json">{
    "name": "...", 
    "series": [
        {
            "items": ["instance-01.dcm", "instance-02.dcm", ...],
            
            <a data-footnote-ref href="#user-content-fn-4">// Read more about "segmentations"</a>
            "segmentations": ["path/segmentation-1.nii.gz", "path/segmentation-2.nii.gz"]
            "segmentMap": {
            
                <a data-footnote-ref href="#user-content-fn-5">// Read more about "1"</a>
                "1": {
                
                    <a data-footnote-ref href="#user-content-fn-6">// Read more about "category"</a>
                    "category": "category-a", 
                    
                    <a data-footnote-ref href="#user-content-fn-7">// Read more about "mask"</a>
                    "mask": "path/segmentation-1.nii.gz",                 
                }, 
                "2": {
                    "category": "category-b", 
                    "mask": "path/segmentation-2.nii.gz"
                }, 
                
                <a data-footnote-ref href="#user-content-fn-8">// Read more about "binaryMask"</a>
                "binaryMask": true,
            }
        }
    ]
}
</code></pre>

[^1]: All "1" within segmentation.nii will map to "category-a".

[^2]: The masks here are not necessarily binary masks, i.e., they might have multiple values within them. \
    \
    The mapping between value and category should be stable across files.&#x20;

[^3]: All "1" within both segmentation files will map to "category-a".

[^4]: For this example, each segmentation file is a binary mask, i.e., all non-zero values in a file will be mapped to a single category.

[^5]: When exported, this segmentation will be represented by "1" in the exported NIfTI.

[^6]: This segmentation will be mapped to "category". The "category" must exist in your Project's Taxonomy.

[^7]: This mapping will apply to the segmentation file defined by "mask".

[^8]: This defines that all segmentation files are binary masks, i.e., all non-zero values represent a single category.&#x20;
