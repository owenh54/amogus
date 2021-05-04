controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        jumpCounter = 1
        mySprite.setVelocity(0, -100)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (mySprite.isHittingTile(CollisionDirection.Bottom)) {
        jumpCounter = 1
        mySprite.setVelocity(0, -100)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`spike`, function (sprite, location) {
    mySprite.setPosition(20, 200)
    pause(100)
    info.changeLifeBy(-1)
})
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(img`
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
        `)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(img`
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
        `)
})
let jumpCounter = 0
let mySprite: Sprite = null
mySprite = sprites.create(assets.image`amou`, SpriteKind.Player)
effects.starField.startScreenEffect()
scene.cameraFollowSprite(mySprite)
game.splash("amogus")
mySprite.say("sus")
tiles.setTilemap(tilemap`level1`)
mySprite.ay = 300
info.setLife(5)
mySprite.setPosition(20, 200)
mySprite.setStayInScreen(true)
controller.moveSprite(mySprite, 100, 0)
jumpCounter = 1
