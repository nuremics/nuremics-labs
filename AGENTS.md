# nuRemics Labs Repository

This AGENTS.md explains the structure of a nuRemics labs repository. It is generic: it applies to any nuRemics labs repository. It is the root map of this codebase; the layered AGENTS.md files described below travel with the code they describe.

## What this repository is

A nuRemics labs repository is a laboratory of scientific applications built on the nuRemics framework. It hosts apps (self-contained scientific tools), and the mutualized code they can share: procs, ops and deps, all classified by theme. The framework itself is external (`nuremics`, imported from `nuremics`): this repository only hosts what the framework orchestrates.

Source layout: the code lives under `src/nuremics_labs/` (setuptools src layout, packages auto-discovered through `__init__.py` files, configured in `pyproject.toml`). The runtime and packaging configs are siblings of `src/`.

```
nuremics-labs/                     # repository root
├── AGENTS.md                      # this file
├── README.md                      # repository presentation
├── pixi.toml                      # runtime registration: features, environments, tasks
├── pixi.lock                      # resolved environments (managed by pixi)
├── pyproject.toml                 # packaging (src layout, package dependencies)
├── ruff.toml                      # code style (ANN, E, F, I; line length 200)
├── specs/                         # scientific requirements, one FRS document per app (<APP_NAME>.md)
└── src/
    └── nuremics_labs/
        ├── system.py              # labs entry point: runs the apps
        ├── registry.yaml          # WHO USES WHAT: reverse index of apps, procs and ops (skills-maintained)
        ├── apps/                  # apps, classified by theme (lowercase)
        │   └── <category>/<APP_NAME>/
        │       ├── AGENTS.md      # app architecture (workflow, discovery, pixi, runtime)
        │       ├── README.md      # app documentation. Inspect FIRST
        │       ├── __init__.py    # empty (package marker)
        │       ├── app.yaml       # the workflow definition
        │       └── procs/<Name>Proc/
        │           ├── AGENTS.md      # proc conventions (travels with the proc)
        │           ├── __init__.py    # mandatory class re-export (discovery)
        │           ├── item.py        # proc class (Process subclass) + operator __main__ block
        │           ├── README.md      # proc documentation. Inspect FIRST
        │           └── ops/
        │               ├── AGENTS.md      # ops conventions (travels with the ops)
        │               ├── __init__.py    # redundant-alias re-exports
        │               ├── README.md      # ops specification (implementation tickets)
        │               └── units.py       # op functions (pure scientific computations)
        ├── procs/                 # shared procs, classified by theme (same proc directory structure)
        ├── ops/                   # shared ops, classified by theme (<op_package>/ with units.py, re-exports and README)
        └── deps/                  # framework-independent utility code, classified by theme
```

## The layered architecture, in short

An app is defined by its workflow: an ordered list of processes (procs) connected through parameters and paths (`app.yaml`). Each proc orchestrates ops (pure scientific functions). Three layers: `app > proc > ops`.

- `apps/<category>/<APP_NAME>/`: one directory per app, `category` being a theme (lowercase). Procs and ops may be local (hosted inside the app, or in the proc that consumes them) or shared (hosted in `src/nuremics_labs/procs/` and `src/nuremics_labs/ops/`).
- `procs/<category>/<Name>Proc/`: shared procs, mutualized between apps, classified by theme. A proc directory is identical whether the proc is local or shared: `item.py` (the `Process` subclass), `__init__.py` (mandatory class re-export, discovery), `README.md` (inspect FIRST), its own AGENTS.md, and possibly its own `ops/` directory.
- `ops/<category>/<op_package>/`: shared ops, mutualized between procs, classified by theme, one package per op group (`units.py` + `__init__.py` re-exports, redundant-alias style, and one README specifying the hosted ops). A proc consuming shared ops imports the package as a module namespace (`from nuremics_labs.ops.<category> import <op_package>`) and calls its ops as `<op_package>.<op_name>(...)`; a proc consuming local ops imports the functions directly.

Proc residency and ops residency are two independent dimensions, each `local` or `shared`: any combination is legitimate. Where a proc is wired from is resolved by the `process` field of its entry in the app's `app.yaml`; where a proc's ops come from is resolved by the `from ...` imports at the top of the proc's `item.py`. The imports are the source of truth; nothing else needs to be inferred.

## deps: framework-independent utility code

`src/nuremics_labs/deps/<category>/` hosts utility code that is neither an app, nor a proc, nor an op: helper functions and scripts (e.g. plotting helpers, imaging scripts) that can be imported from ops (and procs) like an external package such as numpy, pandas or scipy.

