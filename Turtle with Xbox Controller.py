import turtle, pygame
pad1 = pygame.joystick.Joystick(0)# Create a new controller object
racer1 = turtle.Turtle()
racer1.shape('turtle')
window = turtle.Screen()
window.listen()

while True:
    racer1.forward(2)
    # Hats are what pygame calls the d-pad buttons 
    hats = redJoystick.get_numhats() 
    for i in range(hats):
        hat = redJoystick.get_hat(i)
        if str(hat) == "(1, 0)":# Right
            racer1.setheading(0)
        if str(hat) == "(-1, 0)":# Left
            racer1.setheading(180)
        if str(hat) == "(0, 1)":# Up
            racer1.setheading(90)
        if str(hat) == "(0, -1)":# Down
            racer1.setheading(270)
