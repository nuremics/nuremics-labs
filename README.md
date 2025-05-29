<img src="https://raw.githubusercontent.com/julien-siguenza/nuremics-data/main/assets/banner.jpg" alt="NUREMICS Banner" width="100%">

# NUREMICS® Apps

**NUREMICS®** is an open-source Python™ framework for developing customizable scientific workflows.

## Foreword

The **NUREMICS®** project is organized into two complementary repositories:

- **`nuremics`**:
This repository is the core Python library, installable via `pip install`. It provides the foundational components to create modular and extensible software workflows.

- **`nuremics-apps`** _(current repository)_:
This repository contains examples of end-user applications built using the **NUREMICS®** framework. It is intended to be **forked** by developers to initiate their own `nuremics-apps` project and build custom applications tailored to their specific use cases.

Readers are invited to begin their exploration of the **NUREMICS®** project with the [`nuremics`](https://github.com/nuremics/nuremics) repository, to understand the core framework and its foundational concepts. Once you're familiar with the underlying logic, this `nuremics-apps` repository will guide you deeper into the code, showing how to develop your own **NUREMICS®** applications, and operate them both as a developer and as an end-user.

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

3. **Set the environment variable.** Make sure to add the root directory where you cloned the `nuremics-apps` repository to the `PYTHONPATH` environment variable of your local system. If `PYTHONPATH` does not already exist, please create it. This allows Python to locate all project modules correctly.

```bash
/absolute/path/to/nuremics-apps
```

You're now ready to begin your coding journey with **NUREMICS®** 🧬

## Create App

This section walks you through the process of building a custom **NUREMICS®** application from scratch. You'll start by implementing your own **Procs**, which encapsulate domain-specific logic and computational tasks. Then, you’ll learn how to assemble these building blocks into a fully operational **App**, ready to run studies and generate structured results.

Whether you're developing a quick prototype or a full-scale scientific workflow, this guide will help you translate your ideas into modular, reusable, traceable and scalable software components.

### Code Procs

We start by defining the core building blocks of the **App** to be created: the **Procs**. Each **Proc** is a reusable item that encapsulates a specific piece of logic executed within the overall workflow. Internally, this logic can be further decomposed into elementary operations, implemented as individual functions (units) within the **Proc** itself.

To implement our first **Proc**, we begin by importing the `Process` base class from **NUREMICS®**, which all custom **Procs** must inherit from. To make this inheritance simple and structured, we also import the `attrs` library, which helps define clean, data-driven Python classes.

```python
import attrs
from nuremics import Process
```

We then declare our first **Proc** as a Python class named `OneProc`, inheriting from the `Process` base class. This marks it as a modular item of computation which can be executed within a **NUREMICS®** workflow.

```python
import attrs
from nuremics import Process

@attrs.define
class OneProc(Process):
```

We now declare the input data required by our `OneProc`, grouped into two categories: **Parameters** and **Paths**. Each input is defined using `attrs.field()` and marked with `metadata={"input": True}`. This metadata is essential: it tells the **NUREMICS®** framework that these attributes are expected as input data, ensuring they are properly tracked and managed throughout the workflow.

```python
import attrs
from pathlib import Path
from nuremics import Process

@attrs.define
class OneProc(Process):

    # Parameters
    param1: float = attrs.field(init=False, metadata={"input": True})
    param2: int = attrs.field(init=False, metadata={"input": True})
    param3: bool = attrs.field(init=False, metadata={"input": True})
    
    # Paths
    path1: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)
```

In addition to the previously declared input data, a **Proc** can also define internal variables: attributes used during the execution of its internal logic but not provided as input data. These internal variables, like `variable` in our example below, are declared without the `metadata={"input": True}` tag, signaling to the **NUREMICS®** framework that they are not exposed to the workflow and will be set or computed within the **Proc** itself.

```python
import attrs
from pathlib import Path
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
```

The operations executed by the **Proc** are finally implemented as elementary functions, which are then sequentially called within the `__call__()` method to define the overall logic of the **Proc**.

```python
import attrs
from pathlib import Path
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

Note that the **Proc** should at some point produce output data, typically in the form of files or folders generated during the execution of its operations. To make these output data trackable by the **NUREMICS®** framework, each must be registered in the `self.output_paths` dictionary using a label that is unique to the **Proc** (e.g., `"out1"`). Using the dictionary syntax `self.output_paths["out1"]` effectively declares an output variable named `out1`, which will later be instantiated by assigning it a specific file or folder name when integrating the **Proc** into a broader application workflow.

```python
import attrs
from pathlib import Path
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
        file = self.output_paths["out1"]
        # </> Write file </>
```

Even though **Procs** are not intended to be executed independently by end-users, they are still designed with the possibility to run _out of the box_. This allows developers to easily execute them during the development phase or when implementing dedicated unit tests for a specific **Proc**. In such cases, it is important to set `set_inputs=True` when instantiating the **Proc**, to explicitly inform the **NUREMICS®** framework that the input data are being provided manually, outside of any workflow context.

```python
import os
import attrs
from pathlib import Path
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
        file = self.output_paths["out1"]
        # </> Write file </>

if __name__ == "__main__":
    
    # Define working directory
    working_dir = ...

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "param1": ...,
        "param2": ...,
        "param3": ...,
        "path1": ...,
    }
    
    # Create process
    process = OneProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )
    process.output_paths["out1"] = "output1.txt"

    # Run process
    process()
    process.finalize()
```

**Note:** The complete implementation of the `OneProc` **Proc**, as well as that of the `AnotherProc` **Proc** later used in this tutorial, can be found in the repository under `procs/OneProc/item.py` and `procs/AnotherProc/item.py`, respectively.

### Assemble Procs into App

Most of the development effort has already been carried out when implementing the individual **Procs**. The next step consists in assembling them into a coherent **App**, where each **Proc** is instantiated, connected, and orchestrated to form a complete, executable workflow.

We start by defining the name of our **App**.

```python
APP_NAME = "ONE_APP"
```

We then import the `Application` class from the **NUREMICS®** framework, which serves as the container and manager to define a workflow composed of multiple **Procs**.

```python
APP_NAME = "ONE_APP"

from nuremics import Application
```

We now import the two **Procs**, `OneProc` and `AnotherProc`, that we previously implemented. These will be the building blocks to assemble into our final **App**.

```python
APP_NAME = "ONE_APP"

from nuremics import Application

from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc
```

The source code of the **App** then adopts the structure of a standard Python script, which can both be executed directly or imported as a module. This is achieved by defining a `main()` function and guarding it with the typical `if __name__ == "__main__":` statement.

```python
APP_NAME = "ONE_APP"

from nuremics import Application

from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc

def main():
    # Application logic here

if __name__ == "__main__":
    main()
```

```bash
> APPLICATION <

| Workflow |
MY_APP_____
           |_____OneProc_____
                             |_____operation1
                             |_____operation2
                             |_____operation3
                             |_____operation4
```

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