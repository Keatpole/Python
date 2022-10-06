import pygame, os

map_img = pygame.image.load("map.png")

map_img = pygame.transform.scale(map_img, (780, 780))

screen = pygame.display.set_mode((map_img.get_width(), map_img.get_height()))
pygame.display.set_caption("Subnautica Map Tracker")

def rgb_to_biome(rgb):
    if   rgb == (117, 134, 142): return "Safe Shallows (Center)"
    elif rgb == (117, 134, 141): return "Safe Shallows (West)"
    elif rgb == (175, 225, 126): return "Kelp Forest (West)"
    elif rgb == (175, 226, 126): return "Kelp Forest (North)"
    elif rgb == (175, 224, 126): return "Kelp Forest (More South)"
    elif rgb == (175, 223, 126): return "Kelp Forest (South)"
    elif rgb == (202, 70, 101):  return "Grassy Plateaus (South West)"
    elif rgb == (204, 70, 101):  return "Grassy Plateaus (South East)"
    elif rgb == (203, 70, 101):  return "Grassy Plateaus (North West)"
    elif rgb == (201, 70, 101):  return "Grassy Plateaus (North East)"
    elif rgb == (42, 49, 51):    return "Mountains"
    elif rgb == (55, 79, 168):   return "Mushroom Forest (West)"
    elif rgb == (55, 79, 169):   return "Mushroom Forest (East)"
    elif rgb == (225, 82, 255):  return "Blood Kelp Zone (North)"
    elif rgb == (226, 82, 255):  return "Blood Kelp Zone (South)"
    elif rgb == (184, 119, 93):  return "Underwater Islands"
    elif rgb == (158, 144, 213): return "Bulb Zone"
    elif rgb == (246, 229, 169): return "Dunes"
    elif rgb == (123, 160, 188): return "Sea Treader's Path"
    elif rgb == (62, 100, 77):   return "Sparse Reef"
    elif rgb == (70, 146, 187):  return "Grand Reef"
    elif rgb == (126, 90, 90):   return "Crash Zone"
    elif rgb == (90, 21, 0):     return "Grag Field"
    elif rgb == (0, 0, 0):       return "Void"
    elif rgb == selected_color:  return rgb_to_biome(selected)
    else:                        return "Unknown"

selected = None
selected_color = (43, 214, 83)

while True:
    screen.blit(map_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            color = map_img.get_at(pygame.mouse.get_pos())[:3]
            biome = rgb_to_biome(color)

            if biome != "Unknown":
                os.system("cls" if os.name == "nt" else "clear")
                print(biome)

                if selected is not None:
                    for x in range(map_img.get_width()):
                        for y in range(map_img.get_height()):
                            if map_img.get_at((x, y))[:3] == selected_color:
                                map_img.set_at((x, y), selected)

                selected = color
                
                for x in range(map_img.get_width()):
                    for y in range(map_img.get_height()):
                        if map_img.get_at((x, y))[:3] == color:
                            map_img.set_at((x, y), selected_color)
            

    pygame.display.flip()
