from trytond.pool import Pool
from .union import *
from .campo import * 
from .distrito import * 
from .gp import * 
from .iglesia import * 
from .party import * 
from .reporte import * 
from .reportebautizo import * 
from .zona import * 
from .division import *
from .user import * 
from .config import * 
from .reporteadd import *
  
def register():
    Pool.register(
        Division, 
        Union,
        Campo,
        Zona,
        Distrito, 
        Iglesia,
        Gp, 
        Party,
        Reporte, 
        ReporteBautizo,
        InformeIglesia,
        InformeIglesiaContexto,
        InformeDistrito, 
        InformeDistritoContexto,
        InformeDistritoLider, 
        InformeDistritoLiderContexto, 
        InformeZona, 
        InformeZonaContexto,
        InformeCampo,
        InformeCampoContexto,  
        InformeUnion, 
        InformeUnionContexto,
        User, 
        GpSequence,
        ImprimirReporteIglesiaInicio,
        ReporteIglesiaTableGlobal,
        ReporteIglesiaTableResumen,
        ImprimirReporteDistritoInicio,
        ReporteDistritoTable,
        ImprimirReporteZonaInicio,
        ReporteZonaTable,
        ImprimirReporteCampoInicio,
        ReporteCampoTable,
        ImprimirReporteUnionInicio,
        ReporteUnionTable,
        ImprimirReporteLiderDestacadoInicio,
        ReporteLiderDestacadoTable,
        ImprimirReporteLiderCeroInicio,
        ReporteLiderCeroTable,
        ImprimirReporteLiderDistritoInicio,
        ReporteLiderDistritoTable,
        module='discipulado', type_='model')

    Pool.register(
        ImprimirReporteIglesia,
        ImprimirReporteDistrito,
        ImprimirReporteZona,
        ImprimirReporteCampo,
        ImprimirReporteUnion,
        ImprimirReporteLiderDestacado,
        ImprimirReporteLiderCero,
        ImprimirReporteLiderDistrito,
        module='discipulado', type_='wizard')

    Pool.register(
        ReporteIglesia,
        ReporteDistrito,
        ReporteZona,
        ReporteCampo,
        ReporteUnion,
        ReporteLiderDestacado,
        ReporteLiderCero,
        ReporteLiderDistrito,
        module='discipulado', type_='report') 