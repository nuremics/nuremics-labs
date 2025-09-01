# CANTILEVER_SHEAR_APP

<p align="left">
  <img src="https://img.shields.io/badge/CadQuery-2.5.2+-2980b9" />
</p>

## Workflow

1. **[`GeometryProc`](https://github.com/nuremics/nuremics-labs/tree/cantilever-shear/src/labs/apps/cms/CANTILEVER_SHEAR_APP/procs/GeometryProc):** Create a geometric representation of a physical system.<br>
  A/ **`create_geometry`:** Create and export a simple geometric entity (beam, plate, or block) in STEP or BREP format.

```mermaid
flowchart RL
  **GeometryProc** e1@--1--o **CANTILEVER_SHEAR_APP**
  **create_geometry** e2@--A--o **GeometryProc**
  e1@{ animate: true }
  e2@{ animate: true }
```

## Mapping

```mermaid
erDiagram
  **CANTILEVER_SHEAR_APP** ||--|| **user_params** : mapping
  **CANTILEVER_SHEAR_APP** ||--|| **hard_params** : mapping
  **CANTILEVER_SHEAR_APP** ||--|| **output_paths** : mapping
  **user_params** ||--|| **GeometryProc** : mapping
  **hard_params** ||--|| **GeometryProc** : mapping
  **output_paths** ||--|| **GeometryProc** : mapping

  **user_params** {
    int dim "dimension"
  }
  **hard_params** {
    float length "10.0"
    float width "1.0"
    float height "0.1"
  }
  **output_paths** {
    file outfile "geometry.(step/brep)"
  }
```

## I/O Interface

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Parameters**
      direction LR
      param1["dimension _(int)_"]
    end
  end

  subgraph **CANTILEVER_SHEAR_APP**
    direction RL
    proc1["GeometryProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out1["geometry.(step/brep) _(file)_"]
  end

  **INPUTS** --> **CANTILEVER_SHEAR_APP**
  **CANTILEVER_SHEAR_APP** --> **OUTPUTS**
```

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Parameters**
      direction LR
      param1["dimension _(int)_"]
    end
  end

  subgraph **CANTILEVER_SHEAR_APP**
    direction RL
    proc1["GeometryProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out1["geometry.(step/brep) _(file)_"]
  end

  **INPUTS** --> proc1
  proc1 --> **OUTPUTS**
```

### INPUTS

#### Parameters

- **`dimension`:** Dimension of the geometry: 1 for a line (beam), 2 for a rectangle (plate), 3 for a box (block).

### OUTPUTS

- **`geometry.(step/brep)`:** File containing the created geometry (in .step if `dimension` = 3|2 or .brep if `dimension` = 1).