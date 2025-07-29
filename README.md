<img src="https://raw.githubusercontent.com/nuremics/nuremics.github.io/main/images/banner.jpg" width="100%">
<p align="left">
  <img src="https://img.shields.io/badge/Python-3.12+-ffcd3b?style=flat&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/nuremics-1.0.0-007bff" />
</p>

# NUREMICS® _Labs_

**NUREMICS is an open-source Python framework for developing software-grade scientific workflows.**

🧠 Code like a scientist — build like an engineer.<br>
🧩 Modular workflows — no more tangled scripts.<br>
🧪 Parametric exploration — configuration over code.<br>
💾 Full traceability — everything written to disk.<br>
🛠️ Industrial mindset — R&D speed, software rigor.

## Foreword

The **NUREMICS** project is organized into two complementary repositories:

- [**`nuremics`**](https://github.com/nuremics/nuremics):
This repository is the core Python library. It provides the foundational components to create modular and extensible software workflows.

- **`nuremics-labs`** _(current repository)_:
This repository contains examples of end-user applications built using the **NUREMICS** framework. It is intended to be **forked** by developers to initiate their own `nuremics-labs` project and build custom scientific applications tailored to their specific use cases.

Developers are thus encouraged to treat `nuremics` as the core engine, and to use `nuremics-labs` as a starting point for developing and maintaining their own scientific software applications built on top of the **NUREMICS** framework.

## Getting Started

### Installation

1. **Fork and clone the `nuremics-labs` repository.** You have two options to get started:
    
    - Option A (recommended): Fork the repo to your own GitHub or GitLab account, then clone your fork. This allows you to modify the code and push your changes to your personal version of the project.

        ```bash
            nuremics-labs  →  fork  →  your-labs  →  clone
        ```
    
    - Option B (quick start): If you just want to try the framework without making changes, you can simply clone the main repo directly.

2. **Create the NUREMICS virtual environment.** From the root directory of your cloned repo, use either conda or micromamba to create and install the environment using the provided `environment.yml` file.

    <details>
    <summary><strong>Using Conda</strong></summary>

    ```bash
    conda create -f environment.yml
    ```
    ```bash
    conda activate nrs-env
    ```

    </details>

    <details>
    <summary><strong>Using Micromamba</strong></summary>

    ```bash
    micromamba create -f environment.yml
    ```
    ```bash
    micromamba activate nrs-env
    ```

    </details>


3. **Install the demo application.** Each application in `nuremics-labs` can be installed independently. You can start by installing the [`DEMO_APP`](https://github.com/nuremics/nuremics-labs/tree/main/src/labs/apps/general/DEMO_APP).

    ```bash
    pip install .[DEMO_APP]
    ```

    This will install both the core `nuremics` framework and the `nuremics-labs` demo application.

### Run the demo

To get hands-on experience with the **NUREMICS** framework, you'll start by running the `DEMO_APP` and reproducing the scientific results of the `Study_Shape` and `Study_Velocity` studies, as demonstrated in the video below.

▶️ [Watch video](https://youtu.be/HyUkWXGqEIM)

When first run, a **NUREMICS App** creates a local workspace on your system, where you configure studies, set input data, and collect results. In this tutorial, instead of setting up from scratch, you'll start with a preconfigured folder to reproduce the `Study_Shape` and `Study_Velocity` studies.

Follow these steps:

1. **Download the NUREMICS working directory.** Get the preconfigured `nrs_working_dir` archive, unzip it, and place it anywhere on your system.

    📦 [Download NUREMICS working directory](assets/nrs_working_dir.zip)

2. **Download the `.nuremics` directory.** This folder contains `settings.json`, the central config file for all your **Apps**. Unzip it at the root of your forked/cloned `nuremics-labs` repo.

    📦 [Download .nuremics](assets/nrs_working_dir.zip)

3. **Set the working directory for `DEMO_APP`**. Edit the `"working_dir"` field in `.nuremics/settings.json` and set the full path to your local `nrs_working_dir`.

    <details>
    <summary><strong>📄 nuremics-labs/.nuremics/settings.json</strong></summary>
    
    ```json
    {
        "default_working_dir": null,
        "apps": [
            {
                "id": 0,
                "name": "DEMO_APP",
            >>> "working_dir": "path/to/nrs_working_dir", <<<
                "studies": [
                    "Study_Shape",
                    "Study_Velocity"
                ]
            }
        ]
    }
    ```
    </details>

4. **Run the `DEMO_APP`**. From the `nuremics-labs/src/labs/apps/general/DEMO_APP` folder, run the **App**.

    ```python
    python src/labs/apps/general/DEMO_APP/system.py
    ```

    This will launch both studies and store results in `nrs_working_dir/DEMO_APP`.

### Play with it

Now that you've successfully run the `DEMO_APP` and reproduced the scientific results of the `Study_Shape` and `Study_Velocity` studies, let's play with it!

#### Skip a study

Want to skip the execution of a specific study when running your **App**? Set its `"execute"` field to `false` in the `studies.json` file.

<details>
<summary><strong>📄 nrs_working_dir/DEMO_APP/studies.json</strong></summary>

```json
{
    "Study_Shape": {
    >>> "execute": false, <<<
        "..."
    },
    "Study_Velocity": {
        "execute": true,
        "..."
    }
}
```
</details>

#### Skip a process

Want to skip the execution of a specific process (**Proc**) within a study? Set its `"execute"` field to `false` in the `process.json` file.

<details>
<summary><strong>📄 nrs_working_dir/DEMO_APP/Study_Velocity/process.json</strong></summary>

```json
{
    "PolygonGeometryProc": {
    >>> "execute": false, <<<
        "silent": false
    },
    "ProjectileModelProc": {
        "execute": true,
        "silent": false
    },
    "TrajectoryAnalysisProc": {
        "execute": true,
        "silent": false
    }
}
```
</details>

#### Silent a process

Want a specific process (**Proc**) to be executed in silent mode within a study? Set its `"silent"` field to `true` in the `process.json` file.

<details>
<summary><strong>📄 nrs_working_dir/DEMO_APP/Study_Velocity/process.json</strong></summary>

```json
{
    "PolygonGeometryProc": {
        "execute": false,
        "silent": false
    },
    "ProjectileModelProc": {
        "execute": true,
    >>> "silent": true <<<
    },
    "TrajectoryAnalysisProc": {
        "execute": true,
        "silent": false
    }
}
```
</details>

#### Skip an experiment

Want to skip the execution of a specific experiment in a study? Set the value of the `EXECUTE` flag to `0` in the `inputs.csv` file for the experiment you want to skip.

<details>
<summary><strong>📄 nrs_working_dir/DEMO_APP/Study_Velocity/inputs.csv</strong></summary>

```csv
ID,EXECUTE
Test1,1
Test2,0 🔴
Test3,1
```
</details>

#### Run a new experiment

Want to run a new experiment in a study? Add a new line with a unique `ID` to the `inputs.csv` file.

<details>
<summary><strong>📄 nrs_working_dir/DEMO_APP/Study_Velocity/inputs.csv</strong></summary>

```csv
ID,EXECUTE
Test1,1
Test2,0
Test3,1
MyExp,1 🔴
```
</details>

Then run the **App**, which will automatically generate the corresponding input folder where you must upload the required `velocity.json` file.

<details>
<summary><code>📄 nrs_working_dir/DEMO_APP/Study_Velocity/0_inputs/0_datasets/MyExp/velocity.json</code></summary>

```json
{
    "v0": 15.0,
    "angle": 60.0
}
```
</details>

## Dive into NUREMICS

Ready to go beyond the demo?

Explore the **NUREMICS Handbook** to unlock the full potential of the framework and start building your own scientific software applications:

🔗 [nuremics.github.io](https://nuremics.github.io/)