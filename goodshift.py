"""Little script encouraging you to use the the right mod for the right key;
it deletes badly pressed modifier shortcuts and shift text"""
from pynput import keyboard

rightKeys = ['&', 'é', '"', '\'', '(', 'a', 'z', 'e', 'r', 't', 'q', 's', 'd', 'f', 'g', 'w', 'x', 'c', 'v', 'b']
leftKeys = ['è', '_', 'ç', 'à', ')', '=', 'Y', 'u', 'i', 'o', 'p', '^', '$', 'h', 'j', 'k', 'l', 'm', 'ù', '*', 'n', ',', ';', ':', '!']
rightModKeys = [keyboard.Key.shift_r]
leftModKeys = [keyboard.Key.shift]

kbd = keyboard.Controller()
leftModPressed = False
rightModPressed = False


def on_press(key):
    global rightModPressed
    global leftModPressed

    print(str(key))
    print(str(key).strip("'"))

    if key in leftModKeys:
        leftModPressed = True
        print(f"Left mod key pressed: {key}")

    if key in rightModKeys:
        rightModPressed = True
        print(f"Right mod key pressed: {key}")

    if (str(key).strip("'") in rightKeys) and rightModPressed:
        kbd.press(keyboard.Key.backspace)
        kbd.release(keyboard.Key.backspace)
        print(f"Bad combination pressed; deleting last character ({key})")

    if (str(key).strip("'") in leftKeys) and leftModPressed:
        kbd.press(keyboard.Key.backspace)
        kbd.release(keyboard.Key.backspace)
        print(f"Bad combination pressed; deleting last character ({key})")


def on_release(key):
    global leftModPressed
    global rightModPressed

    if key in leftModKeys:
        leftModPressed = True
        print(f"Left mod key released: {key}")

    elif key in rightModKeys:
        rightModPressed = False
        print(f"Right mod key released: {key}")


if __name__ == '__main__':
    with keyboard.Listener(on_press=on_press, on_release=on_release) as l:
        l.join()
