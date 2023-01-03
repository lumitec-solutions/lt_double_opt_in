##############################################################################
# Copyright (c) 2020 brain-tec AG (http://www.braintec-group.com)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################

from odoo import _, api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals):
        partner = super(ResPartner, self).create(vals)
        partner.update_mailing_contact()
        return partner

    def write(self, vals):
        result = super(ResPartner, self).write(vals)
        self.update_mailing_contact()
        return result

    def update_mailing_contact(self):
        category_names = self.category_id.mapped('name')
        company_name = self.parent_id.name if self.parent_id else self.name
        self.env['mailing.contact'].merge_with(self.email,
                                               self.name,
                                               company_name,
                                               self.country_id.id,
                                               self.title.id,
                                               self.lang,
                                               category_names)
