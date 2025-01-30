# Instance vs. Semantic

**Semantic segmentation** treats multiple objects of the same class as a single entity. In the example below, you can see that the labeler is responsible for annotating a single structure ("Vertebrae"), regardless of the vertebrae's classification (e.g. L1, S1, etc.).&#x20;

<figure><img src="../../.gitbook/assets/image (10).png" alt=""><figcaption><p>Semantic Segmentation</p></figcaption></figure>

On the other hand, **instance segmentation** treats multiple objects of the same class as distinct individual objects (or instances). In the example below, the annotator must create a unique annotation (as represented by an Instance in Redbrick AI) for each specific vertebrae.

<figure><img src="../../.gitbook/assets/image (13).png" alt=""><figcaption><p>Instance Segmentation</p></figcaption></figure>

On RedBrick AI, you can **perform both semantic and instance segmentation** by controlling how many instances of a particular category you create on the left side bar. If you create more than one instance of a single category, on export, you will be able to correlate the instance ID's in your segmentation mask to your category names.&#x20;

Check out this video for an overview:

{% embed url="https://www.loom.com/share/a157d1c350a34192bb53a33c51488d09" %}
