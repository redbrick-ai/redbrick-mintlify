# Agreement calculation

This section of the documentation will cover how RedBrick AI calculates inter-annotator agreement between two users.&#x20;

For two sets of labels, annotation instances are matched up by category. For the same category, instances are matched up by selecting pairs that maximize the overall agreement score. For two instances of the same category, RedBrick AI uses the following similarity functions

#### Bounding box, Polygon, and Pixel Segmentation

RedBrick AI uses IOU for these annotation types. For two annotations A and B IOU is defined by:

$$
IOU = \frac{A\cup B}{A\cap B}
$$

​**Landmarks**

For landmarks/keypoints, RedBrick AI uses a normalized Root Mean Squared Error (RMSE) to compute similarity, where similarity is $$Similarity = 1 - RMSE$$.&#x20;

$$
MSE = \frac{1}{n}\sum_{i}^{n}(P_{i} - \hat P_{i})^2
\\
RMSE = \sqrt{MSE}
$$

Where $$n$$​ is the number of components of the point (2 for 2D, 3 for 3D), and $$P_i, \hat{P_i}$$​ are normalized components (by width, height, depth of the image) of the two points.&#x20;

#### Length Measurements

Comparisons of length measurements are done by comparing the two sets of points (using the technique covered above) that define the length line.

#### Angle Measurements&#x20;

For angle measurements, the vectors between each arm of the angle measurement are compared. The two angles comparing both sets of measurement arms are computed. The similarity score is then defined by:

$$
Similarity = 1 - \frac{\theta_1 + \theta_2}{2\pi}
$$

​Where $$\theta_1, \theta_2$$​ are the angles between the two sets of measurement arms.

#### Classification

For classification labels, the agreement is binary. If the chosen category and attributes match, the consensus score will be 100%, otherwise, it will be 0%.

## Generating a single score

To generate a single score between two sets of labels, a series of averages are computed.&#x20;

1. Scores of matching annotations instances of the same category are averaged, to generate a single score per category.&#x20;
2. Scores are then averaged per category.&#x20;
3. Scores are then averaged per label type to generate a single score per label type.&#x20;
4. For videos, scores are calculated per frame and averaged to generate a single score per sequence.&#x20;
5. For multi-series studies, scores are averaged by volume to generate a single score per study. ​
