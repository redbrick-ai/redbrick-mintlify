# Creating & cloning projects

Almost all CLI operations need to be performed within a _local project_ directory. A local project directory can be created by cloning a RedBrick AI project, or by creating a new project using the CLI.&#x20;

## Creating a new project

To create a new project, first navigate to an empty directory. We recommend _creating a new_ directory, and naming it after your new project.

```bash
$ mkdir my-new-project
$ cd my-new-project
```

Now to create a new project, simply run:&#x20;

```bash
$ redbrick init
> Name: my-new-project
> Taxonomy: my-taxonomy-name
> Reviews: 1
```

You can now verify your current directory is a _local project directory_ by doing:&#x20;

```bash
$ redbrick info
                 Organization                  
╭──────┬──────────────────────────────────────╮
│ ID   │               ...                    │
│ Name │ My Organization                      │
╰──────┴──────────────────────────────────────╯
                                    Project                                     
╭──────────┬───────────────────────────────────────────────────────────────────╮
│ ID       │ ...                                                               │
│ Name     │ my-new-project                                                    │
│ Taxonomy │ my-taxonomy-name                                                  │
│ URL      │ https://app.redbrickai.com/.../projects/.../                      │
╰──────────┴───────────────────────────────────────────────────────────────────╯
```

## Clone an existing project

You can clone an existing project that you (or someone else) created.&#x20;

```bash
$ redbrick clone 
> Project: 
❯ 3/3
❯ my-new-project (...)
  my-first-project (...)
  my-old-project (...)
```

You can directly clone a project using it's project ID.

```bash
$ redbrick clone PROJECTID # replace PROJECTID with your project's ID
```

The project will now be cloned **in a directory named after your project** (within your current working directory).&#x20;
