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
    
    - Option A (recommended): Fork the repository to your own GitHub or GitLab account, then clone your fork. This allows you to modify the code and push your changes to your personal version of the project.

        ```bash
            nuremics-labs  →  fork  →  your-labs  →  clone
        ```
    
    - Option B (quick start): If you just want to try the framework without making changes, you can simply clone the main repository directly.

2. **Create the NUREMICS virtual environment.** From the root directory of your cloned repository, use either conda or micromamba to create and install the environment using the provided `environment.yml` file.

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

The essence of the **NUREMICS** framework is to enable the development of scientific software applications that generate reproducible scientific outcomes.

To get hands-on experience, you'll start by running the `DEMO_APP` and reproduce the scientific results of the `Study_Shape` and `Study_Velocity` studies, as presented in the video below.

▶️ [Watch Video](https://youtu.be/HyUkWXGqEIM)

When you run a **NUREMICS App** for the first time, the **NUREMICS** framework generates a local folder on your system. This folder becomes the workspace of your application, where you configure your studies, set the input data for the experiments you want to run, and collect the resulting output data.

In this tutorial, you won't start `DEMO_APP` from scratch. Instead, you'll begin with a preconfigured folder that already contains the input data required to reproduce the `Study_Shape` and `Study_Velocity` studies. 

Here are the steps to follow in order to reproduce these scientific studies with the `DEMO_APP`:

1. **Download the NUREMICS working directory.** You’ll receive it as a compressed `nrs_working_dir` archive which contains the preconfigured `DEMO_APP` folder. Unzip it and place it anywhere you want on your system.

    📦 [Download NUREMICS working directory](assets/nrs_working_dir.zip)

2. **Download the `.nuremics` directory.** This special folder contains the `settings.json` file, which acts as the central manager for all your **NUREMICS Apps**. Unzip it and place it at the root of your forked/cloned `nuremics-labs` repository.

    📦 [Download .nuremics directory](assets/nrs_working_dir.zip)

3. **Set the working directory for `DEMO_APP`**. You now need to tell **NUREMICS** where to find the `nrs_working_dir` folder on your system, from which the `DEMO_APP` will be executed. This is done by editing the `settings.json` file (downloaded in step 2). Update the `working_dir` field with the full path to your local `nrs_working_dir` folder.

    📄 `nuremics-labs/.nuremics/settings.json`
    ```json hl_lines="7"
    {
        "default_working_dir": null,
        "apps": [
            {
                "id": 0,
                "name": "DEMO_APP",
                "working_dir": "path/to/nrs_working_dir",
                "studies": [
                    "Study_Shape",
                    "Study_Velocity"
                ]
            }
        ]
    }
    ```

4. **Run the `DEMO_APP`**. The source code of the `DEMO_APP` is in the `nuremics-labs/src/labs/apps/general/DEMO_APP` directory. Inside this folder, you'll find a `system.py` file, which is the main entry point of the **App**. You can run it directly to launch the `Study_Shape` and `Study_Velocity` studies that were preconfigured in the `DEMO_APP` working directory.

    ```python
    python src/labs/apps/general/DEMO_APP/system.py
    ```

    As the execution proceeds, output data will be generated and stored inside the `nrs_working_dir/DEMO_APP` working directory.

## Dive into NUREMICS

Ready to go beyond the demo?

Explore the **NUREMICS Handbook** to unlock the full potential of the framework and start building your own scientific software applications:

🔗 [nuremics.github.io](https://nuremics.github.io/)