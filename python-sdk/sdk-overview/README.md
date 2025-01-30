# SDK Overview

The RedBrick AI Python SDK is a Python package that allows developers to interact with the RedBrick AI application programmatically.&#x20;

We recommend you use the Python SDK if you want to:

* Build data pipelines with Python and want to integrate your RedBrick AI annotation;
* Write advanced scripts beyond simple import & export;
* Take advantage of certain features such as [HTML Tooltips](https://docs.redbrickai.com/projects/taxonomies#html-tooltips), [Series and/or Task Level Metadata](https://docs.redbrickai.com/python-sdk/formats/full-format-reference#items-list-and-tasks.json), or [Taxonomy Nesting](https://docs.redbrickai.com/projects/taxonomies#nested-taxonomies);

For simple data import and annotation export, we [recommend you use the CLI](../cli-overview/), which has a simple interface with optimizations for basic use cases.&#x20;

{% content-ref url="../cli-overview/" %}
[cli-overview](../cli-overview/)
{% endcontent-ref %}

This SDK documentation is intended to cover high-level guides and use cases. If you are interested in more detailed documentation of the SDK interface, [please visit the full SDK reference documentation](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html).

## **Initializing the RedBrick SDK in Python**

Nearly all operations with the SDK are performed on either the [Project](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.project.RBProject) or [Organization](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.organization.RBOrganization) objects. You can instantiate these objects using your [API Key, Org ID, and Project ID](../installation-and-api-keys.md).&#x20;

```python
import redbrick

project = redbrick.get_project(
    org_id="...",
    project_id="...",
    api_key="...",
)
organization = redbrick.get_org(
    org_id="...", 
    api_key="...",
)
```

{% hint style="info" %}
Both [redbrick.get\_project](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.get\_project) and [redbrick.get\_org](https://redbrick-sdk.readthedocs.io/en/stable/sdk.html#redbrick.get\_org) take an optional `url` argument that defaults to [https://api.redbrickai.com](https://api.redbrickai.com). \
\
If you are using a private/single-tenant deployment of RedBrick AI, this will need to be changed for your deployment - reach out to us for confirmation of what your case-specific URL needs to be.
{% endhint %}
