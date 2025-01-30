---
description: Write a script to dynamically arrange the viewports for your project
---

# Custom Hanging Protocol

The Custom Hanging Protocol feature allows you to write a script that will programmatically define the visual layout of your Annotation Tool **at the Project level**.&#x20;

Pre-configuring parameters such as Windowing settings, Thresholding settings, the number of viewports in a Layout Tab, which views display by default, etc., is both an easy way to save time for your annotators and makes for a much smoother overall annotation experience.

{% embed url="https://www.loom.com/share/a5b5255cd1954bd590849a8e939c9b5f" %}

## Script Usage Guide

This guide provides an overview of the available functions and types to help you effectively manage these settings. At present, you can control the following:&#x20;

*   The dimensions of a Layout Tab (`setDimensions`):

    * **REQUIRED:** the number of columns in a Layout Tab (`numColumns`)
    * **REQUIRED:** the number of rows in a Layout Tab (`numRows`)


*   The contents of each viewport in a Layout Tab (`setViews`):

    * **REQUIRED:** an array describing each viewport's content (`views`)
    * **REQUIRED:** Which series to show (`seriesIndex`)
    * **REQUIRED:** Which way to view the series (`plane`)
    * Flip the view horizontally (`flippedHorizontally`)
    * Flip the view vertically (`flippedVertically`)
    * Activate Intellisync (`synchronized`)
    * Maximize a single viewport in a Layout Tab (`expanded`)


*   The default Windowing setting for each Series (`setWindowing`):

    * **REQUIRED:** the number of the Series (`seriesIndex`)
    * **REQUIRED:** the desired Windowing Level (`level`)
    * **REQUIRED:** the desired Windowing Width (`width`)


*   The default Thresholding setting for each Series (`setThresholding`):

    * **REQUIRED:** the number of the Series (`seriesIndex`)
    * **REQUIRED:** the lower limit of the Thresholding range (`min`)
    * **REQUIRED:** the upper limit of the Thresholding range (`max`)


* Create and configure a new Layout Tab in your Task (`nextTab`)\

* Disable certain viewports (`disableViewType`)

{% hint style="info" %}
The Custom Hanging Protocol script takes the available Series for a particular Task as input and returns the layout dimensions and list of views to display.
{% endhint %}

## Custom Hanging Protocol Format Reference

```typescript
function setViews(views: View[]) {
 //...
}
function setDimensions(numColumns: number, numRows: number) {
 // ...
}
function setWindowing(seriesIndex: number, level: number, width: number){
 // ...
}
function setThresholding(seriesIndex: number, min: number, max: number) {
 // ...
}

function nextTab()

function disableViewType(seriesIndex: number, typeName: 'AXIAL' | 'SAGITTAL' | 'CORONAL' | '3D' | 'MIP') { }


// this function has been replaced by the Tool Settings page of Project Settings
function setSegmentationSettings(
  [  
    { 
      toolName: ToolOptions; 
      enabled: boolean;
      modes?: ToolModes[];
      defaultMode?: ToolModes;
      defaultTool?: boolean;
    }
  ]
);

// When a user uploads a Task and enables Hanging Protocols, 
// the hangingProtocol() function takes Series[] and the following parameters as input
interface Series {
  seriesIndex: number;
  is2DImage: boolean;
  isVideo: boolean;
  numFrames: number;
  name: string; // User defined name if available, else "A", "B", ...
  imagingAxis: 'AXIAL' | 'SAGITTAL' | 'CORONAL';
}

interface View {
  plane: 'AXIAL' | 'SAGITTAL' | 'CORONAL' | '3D' | 'MIP';
  seriesIndex: number;
  flippedHorizontally?: boolean;
  flippedVertically?: boolean;
  synchronized?: boolean;
  expanded?: boolean; // Only applicable to a single view in a given Layout Tab
}
```

## Examples

### Default Script

This default script uses some defined macros to make setting the view easier.&#x20;

```typescript
function hangingProtocol(allSeries: Series[]) {
  // This is the default layout script
  if (allSeries.length > 1) {
    setMultiSeries();
  } else if (allSeries[0].is2DImage) {
    setSingleView();
  } else {
    setMPR();
  }
}
```

***

### Set Single View

```javascript
function setSingleView(seriesIndex=0) {
  setDimensions(1,1);
  setViews([
    {
      plane: allSeries[seriesIndex].imagingAxis,
      seriesIndex: seriesIndex,
    }
  ]);
}
```

