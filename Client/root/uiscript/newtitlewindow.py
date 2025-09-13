import uiScriptLocale

BOARD_WIDTH = 650
BOARD_HEIGHT = 350

window = {
	"name" : "NewTitleWindow",
	"style" : ("movable", "float",),

	"x" : (SCREEN_WIDTH - BOARD_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - BOARD_HEIGHT) / 2,

	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,

	"children" :
	(
		{
			"name" : "board_title",
			"type" : "board",
			"style" : ("attach",),

			"x" : 0,
			"y" : 0,

			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,

			"children" :
			(
				{
					"name" : "titlebar_title",
					"type" : "titlebar",
					"style" : ("attach",),

					"x" : 0,
					"y" : 0,

					"width" : BOARD_WIDTH,
					"color" : "red",

					"children" :
					(
						{ "name" : "titlebar_title_text", "type" : "text", "x" : 0, "y" : -1, "text" : "Title and Align System", "all_align" : "center" },
					),
				},
			),
		},
		# {
			# "name" : "board_align",
			# "type" : "board",
			# "style" : ("attach",),

			# "x" : 0,
			# "y" : BOARD_HEIGHT / 2 - 10,

			# "width" : BOARD_WIDTH,
			# "height" : BOARD_HEIGHT / 2 - 4,

			# "children" :
			# (
				# {
					# "name" : "titlebar_align",
					# "type" : "titlebar",
					# "style" : ("attach",),

					# "x" : 0,
					# "y" : 0,

					# "width" : BOARD_WIDTH,
					# "color" : "red",

					# "children" :
					# (
						# { "name" : "titlebar_align_text", "type" : "text", "x" : 0, "y" : -1, "text" : "Choose your align", "all_align" : "center" },
					# ),
				# },
			# ),
		# },
	),
}