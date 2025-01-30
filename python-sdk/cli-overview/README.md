# CLI Overview

The RedBrick AI Command Line Interface is a package that allows developers to interact with the RedBrick AI application programmatically.

We recommend you use the CLI for most regular import & export actions. If you want to write Python scripts to perform these actions, or you are interested in more advanced scripting, [please use our Python SDK](../sdk-overview/).

This documentation covers high-level guides and usecases. If you are interested in more detailed documentation of the CLI interface, please [visit the full CLI reference documentation](https://redbrick-sdk.readthedocs.io/en/stable/cli.html).

## Configure your CLI credentials

Once you have [installed the CLI](../installation-and-api-keys.md), you need to configure your credentials.&#x20;

<pre class="language-bash"><code class="lang-bash"><strong>$ redbrick config
</strong>> Org ID: ...
> API KEY: ...
> URL: https://api.redbrickai.com
> Profile name: ...
✔ RedBrick AI Organization
</code></pre>

{% hint style="info" %}
The URL should default to [https://api.redbrickai.com](https://api.redbrickai.com). If you are using a private/single-tenant deployment of RedBrick AI, this will need to be changed for your deployment - reach out to us for confirmation on what the URL needs to be.
{% endhint %}

For most scenarios, you will only need a single credentials profile. However, if you want to create multiple profiles (perhaps for different organizations), you can do it in the following way:&#x20;

```bash
$ redbrick config add
```

To change your profile:

```bash
$ redbrick config set
```
