# controllers/main.py
# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CustomersController(http.Controller):

    @http.route(['/customers'], type='http', auth='public', website=True)
    def customers_page(self, **kw):
        # Busca los clientes (res.partner con is_company o customer_rank > 0)
        customers = request.env['res.partner'].sudo().search([('customer_rank', '>', 0)])
        return request.render('crm_social_profile_full.view_customers_page', {
            'customers': customers
        })
