#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring"""


class BaseError(Exception):
    """Base Error Class"""
    pass


class StringError(BaseError, TypeError):
    """String Error Class"""
    pass


class NumberError(BaseError, TypeError):
    """Number error Class"""
    pass


class NonZeroError(NumberError):
    """Non Zero Error Class"""
    pass
