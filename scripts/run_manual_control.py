import holoocean
from manual_control import key_controlling
from pynput import keyboard

pressed_keys = list()
FORCE = 55
TORQUE = 0.05
GIRO = 5

def on_press(key):
    global pressed_keys
    if hasattr(key, 'char'):
        pressed_keys.append(key.char)
        pressed_keys = list(set(pressed_keys))

def on_release(key):
    global pressed_keys
    if hasattr(key, 'char'):
        pressed_keys.remove(key.char)

listener = keyboard.Listener(
    on_press = on_press,
    on_release = on_release)
listener.start()


with holoocean.make("SimpleUnderwater") as env:
    while True:
        if 'q' in pressed_keys:
            break
        command = key_controlling.parse_keys_drone(pressed_keys, FORCE, TORQUE, GIRO)

        env.act("auv0", command)
        state = env.tick()