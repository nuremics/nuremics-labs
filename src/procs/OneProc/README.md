## Diagram

```mermaid
erDiagram
  **Parameters** ||--|| **Inputs** : provides
  **Paths** ||--|| **Inputs** : provides
  **Inputs** ||--|| **OneProc** : feeds
  **OneProc** ||--|| **Outputs** : generates

  **Parameters** {
    float param1
    int param2
  }
  **Paths** {
    file path1 "txt"
  }
  **OneProc** {
    function operation1
    function operation2
  }
  **Outputs** {
    file out1 "csv"
    file out2 "png"
  }
```

## Description

Generate and plot a regular polygon shape.

## Pipeline

1. **`operation1`:** Generate the 2D coordinates of a regular polygon (given radius and number of sides).
2. **`operation2`:** Plot the shape with a title read from an external file.

## Input Parameter(s)

- **`param1`:** Radius of the polygon.

- **`param2`:** Number of sides of the polygon.

## Input Path(s)

- **`path1`:** Path to a text file containing the plot title.

## Output Path(s)

- **`out1`:** File containing the X/Y coordinates of the polygon vertices.

- **`out2`:** Image of the plotted polygon figure.