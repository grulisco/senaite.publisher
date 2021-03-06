# -*- coding: utf-8 -*-
#
# This file is part of SENAITE.LIMS
#
# Copyright 2018 by it's authors.
# Some rights reserved. See LICENSE and CONTRIBUTING.

from senaite.publisher import senaiteMessageFactory as _

# Value of key `format` must match the allowed CSS size attribute:
# https://developer.mozilla.org/en-US/docs/Web/CSS/@page/size
PAPERFORMATS = {
    "A4": {
        "name": _("European A4"),
        "format": "A4",
        "dpi": 96,
        "margin_top": 20.0,
        "margin_right": 20.0,
        "margin_bottom": 20.0,
        "margin_left": 20.0,
        "orientation": "portrait",
        "page_width": 210.0,
        "page_height": 297.0,
        "header_line": False,
        "header_spacing": 35.0,

    },

    "A5": {
        "name": _("European A5"),
        "format": "A5",
        "dpi": 96,
        "margin_top": 15.0,
        "margin_right": 15.0,
        "margin_bottom": 15.0,
        "margin_left": 15.0,
        "orientation": "portrait",
        "page_width": 148.0,
        "page_height": 210.0,
        "header_line": False,
        "header_spacing": 35.0,
    },

    "letter": {
        "name": _("US Letter"),
        "format": "letter",
        "dpi": 96,
        "margin_top": 20.0,
        "margin_right": 20.0,
        "margin_bottom": 20.0,
        "margin_left": 20.0,
        "orientation": "portrait",
        "page_width": 215.9,
        "page_height": 279.4,
        "header_line": False,
        "header_spacing": 35.0,
    },
}
