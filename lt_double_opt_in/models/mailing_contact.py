##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################
import logging
from odoo import api, fields, models
from collections import defaultdict
from odoo.addons.base.models.res_partner import _lang_get

_logger = logging.getLogger(__name__)


class MailingContact(models.Model):
    _inherit = 'mailing.contact'

    category_ids = fields.Many2many('mailing.tag', string='Mailing Tags')
    double_opt_in = fields.Boolean(string='Double Opt-In', readonly=True,
                                   copy=False)
    can_manually_set_double_opt_in = fields.Boolean(
        "Can Manually Set Double Opt In",
        compute="_compute_can_set_double_opt_in")
    lang = fields.Selection(_lang_get, string='Language')
    