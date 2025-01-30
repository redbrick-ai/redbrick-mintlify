# Full Format Reference

## Items List and `tasks.json`

Most RedBrick flows incorporate two key JSON files:

1. [Items List](https://docs.redbrickai.com/importing-data/import-cloud-data/creating-an-items-list) - a file which points RedBrick AI to visual assets within a third-party storage solution;
2. `tasks.json` - a file generated upon export that contains a record of the annotation work completed within a Project. Upon export, the `tasks.json` file will contain a **single entry for each Task**;

If you'd like to upload annotations along with your data using either the [CLI](../cli-overview/import-data-and-annotations.md) or the [SDK](../sdk-overview/importing-data-and-annotations.md), please see the corresponding documentation.

## Object Reference

Please see the definition (in TypeScript) of RedBrick's various objects below:

```typescript
type Tasks = Task[];
​
// Single task on RedBrick can be single/multi-series
type Task = {
  // Required on upload and export
  name: string;
  series: Series[];
​
  // Task level annotation information
  classification?: Classification;
​
  // Not required on upload, present in tasks.json
  taskId?: string;
  currentStageName?: string;
  createdBy?: string;
  createdAt?: string;
  updatedBy?: string;
  updatedAt?: string;
  
  // assign metadata to a Task on upload, present in tasks.json
  metaData?: { [key: string]: string }
  
  // assign priorities to a Task on upload
  priority?: number;
  
  // Prescribe task assignent upon upload
  preAssign?: {
    [stageName: string]: string
  }
};
​
// How to correctly format a Series object for upload
// A single series can be 2D, 3D, video etc.
// Also present in tasks.json
type Series = {
  items: string | string[];
  name?: string;
​
  segmentations?: string | string[];
  segmentMap?: {
    [instanceId: string]: number | string | string[] | {
      category: number | string | string[];
      attributes?: Attributes;
      mask?: string;
    };
  };
  binaryMask?: boolean;
  semanticMask?: boolean;
  pngMask?: boolean;
  
  landmarks?: Landmark[];
  landmarks3d?: Landmark3D[];
  measurements?: (MeasureLength | MeasureAngle)[];
  boundingBoxes?: BoundingBox[];
  cuboids?: Cuboid[];
  ellipses?: Ellipse[];
  polygons?: Polygon[];
  polylines?: Polyline[];
  
  classifications?: Classification[];
  instanceClassifications?: InstanceClassification[];
   metaData?: { [ key: string ]: string };
};
​
// Label Types

type Landmark = {
  point: Point2D;
  category: number | string | string[];
  attributes?: Attributes;

  // video meta-data
  video?: VideoMetaData;
};

type Landmark3D = {
  point: VoxelPoint;
  category: number | string | string[];
  attributes?: Attributes;
};
​
type MeasureLength = {
  type: 'length';
  point1: VoxelPoint;
  point2: VoxelPoint;
  absolutePoint1: WorldPoint;
  absolutePoint2: WorldPoint;
  normal: [number, number, number];
  length: number;
  category: number | string | string[];
  attributes?: Attributes;
};
​
type MeasureAngle = {
  type: 'angle';
  point1: VoxelPoint;
  point2: VoxelPoint;
  vertex: VoxelPoint;
  absolutePoint1: WorldPoint;
  absolutePoint2: WorldPoint;
  absoluteVertex: WorldPoint;
  normal: [number, number, number];
  angle: number;
  category: number | string | string[];
  attributes?: Attributes;
};
​
type BoundingBox = {
  pointTopLeft: Point2D;
  wNorm: number;
  hNorm: number;
  category: number | string | string[];
  attributes?: Attributes;
  stats?: MeasurementStats;
​
  // video meta-data
  video?: VideoMetaData;
};

type Cuboid = {
  point1: VoxelPoint;
  point2: VoxelPoint;
  absolutePoint1: WorldPoint;
  absolutePoint2: WorldPoint;
  category: number | string | string[];
  attributes?: Attributes;
  stats?: MeasurementStats;
}

type Ellipse = {
  pointCenter: Point2D;
  xRadiusNorm: number;
  yRadiusNorm: number;
  rotationRad: number;
  category: number | string | string[];
  attributes?: Attributes;
  stats?: MeasurementStats;
  
  // video meta-data
  video?: VideoMetaData;
}
​
type Polygon = {
  points: Point2D[];
​
  category: number | string | string[];
  attributes?: Attributes;
  stats?: MeasurementStats;
​
  // video meta-data
  video?: VideoMetaData;
};
​
type Polyline = {
  points: Point2D[];
  category: number | string | string[];
  attributes?: Attributes;
​
  // video meta-data
  video?: VideoMetaData;
};
​
type Classification = {
  category: number | string | string[];
​
  // video meta-data
  video?: VideoMetaData;
};
​
type InstanceClassification = {
  fileIndex: number;
  fileName?: string;
  values: { [attributeName: string] : boolean};
}

type Attributes =
  | { // Taxonomy V2 attributes
      attrId?: number;
      name?: string;
      optionId?: number | number[];
      value?: string | boolean | string[];
    }[]
  | { // Taxonomy V1 attributes
      [attributeName: string]: string | boolean | string[];
    };
​
type VideoMetaData = {
  frameIndex: number;
  trackId?: string;
  keyFrame?: number;
  endTrack?: Boolean;
};
​
// i is rows, j is columns, k is slice
type VoxelPoint = {
  i: number;
  j: number;
  k: number;
};
// The position of VoxelPoint in physical space (world coordinate) computed using the Image Plane Module
type WorldPoint = {
  x: number;
  y: number;
  z: number;
};
type Point2D = {
  xNorm: number;
  yNorm: number;
};

type MeasurementStats = {
  average: number;
  area?: number;
  volume?: number;
  minimum: number;
  maximum: number;
};
```

## Object Glossary

### Task

The `Task` object represents a single task on RedBrick AI. It contains task-level meta-data information about all the series within the task. A task can contain a single series or multiple series (ex. a full MRI study).&#x20;

#### `name: string`

A user-defined string is defined on upload, it is _required to be unique_ across all tasks in your project. The `name` is meant to be a human-readable string that can help identify tasks ex. you can set `name` of a task to `patient/study01`.

#### `taskId?: string`

A unique identifier generated for each Task by RedBrick AI. This value is provided on export.

#### `currentStageName?: string`

The Stage a Task is in is when it is exported.&#x20;

#### `createdBy?: string`

The email address of the user who uploaded the Task.

#### `createdAt?: string`

The datetime this Task was created (i.e. uploaded).

#### `updatedBy?: string`

The email of the last user to make edits to this Task.

#### `updatedAt?: string`

The datetime that this Task was last edited.

#### **`preAssign?: { [ stageName : string ] : string }`**

When uploading a Task, prescribe which users will have the Task assigned to them by Stage.&#x20;

You can define the assignment for each Stage of the workflow, for example, Label and Review, `{"Label": "name1@redbrickai.com", "Review": "name2@redbrickai.com"}`.

#### `classification: { attributes : [ string : boolean ] }`

A list of attributes assigned to an entire Task (or study, if the Task encapsulates an entire study).

**`metaData?: { [ key: string ]: string }`**

A list of key value pairs that can be affixed to a Task. This information is visible in the Annotation Tool.

**`priority?: number`**

Assign a priority value to a specific Task, which will influence the order in which the Task displays on the Data Page. The Automatic Assignment protocol will also auto-assign Tasks with a priority value to a user’s Labeling / Review Queue before moving on to Tasks without priority values.

***

### Series

The `Series` object has metadata and annotations for a single Series within a Task. A Series can represent anything from a single MRI/CT series, a video, or a single 2D image.&#x20;

If a Series contains annotations, you can expect one or more of the label entries to be present (e.g. `segmentations`, `polygons` etc.).

#### `items: string | string[]`

The items entry is a list of file paths that point to your data. Please have a look at the [#items-list](../../importing-data/import-cloud-data.md#items-list "mention")documentation for a fuller explanation of how to format for various modalities and series/study uploads.

#### `name: string`

An optional user-defined string, _needs to be unique_ across all series. Individual [series will be named after this value on the labeling tool](https://www.loom.com/i/ea12e486bd8845d7b3b8a83fc115ad58). Exported segmentation files will also be named using this value. Using the Series Instance UID here is good practice. &#x20;

#### `classifications: { attributes: [ string : boolean ] }`

A list of attributes assigned to a specific Series.

#### `instanceClassifications: fileIndex | fileName | [ values: { string : boolean } ]`

The `instanceClassifications` object defines a series of boolean values that can be assigned to individual instances (e.g. frames in a video).

**`metaData?: { [ key: string ]: string }`**

A list of key value pairs that can be affixed to a Series. This information is visible in the Annotation Tool.

**`binaryMask?: boolean`**

Reflects the user’s choice of optionally exporting annotations as a binary mask.

**`semanticMask?: boolean`**

Reflects the user’s choice of optionally using semantic export.

**`pngMask?: boolean`**

Reflects the user’s choice of optionally exporting annotations as a PNG mask.

***

### Common Label Keys

Here are the definition for some common entries present in some/all label entries.&#x20;

#### `category: string | string[]`

The class of your annotations. This value is part of your Project [Taxonomy](../../dashboard/taxonomies.md). If the class is nested, `category` will be `string[]`.

#### `attributes: { [ attributeName: string ]: string | boolean }`

Each annotation can have accompanying attributes, that are also defined in your Project [Taxonomy](../../dashboard/taxonomies.md). `attributeName` is defined when creating your Taxonomy.&#x20;

#### `voxelPoint: { i: number, j: number, k: number }`

`VoxelPoint` represents a three-dimensional point in image space, where i and j are columns and rows, and k is the slice number.&#x20;

#### `worldPoint: { x: number, y: number, j: number }`

`WorldPoint` represents a three-dimensional point in physical space/world coordinates. The world coordinates are calculated using `VoxelPoint` and the [Image Plane Module](https://dicom.nema.org/medical/dicom/current/output/chtml/part03/sect_C.7.6.2.html).

#### `point2D: { xnorm: number, ynorm: number }`

`Point2D` represents a two dimensional point. This is used to define annotation types on 2D data. `xnorm` has been normalized by image width, `hnorm` has been normalized by image height.

#### `fileIndex: number`

`fileIndex` is an integer that corresponds to a specific frame in a video series.

#### `fileName: string`

`fileName` represents the name given to an image or specific frame in a video series.

#### `measurementStats: Dict`

A dictionary containing a variety of geometric information about certain Object Labels.

#### `group?: string`

A unique string identifier that corresponds to a group of linked labels.

***

### Measurement Stats

A dictionary (`measurementStats`) containing geometric information about certain Object Labels.

**`average: number`**

The average pixel intensity value inside of a structure.

**`area?: number`**

The area of a 2D Object Label (e.g. Bounding Box, Ellipse), measured in square millimeters.

**`volume?: number`**

The volume of a 3D structure (e.g. Cuboid), measured in cubic millimeters.

**`minimum: number`**

The lowest pixel intensity value present in the structure.

**`maximum: number`**

The highest pixel intensity value present in the structure.

***

### Video Meta Data

#### `videoMetaData: Dict`

A dictionary containing `frameIndex`, `trackId`, `keyFrame`, and `endFrame`.

#### `frameIndex: number` (video)

This specifies which frame in a video sequence the annotation was created.&#x20;

#### `trackId: string` (video)

A unique string that identifies distinct object tracks in a video sequence.

#### `keyFrame: boolean` (video)

If true, this annotation was manually added on a particular video sequence. If false, this annotation is a result of linear interpolation.

#### `endFrame: boolean` (video)

If true, the annotation is the last annotation for a particular video track segment.&#x20;

***

### Segmentations and `segmentMap`

#### `segmentations?: string | string[]`

A list of file paths of segmentation files for this series. Either a single `.nii` file, or multiple `.nii` files containing different instances.

**`segmentMap?: { [ instanceId: number ]: { category: string | string[]; attributes?: Attributes; overlappingGroups?: number[]; group?: string; } };`**

A mapping between a segmentation's instance ID, your Taxonomy category name, and any accompanying attributes. The mapping will apply only to the current series, and instance IDs must be unique across all series in a task (this is useful for instance segmentation).

Please note that the `segmentMap`'s instanceId is generated **incrementally based on the order in which annotations were created by the labeler**. You can find an example JSON output below.&#x20;

```json
"items": ["image-file.ima",],
"segmentations": "./path/to/segmentation/file.nii.gz",
"segmentMap": {
  "1": {
    // This is the first annotation the labeler created
    "category": "Vertebral Body"
  },
  "2": {
    // This is the second annotation the labeler created
    "category": "Vertebral Body"
  },
  "3": {
    // This is the third annotation the labeler created
    "category": "Vertebral Body"
  },
  "4": {
    // This is the fourth annotation the labeler created
    "category": "Spinal Canal Mass"
  },
  "5": {
    // This is the fifth annotation the labeler created
    "category": "Disc Pathology"
  }
},

```

#### `mask?: string`

The path for the annotation file associated with a specific instanceId.

***

### BoundingBox

Contains information about the Bounding Box Object Label.

#### `pointTopLeft:` [`Point2D`](full-format-reference.md#point2d-xnorm-number-ynorm-number)

The location of the top-left point of the bounding box.

#### `wNorm, hNorm: number`

The width and height of the bounding box, normalized by the width and height of the image.

***

### Polygon

Contains information about the Polygon Object Label.

#### `points:` [`Point2D`](full-format-reference.md#point2d-xnorm-number-ynorm-number)`[]`

A list of 2D points that are connected to form a polygon. This list is ordered such that, $$point_i$$ is connected to $$point_{i+1}$$. The last point is also connected to the first point to close the polygon.&#x20;

***

### MeasureLength

Contains information about the Length Measurement Object Label.

#### `point1, point2 :` [`VoxelPoint`](full-format-reference.md#voxelpoint-i-number-j-number-k-number)

A length measurement is defined by two points, and the length measurement is the distance between the two points.

#### `absolutePoint1, absolutePoint2 :` [`WorldPoint`](full-format-reference.md#worldpoint-x-number-y-number-j-number)

Corresponding to `point1`, `point2` these are points in physical space.

#### `normal: [number, number, number]`

Measurements can be made on oblique planes. `normal` defines the normal unit vector to the slice on which this annotation was made. For annotations made on non-oblique planes, the normal will be `[0,0,1]`.

#### `length: number`

The value of the measurement in mm.

***

### MeasureAngle

Contains information about the Angle Object Label.

#### `point1, point2, vertex :` [`VoxelPoint`](full-format-reference.md#voxelpoint-i-number-j-number-k-number)&#x20;

Angle measurement is defined by three points, where the vertex is the middle point. The angle between the two vectors (vertex -> point1 and vertex -> point2) defines the angle measurement. These points are all represented in IJK image coordinate space.&#x20;

#### `absolutePoint1, absolutePoint2 :` [`WorldPoint`](full-format-reference.md#worldpoint-x-number-y-number-j-number)&#x20;

Corresponding to `point1`, `point2`, `vertex`, these values are coordinates in the DICOM world coordinate system i.e. physical space.&#x20;

#### `normal: [number, number, number]`

Measurements can be made on oblique planes. `normal` defines the normal unit vector to the slice on which this annotation was made. For annotations made on non-oblique planes, the normal will be `[0,0,1]`.

#### `angle: number`

The value of the angle in degrees.

***

### Ellipse

Contains information about the Ellipse Object Label.

**`pointCenter: point2D`**

Information regarding the exact center of the Ellipse Object Label.

**`xRadiusNorm: number`**

A numeric value equivalent to half the length of the Ellipse Object Label’s major axis.

**`yRadiusNorm: number`**

A numeric value equivalent to half the length of the Ellipse Object Label’s minor axis.

**`rotationRad: number`**

The rotation angle of the Ellipse Object Label, expressed in radians.

***

### Landmark

Contains information about the Landmark Object Label on 2D images.

**`point: point2D`**

The point in physical space on a 2D image where the Landmark is located.

***

### Landmark 3D

Contains information about the Landmark Object Label on 3D volumes.

**`point: voxelPoint`**

The point in physical space on a 3D volume where the Landmark is located.

***

### Cuboid

Contains information about the Cuboid Object Label.

**`point1, point2: voxelPoint`**

Information about the initial point of the Cuboid (`point1`) and the final point (`point2`, opposite diagonal corner).

**`absolutePoint1, absolutePoint2: worldPoint`**

The position of `VoxelPoints` `point1` and `point2` in physical space (world coordinate) computed using the Image Plane Module.

***

## Consensus Formats&#x20;

### Consensus `tasks.json`

```typescript
// Single task on RedBrick can be single/multi-series
type Task = {
  // Required on upload and export
  name: string;
  consensus: true; 
  consensusScore: number; // overall consensus score
  consensusTasks: ConsensusTask[]

  // Only required on export
  taskId?: string;
  currentStageName?: string;
  createdBy?: string;
  createdAt?: string;
  updatedBy?: string;
  updatedAt?: string;
};

type ConsensusTask = {
  updatedBy: string;
  updatedAt: string; 
  scores: {secondaryUserEmail: string, score: number}[]
  series: Series[]
}
```

### The `ConsensusTask` Object

The consensus task object contains information about the consensus annotations for this task. There will be a single entry for every annotator who annotated this task. For example, if 3 users annotated each task in your project, the length of the `consensusTasks` array will be 3.

#### `updatedBy: string`

The e-mail of the user who annotated the task.

#### `updatedAt: string`

The datetime when the user last updated the task.

#### `scores: {secondaryUserEmail: string, score: number}[]`&#x20;

The `scores` entry compares the current users' annotations with every other user. The scores array will be of length n-1, where n is the number of users who annotated this task. `score` is the similarity score between the current user, and `secondaryUserEmail`.

#### `series: Series[]`

The [series entry](full-format-reference.md#series) for the current user only.

***

## Taxonomy Object

```typescript
type Taxonomy = {
    orgId: string;
    name: string;
    createdAt: datetime;
    archived: boolean;
    isNew: true;
    taxId: string;
    studyClassify: Attribute[];
    seriesClassify: Attribute[];
    instanceClassify: Attribute[];
    objectTypes: ObjectType[];
}

type ObjectType = {
    category: string;
    classId: number; // [0, n)
    labelType: BBOX | POINT | POLYLINE | POLYGON | ELLIPSE | SEGMENTATION | LENGTH | ANGLE | CUBOID;
    attributes?: Attribute[];
    color?: string;
    archived?: boolean;
    parents?: string[];
    hint?: string;
}

type Attribute = {
    name: string;
    attrType: BOOL | TEXT | SELECT | MULTISELECT;
    attrId: number;
    options?: AttributeOption[];
    archived?: boolean;
    parents?: string[];
    hint?: string;
    defaultValue?: number | number[]; // pre-populated optionId(s) for SELECT/MULTISELECT
}

type AttributeOption = {
    name: string;
    optionId: number;
    color?: string;
    archived?: boolean;
}
```
