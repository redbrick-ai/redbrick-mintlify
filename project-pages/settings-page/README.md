# Settings Page

Any Project on RedBrick can be highly customized to support the specifics of your desired workflow.

The Project Settings tabs allow you to adjust your Project's configuration, workflows, export your Project and metadata, execute Bulk Actions, customize your Project toolkit, and much more.

Project Settings are broken down into the following subcategories:

* General Settings
* Consensus (for Consensus Projects)
* Export Labels
* Label Validation Script
* Hanging Protocol
* Direct Uploads
* Export Metadata
* Annotation Storage
* Bulk Actions
* Tool Settings
* Webhooks

You can also quickly navigate to several of these tabs from anywhere within a Project by clicking on the corresponding Settings Shortcut in the top-right corner of the screen.

<figure><img src="../../.gitbook/assets/CleanShot 2024-08-14 at 11.49.20@2x.png" alt=""><figcaption></figcaption></figure>

## General Settings

The General Settings tab contains basic information about your Project and allows you to modify:

* your Project's name, description, and labeling instructions URL;
* your caching settings&#x20;
* your [labeler evaluation](../../projects/labeler-evaluation.md) settings;
* your [Task assignment](../../projects/tasks-and-assignment.md) settings and the size of your [Labeling/Review Queue](../../projects/tasks-and-assignment.md#labeling-queue);
* your Review Stage settings, including your [pseudo-random review percentage](../../quick-start/get-started-with-a-project.md#step-3-define-your-project-workflow);
* control your permissions settings for [Read-only Labels](../../annotation-and-viewer/creating-editing-and-deleting-annotations.md#setting-permissions-for-read-only-labels);

You can also add Review Stages to a Project's workflow. However, this is a permanent action that cannot be undone.

{% hint style="info" %}
**Oops!:** if a Review Stage has been added to your Project in error, you can reduce the review percentage to 0% to allow all Tasks to "pass through" it.
{% endhint %}

***

## Consensus

If you are working inside of a multi-reader Project, you can find Consensus settings in the corresponding tab. For a full overview of how to set up and configure multi-reader Projects on Redbrick, please see the following documentation:

[consensus](../multiple-labeling/consensus/ "mention")

***

## Export Labels

The Export Labels tab contains pre-filled commands to allow you to easily clone your Project to a directory on your local machine and export it.

For a more comprehensive overview of using the CLI to export a RedBrick Project, relevant tags, and common variants, please see our [CLI export documentation](../../python-sdk/cli-overview/exporting-annotations.md#export-annotations-to-a-local-directory-using-the-cli).

***

## Label Validation Script

The Label Validation Script tab allows you to use Javascript to enforce specific labeling behaviors and implement automated QA flows to your Project.&#x20;

A more comprehensive overview and example scripts can be found on the following page:

[custom-label-validation.md](custom-label-validation.md "mention")

***

## Hanging Protocol

Custom hanging protocols can also be added to a Project's configuration to give admins greater control over the default annotation environment, specifically:

* windowing settings;
* the contents of a viewport, including viewing planes, synchronization with other viewports, flipping, etc.;
* Task layout (i.e. the viewport grid, the number of Layout tabs available and their contents, etc.);
* thresholding settings;

[custom-hanging-protocol.md](custom-hanging-protocol.md "mention")

***

## Data Uploads

The Data Uploads tab provides a summary of all of the upload operations that have been carried out within your Project.

{% hint style="danger" %}
If something is erroneously uploaded to your Project, you can "undo" the upload by deleting it in the Data Uploads tab.&#x20;

The delete operation removes all images, labels, and Tasks associated with the upload - use caution!
{% endhint %}

<figure><img src="../../.gitbook/assets/CleanShot 2024-08-14 at 12.19.37@2x.png" alt=""><figcaption><p>Deleting the contents of an upload</p></figcaption></figure>

***

## Export Metadata

{% hint style="warning" %}
As of **v1.1.2**, the Export Metadata tab has been removed and transferred to the Project Data Page (for Comment Exports) and Project Overview Page (Productivity Data Export).
{% endhint %}

#### Comment Exports

You can now export all of a Project's Comments by clicking on the corresponding button on the Project Data Page.

<figure><img src="../../.gitbook/assets/CleanShot 2024-08-30 at 11.07.39@2x.png" alt=""><figcaption></figcaption></figure>

#### Workforce Productivity Export

Productivity data includes each labeler or reviewer's active work time (measured in milliseconds) and the number of Tasks completed per day and can be accessed on the Project's Overview Page.

You can also customize the date range for your export to retrieve more specific data.

<figure><img src="../../.gitbook/assets/CleanShot 2024-08-30 at 11.09.51@2x.png" alt=""><figcaption></figcaption></figure>

***

## Annotation Storage

By default, all annotations generated on RedBrick AI are stored on our servers in NIfTI format.

The Annotation Storage tab allows you designate any Storage Method that you have integrated to the platform and store your annotations there.

<figure><img src="../../.gitbook/assets/CleanShot 2024-08-14 at 12.28.10@2x.png" alt=""><figcaption><p>Selecting a non-RedBrick Storage Method for annotation storage</p></figcaption></figure>

***

## Bulk Actions

The Bulk Actions tab allows you to execute Stage-level operations for your workflow. Common operations include:

* sending all Ground Truth Tasks back to a Label or Review Stage;
* pushing Label Stage Tasks with pre-uploaded annotations to a later Stage;
* accepting or rejecting Tasks that have been pseudo-randomly retained in a Review Stage;

<figure><img src="../../.gitbook/assets/CleanShot 2024-08-14 at 12.29.13@2x.png" alt=""><figcaption><p>The Bulk Actions tab of a Project with a simple workflow</p></figcaption></figure>

Bulk Actions are also reflected in Task History as a **System operation**. For example, if user "Ben Stewart" bulk rejected all Tasks in the Review\_1 Stage, the Task History would display as follows:

<figure><img src="../../.gitbook/assets/CleanShot 2024-08-14 at 12.33.17@2x.png" alt=""><figcaption><p>The Task History of a recently bulk rejected Task</p></figcaption></figure>

***

## Tool Settings

The Tool Settings page allows admins to configure exact scope of the Segmentation toolkit available to labelers and reviewers.&#x20;

For more information about our Segmentation Toolkit and the Tool Settings page, please see the following pages:&#x20;

[segmentation-tools.md](../../annotation-and-viewer/segmentation/segmentation-tools.md "mention")

[#tool-configuration](../../annotation-and-viewer/segmentation/segmentation-tools.md#tool-configuration "mention")

***

## Webhooks

If you'd like to integrate webhooks to your Project, you can do so here.

For a more detailed overview of the available webhooks and how to integrate them, please see the following page:

[webhooks.md](webhooks.md "mention")
