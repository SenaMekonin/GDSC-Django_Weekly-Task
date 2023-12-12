# 1 (A) (Basic Operation function)
def basic_operation(a,b):
    sum = a + b
    sub = a - b
    multi = a * b
    try:
        div = a / b
    except:
        print("Number can't didvide by Zero")
    return sum, sub, multi, div
print("Basic Operation Result:", basic_operation(10,5))
# 1 (B) (Power Operation function)
def power_operation(base, exponent, **kwargs):
    po = base ** exponent
    try:
        base % kwargs['modulo']
    except KeyError:
        return {"Power result": po}
    else:
        modulo = base % kwargs['modulo']

        return {'Power result': po, 'modulo': modulo}
print("Power Operation Result: ", power_operation(2,3))
print("Power Operation Result with Modulo Result:", power_operation(2,3, modulo=5) )
# 1 (C) (Exception Handling)
def apply_operations(operation_list):
    results = []
    for operation in operation_list:
        try:
            result = operation[0](*operation[1])
            results.append(result)
        except Exception as e:
            results.append(f"Error: {e}")

    return results

        # Test apply_operations with exception handling
operations= [
            (lambda x, y: x + y, (3, 4)),

            (lambda x, y: x * y, (2, 5)),
        ]
print("Apply Result:", apply_operations(operations))


