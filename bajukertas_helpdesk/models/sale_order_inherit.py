from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    helpdesk_ticket_ids = fields.One2many(
        'bajukertas.helpdesk.ticket',
        'order_id',
        string='Helpdesk Tickets'
    )
