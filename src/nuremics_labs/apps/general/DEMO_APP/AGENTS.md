# nuRemics App

This file is generic and byte-identical at the root of every nuRemics app. Do not customize it. App-specific behavior lives in the README.md files. If you have already read this file once in your session, do not re-read other copies: it is byte-identical everywhere.

## What this layer is

An app is a self-contained scientific application built on the nuRemics framework, defined by its workflow: an ordered list of processes (procs) connected through parameters and paths. Everything about an app lives under `apps/<category>/<APP_NAME>/` in a nuRemics labs repository:

```
apps/<category>/<APP_NAME>/
├── AGENTS.md          # this file
├── README.md          # app documentation. Inspect FIRST
├── __init__.py        # empty (package marker for discovery)
├── app.yaml           # the workflow definition
└── procs/
    ├── __init__.py    # empty (package marker)
    └── <Name>Proc/
        ├── AGENTS.md          # proc conventions (travels with the proc)
        ├── __init__.py        # re-exports the proc class (discovery)
        ├── item.py            # proc class (Process subclass)
        ├── README.md          # proc documentation
        └── ops/
            ├── AGENTS.md      # ops layer conventions
            ├── __init__.py    # re-exports ops (redundant-alias style)
            ├── README.md      # ops specification (implementation tickets)
            └── units.py       # op functions (pure scientific computations)
```

The architecture is a three-layer stack: `app > proc > ops`. The app wires procs; each proc orchestrates ops; each op performs one pure scientific computation.

The `procs/` directory may stay empty (only its `__init__.py`): an app whose workflow wires only shared procs needs no local procs.

## The freshly initialized skeleton

An app created by the initialization skill (`/init-nuremics-app`) starts as an empty skeleton shell: the minimal instance of the tree above, with unmistakable markers, so a later session can tell it apart from an app already under construction:

- `app.yaml` declares `workflow: []`, preceded by a comment block showing the shape of a workflow entry.
- `procs/` holds only its empty `__init__.py`: no proc exists yet.
- The README's Workflow section carries a single marker line ("Empty skeleton: no proc wired yet") and has no Mapping/I-O sections yet; no badge is installed.

