# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase

class TestPartnerProfileComplete(TransactionCase):

    def setUp(self):
        super().setUp()
        self.partner_model = self.env['res.partner']

    def test_profile_complete_true(self):
        """Debe marcar True si todos los campos están llenos"""
        partner = self.partner_model.create({
            'name': 'Cliente Completo',
            'facebook_url': 'https://facebook.com/test',
            'linkedin_url': 'https://linkedin.com/test',
            'twitter_url': 'https://twitter.com/test',
            'instagram_url': 'https://instagram.com/test',
        })
        self.assertTrue(partner.is_profile_complete)

    def test_profile_complete_false(self):
        """Debe marcar False si falta alguno de los campos"""
        partner = self.partner_model.create({
            'name': 'Cliente Incompleto',
            'facebook_url': 'https://facebook.com/test',
        })
        self.assertFalse(partner.is_profile_complete)
