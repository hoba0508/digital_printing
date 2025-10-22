# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.exceptions import AccessError
import base64

class BajukertasHelpdeskPortal(http.Controller):

    @http.route(['/helpdesk/login'], type='http', auth='public', website=True)
    def portal_login(self, **kwargs):
        return request.render('bajukertas_helpdesk.portal_login', {})

    @http.route(['/helpdesk/login/submit'], type='http', auth='public', methods=['POST'], website=True)
    def portal_login_submit(self, **kwargs):
        email = kwargs.get('login')
        password = kwargs.get('password')
        user = request.env['res.users'].sudo().search([('login', '=', email)], limit=1)
        if user and user._check_credentials(password):
            request.session.uid = user.id
            return request.redirect('/helpdesk/dashboard')
        return request.render('bajukertas_helpdesk.portal_login', {'error': 'Invalid credentials'})

    @http.route(['/helpdesk/dashboard'], type='http', auth='user', website=True)
    def portal_dashboard(self, **kwargs):
        user = request.env.user
        # Only allow customers (sales order partners)
        orders = request.env['sale.order'].sudo().search([('partner_id','=',user.partner_id.id)])
        tickets = request.env['bajukertas.helpdesk.ticket'].sudo().search([('order_id.partner_id','=',user.partner_id.id)])
        return request.render('bajukertas_helpdesk.portal_dashboard', {
            'orders': orders,
            'tickets': tickets
        })

    @http.route(['/helpdesk/ticket/create/<int:order_id>'], type='http', auth='user', website=True)
    def create_ticket_form(self, order_id, **kwargs):
        order = request.env['sale.order'].sudo().browse(order_id)
        if not order.exists() or order.partner_id != request.env.user.partner_id:
            return "Access Denied"
        return request.render('bajukertas_helpdesk.portal_ticket_form', {'order': order})

    @http.route(['/helpdesk/ticket/submit/<int:order_id>'], type='http', auth='user', methods=['POST'], website=True)
    def portal_ticket_submit(self, order_id, **kwargs):
        order = request.env['sale.order'].sudo().browse(order_id)
        if not order.exists() or order.partner_id != request.env.user.partner_id:
            return "Access Denied"

        # Get uploaded files
        attachments = kwargs.getlist('attachments')
        files = []
        for f in attachments:
            if f.filename:
                data = f.read()
                files.append((0, 0, {
                    'name': f.filename,
                    'datas': base64.b64encode(data),
                    'type': 'binary'
                }))

        # Create ticket
        request.env['bajukertas.helpdesk.ticket'].sudo().create({
            'name': kwargs.get('name'),
            'order_id': order.id,
            'description': kwargs.get('description'),
            'attachment_ids': files,
            'state': 'open',
        })
        return request.redirect('/helpdesk/dashboard')
