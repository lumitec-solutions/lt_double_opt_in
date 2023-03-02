##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
import hashlib
import hmac
import uuid
from datetime import date
from dateutil.relativedelta import relativedelta
from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class MailingToken(models.Model):
    _name = "mailing.contact.token"
    _description = "Mailing Contact Token"

    access_token = fields.Char('Security Token',
                               compute='_compute_access_token', store=True,
                               readonly=True,
                               copy=False)
    token_generation_date = fields.Date('Token Generation Date',
                                        compute='_compute_access_token',
                                        store=True,
                                        readonly=True, copy=False)
    mailing_contact_id = fields.Many2one('mailing.contact',
                                         string='Mailing Contact',
                                         required=True, readonly=True,
                                         copy=False)
    action = fields.Selection([('double_opt_in', 'Double Opt-In')],
                              string="Action", default='double_opt_in',
                              required=True, readonly=True, copy=False)
