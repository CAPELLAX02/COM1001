def fahrenheitToCelsius(t):
 # Convert Fahrenheit temperature to Celsius.
  convertedTemperature = (5 / 9) * (t - 32)
  return convertedTemperature

fahrenheitTemp = eval(input("Enter a temperature in degrees Fahrenheit: "))
celsiusTemp = fahrenheitToCelsius(fahrenheitTemp)

print("Celsius equivalent:", celsiusTemp, "degrees")