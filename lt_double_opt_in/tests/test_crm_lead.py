##############################################################################
# Copyright (c) 2022 lumitec GmbH (https://www.lumitec.solutions)
# All Right Reserved
#
# See LICENSE file for full licensing details.
##############################################################################


from odoo.tests import common


class TestLead(common.TransactionCase):
    def setUp(self):
        super(TestLead, self).setUp()

    def test_01_lead_creation(self):
        """Test creation of mailing contact on creation of lead"""
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Tag',
        })
        crm_tag = self.env['crm.tag'].create({
            'name': 'Tag',
        })
        lead = self.env['crm.lead'].create({
            'name': 'Test Leads 1',
            'email_from': 'test_1@example.com',
            'tag_ids': [crm_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', lead.email_from)])
        self.assertEqual(1, len(mailing_contact))
        self.assertTrue(mailing_contact.category_ids)

    def test_02_lead_creation(self):
        """Test creation of mailing contact on creation of lead without tag"""
        lead = self.env['crm.lead'].create({
            'name': 'Test Leads 2',
            'email_from': 'test_2@example.com',
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', lead.email_from)])
        self.assertEqual(1, len(mailing_contact))
        self.assertFalse(mailing_contact.category_ids)

    def test_03_lead_creation(self):
        """Test creation of mailing contact on creation of lead with crm tag not in mailing tag"""
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Tag',
        })
        crm_tag = self.env['crm.tag'].create({
            'name': 'Crm Tag',
        })
        lead = self.env['crm.lead'].create({
            'name': 'Test Leads 3',
            'email_from': 'test_3@example.com',
            'tag_ids': [crm_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', lead.email_from)])
        self.assertEqual(1, len(mailing_contact))
        self.assertFalse(mailing_contact.category_ids)

    def test_04_lead_creation(self):
        """Test creation of mailing contact on creation of lead with tags with double optin"""
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Tag',
            'send_double_opt_in': True
        })
        crm_tag = self.env['crm.tag'].create({
            'name': 'Tag',
        })
        lead = self.env['crm.lead'].create({
            'name': 'Test Leads 4',
            'email_from': 'test_4@example.com',
            'tag_ids': [crm_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', lead.email_from)])
        self.assertEqual(1, len(mailing_contact))
        self.assertTrue(mailing_contact.category_ids)

    def test_05_lead_creation(self):
        """Test updation of mailing contact on creation of lead with tags with double optin"""
        mailing_contact_1 = self.env['mailing.contact'].create({
            'name': 'Test Leads 5',
            'email': 'test_5@example.com',
        })
        mailing_tag = self.env['mailing.tag'].create({
            'name': 'Tag',
            'send_double_opt_in': True
        })
        crm_tag = self.env['crm.tag'].create({
            'name': 'Tag',
        })
        lead = self.env['crm.lead'].create({
            'name': 'Test Leads 4',
            'email_from': 'test_5@example.com',
            'tag_ids': [crm_tag.id]
        })
        mailing_contact = self.env['mailing.contact'].search([('email', '=', lead.email_from)])
        self.assertEqual(1, len(mailing_contact))
