# -*- coding: utf-8 -*-
from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    facebook_url = fields.Char(string='Facebook URL')
    linkedin_url = fields.Char(string='LinkedIn URL')
    twitter_url = fields.Char(string='Twitter URL')
    instagram_url = fields.Char(string='Instagram URL')

    is_profile_complete = fields.Boolean(
        string='Profile Complete',
        compute='_compute_is_profile_complete',
        store=True,
    )

    @api.depends('facebook_url', 'linkedin_url', 'twitter_url','instagram_url')
    def _compute_is_profile_complete(self):
        for rec in self:
            rec.is_profile_complete = bool(
                (rec.facebook_url or '').strip() and
                (rec.linkedin_url or '').strip() and
                (rec.instagram_url or '').strip() and
                (rec.twitter_url or '').strip()
            )
