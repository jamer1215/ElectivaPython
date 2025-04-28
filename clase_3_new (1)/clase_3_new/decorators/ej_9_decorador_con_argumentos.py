def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print(f"Mis argumentos son: {arg1}, {arg2}")
        return function(arg1, arg2)
    return wrapper_accepting_arguments


@decorator_with_arguments
def cities(city_one, city_two):
    return f"Ciudades que me gustan {city_one} y {city_two}"
    # return "algo"

# Lo siguiente es lo mismo que hacer:  wrapper_accepting_arguments("Puerto La Cruz", "Barquisimeto")
ciudades = cities("Puerto La Cruz", "Barquisimeto")
print(ciudades)