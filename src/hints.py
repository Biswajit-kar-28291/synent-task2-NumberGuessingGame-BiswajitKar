def get_hint(secret_number, guess):
    difference=abs(secret_number-guess)

    if guess<secret_number:
        direction="Too low"
    else:
        direction="Too high"
    
    if difference <=5:
        closeness="Very close!"
    elif difference <=15:
        closeness="close!"
    else:
        closeness="Far away!"

    return f"{direction} | Hint: {closeness}"