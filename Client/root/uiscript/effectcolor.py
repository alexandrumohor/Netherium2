import uiScriptLocale
import item

BOARD_WIDTH = 325 + 305
BOARD_HEIGHT = 340 + 14
THINBOARD_WIDTH = 310
THINBOARD_HEIGHT = 280 + 14
BUTTON_GAP = 12.5
COLOR_PICKER_WIDTH = 256
COLOR_PICKER_HEIGHT = 256

window = {
	"name" : "EffectColorWindow",
	"style" : ("movable", "float",),
	"x" : (SCREEN_WIDTH - BOARD_WIDTH) / 2,
	"y" : (SCREEN_HEIGHT - BOARD_HEIGHT) / 2,
	"width" : BOARD_WIDTH,
	"height" : BOARD_HEIGHT,
	"children" :
	(
		{
			"name" : "Board",
			"type" : "board_with_titlebar",
			"style" : ("attach",),
			"x" : 0,
			"y" : 0,
			"width" : BOARD_WIDTH,
			"height" : BOARD_HEIGHT,
			"title":"Specular Color",
			"children" :
			(
				{
					"name" : "ThinBoard",
					"type" : "thinboard_circle",
					"x" : 13,
					"y" : 35,
					"width" : THINBOARD_WIDTH - 15,
					"height" : THINBOARD_HEIGHT - 15,
					"children" :
					(
						{
							"name" : "BGColorBar",
							"type" : "bar",
							"x" : 0,
							"y" : 0,
							"width" : THINBOARD_WIDTH - 15,
							"height" : THINBOARD_HEIGHT - 15,
							"color" : 0xff303030,
						},
						{
							"name" : "BGImage",
							"type" : "image",
							"x" : 2.5,
							"y" : 2.5,
							"image" : "d:/ymir work/ui/skillcolor/background_expanded.tga",
						},
						{
							"name" : "BGColorPickerImage",
							"type" : "image",
							"x" : 35,
							"y" : 20,
							"width" : COLOR_PICKER_WIDTH,
							"height" : COLOR_PICKER_HEIGHT,
							"image" : "d:/ymir work/ui/skillcolor/color_picker_background.tga",
							"children" :
							(
								{
									"name" : "BGColorPickerButton",
									"type" : "button",
									"x" : 0,
									"y" : 0,
									"width" : COLOR_PICKER_WIDTH,
									"height" : COLOR_PICKER_HEIGHT,
								},
								{
									"name" : "BGColorPickerDotImage",
									"type" : "image",
									"x" : 0,
									"y" : 0,
									"width" : 12,
									"height" : 12,
									"image" : "d:/ymir work/ui/skillcolor/color_picker_dot.tga",
								},
							),
						},
					),
				},
				{
					"name" : "SpecularIntensity",
					"type" : "sliderbar",
					"x" : 73,
					"y" : BOARD_HEIGHT - 64,
				},
				{
					"name" : "ConfirmButton",
					"type" : "button",
					"x" : BUTTON_GAP,
					"y" : BOARD_HEIGHT - 35.5,
					"text":"Set Specular Color",
					"text_height" : 6,
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				{
					"name" : "CancelButton",
					"type" : "button",
					"x" : BUTTON_GAP + 150,
					"y" : BOARD_HEIGHT - 35.5,
					"text" : "Cancel",
					"text_height" : 6,
					"default_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_01.sub",
					"over_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_02.sub",
					"down_image" : "d:/ymir work/ui/game/myshop_deco/select_btn_03.sub",
				},
				
				# RenderView
				{
					"name" : "RenderTarget",
					"type" : "render_target",
					"style" : ("attach",),

					"x" : THINBOARD_WIDTH + 10,
					"y" : 35,

					"width" : 290,
					"height" : 307,

					"index" : 2,
					"children" :
					(
						{
							"name" : "mvUpCmrBtn",
							"type" : "button",

							"x" : 132-55,
							"y" : 286,

							"default_image" : "d:/ymir work/ui/game/monster_card/button/up_camera/up_camera_button_default.sub",
							"over_image" : "d:/ymir work/ui/game/monster_card/button/up_camera/up_camera_button_over.sub",
							"down_image" : "d:/ymir work/ui/game/monster_card/button/up_camera/up_camera_button_down.sub",
						},

						{
							"name" : "mvDownCmrBtn",
							"type" : "button",

							"x" : 153-55,
							"y" : 286,

							"default_image" : "d:/ymir work/ui/game/monster_card/button/down_camera/down_camera_button_default.sub",
							"over_image" : "d:/ymir work/ui/game/monster_card/button/down_camera/down_camera_button_over.sub",
							"down_image" : "d:/ymir work/ui/game/monster_card/button/down_camera/down_camera_button_down.sub",
						},
						{
							"name" : "rotLeftBtn",
							"type" : "button",

							"x" : 174-55,
							"y" : 286,

							"default_image" : "d:/ymir work/ui/game/monster_card/button/left_rotation/left_rotation_button_default.sub",
							"over_image" : "d:/ymir work/ui/game/monster_card/button/left_rotation/left_rotation_button_over.sub",
							"down_image" : "d:/ymir work/ui/game/monster_card/button/left_rotation/left_rotation_button_down.sub",
						},

						{
							"name" : "rotRightBtn",
							"type" : "button",

							"x" : 195-55,
							"y" : 286,

							"default_image" : "d:/ymir work/ui/game/monster_card/button/right_rotation/right_rotation_button_default.sub",
							"over_image" : "d:/ymir work/ui/game/monster_card/button/right_rotation/right_rotation_button_over.sub",
							"down_image" : "d:/ymir work/ui/game/monster_card/button/right_rotation/right_rotation_button_down.sub",
						},

						{
							"name" : "mvResetBtn",
							"type" : "button",

							"x" : 216-55,
							"y" : 286,

							"default_image" : "d:/ymir work/ui/game/monster_card/button/mv_reset/mv_reset_button_default.sub",
							"over_image" : "d:/ymir work/ui/game/monster_card/button/mv_reset/mv_reset_button_over.sub",
							"down_image" : "d:/ymir work/ui/game/monster_card/button/mv_reset/mv_reset_button_down.sub",
						},

						{
							"name" : "zumInBtn",
							"type" : "button",

							"x" : 237-55,
							"y" : 286,

							"default_image" : "d:/ymir work/ui/game/monster_card/button/zoomin/zoomin_rotation_button_default.sub",
							"over_image" : "d:/ymir work/ui/game/monster_card/button/zoomin/zoomin_rotation_button_over.sub",
							"down_image" : "d:/ymir work/ui/game/monster_card/button/zoomin/zoomin_rotation_button_down.sub",
						},

						{
							"name" : "zumOutBtn",
							"type" : "button",

							"x" : 258-55,
							"y" : 286,

							"default_image" : "d:/ymir work/ui/game/monster_card/button/zoomout/zoomin_rotation_button_default.sub",
							"over_image" : "d:/ymir work/ui/game/monster_card/button/zoomout/zoomin_rotation_button_over.sub",
							"down_image" : "d:/ymir work/ui/game/monster_card/button/zoomout/zoomin_rotation_button_down.sub",
						},
					),
				},
			)
		},
	),
}

