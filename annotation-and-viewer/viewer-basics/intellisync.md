---
description: Smart synchronization between multiple volumes in a single study.
---

# Intellisync

It is common to have multiple scans that are taken with different parameters in the same axis (i.e. T1 vs T2 MRI). Intellisync is a feature that synchronizes multiple series in different viewports to make annotation and diagnosis faster. For viewports that are aligned, scroll position will be synchronized. For viewports that are out of alignment, the intersection between the current instance and the other viewport is shown as a reference line.

## Activating Intellisync

When activated, intellisync applies to all 2D viewports of the chosen series. It can also be activated for all series at once.

1. Command bar: search for `Intellisync`
2. Keyboard (selected viewport): `Command + a` (Mac) or `Control + a` (Windows)
3. Keyboard (All series): `Shift + Command + a` (Mac) or `Shift + Control + a` (Windows)
4. Mouse: Through the action dropdown in the top right of the given viewport

{% embed url="https://www.loom.com/share/31ee8cf4d40946059365ee9686d95514" %}
Intellisync with orthogonal imaging axis
{% endembed %}

{% embed url="https://www.loom.com/share/b3fcff5356d244e5b3a952681d435a1b" %}
Intellisync with label mirroring and weighted MRIs
{% endembed %}

## Troubleshooting and limitations

* Reference lines are computed based on image position patient and image orientation patient headers in each DICOM instance. Therefore, reference lines are only available for data sourced from DICOM files.
* For scroll syncing, the absolute world position is used. This means that data must be registered correctly. This feature will work best on data with identical headers (position, direction, dimensions, and orientation).
* For scroll syncing, eligibility for syncing is computed based on the viewing angle of the viewports. Therefore, two views that seem like they should sync because they both say "AXIAL"  may not if their coordinate systems don't align well.