- `deps` is independent of nuRemics: it does not derive from any framework class and knows nothing about apps, procs or ops. It could live in a standalone repository.
- `deps` is the incubator for specific developments: code written here may later migrate out and be externalized into its own repo, becoming a dependency of the labs package like any external library.
- Classified by theme like the other directories (lowercase, e.g. `plotting`, `imaging`, `postproc`), imported as `from nuremics_labs.deps.<category> import ...`.
- Convention: no README and no AGENTS.md in `deps`. For anything framework-orchestrated (app, proc, op), READMEs are the convention, not here.

## specs: the scientific requirements (FRS)

`specs/` hosts the scientific requirements documents of the repository, one per app: `<APP_NAME>.md`. One document scopes one app, even when that app does not exist yet: the FRS is written from the scientific need, and the components (procs, then the app) are developed from it. It sits outside `src/` on purpose: the FRS is prescriptive (WHY the app exists and WHAT it must achieve, requirement by requirement, in scientific language), while everything under `src/` is the implementation response.

- Each functional requirement (FR-1, FR-2, ...) of an FRS defines one processing step of the app, implemented as one proc carrying the same name. The FRS titles carry the implementation state: the app title links to the app folder once the app exists, and each FR title links to its proc folder once the proc is wired into the app. A linked title means the component exists; a bare title means it does not yet. The FR numbering follows the real workflow order: an inserted proc renumbers the FRs it shifts (the FRS references and the proc README anchors updated accordingly).
- An FRS is the north star of the development and evolves with it: an early draft states the intent, implementation sharpens the requirements, and the FRS is updated before the code when a requirement changes.
- The titles point both ways: the FRS titles link to the implemented components (app title to the app folder, FR titles to the proc folders), and the README titles link back to the FRS (the app README title to the FRS document, each proc README title to the FR section it implements). The FRS is read before the READMEs: it tells WHY and WHAT must be achieved; the READMEs describe what the implemented code does.
- Inside the READMEs, every proc and op mention in prose is a link to the component it names (the mermaid nodes are not): the app README Workflow links each proc to its folder and each op to its section in the ops README of its proc (`procs/<Name>Proc/ops/README.md#<op_name>` for local ops) or of its shared ops package (`../../../ops/<category>/<op_package>/README.md#<op_name>`); a proc README Process section links each op to its section in its ops README (`ops/README.md#<op_name>` for local ops, the shared package README for shared ops). The call-order letters (A/, B/, C/, ...) appear only in the proc and app READMEs, never in an ops README. Link text keeps the backticks.
- Relative links carry the minimal number of `..`: never exit a directory to re-enter it. From an app README, a shared ops package is `../../../ops/<category>/<op_package>/README.md`; from a proc README (one level deeper), `../../../../../ops/<category>/<op_package>/README.md`.

## Inspect READMEs first

Every framework-orchestrated component (app, proc, op group) is documented by a README.md, kept next to the code it describes:

- one README.md at the root of each app,
- one README.md in each proc directory (local or shared),
- one README.md in every `ops/` directory: inside the proc for local ops, inside the shared ops package for shared ops (one README per units.py, same format in both cases).

READMEs are the primary inspection target, before any code: they are the human-readable interface of the apps and act as a guardrail when inspecting code. Only go to the code (in a second step) when the READMEs are not enough for the context at hand. The nuRemics code is deliberately modular so that this inspection stays cheap: understanding what an app does should never require reading more than the READMEs. The layered AGENTS.md files (this one, app, proc, ops) explain HOW the codebase is constructed; the FRS in `specs/` explains WHY the app exists and WHAT it must achieve; the READMEs explain what the implemented code does. When an app is governed by an FRS, read it first (see the section above).

## How apps and procs are run

Two execution paths, both wired as pixi tasks in `pixi.toml`:

