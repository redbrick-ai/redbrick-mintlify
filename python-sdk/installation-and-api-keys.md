# Installation & API Keys

## Installation

The RedBrick AI SDK and CLI are available on [PyPI](https://pypi.org/project/redbrick-sdk/) and can be installed using `pip`. The SDK and CLI are packaged together.&#x20;

```bash
$ pip install -U redbrick-sdk
```

{% hint style="info" %}
The SDK and CLI work on Mac, Windows, and Linux.

They are compatible with **python version 3.8+**
{% endhint %}

## API Keys

In order to use the Python SDK or CLI, you'll first need to generate an API key. To do so:

1. Click on **Integrations** (or use the "i" shortcut)
2. Click on **API Keys** (or use the "2" shortcut)
3. In the top right corner, click on **Create API Key**
4. In the pop-up field, give your API key a name

<figure><img src="../.gitbook/assets/CleanShot 2025-01-07 at 12.18.08.png" alt=""><figcaption><p>The Integrations tab</p></figcaption></figure>

<figure><img src="../.gitbook/assets/CleanShot 2025-01-07 at 12.19.48.png" alt=""><figcaption><p>The API Keys page</p></figcaption></figure>

After you've generated your API key, you can copy it to wherever is necessary - your CLI credentials file, your Python file, etc.

**Please note** that all API keys provide the user with the equivalent of [Org Admin permissions](../organizations/what-is-an-organization.md#organization-level-roles). Be sure to use your API keys with care!

## Organization and Project IDs

For most SDK / CLI operations, you will need your Organization and/or Project ids. These are unique ids for each entity. You can find both the Organization and Project ID inside the **Settings Page of any Project**.&#x20;

You can also find the Organization and Project IDs within the browser URL -> head over to any project - https://app.redbrickai.com/\<org\_id>/projects/\<project\_id>.

<figure><img src="../.gitbook/assets/CleanShot 2023-12-23 at 13.07.35@2x.png" alt=""><figcaption></figcaption></figure>
