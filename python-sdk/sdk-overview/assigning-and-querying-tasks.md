# Assigning & Querying Tasks

The SDK offers multiple ways to query/search through your project tasks and programmatically assign them to various users.&#x20;

## Search by Task Name

Use `list_tasks` to search for tasks by `name` and get their corresponding `task_id`. Often, users will have Task `name`s readily accessible, and can use `list_tasks` to get the corresponding `task_id,` which may be needed in other SDK functions.&#x20;

{% hint style="success" %}
Please see a detailed reference for [`list_tasks` here](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.export.Export.search\_tasks).
{% endhint %}

```python
project = redbrick.get_project(org_id, project_id, api_key)

tasks = project.export.list_tasks() # fetches all tasks
specific_task = project.list_tasks(task_name="...") # fetches specific task by name
```

***

## Assign Tasks to a User

Use `assign_task` when you already have the `task_id` you want to assign to a particular user. If you don’t have the `task_id`, you can query all the Tasks using [`list_tasks`](exporting-annotations.md#export-all-tasks) or query tasks assigned to a particular user/unassigned tasks using [`list_tasks(user_id="...")`](assigning-and-querying-tasks.md#retrieve-queued-tasks).

#### Assign to a Specific User

```python
project = redbrick.get_project(org_id, project_id, api_key)

# Assign tasks in Label stage to a specific user
project.labeling.assign_tasks(task_ids=["..."], email="...")

# Assign tasks in Review stage to specific user
project.review.assign_tasks(task_ids=["..."], email="...")
```

***

## Retrieve Queued Tasks

Use `list_tasks` in conjunction with a specific `user_id` when you want to retrieve the Tasks assigned to a particular user. This can be useful in preparation for using [`assign_tasks`](assigning-and-querying-tasks.md#assign-tasks-to-a-user) to programmatically assigning unassigned tasks, or [`put_tasks`](programmatic-label-and-review.md) to programmatically label/review tasks assigned to you.

### Retrieve Tasks Assigned to Specific User

```python
project = redbrick.get_project(org_id, project_id, api_key)

# Get Tasks assigned to email@email.com in Label Stage
project.export.list_tasks(labeling.(stage_name="Label", user_id="email@email.com")

# Get Tasks assigned to email@email.com in Review_1 Stage
project.export.list_tasks(stage_name="Review_1", user_id="email@email.com")
```

### Retrieve Unassigned Tasks

You can also fetch all unassigned Tasks in a particular stage. This information may be useful when choosing which Tasks to assign to users.&#x20;

```python
project = redbrick.get_project(org_id, project_id, api_key)

# Get unassigned tasks in Label labeling stage
project.export.list_tasks(redbrick.TaskFilters.UNASSIGNED, stage_name="Label")

# Get unassigned tasks in Review_1 review stage
project.export.list_tasks(redbrick.TaskFilters.UNASSIGNED, stage_name="Review_1")
```

***

## Retrieve Tasks Assigned to You

With the correct configuration of list\_tasks(), you can perform functions as specific as retrieving a list of Tasks from a specific Stage to your specific API key. Please see the code snippet below for an example:

```python
project = redbrick.get_project(org_id, project_id, api_key)

# Get tasks assigned to your API key in Label stage
project.export.list_tasks(
    redbrick.TaskFilters.QUEUED, 
    stage_name="Label", 
    user_id=project.context.key_id
    )
```