- **Apps** are run through the labs entry point `src/nuremics_labs/system.py`, one task per app: `<APP_NAME> = "python ./src/nuremics_labs/system.py <category> <APP_NAME>"`. `system.py` builds `Application(app_id=[<category>, <APP_NAME>], apps_dir, stage)` from the framework: the framework resolves the app from `apps_dir` (this package directory), reading `apps/<category>/<APP_NAME>/app.yaml` to build the workflow of procs and execute it. The `<category>` first argument selects the app: the app id is `[<category>, <APP_NAME>]`, not a single flat name.
- **Procs** can also be run standalone, WITHOUT `system.py`: a task targeting the proc's `item.py` directly (`<Name>Proc = "python ./src/nuremics_labs/apps/<category>/<APP_NAME>/procs/<Name>Proc/item.py"`, or the path of a shared proc). The operator block at the bottom of `item.py` ("USER-DEFINED PARAMETERS / >>>>> TO BE EDITED BY THE OPERATOR <<<<<") defines the working directory and the inputs, builds `dict_inputs`, then runs `process = <Name>Proc(dict_inputs=dict_inputs, set_inputs=True)`, `process.silent = True`, `process()` and `process.finalize()`. It is the standalone execution path of one proc, outside any app workflow.

Package discovery is automatic in both cases: the framework resolves apps from `apps_dir`, and setuptools finds packages through `__init__.py` files. A proc class must be importable from its package (hence the mandatory re-export in each proc's `__init__.py`). No manual registration in the package.

## pixi.toml: features and environments

`pixi.toml` is designed so that the repository can grow into a wide range of apps without forcing their dependencies onto each other:

- A **feature** (`[feature.X.dependencies]`, `[feature.X.pypi-dependencies]`, `[feature.X.tasks]`, `X` in UPPER_SNAKE_CASE) declares the dependencies of one app (or one group of apps) and the tasks that run them. Each app gets its app task (and, typically, its standalone proc tasks) inside a feature's `[feature.X.tasks]` section.
- An **environment** (`[environments]`, lower-kebab-case) groups one or more features: `env-name = ["FEATURE"]`. Pixi resolves and installs each environment separately: running an app only requires the dependencies of its own feature.
- This decomposition is what keeps installations lean: a large labs repository hosts many apps with very different dependencies (e.g. an imaging app needing pyvista, an analytics app needing openpyxl). Without it, every app installation would pull every dependency of every app. With it, each app runs in an environment that carries only what it needs.
- Features and app categories are independent dimensions (a `DICOM` feature can run an app stored in the `imaging` category), and there is no one-app-per-feature rule: a feature may host several apps.
- `pixi.lock` (sibling of `pixi.toml`) holds the resolved environments: managed by pixi, updated by `pixi install`, never hand-edited.

## registry.yaml: WHO USES WHAT

`src/nuremics_labs/registry.yaml` is the reverse index of the repository's apps, procs and ops. Where the READMEs tell WHAT each component does and the layered AGENTS.md files tell HOW it is organized, the registry tells WHO USES it. Use cases: impact analysis before modifying a shared component (find every consuming app/proc), import resolution (find the exact import path of an existing component), duplication check (before writing a new op, check the registry first).

Structure: three top-level sections (`apps`, `procs`, `ops`). Keys are import paths exactly as used by the code:

```yaml
apps:
  <APP_NAME>:
    category: <category>
    app_id: [<category>, <APP_NAME>]
    procs:
      - <proc import path>       # exactly as wired in app.yaml
    pixi:
      feature: <FEATURE>
      env: <env-name>

procs:
  <proc import path>:
    residency: local             # or shared
    item: <repo path of item.py>
    apps:
      - <APP_NAME>               # every app wiring this proc
    ops:
      - <op function import path> # every op function consumed by this proc

ops:
  <op function import path>:
    residency: local             # or shared
    units: <repo path of units.py>
    procs:
      - <proc import path>       # every proc consuming this function directly
```

- Ops are the public functions of every `units.py`: each op gets its own entry, keyed by its function import path (`nuremics_labs.ops.<category>.<op_package>.<op_name>` for shared ops; the full `...procs.<Name>Proc.ops.<op_name>` path for local ops). Underscore-prefixed helper functions are internal to the ops (used inside them, never by a proc) and are not listed.
- Residency values are `local` or `shared` (for a proc: hosted in the app; for an op: hosted in the consuming proc's own `ops/` directory): the field is defined inside an app or a proc, so no finer distinction is needed. The two dimensions are fully decoupled: any combination is legitimate.
- Maintenance: the registry is machine-maintained by nuRemics skills (init-nuremics-app adds the entries of each initialized app; future proc/op skills maintain their own entries). Never hand-edited, never deleted, other entries never touched.
- deps are out of scope (incubator, not stabilized).

## Code style

Code style everywhere in the package: ruff (linters `ANN`, `E`, `F`, `I`, line length 200, configured in `ruff.toml`), annotated functions, sorted imports, no docstrings in local proc code (READMEs are the reference), redundant-alias re-exports (`from .x import y as y`).
