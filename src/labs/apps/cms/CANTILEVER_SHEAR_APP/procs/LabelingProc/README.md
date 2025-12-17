# LabelingProc

<p align="left">
  <img src="https://img.shields.io/badge/pythonocc--core-7.9.0-f7941e" />
  <img src="https://img.shields.io/badge/PyQt6-6.9.1-000000" />
</p>

## Process

Define and label the entities of a physical system from its geometric representation.<br>
A/ **`label_entities`:** Assign labels to the entities of a geometric model.

```mermaid
erDiagram
  **Parameters** ||--|| **Inputs** : provides
  **Paths** ||--|| **Inputs** : provides
  **Inputs** ||--|| **LabelingProc** : feeds
  **LabelingProc** ||--|| **Outputs** : generates

  **Parameters** {
    int dim
  }
  **Paths** {
    file infile "step/brep"
  }
  **LabelingProc** {
    op label_entities
  }
  **Outputs** {
    file outfile "json"
  }
```

## Input Parameter(s)

- **`dim`:** Dimension of the geometry: 1 for a line (beam), 2 for a rectangle (plate), 3 for a box (block).

## Input Path(s)

- **`infile`:** File containing the geometric model (in .step if `dim` = 3|2 or .brep if `dim` = 1).

## Output Path(s)

- **`outfile`:** File containing the labeled geometric entities.