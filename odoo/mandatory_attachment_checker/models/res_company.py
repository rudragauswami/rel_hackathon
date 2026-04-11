# -*- coding: utf-8 -*-

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = 'res.company'

    require_attachment_sale_order = fields.Boolean(
        string='Require Attachment on Sales Orders',
        default=False,
        help='When enabled, sales order confirmation is blocked if no attachment '
             'is present on the order.',
    )
    require_attachment_purchase_order = fields.Boolean(
        string='Require Attachment on Purchase Orders',
        default=False,
        help='When enabled, purchase order confirmation is blocked if no attachment '
             'is present on the order.',
    )
    require_attachment_invoice = fields.Boolean(
        string='Require Attachment on Invoices',
        default=False,
        help='When enabled, invoice confirmation or posting is blocked if no '
             'attachment is present on the invoice.',
    )
    require_attachment_expense = fields.Boolean(
        string='Require Attachment on Expenses',
        default=False,
        help='When enabled, expense submission or approval steps are blocked if '
             'no attachment is present on the expense.',
    )
