"""This module includes the Color class.

The Color class provides nearly every thing one could want to do with colors.

"""

from colorsys import hsv_to_rgb, rgb_to_hsv

__all__ = ('Color',)

class classproperty(property):
	def __get__(self, instance, owner):
		return self.fget.__get__(None, owner)(owner)

class Color:

	"""A class to represent a color.

	Valid color values are three- or six-character hexadecimal values or a
	three integers corresponding to red, green, and blue values.

	Since this class is intended to be mutable, the class property "constants"
	return a new instance with each access.

"""

	def __init__(self, *args):
		if len(args) == 1:
			value = args[0][1:] if args[0][0] == '#' else args[0]
			if len(value) == 6:
				self.red = int(value[:2], 16)
				self.green = int(value[2:4], 16)
				self.blue = int(value[4:], 16)
			elif len(value) == 3:
				self.red = int(value[0] * 2, 16)
				self.green = int(value[1] * 2, 16)
				self.blue = int(value[2] * 2, 16)
			else:
				raise ValueError('Invalid number of characters')
		else:
			self.red, self.green, self.blue = args

	def __repr__(self):
		return '{}({}, {}, {})'.format(self.__class__.__name__, self.red,
			self.green, self.blue)

	@property
	def hex(self):
		return '#{:02x}{:02x}{:02x}'.format(round(self.red),
			round(self.green), round(self.blue))

	@property
	def red(self):
		return self._red

	@red.setter
	def red(self, value):
		if 0 <= value <= 255:
			self._red = value
		else:
			raise ValueError('Value must be within 0 to 255')

	@property
	def green(self):
		return self._green

	@green.setter
	def green(self, value):
		if 0 <= value <= 255:
			self._green = value
		else:
			raise ValueError('Value must be within 0 to 255')

	@property
	def blue(self):
		return self._blue

	@blue.setter
	def blue(self, value):
		if 0 <= value <= 255:
			self._blue = value
		else:
			raise ValueError('Value must be within 0 to 255')

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
			value += 360 * abs(hue // 360)

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
		rgb = hsv_to_rgb(hsv[0], saturation / 100,  hsv[2])
		self.red = rgb[0]
		self.green = rgb[1]
		self.blue = rgb[2]

	@property
	def value(self):
		return rgb_to_hsv(self.red, self.green, self.blue)[2] * 100 / 255

	@value.setter
	def value(self, value):
		if value < 0 or value > 100:
			raise ValueError('Value must be within 0 and 100 (inclusive)')

		hsv = rgb_to_hsv(self._red, self._green, self._blue)
		rgb = hsv_to_rgb(hsv[0], hsv[1], value * 2.55)
		self._red = rgb[0]
		self._green = rgb[1]
		self._blue = rgb[2]

	@property
	def hsv(self):
		hsv = rgb_to_hsv(self._red, self._green, self._blue)
		return hsv[0] * 360, hsv[1] * 100, hsv[2] * 100 / 255

	@classproperty
	def ALICEBLUE(cls):
		return cls(240, 248, 255)

	@classproperty
	def ANTIQUEWHITE(cls):
		return cls(250, 235, 215)

	@classproperty
	def AQUA(cls):
		return cls(0, 255, 255)

	@classproperty
	def AQUAMARINE(cls):
		return cls(127, 255, 212)

	@classproperty
	def AZURE(cls):
		return cls(240, 255, 255)

	@classproperty
	def BEIGE(cls):
		return cls(245, 245, 220)

	@classproperty
	def BISQUE(cls):
		return cls(255, 228, 196)

	@classproperty
	def BLACK(cls):
		return cls(0, 0, 0)

	@classproperty
	def BLANCHEDALMOND(cls):
		return cls(255, 235, 205)

	@classproperty
	def BLUE(cls):
		return cls(0, 0, 255)

	@classproperty
	def BLUEVIOLET(cls):
		return cls(138, 43, 226)

	@classproperty
	def BROWN(cls):
		return cls(165, 42, 42)

	@classproperty
	def BURLYWOOD(cls):
		return cls(222, 184, 135)

	@classproperty
	def CADETBLUE(cls):
		return cls(95, 158, 160)

	@classproperty
	def CHARTREUSE(cls):
		return cls(127, 255, 0)

	@classproperty
	def CHOCOLATE(cls):
		return cls(210, 105, 30)

	@classproperty
	def CORAL(cls):
		return cls(255, 127, 80)

	@classproperty
	def CORNFLOWERBLUE(cls):
		return cls(100, 149, 237)

	@classproperty
	def CORNSILK(cls):
		return cls(255, 248, 220)

	@classproperty
	def CRIMSON(cls):
		return cls(220, 20, 60)

	@classproperty
	def CYAN(cls):
		return cls(0, 255, 255)

	@classproperty
	def DARKBLUE(cls):
		return cls(0, 0, 139)

	@classproperty
	def DARKCYAN(cls):
		return cls(0, 139, 139)

	@classproperty
	def DARKGOLDENROD(cls):
		return cls(184, 134, 11)

	@classproperty
	def DARKGRAY(cls):
		return cls(169, 169, 169)

	@classproperty
	def DARKGREY(cls):
		return cls(169, 169, 169)

	@classproperty
	def DARKGREEN(cls):
		return cls(0, 100, 0)

	@classproperty
	def DARKKHAKI(cls):
		return cls(189, 183, 107)

	@classproperty
	def DARKMAGENTA(cls):
		return cls(139, 0, 139)

	@classproperty
	def DARKOLIVEGREEN(cls):
		return cls(85, 107, 47)

	@classproperty
	def DARKORANGE(cls):
		return cls(255, 140, 0)

	@classproperty
	def DARKORCHID(cls):
		return cls(153, 50, 204)

	@classproperty
	def DARKRED(cls):
		return cls(139, 0, 0)

	@classproperty
	def DARKSALMON(cls):
		return cls(233, 150, 122)

	@classproperty
	def DARKSEAGREEN(cls):
		return cls(143, 188, 143)

	@classproperty
	def DARKSLATEBLUE(cls):
		return cls(72, 61, 139)

	@classproperty
	def DARKSLATEGRAY(cls):
		return cls(47, 79, 79)

	@classproperty
	def DARKSLATEGREY(cls):
		return cls(47, 79, 79)

	@classproperty
	def DARKTURQUOISE(cls):
		return cls(0, 206, 209)

	@classproperty
	def DARKVIOLET(cls):
		return cls(148, 0, 211)

	@classproperty
	def DEEPPINK(cls):
		return cls(255, 20, 147)

	@classproperty
	def DEEPSKYBLUE(cls):
		return cls(0, 191, 255)

	@classproperty
	def DIMGRAY(cls):
		return cls(105, 105, 105)

	@classproperty
	def DIMGREY(cls):
		return cls(105, 105, 105)

	@classproperty
	def DODGERBLUE(cls):
		return cls(30, 144, 255)

	@classproperty
	def FIREBRICK(cls):
		return cls(178, 34, 34)

	@classproperty
	def FLORALWHITE(cls):
		return cls(255, 250, 240)

	@classproperty
	def FORESTGREEN(cls):
		return cls(34, 139, 34)

	@classproperty
	def FUCHSIA(cls):
		return cls(255, 0, 255)

	@classproperty
	def GAINSBORO(cls):
		return cls(220, 220, 220)

	@classproperty
	def GHOSTWHITE(cls):
		return cls(248, 248, 255)

	@classproperty
	def GOLD(cls):
		return cls(255, 215, 0)

	@classproperty
	def GOLDENROD(cls):
		return cls(218, 165, 32)

	@classproperty
	def GRAY(cls):
		return cls(128, 128, 128)

	@classproperty
	def GREY(cls):
		return cls(128, 128, 128)

	@classproperty
	def GREEN(cls):
		return cls(0, 128, 0)

	@classproperty
	def GREENYELLOW(cls):
		return cls(173, 255, 47)

	@classproperty
	def HONEYDEW(cls):
		return cls(240, 255, 240)

	@classproperty
	def HOTPINK(cls):
		return cls(255, 105, 180)

	@classproperty
	def INDIANRED(cls):
		return cls(205, 92, 92)

	@classproperty
	def INDIGO(cls):
		return cls(75, 0, 130)

	@classproperty
	def IVORY(cls):
		return cls(255, 255, 240)

	@classproperty
	def KHAKI(cls):
		return cls(240, 230, 140)

	@classproperty
	def LAVENDER(cls):
		return cls(230, 230, 250)

	@classproperty
	def LAVENDERBLUSH(cls):
		return cls(255, 240, 245)

	@classproperty
	def LAWNGREEN(cls):
		return cls(124, 252, 0)

	@classproperty
	def LEMONCHIFFON(cls):
		return cls(255, 250, 205)

	@classproperty
	def LIGHTBLUE(cls):
		return cls(173, 216, 230)

	@classproperty
	def LIGHTCORAL(cls):
		return cls(240, 128, 128)

	@classproperty
	def LIGHTCYAN(cls):
		return cls(224, 255, 255)

	@classproperty
	def LIGHTGOLDENRODYELLOW(cls):
		return cls(250, 250, 210)

	@classproperty
	def LIGHTGRAY(cls):
		return cls(211, 211, 211)

	@classproperty
	def LIGHTGREY(cls):
		return cls(211, 211, 211)

	@classproperty
	def LIGHTGREEN(cls):
		return cls(144, 238, 144)

	@classproperty
	def LIGHTPINK(cls):
		return cls(255, 182, 193)

	@classproperty
	def LIGHTSALMON(cls):
		return cls(255, 160, 122)

	@classproperty
	def LIGHTSEAGREEN(cls):
		return cls(32, 178, 170)

	@classproperty
	def LIGHTSKYBLUE(cls):
		return cls(135, 206, 250)

	@classproperty
	def LIGHTSLATEGRAY(cls):
		return cls(119, 136, 153)

	@classproperty
	def LIGHTSLATEGREY(cls):
		return cls(119, 136, 153)

	@classproperty
	def LIGHTSTEELBLUE(cls):
		return cls(176, 196, 222)

	@classproperty
	def LIGHTYELLOW(cls):
		return cls(255, 255, 224)

	@classproperty
	def LIME(cls):
		return cls(0, 255, 0)

	@classproperty
	def LIMEGREEN(cls):
		return cls(50, 205, 50)

	@classproperty
	def LINEN(cls):
		return cls(250, 240, 230)

	@classproperty
	def MAGENTA(cls):
		return cls(255, 0, 255)

	@classproperty
	def MAROON(cls):
		return cls(128, 0, 0)

	@classproperty
	def MEDIUMAQUAMARINE(cls):
		return cls(102, 205, 170)

	@classproperty
	def MEDIUMBLUE(cls):
		return cls(0, 0, 205)

	@classproperty
	def MEDIUMORCHID(cls):
		return cls(186, 85, 211)

	@classproperty
	def MEDIUMPURPLE(cls):
		return cls(147, 112, 216)

	@classproperty
	def MEDIUMSEAGREEN(cls):
		return cls(60, 179, 113)

	@classproperty
	def MEDIUMSLATEBLUE(cls):
		return cls(123, 104, 238)

	@classproperty
	def MEDIUMSPRINGGREEN(cls):
		return cls(0, 250, 154)

	@classproperty
	def MEDIUMTURQUOISE(cls):
		return cls(72, 209, 204)

	@classproperty
	def MEDIUMVIOLETRED(cls):
		return cls(199, 21, 133)

	@classproperty
	def MIDNIGHTBLUE(cls):
		return cls(25, 25, 112)

	@classproperty
	def MINTCREAM(cls):
		return cls(245, 255, 250)

	@classproperty
	def MISTYROSE(cls):
		return cls(255, 228, 225)

	@classproperty
	def MOCCASIN(cls):
		return cls(255, 228, 181)

	@classproperty
	def NAVAJOWHITE(cls):
		return cls(255, 222, 173)

	@classproperty
	def NAVY(cls):
		return cls(0, 0, 128)

	@classproperty
	def OLDLACE(cls):
		return cls(253, 245, 230)

	@classproperty
	def OLIVE(cls):
		return cls(128, 128, 0)

	@classproperty
	def OLIVEDRAB(cls):
		return cls(107, 142, 35)

	@classproperty
	def ORANGE(cls):
		return cls(255, 165, 0)

	@classproperty
	def ORANGERED(cls):
		return cls(255, 69, 0)

	@classproperty
	def ORCHID(cls):
		return cls(218, 112, 214)

	@classproperty
	def PALEGOLDENROD(cls):
		return cls(238, 232, 170)

	@classproperty
	def PALEGREEN(cls):
		return cls(152, 251, 152)

	@classproperty
	def PALETURQUOISE(cls):
		return cls(175, 238, 238)

	@classproperty
	def PALEVIOLETRED(cls):
		return cls(216, 112, 147)

	@classproperty
	def PAPAYAWHIP(cls):
		return cls(255, 239, 213)

	@classproperty
	def PEACHPUFF(cls):
		return cls(255, 218, 185)

	@classproperty
	def PERU(cls):
		return cls(205, 133, 63)

	@classproperty
	def PINK(cls):
		return cls(255, 192, 203)

	@classproperty
	def PLUM(cls):
		return cls(221, 160, 221)

	@classproperty
	def POWDERBLUE(cls):
		return cls(176, 224, 230)

	@classproperty
	def PURPLE(cls):
		return cls(128, 0, 128)

	@classproperty
	def RED(cls):
		return cls(255, 0, 0)

	@classproperty
	def ROSYBROWN(cls):
		return cls(188, 143, 143)

	@classproperty
	def ROYALBLUE(cls):
		return cls(65, 105, 225)

	@classproperty
	def SADDLEBROWN(cls):
		return cls(139, 69, 19)

	@classproperty
	def SALMON(cls):
		return cls(250, 128, 114)

	@classproperty
	def SANDYBROWN(cls):
		return cls(244, 164, 96)

	@classproperty
	def SEAGREEN(cls):
		return cls(46, 139, 87)

	@classproperty
	def SEASHELL(cls):
		return cls(255, 245, 238)

	@classproperty
	def SIENNA(cls):
		return cls(160, 82, 45)

	@classproperty
	def SILVER(cls):
		return cls(192, 192, 192)

	@classproperty
	def SKYBLUE(cls):
		return cls(135, 206, 235)

	@classproperty
	def SLATEBLUE(cls):
		return cls(106, 90, 205)

	@classproperty
	def SLATEGRAY(cls):
		return cls(112, 128, 144)

	@classproperty
	def SLATEGREY(cls):
		return cls(112, 128, 144)

	@classproperty
	def SNOW(cls):
		return cls(255, 250, 250)

	@classproperty
	def SPRINGGREEN(cls):
		return cls(0, 255, 127)

	@classproperty
	def STEELBLUE(cls):
		return cls(70, 130, 180)

	@classproperty
	def TAN(cls):
		return cls(210, 180, 140)

	@classproperty
	def TEAL(cls):
		return cls(0, 128, 128)

	@classproperty
	def THISTLE(cls):
		return cls(216, 191, 216)

	@classproperty
	def TOMATO(cls):
		return cls(255, 99, 71)

	@classproperty
	def TURQUOISE(cls):
		return cls(64, 224, 208)

	@classproperty
	def VIOLET(cls):
		return cls(238, 130, 238)

	@classproperty
	def WHEAT(cls):
		return cls(245, 222, 179)

	@classproperty
	def WHITE(cls):
		return cls(255, 255, 255)

	@classproperty
	def WHITESMOKE(cls):
		return cls(245, 245, 245)

	@classproperty
	def YELLOW(cls):
		return cls(255, 255, 0)

	@classproperty
	def YELLOWGREEN(cls):
		return cls(154, 205, 50)