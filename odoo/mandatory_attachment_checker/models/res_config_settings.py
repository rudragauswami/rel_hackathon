# -*- coding: utf-8 -*-

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    require_attachment_sale_order = fields.Boolean(
        string='Require Attachment on Sales Orders',
        related='company_id.require_attachment_sale_order',
        readonly=False,
    )
    require_attachment_purchase_order = fields.Boolean(
        string='Require Attachment on Purchase Orders',
        related='company_id.require_attachment_purchase_order',
        readonly=False,
    )
    require_attachment_invoice = fields.Boolean(
        string='Require Attachment on Invoices',
        related='company_id.require_attachment_invoice',
        readonly=False,
    )
    require_attachment_expense = fields.Boolean(
        string='Require Attachment on Expenses',
        related='company_id.require_attachment_expense',
        readonly=False,
    )
