from flask import Flask, render_template, request

app = Flask(__name__)

def do_calculation(funct, number1, number2):
  if (funct=="addition"):
    return number1+number2
  elif (funct == "subtraction"):
    return number1-number2
  elif (funct == "multiplication"):
    return number1*number2
  elif (funct == "division"):
    return round(float(number1/number2),3)

@app.route('/', methods=["GET", "POST"])
def start():
  errors = []
  if request.method == "POST":
    number1 = None
    number2 = None
    calc = None
    try:
      number1 = float(request.form["number1"])
    except:
      errors.append("{!r} is not a number.\n".format(request.form["number1"]))
    try:
      number2 = float(request.form["number2"])
    except:
      errors.append("{!r} is not a number.\n".format(request.form["number2"]))
      error = "{!r} is not a number.".format(request.form["number2"])
      errors.append(error)
    try:
      calc = request.form["calc"]
      errors.append("{!r} selected".format(request.form["calc"]))
    except:
      errors.append("No calculation type selected.")

    if number1 is not None and number2 is not None and calc is not None:
      result = do_calculation(calc, number1, number2)
      return render_template("calculation.html", calc=calc, number1=number1, number2=number2, result=result)

      

  return render_template("index.html", errors=errors)


if __name__=="__main__":
  app.run(host='0.0.0.0')