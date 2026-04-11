# -*- coding: utf-8 -*-
{
    'name': 'Mandatory Attachment Checker',
    'version': '19.0.1.0.0',
    'category': 'Technical',
    'summary': 'Company-level policy switches to enforce document attachments across Sales, Purchasing, Invoicing, and Expenses.',
    'description': """
Mandatory Attachment Checker
==============================

Enterprise-grade compliance guardrails for document-centric workflows. This module
exposes centralized, per-company toggles that designate whether supporting
attachments are mandatory before key business objects in **Sales**, **Purchases**,
**Accounting (Invoices)**, and **HR Expenses** can progress through validation
or posting—ideal for audit readiness, SOX-style controls, and hackathon demos
that showcase policy-driven ERP behavior without hard-coding rules into each app.

**Highlights**

* Single source of truth on ``res.company`` for attachment requirements.
* Native integration with ``res.config.settings`` for administrator-friendly setup.
* Clean dependency graph on ``base``, ``account``, ``sale_management``, ``purchase``,
  and ``hr_expense`` so policies align with the applications that own those documents.

Designed as a foundation module: enforcement logic (constraints, server actions, or
UI checks) can be layered on top while configuration remains consistent and
multi-company aware.
    """,
    'author': 'Rudra',
    'website': 'https://www.odoo.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'account',
        'hr_expense',
        'purchase',
        'sale_management',
    ],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
