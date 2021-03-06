#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""


class CustomError(Exception):
    """Custom Error Class"""

    def __init__(self, message, cause):
        super(CustomError, self).__init__(message)
        self.message = message
        self.cause = cause
