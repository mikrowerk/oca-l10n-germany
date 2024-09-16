# Copyright 2015 Tecnativa - Antonio Espinosa
# Copyright 2015 Tecnativa - Jairo Llopis
# Copyright 2015 Tecnativa - David Vidal
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    "name": "NUTS Regions for German",
    "summary": "NUTS specific options for German",
    "version": "17.0.1.0.1",
    "category": "Localisation/Europe",
    "website": "https://github.com/OCA/l10n-germany",
    "author": "Tecnativa, " "Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "depends": [
        "base_location_nuts",
    ],
    "post_init_hook": "post_init_hook",
    "installable": True,
    "maintainers": ["rafaelbn", "edlopen"],
}
