from odoo import http
from odoo.http import request

class HelpdeskPortal(http.Controller):

    @http.route(['/helpdesk'], type='http', auth='user', website=True)
    def portal_ticket_list(self, **kwargs):
        # Show all tickets of the logged-in customer
        tickets = request.env['bajukertas.helpdesk.ticket'].sudo().search([
            ('customer_id', '=', request.env.user.partner_id.id)
        ])
        return request.render('bajukertas_helpdesk.portal_ticket_list', {'tickets': tickets})

    @http.route(['/helpdesk/new'], type='http', auth='user', website=True)
    def portal_ticket_form(self, **kwargs):
        # Show form to create new ticket
        orders = request.env['sale.order'].sudo().search([
            ('partner_id', '=', request.env.user.partner_id.id)
        ])
        return request.render('bajukertas_helpdesk.portal_ticket_form', {'orders': orders})

    @http.route(['/helpdesk/create'], type='http', auth='user', methods=['POST'], website=True)
    def portal_ticket_create(self, **post):
        attachments = post.getlist('attachment_ids')
        ticket_vals = {
            'name': post.get('name'),
            'order_id': int(post.get('order_id')),
            'customer_id': request.env.user.partner_id.id,
            'description': post.get('description'),
        }
        ticket = request.env['bajukertas.helpdesk.ticket'].sudo().create(ticket_vals)

        # Handle attachments
        for f in attachments:
            attachment = request.env['ir.attachment'].sudo().create({
                'name': f.filename,
                'type': 'binary',
                'datas': f.read().encode('base64') if hasattr(f, 'read') else None,
                'res_model': 'bajukertas.helpdesk.ticket',
                'res_id': ticket.id,
            })
            ticket.write({'attachment_ids': [(4, attachment.id)]})

        return request.redirect('/helpdesk')
