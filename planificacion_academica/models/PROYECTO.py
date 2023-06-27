# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Solución ERP de código abierto
#
#    Este programa es software libre: se puede redistribuir y / o modificar
#    bajo los términos de la GNU Affero General Public License
#
#    Debería haber recibido una copia de la Licencia Pública General GNU Affero
#    Junto con este programa. Si no es así, consulte <http://www.gnu.org/licenses/>.
#
##############################################################################
# Generado por el plugin Odoo V10 para Dia!

from odoo import api, fields, models

class Aula(models.Model):
    _name = 'aula'
    #_rec_name = ''
    idaula = fields.Integer()
    nucleo = fields.Char()
    codigo = fields.Char()
    numeroestudiantes = fields.Integer()


class Horarios(models.Model):
    _name = 'horarios'
    #_rec_name = ''
    idhorario = fields.Integer()
    programa = fields.Char()
    nucleo = fields.Char()
    docente = fields.Char()
    aula = fields.Char()
    dia = fields.Char()
    hora = fields.Char()
    grupo = fields.Integer()

class Estudiante(models.Model):
    """(NULL)"""
    _name = 'estudiante'
    #_rec_name = ''
    idestudiante = fields.Integer()
    nombre = fields.Char()
    apellido = fields.Char()
    programa = fields.Char()
    nucleo = fields.Char()
    turno = fields.Char()
    uc = fields.Char()

class Estadistica(models.Model):

    _name = 'estadistica'

    idestudiante = fields.Many2one('estudiante', String='Estudiante')
    iddocente = fields.Many2one('docente', String='Docente')
    estadisticas = fields.Integer(string='Número de estudiantes', compute='_compute_estadisticas', store=False)
    estadistica = fields.Integer(string='Número de docentes', compute='_compute_estadistica', store=False)
    programaestadistica = fields.Char(string='Programa', default = 'PNFI')
    nucleoestadistica = fields.Char(string='Nucleo', default = 'La Urbina')
    turnoestadistica = fields.Char(string='Turno', default = 'Nocturno')
    ucestadistica = fields.Char(string='Unidad Curricular', default = 'TIC')

    @api.depends('idestudiante')
    def _compute_estadisticas(self):
        self.env.cr.execute("SELECT COUNT(*) FROM estudiante WHERE programa = 'PNFI' AND nucleo = 'La Urbina' AND turno = 'Nocturno' AND uc = 'TIC'")
        result = self.env.cr.fetchone()
        count = result[0] if result else 0
        self.estadisticas = count

    def update_estadisticas(self):
        self._compute_estadisticas()

    @api.depends('iddocente')
    def _compute_estadistica(self):
        self.env.cr.execute("SELECT COUNT(*) FROM docente WHERE programadocente = 'PNFI' AND nucleodocente = 'La Urbina' AND turnodocente = 'Nocturno' AND ucdocente = 'TIC'")
        result = self.env.cr.fetchone()
        countdocente = result[0] if result else 0
        self.estadistica = countdocente

    def update_estadistica(self):
        self._compute_estadistica()

class Docente(models.Model):
    """(NULL)"""
    _name = 'docente'
    #_rec_name = ''
    iddocente = fields.Integer()
    nombredocente = fields.Char()
    apellidodocente = fields.Char()
    programadocente = fields.Char()
    nucleodocente = fields.Char()
    turnodocente = fields.Char()
    ucdocente = fields.Char()

"""
Este modelo determina los campos en la base de datos de las clases aula, horarios,estudiantes,estadísticas y docentes
La clase llamada estadísticas define campos Many2one que hacen referencia a otros campos
definidos en otros modelos y también tiene campos que cuentan la cantidad de estudiantes/docentes
"""    


    