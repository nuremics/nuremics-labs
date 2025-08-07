# FirstProc

<p align="left">
  <img src="https://img.shields.io/badge/dependency-x.x.x+-007bff" />
</p>

## Process

Description of the Proc.<br>
A/ **`operation`:** Description of the operation.<br>

```mermaid
erDiagram
  **Parameters** ||--|| **Inputs** : provides
  **Paths** ||--|| **Inputs** : provides
  **Inputs** ||--|| **FirstProc** : feeds
  **FirstProc** ||--|| **Outputs** : generates

  **Parameters** {
    float param
  }
  **Paths** {
    file infile "txt"
  }
  **FirstProc** {
    op operation
  }
  **Outputs** {
    file outfile "txt"
  }
```

## Input Parameter(s)

- **`param`:** Description of the parameter.

## Input Path(s)

- **`infile`:** Description of the file.

## Output Path(s)

- **`outfile`:** Description of the file.