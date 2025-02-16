from flask import Flask, render_template, request


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        a = float(request.form["a"])
        b = float(request.form["b"])
        n = int(request.form["n"])
        resultado, suma, formula_valores = expandir_binomio(a, b, n)
        return render_template(
            "index.html",
            resultado=resultado,
            suma=suma,
            formula_valores=formula_valores,
            a=a,
            b=b,
            n=n,
        )
    return render_template(
        "index.html",
        resultado=None,
        suma=None,
        formula_valores=None,
        a=None,
        b=None,
        n=None,
    )


def coef_binomial(n, k):
    import math

    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


def format_number(num):
    if num.is_integer():
        return str(int(num))
    else:
        return str(num)


def expandir_binomio(a, b, n):
    expansion = "$$"
    formula_valores = f"$$({a} + {b})^{n} ="
    suma_total = 0
    for k in range(n + 1):
        coef = coef_binomial(n, k)
        term_value = coef * (a ** (n - k)) * (b**k)
        suma_total += term_value
        a_formatted = format_number(a)
        b_formatted = format_number(b)
        coef_formatted = format_number(coef)
        term = f"{coef_formatted}{a_formatted}^{{{n-k}}}{b_formatted}^{{{k}}}"
        term_valores = (
            f"{coef_formatted}({a_formatted})^{{{n-k}}}({b_formatted})^{{{k}}}"
        )
        if k > 0:
            expansion += " + " + term
            formula_valores += " + " + term_valores
        else:
            expansion += term
            formula_valores += term_valores
    expansion += "$$"
    formula_valores += "$$"
    return expansion, suma_total, formula_valores


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)