import re
equation = '(- x^2+3.5xy) + y + 10 = y^2 - xy + y'

ADDENDUM_RE = re.compile(r'^(?:(?:[+-])?(?:\d*\.\d+|\d+))$|^(?:(?:[+-])?(?:\d*\.\d+|\d+)?(?:[a-zA-Z]{1}(?:\^[+-]?\d+)?)+)$')  # noqa
SIGN_RE = re.compile(r'([+-])')
COEFFICIENT_RE = re.compile(r'(\d*\.\d+|\d+)')
VARIABLE_RE = re.compile(r'([a-zA-Z]{1}(?:\^[+-]?\d+)?)')


def simplify(equation):
    """Привести уравнение к каноническому виду."""
    parts = equation.split('=')
    if len(parts) != 2:
        raise SyntaxError('{} is not valid equation'.format(equation))
    parts = [part.strip() for part in parts]

    left, right = parts
    left_coefficients = get_coefficients(left)
    right_coefficients = get_coefficients(right)

    for variables, coefficient in right_coefficients.items():
        new_coefficient = left_coefficients.get(variables, 0) - coefficient
        left_coefficients[variables] = new_coefficient

    return coefficients_to_equation(left_coefficients)


def remove_parentheses(expression):
    """Удалить скобки из строкового выражения."""
    cleared = ''
    opened = 0
    for symbol in expression:
        if symbol == '(':
            opened += 1
        elif symbol == ')':
            if opened == 0:
                raise SyntaxError('Unpaired parentheses')
            opened -= 1
        else:
            cleared += symbol
    if opened > 0:
        raise SyntaxError('Unpaired parentheses')
    return cleared


def get_coefficients(expression):
    """Получить коэффициенты из строкового выражения уравнения."""
    coefficients = {}
    cleared_expression = remove_parentheses(expression)
    elements = []
    element = ''
    for symbol in cleared_expression:
        if symbol in ('+', '-'):
            if not element:
                element += symbol
                continue
            elements.append(element.strip())
            element = symbol
        else:
            element += symbol
    if element:
        elements.append(element.strip())
    for element in elements:
        element = element.replace(' ', '')
        if not ADDENDUM_RE.match(element):
            raise SyntaxError('Invalid addendum {}'.format(element))
        sign = SIGN_RE.findall(element)
        if not sign:
            sign = '+'
        else:
            sign = sign[0]
        element = SIGN_RE.sub('', element)
        variables = sorted(VARIABLE_RE.findall(element))
        if not variables:
            variables = '1'
        else:
            variables = ''.join(variables)
        element = VARIABLE_RE.sub('', element)
        coefficient = COEFFICIENT_RE.findall(element)
        if not coefficient:
            coefficient = '1'
        else:
            coefficient = ''.join(coefficient)
        new_coefficient = coefficients.get(variables, 0)
        new_coefficient += float('{}{}'.format(sign, coefficient))
        coefficients[variables] = new_coefficient
    return coefficients


def coefficients_to_equation(coefficients):
    """Преобразовать коэффициенты в строку уравнения."""
    equation = ''
    for variables in sorted(coefficients.keys()):
        coefficient = coefficients[variables]
        if coefficient == 0:
            continue
        if variables == '1':
            equation += '{:+}'.format(coefficient)
            continue
        if coefficient == 1:
            equation += '+{}'.format(variables)
            continue
        if coefficient == -1:
            equation += '-{}'.format(variables)
            continue
        equation += '{:+}{}'.format(coefficient, variables)
    equation = equation.replace('-', ' - ')
    equation = equation.replace('+', ' + ')
    equation = equation.strip('+ ')
    equation += " = 0"
    return equation
