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

    This will create a reproducible virtual environment with all required dependencies, including the `nuremics` core package itself.


3. **Install the demo application.** Each application in `nuremics-labs` can be installed independently. You can start by installing the [DEMO_APP](https://github.com/nuremics/nuremics-labs/tree/main/src/labs/apps/general/DEMO_APP).

    ```bash
    pip install .[DEMO_APP]
    ```

### Run the demo

## Dive into NUREMICS

Ready to go beyond the demo?

Explore the **NUREMICS Handbook** to unlock the full potential of the framework and start building your own scientific software applications:

🔗 [nuremics.github.io](https://nuremics.github.io/)