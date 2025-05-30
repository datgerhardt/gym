import math
import operator as op 

# Type Definition 

Symbol = str 
Number = (int, float)
Atom = (Symbol, Number)
List = list
Exp = (Atom, List)
Env = dict


def tokenize(chars: str) -> list:
    """ Convert string of charaters into tokens

    >>> tokenize("(begin (define r 10) (* pi (* r r)))")
    ['(', 'begin', '(', 'define', 'r', '10', ')', '(', '*', 'pi', '(', '*', 'r', 'r', ')', ')', ')']
    """
    return chars.replace('(', ' ( ').replace(')', ' ) ').split()

def parse(program: str) -> Exp:
    """Read Scheme Expression from string

    >>> parse("(begin (define r 10) (* pi (* r r)))")
    ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]
    """
    return read_from_tokens(tokenize(program))
                           
def read_from_tokens(tokens: list) -> Exp:
    """ Convert Tokens into Exp 
    
    >>> tokens = ['(', 'begin', '(', 'define', 'r', '10', ')', '(', '*', 'pi', '(', '*', 'r', 'r', ')', ')', ')']
    >>> read_from_tokens(tokens)
    ['begin', ['define', 'r', 10], ['*', 'pi', ['*', 'r', 'r']]]

    >>> read_from_tokens([')'])
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected EOF
    """
    if len(tokens) == 0:
        raise SyntaxError('unexpected EOF')
    token = tokens.pop(0)
    if token == '(':
        L = []
        while tokens[0] != ')':
            L.append(read_from_tokens(tokens))
        tokens.pop(0) # pop off ')'
        return L
    elif token == ')':
        raise SyntaxError('unexpected EOF')
    else:
        return atom(token)

def atom(token: str) -> Atom:
    try: return int(token)
    except ValueError:
        try: return float(token)    
        except ValueError:
            return Symbol(token)    


def standard_env() -> Env:
    "An environment with some Scheme standard procedures."
    env = Env()
    env.update(vars(math)) # sin, cos, sqrt, pi, ...
    env.update({
        '+':op.add, '-':op.sub, '*':op.mul, '/':op.truediv, 
        '>':op.gt, '<':op.lt, '>=':op.ge, '<=':op.le, '=':op.eq, 
        'abs':     abs,
        'append':  op.add,  
        'apply':   lambda proc, args: proc(*args),
        'begin':   lambda *x: x[-1],
        'car':     lambda x: x[0],
        'cdr':     lambda x: x[1:], 
        'cons':    lambda x,y: [x] + y,
        'eq?':     op.is_, 
        'expt':    pow,
        'equal?':  op.eq, 
        'length':  len, 
        'list':    lambda *x: List(x), 
        'list?':   lambda x: isinstance(x, List), 
        'map':     map,
        'max':     max,
        'min':     min,
        'not':     op.not_,
        'null?':   lambda x: x == [], 
        'number?': lambda x: isinstance(x, Number),  
		'print':   print,
        'procedure?': callable,
        'round':   round,
        'symbol?': lambda x: isinstance(x, Symbol),
    })
    return env


def repl(prompt="λ> "):
    while True:
        val = eval(parse(input(prompt)))
        if val is not None:
            print(schemestr(val))

            
def schemestr(exp):
    if isinstance(exp, List):
        return '(' + " ".join(map(schemestr(exp))) + ')'
    else:
        return str(exp)

class Env(dict):
    "An environment: a dict of {'var': val} pairs, with an outer Env."
    def __init__(self, parms=(), args=(), outer=None):
        self.update(zip(parms, args))
        self.outer = outer
    def find(self, var):
        return self if (var in self) else self.outer.find(var) 

class Procedure(object):
    "A user-defined Scheme procedure."
    def __init__(self, parms, body, env):
        self.parms, self.body, self.env = parms, body, env
    def __call__(self, *args):
        return eval(self.body, Env(self.parms, args, self.env))

global_env = standard_env()

def eval(x, env=global_env) -> Exp:
    "Evaluate an expression in an environment."
    if isinstance(x, Symbol):
        return env.find(x)[x]
    elif not isinstance(x, List):
        return x
    op, *args = x
    if op == 'quote':
        return args[0]
    elif op == 'if':
        (_, test, conseq, alt) = x
        exp = (conseq if eval(test, env) else alt)
        return eval(exp, env)
    elif op == 'define':
        (_, symbol, exp) = x
        env[symbol] = eval(exp,env)
    elif op == 'set!':
        (symbol, exp) = args
        env.find(symbol)[symbol] = eval(exp, env)
    elif op == 'lambda':
        (parms, body) = args
        return Procedure(parms, body, env)
    else:
        proc = eval(op, env)
        args = [eval(arg, env) for arg in args]
        return proc(*args)
        
if __name__ == "__main__":
    import doctest
    doctest.testmod()

