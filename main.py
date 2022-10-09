def on_bluetooth_connected():
    basic.show_icon(IconNames.HAPPY)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SAD)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

# need bluetooth mouse service to be activated. (press A+B)

def on_button_pressed_a():
    mouse.click()
    basic.show_icon(IconNames.HAPPY)
    basic.pause(100)
    basic.show_leds("""
        . # . . .
                . # # . .
                . # # # .
                . # # . .
                . . . # .
    """)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    # bluetooth mouse service activated
    mouse.start_mouse_service()
    basic.show_leds("""
        . # . . .
                . # # . .
                . # # # .
                . # # . .
                . . . # .
    """)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

basic.show_leds("""
    . . . # .
        . . . # .
        . # # # .
        . # . # .
        . # . # .
""")

def on_forever():
    if input.pin_is_pressed(TouchPin.P0):
        mouse.click()
        if input.pin_is_pressed(TouchPin.P0):
            mouse.click()
basic.forever(on_forever)
