import pgzrun
import random
# === Game Constants ===
GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50
WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID_SIZE
GUARDMOVEINTERVAL = 0.5
BACKGROUNDSEED = 12345
# === Game Map ===
MAP = [
    "WWWWWWWWWWWWWWWW",
    "W              W",
    "W              W",
    "W  W  KG       W",
    "W  WWWWWWWWWW  W",
    "W              W",
    "W      P       W",
    "W  WWWWWWWWWW  W",
    "W      GK   W  W",
    "W              W",
    "W              D",
    "WWWWWWWWWWWWWWWW"
]
# === Game State ===
player = None
guards = []
keysToCollect = []
gameOver = False
# === Coordinate Conversion ===
def GetScreenCoords(x, y):
    return (x * GRID_SIZE, y * GRID_SIZE)

def GetActorGridPos(actor):
    return (round(actor.x / GRID_SIZE), round(actor.y / GRID_SIZE))
# === Setup Game ===

def SetupGame():
    global player, keysToCollect, guards, gameOver
    gameOver = False
    player = Actor("player", anchor=("left", "top"))
    keysToCollect = []
    guards = []
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "P":
                player.pos = GetScreenCoords(x, y)
            elif square == "K":
                key = Actor("key", anchor=("left", "top"))
                key.pos = GetScreenCoords(x, y)
                keysToCollect.append(key)
            elif square == "G":
                guard = Actor("guard", anchor=("left", "top"))
                guard.pos = GetScreenCoords(x, y)
                guards.append(guard)
# === Drawing ===
def DrawBackground():
    random.seed(BACKGROUNDSEED)
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            if x % 2 == y % 2:
                screen.blit("floor1", GetScreenCoords(x, y))
            else:
                screen.blit("floor2", GetScreenCoords(x, y))
            n = random.randint(0, 99)
            if n < 5:
                screen.blit("crack1", GetScreenCoords(x, y))
            elif n < 10:
                screen.blit("crack2", GetScreenCoords(x, y))
def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[y][x]
            if square == "W":
                screen.blit("wall", GetScreenCoords(x, y))
            elif square == "D":
                screen.blit("door", GetScreenCoords(x, y))
def DrawActors():
    player.draw()
    for key in keysToCollect:
        key.draw()
    for guard in guards:
        guard.draw()
def draw():
    screen.clear()
    DrawBackground()
    DrawScenery()
    DrawActors()
    if gameOver:
        screen.draw.text(
            "Game Over! Press Space to try again",
            center=(WIDTH // 2, HEIGHT // 2),
            fontsize=60, color="yellow"
        )
def MovePlayer(dx, dy):
    global gameOver
    global playerWon
    if gameOver:
        return
    (x, y) = GetActorGridPos(player)
    x += dx
    y += dy
    square = MAP[y][x]
    if square == "W": # If the player tries to move into a wall
        return # stop the function, dont let the player move
    elif square == "D":
        if len(keysToCollect) > 0: # If there are keys left to collect
            return  # do no let the player exit the door if there are keys left
        else:
            gameOver = True
            playerWon = True
    for key in keysToCollect:
        # Get the grid pos of the current key
        (keyX, keyY) = GetActorGridPos(key) 
        # Check if the new player pos mathces the pos of one of the keys
        if x == keyX and y == keyY:
            # Despawn the key
            keysToCollect.remove(key)
            break
    animate(player, pos=GetScreenCoords(x, y), 
                duration=PLAYER_MOVE_INTERVAL)











