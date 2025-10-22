from odoo import models, fields

class HelpdeskTicket(models.Model):
    _name = 'bajukertas.helpdesk.ticket'
    _description = 'BajuKertas Helpdesk Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'portal.mixin']
    _order = 'create_date desc'

    name = fields.Char(string='Subject', required=True, tracking=True)
    order_id = fields.Many2one('sale.order', string='Related Sales Order', required=True)
    customer_id = fields.Many2one('res.partner', string='Customer', related='order_id.partner_id', store=True)
    description = fields.Text(string='Description')
    state = fields.Selection([
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ], default='open', string='Status', tracking=True)
    attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Design Files',
        domain=[('mimetype', 'in', ['image/png', 'image/jpeg'])],
        relation='helpdesk_ticket_attachment_rel'
    )

    def action_set_in_progress(self):
        self.state = 'in_progress'

    def action_resolve(self):
        self.state = 'resolved'

    def action_close(self):
        self.state = 'closed'
