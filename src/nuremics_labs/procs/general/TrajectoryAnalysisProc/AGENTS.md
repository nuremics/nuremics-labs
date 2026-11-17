# nuRemics Proc

This file is generic and byte-identical in every proc directory of every nuRemics app. Do not customize it. App-specific behavior lives in the README.md files. If you have already read this file once in your session, do not re-read other copies: it is byte-identical everywhere. It travels with the proc wherever the proc lives: local, inside an app's `procs/` directory (`apps/<category>/<APP_NAME>/procs/<Name>Proc/`), or shared between apps, in the labs repository's `procs/` directory at project root (`nuremics_labs/procs/<category>/<Name>Proc/`, mutualized and classified by theme like the apps).

## What this directory is

This directory contains ONE process (proc): one autonomous scientific component that can be wired into an app workflow. It lives next to the code it describes:

- `item.py`: the proc class. A proc is a class deriving from the framework's `Process` base class, defined with `@attrs.define`. Its purpose is one line in its README; its work is performed by calling ops.
- `__init__.py`: re-exports the class from `item.py` (`from .item import <Name>Proc as <Name>Proc`). This re-export is mandatory: the framework and `app.yaml` reference the proc by its package path (`...procs.<Name>Proc`), so the class must be importable from the package.
- `README.md`: the specification of the proc. Inspect it FIRST.
- `ops/`: the ops directory of this proc (its implementation units). It carries its own AGENTS.md.

## The freshly initialized skeleton

A proc created by the initialization skill (`/init-nuremics-proc`) starts as a fill-in skeleton with unmistakable markers, so a later implementation session can tell it apart from a proc already under construction:

- `item.py` carries a single real input parameter (`message: str`), commented extension lines for the three field patterns (input paths, output paths, internal fields), one work method calling `placeholder_op`, and an operator block whose `working_dir` is still the placeholder `Path(r"...")`.
- `ops/units.py` contains only the stub op `placeholder_op`, raising `NotImplementedError` on purpose (the initialization run check expects exactly this failure as the proof that the plumbing works).
- Both READMEs still describe the placeholder (`awaiting its functional specification`).

When these markers are present, the proc is freshly initialized: the FIRST implementation session starts by cleaning the scaffold. Remove the placeholder parameter, the `placeholder_op` method and its stub, and the matching `dict_inputs` entry, then replace them with the real structure of the specification. READMEs first: if the proc README still describes the placeholder, the functional specification has not been written yet; write it before touching the code (the proc README's sections and the ops README's per-function sections are the implementation tickets). The operator block keeps its shape: only its placeholder values are filled. When the markers are gone, the proc follows the normal conventions of this file.

## Where the proc lives, and where its ops come from

Two independent dimensions, fully decoupled. Do not infer one from the other.

**Where the proc lives (proc residency)**

- **Local**: inside the app's `procs/` directory (`apps/<category>/<APP_NAME>/procs/<Name>Proc/`). Its `app.yaml` entry references it as `nuremics_labs.apps.<category>.<APP_NAME>.procs.<Name>Proc`.
- **Shared**: in the labs repository's `procs/` directory at project root, classified by theme (`nuremics_labs.procs.<category>.<Name>Proc`).

Resolved by the `process` field of the proc's entry in the app's `app.yaml`: that field holds the full import path of the proc (`nuremics_labs.apps....` = local, `nuremics_labs.procs....` = shared).

**Where the ops come from (ops residency)**

- **Local**: this proc's own `ops/` directory, inside this proc's directory (wherever the proc lives). Ops are imported from it and called as plain functions.
- **Shared**: the labs repository's `ops/` directory at project root, classified by theme (`nuremics_labs.ops.<category>.<op_package>`). The package is imported as a module namespace (`from nuremics_labs.ops.<category> import <op_package>`) and its ops are called as `<op_package>.<op_name>(...)`.

Resolved by the `from ...` imports at the top of `item.py`: the import path tells which home, and the import style tells how the ops are called (plain functions vs module namespace).

