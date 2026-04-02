from nuremics_labs.procs.general.PolygonGeometryProc import PolygonGeometryProc
from nuremics_labs.procs.general.ProjectileModelProc import ProjectileModelProc
from nuremics_labs.procs.general.TrajectoryAnalysisProc import TrajectoryAnalysisProc

PROCS_REGISTRY = {
    "PolygonGeometryProc": PolygonGeometryProc,
    "ProjectileModelProc": ProjectileModelProc,
    "TrajectoryAnalysisProc": TrajectoryAnalysisProc,
}