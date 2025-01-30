# Webhooks

Webhooks allow you to receive an HTTP push notification triggered by certain events within a project. Currently, webhooks are triggered by the following events:&#x20;

1. **Task created**: When a data point is uploaded, and a task is created from that data point.&#x20;
2. **Task entered stage**: When a task enters a new stage in the labeling workflow.
3. **Task deleted**: When a task is deleted.

{% tabs %}
{% tab title="Task created" %}
```json
{
  "version": "v1.0",
  "events": 1,
  "payload": [
    {
      "event": "TASK_CREATED",
      "id": "...",
      "timestamp": ...,
      "data": {
        "orgId": "...",
        "projectId": "...",
        "taskId": "...",
        "taskName": "...",
        "updatedBy": "..."
      }
    }
  ]
}
```
{% endtab %}

{% tab title="Task entered stage" %}
```json
{
  "version": "v1.0",
  "events": 1,
  "payload": [
    {
      "event": "TASK_ENTERED_STAGE",
      "id": "...",
      "timestamp": ...,
      "data": {
        "orgId": "...",
        "projectId": "...",
        "taskId": "...",
        "stageName": "...",
        "updatedBy": "..."
      }
    }
  ]
}
```
{% endtab %}

{% tab title="Task deleted" %}
```
{
  "version": "v1.0",
  "events": 1,
  "payload": [
    {
      "event": "TASK_DELETED",
      "id": "...",
      "timestamp": ...,
      "data": {
        "orgId": "...",
        "projectId": "...",
        "taskId": "...",
        "taskName": "...",
        "updatedBy": "..."
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

## Using webhooks

Configure webhook from project settings, as shown in the image below.&#x20;

<figure><img src="../../.gitbook/assets/RedBrick AI 2024-04-22 at 11.05.15@2x.png" alt=""><figcaption></figcaption></figure>

You can use tools like [https://webhook.site/](https://webhook.site/#!/view/8df76e5a-9a58-4394-8c65-854d305bb5be) to test the webhook and inspect the response format.&#x20;
