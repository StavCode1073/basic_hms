# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class MedicalSala(models.Model):
    _name = 'medical.sala'

    name = fields.Char('Nombre')
    planta = fields.Integer('Planta o Piso')
    description = fields.Text('Descripción')

