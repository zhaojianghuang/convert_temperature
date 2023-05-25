def fahrenheit_to_celsius(temperature_fahrenheit):
	"""
	Converts temperature in fahrenheit to celsius

	Parameters:
	temperature_fahrenheit

	Returns:
	temperature_celsius

	"""
	temp_celsius = (temperature_fahrenheit - 32) - (5.0/9.0)
	return temp_celsius
