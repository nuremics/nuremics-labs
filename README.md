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

4. **(Optional) Define a default working directory.** It is also suggested to define another environment variable named `WORKING_DIR`, which serves as the default root folder where all your **Apps** write their results. This becomes particularly useful when working on multiple **Apps**, as it allows you to consistently manage output locations across your projects.

```bash
/absolute/path/to/default/working_dir
```

You're now ready to begin your coding journey with **NUREMICS®** 🧬

## Create App

This section walks you through the process of building a custom **NUREMICS®** application from scratch. You'll start by implementing your own **Procs**, which encapsulate domain-specific logic and computational tasks. Then, you’ll learn how to assemble these building blocks into a fully operational **App**, ready to run studies and generate structured results.

Whether you're developing a quick prototype or a full-scale scientific workflow, this guide will help you translate your ideas into modular, reusable, traceable and scalable software components.

### Implement Procs

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

We now declare the input data required by our `OneProc`, grouped into two categories: **Parameters** and **Paths**. Each input is defined using `attrs.field()` and marked with `metadata={"input": True}`.

This metadata is essential: it tells the **NUREMICS®** framework that these attributes are expected as input data, ensuring they are properly tracked and managed throughout the workflow.

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

In addition to the previously declared input data, a **Proc** can also define internal variables: attributes used during the execution of its internal logic but not provided as input data.

These internal variables, like `variable` in our example below, are declared without the `metadata={"input": True}` tag, signaling to the **NUREMICS®** framework that they are not exposed to the workflow and will be set or computed within the **Proc** itself.

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

Note that the **Proc** should at some point produce output data, typically in the form of files or folders generated during the execution of its operations. To make these output data trackable by the **NUREMICS®** framework, each must be registered in the `self.output_paths` dictionary using a label that is unique to the **Proc** (e.g., `"out1"`).

Using the dictionary syntax `self.output_paths["out1"]` effectively declares an output variable named `out1`, which will later be instantiated by assigning it a specific file or folder name when integrating the **Proc** into a broader application workflow.

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

Even though **Procs** are not intended to be executed independently by end-users, they are still designed with the possibility to run _out of the box_. This allows developers to easily execute them during the development phase or when implementing dedicated unit tests for a specific **Proc**.

In such cases, it is important to set `set_inputs=True` when instantiating the **Proc**, to explicitly inform the **NUREMICS®** framework that the input data are being provided manually, outside of any workflow context.

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

In the `main()` function, we add two input arguments that the end-user must specify when launching the **App** inside the `if __name__ == "__main__":` block:

- `working_dir`: the working directory from which the **App** will be executed.

- `studies`: a list of study names that the end-user wants to perform with the **App**.

```python
APP_NAME = "ONE_APP"

from pathlib import Path
from nuremics import Application
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc

def main(
    working_dir: Path = None,
    studies: list = ["Default"],
):
    # Application logic here

if __name__ == "__main__":

    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    working_dir = Path(...)

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

    # --------------- #
    # Run application #
    # --------------- #
    main(
        working_dir=working_dir,
        studies=studies,
    )
```

Inside the `main()` function, we define a list called `workflow` which contains the sequence of **Procs** to be executed, in the order specified. This list is made up of dictionaries, where each dictionary describes the characteristics of a particular **Proc**.

Let's first define the key `"process"` of each dictionary, which specifies the **Proc** class (previously imported, e.g., `OneProc` and `AnotherProc`) to instantiate and execute within the **App** workflow.

This dictionary-based structure offers flexibility to easily add more parameters or options later by simply adding new keys to each dictionary in the workflow.

```python
APP_NAME = "ONE_APP"

from pathlib import Path
from nuremics import Application
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc

def main(
    working_dir: Path = None,
    studies: list = ["Default"],
):
    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": OneProc,
        },
        {
            "process": AnotherProc,
        },
    ]

if __name__ == "__main__":

    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    working_dir = Path(...)

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

    # --------------- #
    # Run application #
    # --------------- #
    main(
        working_dir=working_dir,
        studies=studies,
    )
```

We now create an `Application` object `app`, which acts as the core engine of our **App**. This object is instantiated using the previously defined inputs:

- `app_name`: the name of the **App**.

- `working_dir`: the root directory from which the **App** is executed.

- `workflow`: the ordered list of **Procs** to run.

- `studies`: the list of studies the end-user wishes to perform.

Once the `Application` object is created, calling `app()` launches the workflow execution of all the defined **Procs** for each study.

```python
APP_NAME = "ONE_APP"

from pathlib import Path
from nuremics import Application
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc

def main(
    working_dir: Path = None,
    studies: list = ["Default"],
):
    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": OneProc,
        },
        {
            "process": AnotherProc,
        },
    ]

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_name=APP_NAME,
        working_dir=working_dir,
        workflow=workflow,
        studies=studies,
    )
    # Run it!
    app()

if __name__ == "__main__":

    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    working_dir = Path(...)

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

    # --------------- #
    # Run application #
    # --------------- #
    main(
        working_dir=working_dir,
        studies=studies,
    )
```

