import ploorunshell
def runPloo():
  text = input('ploo >')
  result, error = ploo.run('<stdin>', text)

  if error: print(error.as_string())
  else: print(result)