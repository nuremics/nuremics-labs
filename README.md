<img src="https://raw.githubusercontent.com/julien-siguenza/nuremics-data/main/assets/banner.jpg" alt="NUREMICS Banner" width="100%">

# NUREMICS® apps

**NUREMICS®** is an open-source Python™ framework for developing customizable scientific workflows.

## Foreword

The **NUREMICS®** project is organized into two complementary repositories:

- **`nuremics`**:
This repository is the core Python library, installable via `pip install`. It provides the foundational components to create modular and extensible software workflows.

- **`nuremics-apps`** _(current repository)_:
This repository contains examples of end-user applications built using the **NUREMICS®** framework. It is intended to be **forked** by developers to initiate their own `nuremics-apps` project and build custom applications tailored to their specific use cases.

Readers are invited to begin their exploration of the **NUREMICS®** project with the [`nuremics`](https://github.com/nuremics/nuremics) repository, to understand the core framework and its foundational concepts. Once you're familiar with the underlying logic, this `nuremics-apps` repository will guide you deeper into the code, showing how to implement your own **process items**, assemble them into full **applications**, and operate them both as a developer and as an end-user.

## Installation

Once the present `nuremics-apps` repository has been forked and cloned to your local machine, installation proceeds as follows:

1. **(Recommended)** Create a dedicated coding environment. While not mandatory, using [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) is highly recommended for fast, reproducible, and lightweight environment management:

```bash
micromamba create -n nrs-env python=3.12
micromamba activate nrs-env
```

2. **Install the required dependencies.** Use `pip` to install the packages listed in the `requirements.txt` file. If you need additional packages to support domain-specific application development, remember to add them to this file before running the command:

```bash
pip install -r requirements.txt
```

You're now ready to begin your coding journey with **NUREMICS®** 🧬

<!---
```bash
output/
├── process_item_1/
    ├── Test1/
    ├── Test2/
    └── ...
├── process_item_2/
    ├── Test1/
    ├── Test2/
    └── ...
```
--->