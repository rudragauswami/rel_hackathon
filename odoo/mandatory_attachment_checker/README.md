# Mandatory Attachment Checker

**Stop confirming orders, posting invoices, and submitting expenses without a paper trail.** One settings screen, four toggles, zero ambiguity: teams attach evidence in the chatter *before* critical actions complete—so finance, audit, and operations stay aligned.

[![Odoo](https://img.shields.io/badge/Odoo-19.0-714B67?logo=odoo&logoColor=white)](https://www.odoo.com/)
[![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)](https://www.gnu.org/licenses/lgpl-3.0.en.html)
[![Module](https://img.shields.io/badge/module-mandatory__attachment__checker-875A7B)](./__manifest__.py)

---

## Key features

- **Company-scoped policies** — Each company chooses its own rules; no cross-company surprises in multi-company databases.
- **Native Settings UX** — Toggles live under **Settings** with the same `app` / `block` / `setting` layout users already know from core Odoo.
- **Four enforcement points** — Sales orders (`action_confirm`), purchase orders (`button_confirm`), customer/vendor invoices (`action_post`), and expenses (`action_submit_expenses`).
- **Clear, actionable errors** — When a rule fires, users get a professional `UserError` that names the document and tells them to add a file via the chatter (or receipt on expenses).
- **Attachment-aware counting** — Uses `ir.attachment` with elevated read for counting so record rules on files do not produce false “missing attachment” blocks.
- **Invoice-only posting guard** — Journal entries that are not invoices are not blocked; only moves where `is_invoice()` applies are validated.

---

## How to configure

1. **Add the module to your addons path**  
   Ensure the folder containing `mandatory_attachment_checker` is listed in your Odoo `addons_path`, then restart Odoo if you changed configuration.

2. **Install the module**  
   Enable **Developer Mode** (optional but helpful), open **Apps**, remove the *Apps* filter, search for **Mandatory Attachment Checker**, and click **Install**.

3. **Open Settings**  
   Go to **Settings** (gear menu) and find the **Mandatory attachments** application block (or search the settings page for “attachment”).

4. **Enable the policies you need**  
   For each line of business, turn on the checkbox that matches your control objective:
   - **Sales orders** — require at least one attachment before confirmation.
   - **Purchase orders** — same for vendor PO confirmation.
   - **Invoices** — require at least one attachment before posting customer invoices and vendor bills.
   - **Expenses** — require at least one attachment before submitting expenses to a report.

5. **Save**  
   Use the standard **Save** control on the settings form. Values are stored on the **current company** (`res.company`).

6. **Communicate to users**  
   Brief power users: attachments must be added through the **chatter** on the document (or as expense attachments) *before* they click Confirm / Post / Submit.

---

## How it works

1. **Storage** — Four boolean fields on `res.company` hold the policy flags. `res.config.settings` exposes them as related fields (`readonly=False`) so administrators edit company data through Settings.

2. **UI** — `views/res_config_settings_views.xml` inherits `base.res_config_settings_view_form` and injects a dedicated **Mandatory attachments** app block with explanatory muted help text under each toggle.

3. **Validation** — `models/attachment_validator.py` inherits `sale.order`, `purchase.order`, `account.move`, and `hr.expense`. Before calling `super()` on the respective workflow method, each override checks the **document’s** `company_id` flag. If the policy is on, it counts `ir.attachment` rows linked to that record (`res_model` + `res_id`). A count of zero raises a translated `UserError`; otherwise processing continues normally.

4. **Dependencies** — The module depends on `base`, `account`, `sale_management`, `purchase`, and `hr_expense` so all extended models are present at install time.

---

## Apps “Module Info” / `index.html` not showing

Odoo loads the rich description from **`mandatory_attachment_checker/static/description/index.html`** only when it can resolve the module folder on disk:

1. **`addons_path` must point at the directory that *directly* contains the module folder**  
   If this repo lives at `…/rel_hackathon`, the module path is `…/rel_hackathon/odoo/mandatory_attachment_checker`, so **`addons_path` must include `…/rel_hackathon/odoo`**, not only the repository root. If that path is wrong, Odoo raises `FileNotFoundError` for `index.html` and falls back to the plain manifest **`description`** (RST), so you will not see your HTML layout.

2. **Restart Odoo** after changing `addons_path`, then **Apps → Update Apps List** (with Developer Mode on).

3. **Open the right screen**  
   The kanban card only shows the short **summary**. The full HTML is shown when you open the module and use **Module Info** / the description area on the module form (wording varies slightly by Odoo version).

4. **Sanitizer**  
   Odoo runs module HTML through **`html_sanitize`**, which **removes `<style>` and `<script>` tags**. This module’s `index.html` uses **inline `style="..."` attributes** so layout survives sanitization.

---

## Store banner asset

For Odoo Apps listings, place your **`banner.png`** (recommended landscape artwork) in **`static/description/`**. The manifest already references `static/description/banner.png`; add the file before publishing—no placeholder is shipped in the repository.

---

*Built for hackathon demos and teams who want attachment policy in configuration—not buried in one-off scripts.*
