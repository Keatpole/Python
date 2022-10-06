import pygame

map_img = pygame.image.load("map.png")
map_img = pygame.transform.scale(map_img, (480, 480))

pygame.display.set_caption("Subnautica Map Tracker")

def rgb_to_biome(rgb):
    if rgb == (117, 134, 142):
        return "Safe Shallows"
    elif rgb == (175, 225, 126):
        return "Kelp Forest"
    elif rgb == (202, 70, 101):
        return "Grassy Plateaus"
    elif rgb == (55, 79, 168):
        return "Mushroom Forest"
    elif rgb == (158, 144, 213):
        return "Bulb Zone"
    elif rgb == (184, 119, 93):
        return "Underwater Islands"
    elif rgb == (42, 49, 51):
        return "Mountains"
    elif rgb == (225, 82, 255):
        return "Northern Blood Kelp Zone"
    elif rgb == (246, 229, 169):
        return "Dunes"
    elif rgb == (126, 90, 90):
        return "Crash Zone"
    elif rgb == (123, 160, 188):
        return "Sea Treader's Path"
    elif rgb == (62, 100, 77):
        return "Sparse Reef"
    elif rgb == (90, 21, 0):
        return "Crag Field"
    elif rgb == (131, 59, 110):
        return "Blood Kelp Zone Trench"
    elif rgb == (70, 146, 187):
        return "Grand Reef"
    elif rgb == (0, 0, 0):
        return "Void"
    elif rgb == (0, 255, 0):
        return rgb_to_biome(selected)
    else:
        return "Unknown"

selected = None

pygame.init()

display = pygame.display.set_mode((480, 480))

while True:
    display.blit(map_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = display.get_at(pygame.mouse.get_pos())[:3]

            print(f"Biome: {rgb_to_biome(color)}")

            pixels = pygame.PixelArray(map_img)

            if selected:
                pixels.replace((0, 255, 0), selected)

            pixels.replace(color, (0, 255, 0))
            del pixels

            selected = color

    pygame.display.update()