When these markers are present, the app is freshly initialized: procs are developed first as shared procs (`/init-nuremics-proc`, in the labs repository's `procs/` directory), implemented until stable, then plugged in here by the dedicated plug skill. Plugging means: one `app.yaml` entry per proc, with its mappings (deleting the comment block on the first plug), the registry updated (the app's `procs:` list, each wired proc's `apps:` list), and the README ladder filled (Workflow, Mapping, I/O Interface, INPUTS/OUTPUTS). A plugged proc either moves into this app's `procs/` directory (local, gaining its AGENTS.md copy next to its code) or stays shared. When the markers are gone, the app follows the normal conventions of this file.

## Where the procs and ops come from

Procs and ops each have two possible homes, and the two choices are independent (fully decoupled).

**Proc residency**

- **Local**: this app's `procs/` directory (`apps/<category>/<APP_NAME>/procs/<Name>Proc/`).
- **Shared**: the labs repository's `procs/` directory at project root, classified by theme (`nuremics_labs/procs/<category>/<Name>Proc/`).

Resolved by the `process` field of each `app.yaml` entry: that field holds the full import path of the proc (`nuremics_labs.apps....` = local, `nuremics_labs.procs....` = shared).

**Ops residency (per proc)**

- **Local**: the proc's own `ops/` directory, inside the proc's directory (wherever the proc lives).
- **Shared**: the labs repository's `ops/` directory at project root, classified by theme (`nuremics_labs/ops/<category>/<op_package>/`).

Resolved by the `from ...` imports at the top of the proc's `item.py`: the import path tells which home (local, functions called directly; shared, package used as module namespace `nuremics_labs.ops.<category> import <op_package>`).

**Decoupling**: any combination is legitimate: a local proc may consume shared ops, and a shared proc may consume its own local ops. The `app.yaml` `process` fields and the `item.py` imports are the only sources of truth; nothing else needs to be inferred.

## Inspect READMEs first

Before the READMEs, check the labs repository's `specs/` directory: when a scientific requirements document (`<APP_NAME>.md`, the FRS of the app) governs this app, read it first. The FRS is the prescriptive upstream (why the app exists and what it must achieve, requirement by requirement); the READMEs describe what the implemented code does. When the FRS governs the app, the app README title is a link to the FRS document, and each proc README title is a link to its FR section of the FRS.

Every component of a nuRemics app is documented by a README.md, kept next to the code it describes:

- one README.md at the root of the app,
- one README.md in each proc directory,
- one README.md in the `ops/` directory of each proc.

READMEs are the primary inspection target, before any code. The app README explains what the app does: the workflow (ordered procs, each with its call sequence of ops), the parameter/path mappings (per-proc erDiagram blocks), and the I/O interface (inputs/outputs of the whole app and of each proc, with mermaid diagrams). A proc README explains what that proc does, its inputs and outputs. An ops README specifies each op in call order with one section per function (Overview, Description, Inputs, Outputs); those sections are implementation tickets, sufficient to re-implement an op from scratch. In the app README Workflow, every proc name is a relative link to its folder and every op name is a relative link to its section in the ops README of its proc (`procs/<Name>Proc/ops/README.md#<op_name>` for local ops) or of its shared ops package (`../../../ops/<category>/<op_package>/README.md#<op_name>`). Relative links carry the minimal number of `..`: never exit a directory to re-enter it. Link text keeps the backticks; the mermaid nodes are not linked.

READMEs are the human-readable interface of the app: they let humans and agents understand what each component does, and act as a guardrail when inspecting code. Only go to the code (in a second step) when the READMEs are not enough for the context at hand. The nuRemics code is deliberately modular so that this code inspection stays cheap: understanding what an app does should never require reading more than the READMEs.

## app.yaml: the workflow definition

`app.yaml` lists the workflow as an ordered list of processes. Each entry references the proc by its package path and declares the mappings between the app and the proc:

```yaml
workflow:
  - process: nuremics_labs.apps.<category>.<APP_NAME>.procs.<Name>Proc
    hard_params:            # fixed values set by the app author
      <proc_field>: <value>
    user_params:            # parameters exposed to the app user (mapping)
      <proc_field>: <app_param_name>
    user_paths:             # input paths provided by the app user (mapping)
      <proc_field>: <file_or_folder_name>
    required_paths:         # input paths produced by a previous proc of the workflow (mapping)
      <proc_field>: <file_or_folder_name>
    output_paths:           # paths written by the proc (mapping)
      <proc_field>: <file_or_folder_name>
    overall_analysis:       # analysis input produced by previous procs (mapping)
      <proc_field>: <file_or_folder_name>
    settings:               # proc-specific settings passed as-is
      <key>: <value>

default_params:             # default values for user_params, keyed by app_param_name
  "<app_param_name>": <value>
```

All mapping keys are optional per proc. Procs referenced from the shared library use `nuremics_labs.procs.<category>.<Name>Proc` instead of the local path.

## Discovery and execution

- The framework resolves apps from `apps_dir` (set in the labs repo `src/nuremics_labs/system.py` to the `nuremics_labs` package directory): `Application(app_id, apps_dir, stage)` reads `<category>/<APP_NAME>/app.yaml`. Packages are discovered through `__init__.py` files; a proc class must be importable from its package (hence the re-export in each `procs/<Name>Proc/__init__.py`).
- The labs repo entry point is `src/nuremics_labs/system.py`, invoked as `python ./src/nuremics_labs/system.py <category> <APP_NAME>`.
- Runtime registration lives in the repo root `pixi.toml`: each app gets a task `<APP_NAME> = "python ./src/nuremics_labs/system.py <category> <APP_NAME>"` inside a feature's `[feature.X.tasks]` section, plus (for a new feature) empty `[feature.X.dependencies]` and `[feature.X.pypi-dependencies]` sections and an entry `<env-name> = ["<FEATURE>"]` in `[environments]` (feature and environment in UPPER_SNAKE_CASE and lower-kebab-case respectively). There is no one-app-per-feature rule: a feature may host several apps.

## Runtime (first run of an app)

Two machine-level files (outside the repo, shared by all nuRemics apps of the machine) drive execution. The framework writes them itself; filling their missing entries is a user-level operation, only with explicit consent:

- `settings.json` (user config directory, e.g. `%LOCALAPPDATA%\nuRemics\settings.json` on Windows): registers each app under `apps.<category>.<APP_NAME>.working_dir`. The value is a BASE directory; the real working directory is `<base>/<APP_NAME>`, created by the framework.
- `<working_dir>/<APP_NAME>/studies.json`: declares the studies to execute. `{"studies": ["<name>"], "config": {}}` is the minimal form; the framework auto-populates `config` per study (`execute`, `user_params`, `user_paths`, `clean_outputs`).

## Layer conventions

- Procs: `Process` subclass with `attrs` fields (parameters, paths, outputs, internals), call sequence calling ops, operator `__main__` block. See `procs/<Name>Proc/AGENTS.md` (one per proc directory, local or shared).
- Ops: pure annotated functions in `units.py`, redundant-alias re-exports, README as reference. See `procs/<Name>Proc/ops/AGENTS.md` (one per ops directory, local or shared).
- Code style everywhere: ruff (`ANN`, `E`, `F`, `I`), line length 200, no docstrings in local proc code (READMEs are the reference).

## How this layer integrates

Apps are the deliverable of a nuRemics labs repository: a repository hosts categories (`apps/<category>/`), categories host apps, apps wire procs (local or shared from `nuremics_labs.procs.*`), procs orchestrate ops. An app is fully described by its README + `app.yaml`: anyone (human or agent) should understand the whole app without reading code.