When running the **App**, **NUREMICS®** first provides the following terminal feedback:

- A visual banner indicating the launch of a **NUREMICS® App**.

- A structured overview of the assembled workflow, showing each registered **Proc**, its associated operations (functions), and their order of execution within the **App** workflow.

```shell
                                                              0000000000000000000000
                                      000                  00000000000000000000000000
                                       00000            0000000000000000000000000000000
                                        000000        0000000000000000000000000000000000
                                        0000000      00000000000000000000000000000000000
                                         0000000    000000000000000000000000000000000000
                                         0000000    0000000000000000000000000000000000000
                                         000000  00  00000000000000000000000000000000000
                                        000000  0000  0000000000000000000000000000000000
                                        000000  0000  0000000000000000000000000000000000
                                       000000  000000  00000000000000000000000000000000
                                      0000000  000000  000000000000000000000000000000
                                    00000000  00000000 0000000000000000000000000000
                                  0000000000  00000000  000000000000000000000000
                               0000000000000  00000000  00000000000000
                    000000000000000000000000  00000000  0000000000
                 000000000000000000000000000  00000000  00000000
               000000000000000000000000000000  000000  0000000
              0000000000000000000000000000000  000000  000000
             000000000000000000000000000000000  0000  000000
            0000000000000000000000000000000000  0000  000000
            00000000000000000000000000000000000  00  000000
           0000000000000000000000000000000000000    0000000
           00000000000000000000000000000000000000  00000000
            00000000000000000000000000000000000      0000000
            0000000000000000000000000000000000        000000
             0000000000000000000000000000000            00000
              000000000000000000000000000                  000
                00000000000000000000000                      0
                   000000000000000

> APPLICATION <

| Workflow |
ONE_APP_____
            |_____OneProc_____
            |                 |_____operation1
            |                 |_____operation2
            |                 |_____operation3
            |                 |_____operation4
            |
            |_____AnotherProc_____
                                  |_____operation1
                                  |_____operation2
                                  |_____operation3
```

At this stage, **NUREMICS®** also performs a structural check of each **Proc** by inspecting its `__call__` method. Specifically, it ensures that only functions defined within the **Proc** class itself are invoked during execution.

This design choice enforces a clean and self-contained structure for each **Proc**, where all internal logic remains encapsulated.

Let’s consider a case where the developer does not adhere to this enforced structural rule, for instance, by injecting additional logic directly into the `__call__` method of a **Proc** (in this example, in the `AnotherProc` class).

```python
    def __call__(self):
        super().__call__()

        some_parameter = 2 # <-- External logic added here

        self.operation1()
        self.operation2()
        self.operation3()
```

In this situation, **NUREMICS®** will immediately raise a structural validation error and halt execution.

```shell
| Workflow |
ONE_APP_____
            |_____OneProc_____
            |                 |_____operation1
            |                 |_____operation2
            |                 |_____operation3
            |                 |_____operation4
            |
            |_____AnotherProc_____(X)

(X) Each process must only call its internal function(s):

    def __call__(self):
        super().__call__()

        self.operation1()
        self.operation2()
        self.operation3()
        ...
```

**NUREMICS®** is then expected to display a summary of all required input/output data for each **Proc**, along with their current mapping status within the **App**.

At this stage, the system automatically verifies whether every required input/output data has been properly mapped within the **App** configuration.

If any **input parameters** are missing, they are explicitly listed, and the developer is prompted to define them using either the `"user_params"` or `"hard_params"` key.

```shell
| OneProc |
> Input Parameter(s) :
(float) param1 -----||----- Not defined (X)
(int)   param2 -----||----- Not defined (X)
(bool)  param3 -----||----- Not defined (X)

(X) Please define all input parameters either in "user_params" or "hard_params".
```

The **input parameters** of the **Proc** `OneProc` can be properly mapped within the **App** by defining the `"user_params"` and/or `"hard_params"` keys in its corresponding dictionary entry inside the `workflow` list.

```python
APP_NAME = "ONE_APP"

from pathlib import Path
from nuremics import Application
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc

def main(
    working_dir: Path = None,
    studies: list = ["Default"],
):
    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": OneProc,
            "user_params": {
                "param1": "parameter1",
                "param3": "parameter2",
            },
            "hard_params": {
                "param2": 14,
            },
        },
        {
            "process": AnotherProc,
        },
    ]

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_name=APP_NAME,
        working_dir=working_dir,
        workflow=workflow,
        studies=studies,
    )
    # Run it!
    app()

if __name__ == "__main__":

    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    working_dir = Path(...)

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

    # --------------- #
    # Run application #
    # --------------- #
    main(
        working_dir=working_dir,
        studies=studies,
    )
```

When running the **App** again, **NUREMICS®** detects that all required **input parameters** for `OneProc` have been successfully mapped.

However, it now reports that one or more **input paths** are missing. These are explicitly listed, and the developer is prompted to define them using either the `"user_paths"` or `"required_paths"` key.

