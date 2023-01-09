##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################

from odoo.tests import common


class TestResPartner(common.TransactionCase):
    def setUp(self):
        super(TestResPartner, self).setUp()

    def test_01_partner_creation(self):
        """Test creation of mailing contact on creation of contact"""
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Partner Tag',
        })

        partner_tag = self.env['res.partner.category'].create({
            'name': 'Partner Tag',
        })
        partner = self.env['res.partner'].create({
            'name': 'Test Partner 1',
            'email': 'partnertest_1@example.com',
            'category_id': [partner_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', partner.email)])
        self.assertEqual(1, len(mailing_contact))

    def test_02_partner_creation(self):
        """Test creation of mailing contact on creation of contact without tag"""
        partner = self.env['res.partner'].create({
            'name': 'Test Partner 2',
            'email': 'partnertest_2@example.com',
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', partner.email)])
        self.assertEqual(1, len(mailing_contact))
        self.assertFalse(mailing_contact.category_ids)

    def test_03_partner_creation(self):
        """Test creation of mailing contact on creation of contact with crm tag not in mailing tag"""
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Partner Tag',
        })

        partner_tag = self.env['res.partner.category'].create({
            'name': 'Tag 1',
        })
        partner = self.env['res.partner'].create({
            'name': 'Test Partner 3',
            'email': 'partnertest_3@example.com',
            'category_id': [partner_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', partner.email)])
        self.assertEqual(1, len(mailing_contact))
        self.assertFalse(mailing_contact.category_ids)

    def test_04_partner_creation(self):
        """Test creation of mailing contact on creation of contact with tags with double optin"""
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Partner Tag',
            'send_double_opt_in': True
        })

        partner_tag = self.env['res.partner.category'].create({
            'name': 'Partner Tag',
        })
        partner = self.env['res.partner'].create({
            'name': 'Test Partner 4',
            'email': 'partnertest_4@example.com',
            'category_id': [partner_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', partner.email)])
        self.assertEqual(1, len(mailing_contact))
        self.assertTrue(mailing_contact.category_ids)

    def test_05_partner_creation(self):
        """Test updation of mailing contact on creation of contact with tags with double optin"""
        mailing_contact_1 = self.env['mailing.contact'].create({
            'name': 'Test Partner 5',
            'email': 'partnertest_5@example.com',
        })
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Partner Tag',
            'send_double_opt_in': True
        })

        partner_tag = self.env['res.partner.category'].create({
            'name': 'Partner Tag',
        })
        partner = self.env['res.partner'].create({
            'name': 'Test Partner 4',
            'email': 'partnertest_5@example.com',
            'category_id': [partner_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', partner.email)])
        self.assertEqual(1, len(mailing_contact))
