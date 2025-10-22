# from odoo import http


# class BajukertasHelpdesk(http.Controller):
#     @http.route('/bajukertas_helpdesk/bajukertas_helpdesk', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bajukertas_helpdesk/bajukertas_helpdesk/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('bajukertas_helpdesk.listing', {
#             'root': '/bajukertas_helpdesk/bajukertas_helpdesk',
#             'objects': http.request.env['bajukertas_helpdesk.bajukertas_helpdesk'].search([]),
#         })

#     @http.route('/bajukertas_helpdesk/bajukertas_helpdesk/objects/<model("bajukertas_helpdesk.bajukertas_helpdesk"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bajukertas_helpdesk.object', {
#             'object': obj
#         })

