<img src="https://raw.githubusercontent.com/julien-siguenza/nuremics-data/main/assets/banner.jpg" alt="NUREMICS Banner" width="100%">

# NUREMICS® apps

**NUREMICS®** is an open-source Python™ framework for developing customizable scientific workflows.

## Foreword

The **NUREMICS®** project is organized into two complementary repositories:

- **`nuremics`**:
This repository is the core Python library, installable via `pip install`. It provides the foundational components to create modular and extensible software workflows.

- **`nuremics-apps`** _(current repository)_:
This repository contains examples of end-user applications built using the **NUREMICS®** framework. It is intended to be **forked** by developers to initiate their own `nuremics-apps` project and build custom applications tailored to their specific use cases.

Readers are invited to begin their exploration of the **NUREMICS®** project with the [`nuremics`](https://github.com/nuremics/nuremics) repository, to understand the core framework and its foundational concepts. Once you're familiar with the underlying logic, this `nuremics-apps` repository will guide you deeper into the code, showing how to implement your own **Procs**, assemble them into full **Apps**, and operate them both as a developer and as an end-user.

## Installation

Once the present `nuremics-apps` repository has been forked and cloned to your local machine, installation proceeds as follows:

1. **(Recommended) Create a dedicated coding environment.** While not mandatory, using [micromamba](https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html) is highly recommended for fast, reproducible, and lightweight environment management:

```bash
micromamba create -n nrs-env python=3.12
micromamba activate nrs-env
```

2. **Install the required dependencies.** Use `pip` to install the packages listed in the `requirements.txt` file. If you need additional packages to support domain-specific application development, remember to add them to this file before running the command:

```bash
pip install -r requirements.txt
```

You're now ready to begin your coding journey with **NUREMICS®** 🧬

## Create App

This section walks you through the process of building a custom **NUREMICS®** application from scratch. You'll start by implementing your own **Procs**, which encapsulate domain-specific logic and computational tasks. Then, you’ll learn how to assemble these building blocks into a fully operational **App**, ready to run studies and generate structured results.

Whether you're developing a quick prototype or a full-scale scientific workflow, this guide will help you translate your ideas into modular, reusable, traceable and scalable software components.

### Code Procs

```python
import attrs
from nuremics import Process

@attrs.define
class OneProc(Process):

    # Parameters
    param1: float = attrs.field(init=False, metadata={"input": True})
    param2: int = attrs.field(init=False, metadata={"input": True})
    param3: bool = attrs.field(init=False, metadata={"input": True})
    
    # Paths
    path1: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

    # Internal
    variable: float = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation1()
        self.operation2()
        self.operation3()
        self.operation4()
    
    def operation1(self):
        # </> your code </>

    def operation2(self):
        # </> your code </>

    def operation3(self):
        # </> your code </>

    def operation4(self):
        # </> your code </>
```

### Assemble Procs into App

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