**Decoupling**: any combination is legitimate. A local proc may import its ops from the shared `ops/` library; a shared proc may use its own local `ops/` directory. The `app.yaml` `process` field and the `item.py` imports are the only sources of truth; nothing else needs to be inferred.

## Inspect READMEs first

Every component of a nuRemics app is documented by a README.md, kept next to the code it describes:

- one README.md at the root of the app,
- one README.md in each proc directory,
- one README.md in the `ops/` directory of each proc.

READMEs are the primary inspection target, before any code. The app README explains what the app does and its workflow; a proc README explains what that proc does (purpose, call sequence of ops A/, B/, C/, ... in order, input parameters, input paths, output paths); an ops README specifies each op with one section per function (Overview, Description, Inputs, Outputs). In an ops README, those per-function sections are implementation tickets: documenting an op there is enough to re-implement it from scratch. When the proc implements a functional requirement (FR-1, FR-2, ...) of an FRS, the proc README title is a link to that FR section of the FRS. In the proc README Process section, every op name is a relative link to its section in the ops README (`ops/README.md#<op_name>` for local ops, the README of the shared ops package for shared ops). Relative links carry the minimal number of `..`: never exit a directory to re-enter it (from a proc README, a shared package is `../../../../../ops/<category>/<op_package>/README.md`). Link text keeps the backticks; the mermaid nodes are not linked.

READMEs are the human-readable interface of the app: they let humans and agents understand what each component does, and act as a guardrail when inspecting code. Only go to the code (in a second step) when the READMEs are not enough for the context at hand. The nuRemics code is deliberately modular so that this code inspection stays cheap: understanding what an app does should never require reading more than the READMEs.

## Conventions of this layer

- The proc class derives from `Process` (imported from `nuremics`), defined with `@attrs.define`. No docstrings: the proc README is the reference.
- Fields are declared as `attrs.field(init=False)` with metadata declaring their role: `{"input": True}` for input parameters and input paths, `{"output": True}` for output paths (paths get `converter=Path`). Internal variables are plain `attrs.field(init=False)` fields.
- Functions are annotated (ruff `ANN`), imports sorted (ruff `I`), line length 200.
- The proc is a sequential dispatcher ("SAS" principle): it only routes data between the framework and the ops, in call order. It holds no logic of its own: no control flow (`for`/`while`/`if`), no computation, no formatting, no print, no helper method. All the logic lives in the ops, including the reporting ops (printing IS their function).
- `__call__(self) -> None` starts with `super().__call__()` then calls the work methods in order. Each work method is exactly one op call: it passes the proc's fields as arguments and stores the returned result in an internal field (or lets the op write outputs). Nothing else.
- Every proc carries an operator `__main__` block in `item.py` ("USER-DEFINED PARAMETERS / >>>>> TO BE EDITED BY THE OPERATOR <<<<<"): working directory, inputs as plain variables, `dict_inputs`, then `process = <Name>Proc(dict_inputs=dict_inputs, set_inputs=True)`, `process.silent = True`, `process()` and `process.finalize()`. It is the standalone execution path of the proc (typically wired as a pixi task).
- Ops live in an `ops/` directory (this proc's own one, or the shared one) and are re-exported there with the redundant-alias style (`from .units import op_name as op_name`).
- Proc folders are named in PascalCase with the `Proc` suffix (`CatalogAssessmentProc`); their packages must be importable, hence the mandatory `__init__.py` re-export.

## How this proc integrates

An app wires procs: the app's `app.yaml` lists the workflow as an ordered list of processes, each referenced by its package path (local or shared, see the `process` field) with the parameter/path mappings between the app and the proc.

This proc itself integrates ops from below: each work method calls ops (imported from this proc's own `ops/` directory, or from the repository's shared `ops/` directory, see the `from ...` imports of `item.py`).

For the ops conventions (pure functions, redundant-alias re-exports, README as implementation ticket), see the AGENTS.md in the `ops/` directory. For the full app architecture (workflow wiring, discovery, pixi registration, runtime), see the AGENTS.md at the root of the app that wires this proc.
