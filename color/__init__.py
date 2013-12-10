"""This module includes the Color class.

The Color class provides nearly every thing one could want to do with colors.

"""

from colorsys import hsv_to_rgb, rgb_to_hsv

__all__ = ('Color',)
__author__ = 'Tyler Crompton'


# noinspection PyPep8Naming
class _classproperty(property):
    # noinspection PyMethodOverriding
    def __get__(self, instance, owner):
        return self.fget.__get__(None, owner)(owner)


class Color:
    """A class to represent a color.

    Valid color values are hexadecimal or RGB values.

    Since this class is intended to be mutable, the class property "constants"
    return a new instance with each access.

    """

    def __init__(self, *args):
        if len(args) == 1:
            value = args[0][1:] if args[0].startswith('#') else args[0]
            if len(value) % 3:
                raise ValueError('Invalid number of characters')
            triplet_length = len(value) // 3
            self._bits = len(value) * 3
            self.red = int(value[:triplet_length], 16)
            self.green = int(value[triplet_length:triplet_length * 2], 16)
            self.blue = int(value[triplet_length * 2:triplet_length * 3], 16)
        elif len(args) == 3:
            self._bits = 24
            self.red, self.green, self.blue = args
        else:
            self._bits = args[3]
            self.red, self.green, self.blue, self._bits = args
            if self._bits <= 0 or self._bits % 12:
                raise ValueError(
                    'The number of bits must be divisible by twelve.')

    def __repr__(self):
        return 'Color({}, {}, {}, {})'.format(repr(self.red), repr(self.green),
                                              repr(self.blue),
                                              repr(self._bits))

    @property
    def hex(self):
        return '#{{:0{0}x}}{{:0{0}x}}{{:0{0}x}}'.format(
            self._bits // 12).format(self.red, self.green, self.blue)

    @property
    def red(self):
        return self._red

    # noinspection PyAttributeOutsideInit
    @red.setter
    def red(self, value):
        if 0 <= value <= 16 ** (self._bits // 12) - 1:
            self._red = value
        else:
            raise ValueError('Value must be within 0 to {}.'.format(
                16 ** (self._bits // 12) - 1))

    @property
    def green(self):
        return self._green

    # noinspection PyAttributeOutsideInit
    @green.setter
    def green(self, value):
        if 0 <= value <= 16 ** (self._bits // 12) - 1:
            self._green = value
        else:
            raise ValueError('Value must be within 0 to {}.'.format(
                16 ** (self._bits // 12) - 1))

    @property
    def blue(self):
        return self._blue

    # noinspection PyAttributeOutsideInit
    @blue.setter
    def blue(self, value):
        if 0 <= value <= 16 ** (self._bits // 12) - 1:
            self._blue = value
        else:
            raise ValueError('Value must be within 0 to {}.'.format(
                16 ** (self._bits // 12) - 1))

    @property
    def rgb(self):
        return self.red, self.green, self.blue

    @property
    def hue(self):
        return rgb_to_hsv(self.red, self.green, self.blue)[0] * 360

    @hue.setter
    def hue(self, value):
        value %= 360
        if value < 0:
            value += 360 * abs(value // 360)

        hsv = rgb_to_hsv(self.red, self.green, self.blue)
        rgb = hsv_to_rgb(value / 360, hsv[1], hsv[2])
        self.red = rgb[0]
        self.green = rgb[1]
        self.blue = rgb[2]

    @property
    def saturation(self):
        return rgb_to_hsv(self.red, self.green, self.blue)[1] * 100

    @saturation.setter
    def saturation(self, saturation):
        if saturation < 0 or saturation > 100:
            raise ValueError('Saturation must be within 0 and 100 (inclusive)')

        hsv = rgb_to_hsv(self.red, self.green, self.blue)
        rgb = hsv_to_rgb(hsv[0], saturation / 100, hsv[2])
        self.red = rgb[0]
        self.green = rgb[1]
        self.blue = rgb[2]

    @property
    def value(self):
        return rgb_to_hsv(self.red, self.green, self.blue)[2] * 100 / 16 ** (
            self._bits // 12) - 1

    # noinspection PyAttributeOutsideInit
    @value.setter
    def value(self, value):
        if value < 0 or value > 100:
            raise ValueError('Value must be within 0 and 100 (inclusive)')

        hsv = rgb_to_hsv(self._red, self._green, self._blue)
        rgb = hsv_to_rgb(hsv[0], hsv[1],
                         value * (16 ** (self._bits // 12) - 1) // 100)
        self._red = rgb[0]
        self._green = rgb[1]
        self._blue = rgb[2]

    @property
    def hsv(self):
        hsv = rgb_to_hsv(self._red, self._green, self._blue)
        return hsv[0] * 360, hsv[1] * 100, hsv[2] * 100 / 16 ** (
            self._bits // 12) - 1

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def ALICE_BLUE(cls):
        return cls(240, 248, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def ANTIQUE_WHITE(cls):
        return cls(250, 235, 215)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def AQUA(cls):
        return cls(0, 255, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def AQUA_MARINE(cls):
        return cls(127, 255, 212)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def AZURE(cls):
        return cls(240, 255, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BEIGE(cls):
        return cls(245, 245, 220)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BISQUE(cls):
        return cls(255, 228, 196)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BLACK(cls):
        return cls(0, 0, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BLANCHED_ALMOND(cls):
        return cls(255, 235, 205)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BLUE(cls):
        return cls(0, 0, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BLUE_VIOLET(cls):
        return cls(138, 43, 226)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BROWN(cls):
        return cls(165, 42, 42)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def BURLY_WOOD(cls):
        return cls(222, 184, 135)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CADET_BLUE(cls):
        return cls(95, 158, 160)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CHARTREUSE(cls):
        return cls(127, 255, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CHOCOLATE(cls):
        return cls(210, 105, 30)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CORAL(cls):
        return cls(255, 127, 80)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CORNFLOWER_BLUE(cls):
        return cls(100, 149, 237)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CORN_SILK(cls):
        return cls(255, 248, 220)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CRIMSON(cls):
        return cls(220, 20, 60)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def CYAN(cls):
        return cls(0, 255, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_BLUE(cls):
        return cls(0, 0, 139)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_CYAN(cls):
        return cls(0, 139, 139)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_GOLDENROD(cls):
        return cls(184, 134, 11)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_GRAY(cls):
        return cls(169, 169, 169)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_GREY(cls):
        return cls(169, 169, 169)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_GREEN(cls):
        return cls(0, 100, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_KHAKI(cls):
        return cls(189, 183, 107)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_MAGENTA(cls):
        return cls(139, 0, 139)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_OLIVE_GREEN(cls):
        return cls(85, 107, 47)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_ORANGE(cls):
        return cls(255, 140, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_ORCHID(cls):
        return cls(153, 50, 204)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_RED(cls):
        return cls(139, 0, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_SALMON(cls):
        return cls(233, 150, 122)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_SEA_GREEN(cls):
        return cls(143, 188, 143)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_SLATE_BLUE(cls):
        return cls(72, 61, 139)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_SLATE_GRAY(cls):
        return cls(47, 79, 79)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_SLATE_GREY(cls):
        return cls(47, 79, 79)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_TURQUOISE(cls):
        return cls(0, 206, 209)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DARK_VIOLET(cls):
        return cls(148, 0, 211)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DEEP_PINK(cls):
        return cls(255, 20, 147)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DEEP_SKY_BLUE(cls):
        return cls(0, 191, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DIM_GRAY(cls):
        return cls(105, 105, 105)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DIM_GREY(cls):
        return cls(105, 105, 105)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def DODGER_BLUE(cls):
        return cls(30, 144, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def FIRE_BRICK(cls):
        return cls(178, 34, 34)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def FLORAL_WHITE(cls):
        return cls(255, 250, 240)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def FOREST_GREEN(cls):
        return cls(34, 139, 34)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def FUCHSIA(cls):
        return cls(255, 0, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GAINSBORO(cls):
        return cls(220, 220, 220)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GHOST_WHITE(cls):
        return cls(248, 248, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GOLD(cls):
        return cls(255, 215, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GOLDENROD(cls):
        return cls(218, 165, 32)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GRAY(cls):
        return cls(128, 128, 128)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GREY(cls):
        return cls(128, 128, 128)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GREEN(cls):
        return cls(0, 128, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def GREEN_YELLOW(cls):
        return cls(173, 255, 47)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def HONEYDEW(cls):
        return cls(240, 255, 240)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def HOT_PINK(cls):
        return cls(255, 105, 180)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def INDIAN_RED(cls):
        return cls(205, 92, 92)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def INDIGO(cls):
        return cls(75, 0, 130)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def IVORY(cls):
        return cls(255, 255, 240)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def KHAKI(cls):
        return cls(240, 230, 140)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LAVENDER(cls):
        return cls(230, 230, 250)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LAVENDER_BLUSH(cls):
        return cls(255, 240, 245)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LAWN_GREEN(cls):
        return cls(124, 252, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LEMON_CHIFFON(cls):
        return cls(255, 250, 205)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_BLUE(cls):
        return cls(173, 216, 230)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_CORAL(cls):
        return cls(240, 128, 128)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_CYAN(cls):
        return cls(224, 255, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_GOLDENROD_YELLOW(cls):
        return cls(250, 250, 210)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_GRAY(cls):
        return cls(211, 211, 211)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_GREY(cls):
        return cls(211, 211, 211)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_GREEN(cls):
        return cls(144, 238, 144)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_PINK(cls):
        return cls(255, 182, 193)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_SALMON(cls):
        return cls(255, 160, 122)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_SEA_GREEN(cls):
        return cls(32, 178, 170)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_SKY_BLUE(cls):
        return cls(135, 206, 250)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_SLATE_GRAY(cls):
        return cls(119, 136, 153)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_SLATE_GREY(cls):
        return cls(119, 136, 153)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_STEEL_BLUE(cls):
        return cls(176, 196, 222)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIGHT_YELLOW(cls):
        return cls(255, 255, 224)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIME(cls):
        return cls(0, 255, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LIME_GREEN(cls):
        return cls(50, 205, 50)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def LINEN(cls):
        return cls(250, 240, 230)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MAGENTA(cls):
        return cls(255, 0, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MAROON(cls):
        return cls(128, 0, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_AQUA_MARINE(cls):
        return cls(102, 205, 170)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_BLUE(cls):
        return cls(0, 0, 205)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_ORCHID(cls):
        return cls(186, 85, 211)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_PURPLE(cls):
        return cls(147, 112, 216)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_SEA_GREEN(cls):
        return cls(60, 179, 113)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_SLATE_BLUE(cls):
        return cls(123, 104, 238)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_SPRING_GREEN(cls):
        return cls(0, 250, 154)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_TURQUOISE(cls):
        return cls(72, 209, 204)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MEDIUM_VIOLET_RED(cls):
        return cls(199, 21, 133)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MIDNIGHT_BLUE(cls):
        return cls(25, 25, 112)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MINT_CREAM(cls):
        return cls(245, 255, 250)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MISTY_ROSE(cls):
        return cls(255, 228, 225)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def MOCCASIN(cls):
        return cls(255, 228, 181)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def NAVAJO_WHITE(cls):
        return cls(255, 222, 173)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def NAVY(cls):
        return cls(0, 0, 128)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def OLD_LACE(cls):
        return cls(253, 245, 230)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def OLIVE(cls):
        return cls(128, 128, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def OLIVE_DRAB(cls):
        return cls(107, 142, 35)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def ORANGE(cls):
        return cls(255, 165, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def ORANGE_RED(cls):
        return cls(255, 69, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def ORCHID(cls):
        return cls(218, 112, 214)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PALE_GOLDENROD(cls):
        return cls(238, 232, 170)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PALE_GREEN(cls):
        return cls(152, 251, 152)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PALE_TURQUOISE(cls):
        return cls(175, 238, 238)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PALE_VIOLET_RED(cls):
        return cls(216, 112, 147)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PAPAYA_WHIP(cls):
        return cls(255, 239, 213)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PEACH_PUFF(cls):
        return cls(255, 218, 185)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PERU(cls):
        return cls(205, 133, 63)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PINK(cls):
        return cls(255, 192, 203)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PLUM(cls):
        return cls(221, 160, 221)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def POWDER_BLUE(cls):
        return cls(176, 224, 230)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def PURPLE(cls):
        return cls(128, 0, 128)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def RED(cls):
        return cls(255, 0, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def ROSY_BROWN(cls):
        return cls(188, 143, 143)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def ROYAL_BLUE(cls):
        return cls(65, 105, 225)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SADDLE_BROWN(cls):
        return cls(139, 69, 19)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SALMON(cls):
        return cls(250, 128, 114)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SANDY_BROWN(cls):
        return cls(244, 164, 96)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SEA_GREEN(cls):
        return cls(46, 139, 87)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SEA_SHELL(cls):
        return cls(255, 245, 238)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SIENNA(cls):
        return cls(160, 82, 45)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SILVER(cls):
        return cls(192, 192, 192)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SKY_BLUE(cls):
        return cls(135, 206, 235)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SLATE_BLUE(cls):
        return cls(106, 90, 205)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SLATE_GRAY(cls):
        return cls(112, 128, 144)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SLATE_GREY(cls):
        return cls(112, 128, 144)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SNOW(cls):
        return cls(255, 250, 250)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def SPRING_GREEN(cls):
        return cls(0, 255, 127)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def STEEL_BLUE(cls):
        return cls(70, 130, 180)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def TAN(cls):
        return cls(210, 180, 140)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def TEAL(cls):
        return cls(0, 128, 128)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def THISTLE(cls):
        return cls(216, 191, 216)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def TOMATO(cls):
        return cls(255, 99, 71)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def TURQUOISE(cls):
        return cls(64, 224, 208)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def VIOLET(cls):
        return cls(238, 130, 238)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def WHEAT(cls):
        return cls(245, 222, 179)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def WHITE(cls):
        return cls(255, 255, 255)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def WHITE_SMOKE(cls):
        return cls(245, 245, 245)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def YELLOW(cls):
        return cls(255, 255, 0)

    # noinspection PyPep8Naming,PyMethodParameters,PyCallingNonCallable
    @_classproperty
    def YELLOW_GREEN(cls):
        return cls(154, 205, 50)
