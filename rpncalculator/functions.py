"""Built-in function library"""

import sys


def register(operator_name):
    """decorator to mark functions for auto-registration"""
    def decorator(functor):
        """perform the marking for auto-registration"""
        functor.is_registerable = True
        functor.operator_name = operator_name
        return functor
    return decorator


def register_all(engine):
    """iterate over all members of this module and register all functors with
    'register' attribute"""
    for name, val in sys.modules[__name__].__dict__.items():  # noqa
        if hasattr(val, 'is_registerable'):
            engine.register(val.operator_name, val)


@register('+')
def add(engine):
    """add the top two numbers on the stack"""
    engine.push(engine.pop() + engine.pop())

@register('-')
def subtract(engine):
    """subtract the last number on the stack from the prior"""
    engine.push(engine.pop(-2) - engine.pop(-1))

@register('/')
def divide(engine):
    """floating-point divide stack[-2] by stack[-1]"""
    divisor = engine.pop()
    dividend = engine.pop()
    engine.push(1. * dividend / divisor)

@register('*')
def multiply(engine):
    """floating-point multiply top two numbers on the stack"""
    engine.push(engine.pop() * engine.pop())

@register('^')
def power(engine):
    """floating-point raise stack[-2] to stack[-1] power"""
    engine.push(engine.pop(-2) ** engine.pop(-1))
