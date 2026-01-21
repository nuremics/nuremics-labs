# BASE_APP

<p align="left">
  <img src="https://img.shields.io/badge/dependency-x.x.x+-007bff" />
</p>

## Workflow

1. **[`FirstProc`](https://github.com/nuremics/nuremics-labs/tree/main/src/labs/apps/general/BASE_APP/procs/FirstProc):** Description of the Proc.<br>
  A/ **`operation`:** Description of the operation.
2. **[`SecondProc`](https://github.com/nuremics/nuremics-labs/tree/main/src/labs/apps/general/BASE_APP/procs/SecondProc):** Description of the Proc.<br>
  A/ **`operation`:** Description of the operation.

```mermaid
flowchart RL
  **FirstProc** e1@--1--o **BASE_APP**
  **SecondProc** e2@--2--o **BASE_APP**
  operation1["**operation**"] e3@--A--o **FirstProc**
  operation2["**operation**"] e4@--A--o **SecondProc**
  e1@{ animate: true }
  e2@{ animate: true }
  e3@{ animate: true }
  e4@{ animate: true }
```

## Mapping

```mermaid
erDiagram
  **BASE_APP** ||--|| **hard_params** : mapping
  **BASE_APP** ||--|| **user_paths** : mapping
  **BASE_APP** ||--|| **output_paths** : mapping
  **hard_params** ||--|| **FirstProc** : mapping
  **user_paths** ||--|| **FirstProc** : mapping
  **output_paths** ||--|| **FirstProc** : mapping

  **hard_params** {
    float param "1.4"
  }
  **user_paths** {
    file infile "input.txt"
  }
  **output_paths** {
    file outfile "output.txt"
  }
```

```mermaid
erDiagram
  **BASE_APP** ||--|| **user_params** : mapping
  **BASE_APP** ||--|| **required_paths** : mapping
  **BASE_APP** ||--|| **output_paths** : mapping
  **user_params** ||--|| **SecondProc** : mapping
  **required_paths** ||--|| **SecondProc** : mapping
  **output_paths** ||--|| **SecondProc** : mapping

  **user_params** {
    int param "parameter"   
  }
  **required_paths** {
    file infile "output.txt"
  }
  **output_paths** {
    folder outfolder "output"
  }
```

## I/O Interface

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      path1["input.txt _(file)_"]
    end

    subgraph **Parameters**
      direction LR
      param1["parameter _(int)_"]
    end
  end

  subgraph **BASE_APP**
    direction RL
    proc1["FirstProc"]
    proc2["SecondProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out1["output.txt _(file)_"]
    out2["output _(folder)_"]
  end

  **INPUTS** --> **BASE_APP**
  **BASE_APP** --> **OUTPUTS**
```

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      path1["input.txt _(file)_"]
    end

    subgraph **Parameters**
      direction LR
      param1["_"]
    end
  end

  subgraph **BASE_APP**
    direction RL
    proc1["FirstProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out1["output.txt _(file)_"]
  end

  **INPUTS** --> proc1
  proc1 --> **OUTPUTS**
```

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      out1["output.txt _(file)_"]
    end

    subgraph **Parameters**
      direction LR
      param1["parameter _(int)_"]
    end
  end

  subgraph **BASE_APP**
    direction RL
    proc2["SecondProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out2["output _(folder)_"]
  end

  **INPUTS** --> proc2
  proc2 --> **OUTPUTS**

  classDef blueBox fill:#d0e6ff,stroke:#339,stroke-width:1.5px;
  class out1 blueBox;
```

### INPUTS

#### Parameters

- **`parameter`:** Description of the parameter.

#### Paths

- **`input.txt`:** Description of the file.

### OUTPUTS

- **`output/`**<br>
  **`output1.txt`:** Description of the file.<br>
  **`output2.txt`:** Description of the file.