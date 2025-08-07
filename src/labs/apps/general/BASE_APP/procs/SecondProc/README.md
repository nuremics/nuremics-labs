# SecondProc

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
  **Inputs** ||--|| **SecondProc** : feeds
  **SecondProc** ||--|| **Outputs** : generates

  **Parameters** {
    int param
  }
  **Paths** {
    file infile "txt"
  }
  **SecondProc** {
    op operation
  }
  **Outputs** {
    folder outfolder "_"
  }
```

## Input Parameter(s)

- **`param`:** Description of the parameter.

## Input Path(s)

- **`infile`:** Description of the file.

## Output Path(s)

- **`outfolder/`**<br>
  **`output1.txt`:** Description of the file.<br>
  **`output2.txt`:** Description of the file.