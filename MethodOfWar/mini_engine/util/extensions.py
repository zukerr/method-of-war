import pygame


def getMinutesSecondsFromSeconds(seconds: int) -> str:
    minutes: int = int(seconds / 60)
    seconds: int = seconds % 60
    secondsStr: str = str(seconds)
    if seconds < 10:
        secondsStr = "0" + secondsStr
    return str(minutes) + ":" + secondsStr


def blit_text(surface, maxSize, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = maxSize
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
