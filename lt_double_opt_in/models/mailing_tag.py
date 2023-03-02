##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
from random import randint

from odoo import fields, models


class MailingTag(models.Model):
    _name = "mailing.tag"
    _description = "Mailing Tag"

    name = fields.Char('Tag Name', required=True, translate=True)
    color = fields.Integer('Color')
    send_double_opt_in = fields.Boolean(string='Send Double Opt-In', copy=False)
