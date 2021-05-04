def on_up_pressed():
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f f f . . . . . . . . . 
                . . . f 9 9 6 f . . . . . . . . 
                . . . f 1 9 6 f f f f f f f f f 
                . . f f 1 9 6 f 2 2 2 2 2 2 2 f 
                . f 2 f 9 9 6 f 2 2 2 2 2 2 2 f 
                . f 2 f 9 6 6 f 2 2 2 2 f f f f 
                . f 2 f f 6 f f 2 2 2 c f . . . 
                . f 2 2 f f f 2 2 2 2 c f . . . 
                . f 2 2 2 2 2 2 2 2 c c f f f f 
                . f 2 2 2 2 2 2 2 c c c c c c f 
                . . f 2 2 2 2 c c c c c c c c f 
                . . . f f f f f f f f f f f f f 
                . . . . . f 2 2 2 c c c f . . . 
                . . . . . f f 2 c c c f f . . . 
                . . . . . . f f f f f f . . . .
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    controller.move_sprite(mySprite, 100, 100)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f . . . . . 
                . . . . f 2 2 2 2 2 2 f . . . . 
                . . f f f f f f 2 2 2 2 f . . . 
                . f 9 1 1 9 9 f f 2 2 2 f . . . 
                . f 9 9 9 9 6 6 f 2 2 2 f f f . 
                . f 6 6 6 6 6 f f 2 2 2 f 2 f f 
                . . f f f f f f 2 2 2 c f 2 2 f 
                . . . f 2 2 2 2 2 2 2 c f 2 c f 
                . . . f 2 2 2 2 2 2 c c f c c f 
                . . . f 2 2 2 2 2 c c c f c c f 
                . . . f 2 2 2 c c c c c f c f f 
                . . . f 2 2 f f f f c c f f f . 
                . . . f 2 2 f . . f c c f . . . 
                . . . f 2 2 f . . f c c f . . . 
                . . . f f f f . . f f f f . . .
    """))
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    mySprite.set_image(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f . . . . . 
                . . . . f 2 2 2 2 2 2 f . . . . 
                . . . f 2 2 2 2 f f f f f f . . 
                . . . f 2 2 2 f f 9 9 1 1 9 f . 
                . f f f 2 2 2 f 6 6 9 9 9 9 f . 
                f f 2 f 2 2 2 f f 6 6 6 6 6 f . 
                f 2 2 f c 2 2 2 f f f f f f . . 
                f c 2 f c 2 2 2 2 2 2 2 f . . . 
                f c c f c c 2 2 2 2 2 2 f . . . 
                f c c f c c c 2 2 2 2 2 f . . . 
                f f c f c c c c c 2 2 2 f . . . 
                . f f f c c f f f f 2 2 f . . . 
                . . . f c c f . . f 2 2 f . . . 
                . . . f c c f . . f 2 2 f . . . 
                . . . f f f f . . f f f f . . .
    """))
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_down_pressed():
    mySprite.set_image(img("""
        . . . . f f f f f f . . . . . . 
                . . . f f c c c 2 f f . . . . . 
                . . . f c c c 2 2 2 f . . . . . 
                f f f f f f f f f f f f f . . . 
                f c c c c c c c c 2 2 2 2 f . . 
                f c c c c c c 2 2 2 2 2 2 2 f . 
                f f f f c c 2 2 2 2 2 2 2 2 f . 
                . . . f c 2 2 2 2 f f f 2 2 f . 
                . . . f c 2 2 2 f f 6 f f 2 f . 
                f f f f 2 2 2 2 f 6 6 9 f 2 f . 
                f 2 2 2 2 2 2 2 f 6 9 9 f 2 f . 
                f 2 2 2 2 2 2 2 f 6 9 1 f f . . 
                f f f f f f f f f 6 9 1 f . . . 
                . . . . . . . . f 6 9 9 f . . . 
                . . . . . . . . . f f f . . . . 
                . . . . . . . . . . . . . . . .
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

mySprite: Sprite = None
mySprite = sprites.create(assets.image("""amou"""), SpriteKind.player)
controller.move_sprite(mySprite)
effects.star_field.start_screen_effect()
scene.camera_follow_sprite(mySprite)
game.splash("amogus")
mySprite.say("sus")
