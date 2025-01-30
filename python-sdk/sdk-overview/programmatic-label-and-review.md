# Programmatic Label & Review

It may be useful to programmatically add labels to your uploaded data or perform a review on queued tasks. This scenario may arise if you have an automated way of reviewing data or if you want to bulk-process tasks.&#x20;

{% hint style="success" %}
Please see the detailed reference documentation for [`put_tasks` here](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.labeling.Labeling.put\_tasks).
{% endhint %}

{% hint style="warning" %}
You can only use `put_tasks` on Tasks **assigned to your API key.**

Please consult our [documentation](https://docs.redbrickai.com/python-sdk/sdk-overview/assigning-and-querying-tasks#assign-tasks-to-the-current-user) to learn more about how to assign Tasks to your API key.
{% endhint %}

First, perform the [standard RedBrick AI SDK set-up](./#initializing-the-redbrick-sdk-in-python) to create a project object.

```
project = redbrick.get_project(org_id, project_id, api_key)
```

Next, you need to get a list of Tasks you want to label/review. You can do this by:&#x20;

1. Searching for the `task_id` through the RedBrick AI UI.
2. Retrieving the `task_id` from your filename/custom `name` from the Items List using [search\_tasks](exporting-annotations.md#query-tasks-in-your-project).
3. Retrieving tasks assigned to your API key using `list_tasks`.

#### Programmatically Label Tasks

Add your annotations within the `series` field, along with the `task_id`. Please refer to the reference documentation for the [format of the annotations in Series](../formats/full-format-reference.md).

&#x20;The corresponding Task must be queued in the Label Stage and assigned to your API key.&#x20;

```python
tasks = [
    {
        "taskId": "...",
        "series": [{...}]
    },
]

# Submit tasks with new labels
project.labeling.put_tasks("Label", tasks)

# Save tasks as draft with new labels
project.labeling.put_tasks("Label", tasks, finalize=False)
```

#### Programmatically Review Tasks

Add your review decision in the `review_result` argument, along with the `task_id`. The corresponding Task must be queued in the Review stage that you specify in `stage_name` and must be assigned to your API key.

```python
# Set review_result to True if you want to accept the tasks
project.review.put_tasks("Review_1", [{taskId: "..."}], review_result=True)

# Set review_result to False if you want to reject the tasks
project.review.put_tasks("Review_1", [{taskId: "..."}], review_result=False)

# Add labels if you want to accept the tasks with correction
project.review.put_tasks("Review_1", [{taskId: "...", series: [{...}]}])
```

## Re-annotate Ground Truth Tasks

Once your Task goes through all of the stages in your workflow, it will be stored in the Ground Truth Stage. If you notice issues with one or more of your Ground Truth Tasks, you can either modify them manually within the UI while the Tasks are still in the Ground Truth Stage or **send them back to the Label Stage** for correction.

First, get a list of the `task_id`s you want to send back to Label. You can do this by [exporting only Ground Truth Tasks](exporting-annotations.md#export-only-ground-truth) and filtering them. Then, use `move_tasks_to_start` to send them back to Label.

```python
task_ids = ["...", "..."]
project.labeling.move_tasks_to_start(task_ids=task_ids)
```

{% hint style="warning" %}
All corresponding Tasks need to be in the Ground Truth Stage. This function will not work for Tasks queued in Review.&#x20;
{% endhint %}
