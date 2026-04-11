# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        Attachment = self.env['ir.attachment'].sudo()
        for order in self:
            company = order.company_id or self.env.company
            if not company.require_attachment_sale_order:
                continue
            count = Attachment.search_count([
                ('res_model', '=', self._name),
                ('res_id', '=', order.id),
            ])
            if count == 0:
                raise UserError(_(
                    'Sales order "%s" cannot be confirmed: your company policy requires '
                    'at least one attachment on the order before confirmation, and none '
                    'were found. Add a file via the chatter attachments, then try again.',
                    order.display_name,
                ))
        return super().action_confirm()


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        Attachment = self.env['ir.attachment'].sudo()
        for order in self.filtered(lambda o: o.state in ('draft', 'sent')):
            company = order.company_id or self.env.company
            if not company.require_attachment_purchase_order:
                continue
            count = Attachment.search_count([
                ('res_model', '=', self._name),
                ('res_id', '=', order.id),
            ])
            if count == 0:
                raise UserError(_(
                    'Purchase order "%s" cannot be confirmed: your company policy requires '
                    'at least one attachment on the order before confirmation, and none '
                    'were found. Add a file via the chatter attachments, then try again.',
                    order.display_name,
                ))
        return super().button_confirm()


class AccountMove(models.Model):
    _inherit = 'account.move'

    def action_post(self):
        Attachment = self.env['ir.attachment'].sudo()
        for move in self.filtered(lambda m: m.is_invoice()):
            company = move.company_id or self.env.company
            if not company.require_attachment_invoice:
                continue
            count = Attachment.search_count([
                ('res_model', '=', self._name),
                ('res_id', '=', move.id),
            ])
            if count == 0:
                raise UserError(_(
                    'Invoice "%s" cannot be posted: your company policy requires at least '
                    'one attachment on customer invoices and vendor bills before posting, '
                    'and none were found. Add a file via the chatter attachments, then try '
                    'again.',
                    move.display_name,
                ))
        return super().action_post()


class HrExpense(models.Model):
    _inherit = 'hr.expense'

    def action_submit_expenses(self):
        Attachment = self.env['ir.attachment'].sudo()
        for expense in self:
            company = expense.company_id or self.env.company
            if not company.require_attachment_expense:
                continue
            count = Attachment.search_count([
                ('res_model', '=', self._name),
                ('res_id', '=', expense.id),
            ])
            if count == 0:
                raise UserError(_(
                    'Expense "%s" cannot be submitted: your company policy requires at least '
                    'one attachment on the expense before submission, and none were found. '
                    'Add a receipt or supporting document, then try again.',
                    expense.display_name,
                ))
        return super().action_submit_expenses()