```shell
| OneProc |
> Input Parameter(s) :
(float) param1 -----||----- parameter1 (user_params)
(int)   param2 -----||----- 14         (hard_params)
(bool)  param3 -----||----- parameter2 (user_params)
> Input Path(s) :
path1 -----||----- Not defined (X)

(X) Please define all input paths either in "user_paths" or "required_paths".
```

The **input paths** of the **Proc** `OneProc` can be properly mapped within the **App** by defining the `"user_paths"` and/or `"required_paths"` keys in its corresponding dictionary entry inside the workflow list.

```python
APP_NAME = "ONE_APP"

from pathlib import Path
from nuremics import Application
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc

def main(
    working_dir: Path = None,
    studies: list = ["Default"],
):
    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": OneProc,
            "user_params": {
                "param1": "parameter1",
                "param3": "parameter2",
            },
            "hard_params": {
                "param2": 14,
            },
            "user_paths": {
                "path1": "input1.txt",
            },
        },
        {
            "process": AnotherProc,
        },
    ]

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_name=APP_NAME,
        working_dir=working_dir,
        workflow=workflow,
        studies=studies,
    )
    # Run it!
    app()

if __name__ == "__main__":

    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    working_dir = Path(...)

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

    # --------------- #
    # Run application #
    # --------------- #
    main(
        working_dir=working_dir,
        studies=studies,
    )
```

When running the **App** again, **NUREMICS®** detects that all required **input paths** for `OneProc` have been successfully mapped.

However, it now reports that one or more **output paths** are missing. These are explicitly listed, and the developer is prompted to define them using the `"output_paths"` key.

```shell
| OneProc |
> Input Parameter(s) :
(float) param1 -----||----- parameter1 (user_params)
(int)   param2 -----||----- 14         (hard_params)
(bool)  param3 -----||----- parameter2 (user_params)
> Input Path(s) :
path1 -----||----- input1.txt (user_paths)
> Output Path(s) :
out1 -----||----- Not defined (X)

(X) Please define all output paths in "output_paths".
```

The **output paths** of the **Proc** `OneProc` can be properly mapped within the **App** by defining the `"output_paths"` key in its corresponding dictionary entry inside the workflow list.

In the same way, we also complete the mapping for the **Proc** `AnotherProc` by providing all required entries: `"user_params"` and/or `"hard_params"`, `"user_paths"` and/or `"required_paths"`, `"output_paths"`.

```python
APP_NAME = "ONE_APP"

from pathlib import Path
from nuremics import Application
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc

def main(
    working_dir: Path = None,
    studies: list = ["Default"],
):
    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": OneProc,
            "user_params": {
                "param1": "parameter1",
                "param3": "parameter2",
            },
            "hard_params": {
                "param2": 14,
            },
            "user_paths": {
                "path1": "input1.txt",
            },
            "output_paths": {
                "out1": "output1.csv",
                "out2": "output2",
            },
        },
        {
            "process": AnotherProc,
            "user_params": {
                "param1": "parameter3",
                "param2": "parameter4",
            },
            "user_paths": {
                "path1": "input2",
            },
            "required_paths":{
                "path2": "output1.csv",
            },
            "output_paths": {
                "out1": "output3.vtk",
            },
        },
    ]

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_name=APP_NAME,
        working_dir=working_dir,
        workflow=workflow,
        studies=studies,
    )
    # Run it!
    app()

if __name__ == "__main__":

    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    working_dir = Path(...)

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

    # --------------- #
    # Run application #
    # --------------- #
    main(
        working_dir=working_dir,
        studies=studies,
    )
```

With all required mappings now properly defined for each **Proc**, the **App** can be executed without raising any errors. **NUREMICS®** confirms that the full mapping is complete by prompting a summary for each **Proc**, indicating that all **input parameters**, **input paths**, and **output paths** have been successfully resolved.

```shell
| OneProc |
> Input Parameter(s) :
(float) param1 -----||----- parameter1 (user_params)
(int)   param2 -----||----- 14         (hard_params)
(bool)  param3 -----||----- parameter2 (user_params)
> Input Path(s) :
path1 -----||----- input1.txt (user_paths)
> Output Path(s) :
out1 -----||----- output1.csv (output_paths)
out2 -----||----- output2     (output_paths)

| AnotherProc |
> Input Parameter(s) :
(int) param1 -----||----- parameter3 (user_params)
(str) param2 -----||----- parameter4 (user_params)
> Input Path(s) :
path1 -----||----- input2      (user_paths)
path2 -----||----- output1.csv (required_paths)
> Output Path(s) :
out1 -----||----- output3.vtk (output_paths)
```

<!---

- A summary of the input parameters expected by each **Proc**, and their current status.

As shown below, **NUREMICS®** automatically checks, for each **Proc**, whether all required input parameters have been mapped within the **App**. If any are missing, they are explicitly listed, and the developer is prompted to map them using either the `"user_params"` or `"hard_params"` key.

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