***

### Set Multi-Series Layout

This script sets each Series as a single viewport that is viewed on the imaging axis.

```javascript
function setMultiSeries() {
  function singleSeries(series_, index) {
    return {
      plane: series_.imagingAxis,
      seriesIndex: index,
    };
  }
  let views = allSeries.map(singleSeries);

  setViews(views.slice(0,9));
}
```

***

### Set Multi-Planar Reconstruction

```javascript
function setMPR(seriesIndex=0) {
  let targetSeries = allSeries[seriesIndex];
  setDimensions(2,2);
  setViews([
    {
      plane: 'SAGITTAL',
      seriesIndex: seriesIndex,
      expanded: targetSeries.imagingAxis === 'SAGITTAL',
    },
    {
      plane: 'CORONAL',
      seriesIndex: seriesIndex,
      expanded: targetSeries.imagingAxis === 'CORONAL',
    },
    {
      plane: 'AXIAL',
      seriesIndex: seriesIndex,
      expanded: targetSeries.imagingAxis === 'AXIAL',
    },
    {
      plane: '3D',
      seriesIndex: seriesIndex,
    }
  ]);
}
```

***

### Set and Configure Multiple Layout Tabs

The following script creates 2 Layout Tabs, each containing 2 Series.

```javascript
if (allSeries.length === 4) { // executes when there are 4 total Series in a Task
   setDimensions(2, 1); // set 2x1 layout for Layout Tab 1
   setViews( // adding the first and second image/volume to Layout Tab 1
   [ 
      {
         seriesIndex: 0,
         plane: 'SAGITTAL'
      }, 
      {
         seriesIndex: 1,
         plane: 'SAGITTAL'
      }
   ]
);
   nextTab(); // create and configure Layout Tab 2
   setDimensions(2, 1); // set 2x1 layout for Layout Tab 2
   setViews( // add third and fourth image/volume to Layout Tab 2
   [ 
      {
         seriesIndex: 2,
         plane: 'SAGITTAL'
      }, 
      {
         seriesIndex: 3,
         plane: 'SAGITTAL'
      }
   ]
 )
```

***

### Disable a Specific Viewport

The following script will disable all 3D viewports in the RedBrick Annotation Tool.

```javascript
allSeries.forEach((series) => {
    disableViewType(series.seriesIndex, '3D');
    }
)
```

***

### Synchronize Views

Hanging protocols can be used along side [intellisync.md](../../annotation-and-viewer/viewer-basics/intellisync.md "mention")for ease of use when annotating scans in a study.&#x20;

For example, let's assume that we have uploaded a single Task containing 4 Series from an MRI study: T1, T1CE, T2, and Flair weighted MR scans.

After we enable Hanging Protocols, the `hangingProtocol()` function will take the 4 Series as an input and parse them in the following way:

```javascript
[
    {
        seriesIndex: 0,
        is2DImage: false,
        isVideo: false,
        numFrames: 1,
        name: 'T1',
        imagingAxis: 'SAGITTAL',    
    },
    {
        seriesIndex: 1,
        is2DImage: false,
        isVideo: false,
        numFrames: 1,
        name: 'T2',
        imagingAxis: 'SAGITTAL',    
    },
    {
        seriesIndex: 2,
        is2DImage: false,
        isVideo: false,
        numFrames: 1,
        name: 'T1CE',
        imagingAxis: 'SAGITTAL',    
    },
    {
        seriesIndex: 3,
        is2DImage: false,
        isVideo: false,
        numFrames: 1,
        name: 'Flair',
        imagingAxis: 'SAGITTAL',    
    },
]
```

We can then use the information that has been parsed by the `hangingProtocol()` function to generate a script that sorts our views, displays the imaging axis and activates Intellisync.

```javascript
// sort series by Name
let priorities = ['t1', 't1ce', 't2', 'flair'];
allSeries.sort((a, b)=>priorities.indexOf(a.name.toLowerCase()) - priorities.indexOf(b.name.toLowerCase()));

// display Series along the imaging axis
let imagingAxis = allSeries[0].imagingAxis;

// filter out views that were imaged in a different axis
let eligibleSeries = allSeries.filter((series) => series.imagingAxis === imagingAxis);

// Configure viewports
setViews(eligibleSeries.map((series) => {
  return {
    seriesIndex: series.seriesIndex,
    plane: series.imagingAxis,
    synchronized: true,
  };
}));
```
