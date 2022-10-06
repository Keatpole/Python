import pygame, os, time, argparse

map_img = pygame.image.load("map.png")

map_img = pygame.transform.scale(map_img, (780, 780))

screen = pygame.display.set_mode((map_img.get_width(), map_img.get_height()))
pygame.display.set_caption("Subnautica Map Tracker")

argparser = argparse.ArgumentParser()

argparser.add_argument("--skip-anim", help="skips the animation at the start", action="store_true", default=False, dest="skip_anim")

args = argparser.parse_args()

def rgb_to_biome(rgb):
    if   rgb == (117, 134, 142): return "Safe Shallows (Center)"
    elif rgb == (117, 134, 141): return "Safe Shallows (West)"
    elif rgb == (175, 225, 126): return "Kelp Forest (West)"
    elif rgb == (175, 226, 126): return "Kelp Forest (North)"
    elif rgb == (175, 224, 126): return "Kelp Forest (More South)"
    elif rgb == (175, 225, 125): return "Kelp Forest (South)"
    elif rgb == (175, 225, 127): return "Kelp Forest (South East)"
    elif rgb == (202, 70, 101):  return "Grassy Plateaus (South West)"
    elif rgb == (204, 70, 101):  return "Grassy Plateaus (South East)"
    elif rgb == (203, 70, 101):  return "Grassy Plateaus (North West)"
    elif rgb == (201, 70, 101):  return "Grassy Plateaus (North East)"
    elif rgb == (42, 49, 51):    return "Mountains"
    elif rgb == (55, 79, 168):   return "Mushroom Forest (West)"
    elif rgb == (55, 79, 169):   return "Mushroom Forest (East)"
    elif rgb == (225, 82, 255):  return "Blood Kelp Zone (North)"
    elif rgb == (131, 59, 110):  return "Blood Kelp Zone (South)"
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
    else:                        return False

def biome_to_rgb(biome):
    if   biome == "Safe Shallows (Center)":       return (117, 134, 142)
    elif biome == "Safe Shallows (West)":         return (117, 134, 141)
    elif biome == "Kelp Forest (West)":           return (175, 225, 126)
    elif biome == "Kelp Forest (North)":          return (175, 226, 126)
    elif biome == "Kelp Forest (More South)":     return (175, 224, 126)
    elif biome == "Kelp Forest (South)":          return (175, 225, 125)
    elif biome == "Kelp Forest (South East)":     return (175, 225, 127)
    elif biome == "Grassy Plateaus (South West)": return (202, 70, 101)
    elif biome == "Grassy Plateaus (South East)": return (204, 70, 101)
    elif biome == "Grassy Plateaus (North West)": return (203, 70, 101)
    elif biome == "Grassy Plateaus (North East)": return (201, 70, 101)
    elif biome == "Mountains":                    return (42, 49, 51)
    elif biome == "Mushroom Forest (West)":       return (55, 79, 168)
    elif biome == "Mushroom Forest (East)":       return (55, 79, 169)
    elif biome == "Blood Kelp Zone (North)":      return (225, 82, 255)
    elif biome == "Blood Kelp Zone (South)":      return (131, 59, 110)
    elif biome == "Underwater Islands":           return (184, 119, 93)
    elif biome == "Bulb Zone":                    return (158, 144, 213)
    elif biome == "Dunes":                        return (246, 229, 169)
    elif biome == "Sea Treader's Path":           return (123, 160, 188)
    elif biome == "Sparse Reef":                  return (62, 100, 77)
    elif biome == "Grand Reef":                   return (70, 146, 187)
    elif biome == "Crash Zone":                   return (126, 90, 90)
    elif biome == "Grag Field":                   return (90, 21, 0)
    elif biome == "Void":                         return (0, 0, 0)
    elif biome == rgb_to_biome(selected_color):   return selected
    else:                                         return False

selected = None
selected_color = (0, 255, 0) # Change this to the color the selected color should be (RGB)

log_from_file = []
log = []

def clear():
    os.system("cls" if os.name == "nt" else "clear")

with open("log.txt", "r") as f:
    for l in f.readlines():
        log_from_file.append(biome_to_rgb(l[:-1]))

def anim(t):
    global selected

    for i,l in enumerate(log_from_file):
        screen.blit(map_img, (0, 0))

        pixels = pygame.PixelArray(map_img)

        if selected:
            pixels.replace(selected_color, selected)

        pixels.replace(l, selected_color)

        del pixels

        selected = l

        pygame.display.update(map_img.get_rect())

        clear()

        try:
            print(rgb_to_biome(log_from_file[i - 1]))
        except IndexError:
            pass

        print("Frame:", i)

        time.sleep(t)

    clear()

    if selected:
        print(rgb_to_biome(selected))
        print("Log Size:", len(log_from_file))

animtime = 1

if not args.skip_anim:
    anim(animtime)

while True:
    screen.blit(map_img, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("log.txt", "w+") as f:
                for l in log_from_file:
                    f.write(rgb_to_biome(l) + "\n")

            with open("log.txt", "a+") as f:
                for l in log:
                    f.write(rgb_to_biome(l) + "\n")

            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                color = map_img.get_at(pygame.mouse.get_pos())[:3]
                biome = rgb_to_biome(color) if color != selected_color else "None"

                if biome:
                    clear()
                    print(biome)
                    print("Log Size:", len(log) + len(log_from_file))

                    pixels = pygame.PixelArray(map_img)

                    if selected:
                        pixels.replace(selected_color, selected)

                    pixels.replace(color, selected_color)
                    del pixels

                    selected = color
            elif event.button == 2:
                clear()

                print("Log:\n")
                for l in log_from_file:
                    print(rgb_to_biome(l))
                for l in log:
                    print(rgb_to_biome(l))
            elif event.button == 3:
                if len(log) > 0 and selected == log[-1]:
                    log.pop()
                elif len(log_from_file) > 0 and selected == log_from_file[-1]:
                    log_from_file.pop()
                else:
                    log.append(selected)
                    
                clear()
                print(rgb_to_biome(selected))
                print("Log Size:", len(log) + len(log_from_file))
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                anim(animtime)
            elif event.key == pygame.K_ESCAPE:
                with open("log.txt", "w+") as f:
                    for l in log_from_file:
                        f.write(rgb_to_biome(l) + "\n")

                with open("log.txt", "a+") as f:
                    for l in log:
                        f.write(rgb_to_biome(l) + "\n")

                exit()
            elif event.key == pygame.K_BACKSPACE:
                clear()
                print(rgb_to_biome(selected))
                print("Log Size:", len(log) + len(log_from_file))

                log = []
                log_from_file = []
            elif event.key == pygame.K_DELETE:
                exit()
            elif event.key == pygame.K_MINUS:
                clear()
                print(rgb_to_biome(selected))
                print("Log Size:", len(log) + len(log_from_file))

                animtime -= 0.1
                animtime = round(animtime, 1)
                print("Frame Time:", animtime)
            elif event.key == pygame.K_PLUS:
                clear()
                print(rgb_to_biome(selected))
                print("Log Size:", len(log) + len(log_from_file))

                animtime += 0.1
                animtime = round(animtime, 1)
                print("Frame Time:", animtime)
    pygame.display.flip()