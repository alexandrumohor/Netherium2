import ui
import grp
import player
import chat

TITLE_PREDEFINED = [
	"Write your title",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
	"BOSS DE BOSS",
	"SMECHERIE",
	"MEGAFRAIER",
]

ALIGN_PREDEFINED = [
	"Write your align",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
	"Cavaler",
	"Sugaci",
	"Preot",
]

class NewTitleWindow(ui.ScriptWindow):
	def __init__(self):
		ui.Window.__init__(self)
		self.LoadWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def LoadWindow(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/NewTitleWindow.py")

			titlebar_title = self.GetChild("titlebar_title")
			titlebar_title.SetCloseEvent(ui.__mem_func__(self.Close))

			# titlebar_align = self.GetChild("titlebar_align")
			# titlebar_align.CloseButtonHide()

			self.board_title = self.GetChild("board_title")
			# self.board_title = self.GetChild("board_title")

			############################################################################################

			self.preview_title = self.TextLine(self.board_title, 'Title', 10, 500, self.RGB(255, 650, 650))

			self.confirm_title = self.Button(self.board_title, 'Set Title', 'Set Title', self.board_title.GetWidth() - 616, 285, self.confirm_title_btn, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
			self.remove_title = self.Button(self.board_title, 'Remove Title', 'Remove Title', self.board_title.GetWidth() - 526, 285, self.remove_title_btn, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

			self.rTitleSlider = self.SliderBar(self.board_title, 0.0, self.redTitle_slider, 35, 195)
			self.gTitleSlider = self.SliderBar(self.board_title, 0.0, self.greenTitle_slider, 35, 215)
			self.bTitleSlider = self.SliderBar(self.board_title, 0.0, self.blueTitle_slider, 35, 235)

			############################################################################################

			self.preview_align = self.TextLine(self.board_title, 'Align', self.board_title.GetWidth() - 125, 100, self.RGB(255, 650, 650))

			self.confirm_align = self.Button(self.board_title, 'Set Align', 'Set Align', self.board_title.GetWidth() - 205, 285, self.confirm_align_btn, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
			self.remove_align = self.Button(self.board_title, 'Remove Align', 'Remove Align', self.board_title.GetWidth() - 115, 285, self.remove_align_btn, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')

			self.rAlignSlider = self.SliderBar(self.board_title, 0.0, self.redAlign_slider, self.board_title.GetWidth() - 200, 195)
			self.gAlignSlider = self.SliderBar(self.board_title, 0.0, self.greenAlign_slider, self.board_title.GetWidth() - 200, 215)
			self.bAlignSlider = self.SliderBar(self.board_title, 0.0, self.blueAlign_slider, self.board_title.GetWidth() - 200, 235)

			############################################################################################

			self.title_input, self.titleInput = self.EditLine(self.board_title, '', 35, 28, 160, 15, 34)
			self.titleInput.SetEscapeEvent(ui.__mem_func__(self.Close))

			self.titleListBase = ui.SlotBar()
			self.titleListBase.SetParent(self.board_title)
			self.titleListBase.SetSize(200 - 40, 110)
			self.titleListBase.SetPosition(35, 50)
			self.titleListBase.Show()
			
			self.titleList = ui.ListBox()
			self.titleList.SetParent(self.titleListBase)
			self.titleList.SetSize(200 - 57, 110)
			self.titleList.SetPosition(0, 0)
			self.titleList.Show()
			
			self.titleListScrollBar = ui.ScrollBar()
			self.titleListScrollBar.SetParent(self.titleListBase)
			self.titleListScrollBar.SetPosition(19, 4)
			self.titleListScrollBar.SetScrollBarSize(105)
			self.titleListScrollBar.SetWindowHorizontalAlignRight()
			self.titleListScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScrollTitle))
			self.titleListScrollBar.Show()

			############################################################################################

			self.align_input, self.alignInput = self.EditLine(self.board_title, '', 455, 28, 160, 15, 34)
			self.alignInput.SetEscapeEvent(ui.__mem_func__(self.Close))

			self.alignListBase = ui.SlotBar()
			self.alignListBase.SetParent(self.board_title)
			self.alignListBase.SetSize(200 - 40, 110)
			self.alignListBase.SetPosition(455, 50)
			self.alignListBase.Show()

			self.alignList = ui.ListBox()
			self.alignList.SetParent(self.alignListBase)
			self.alignList.SetSize(200 - 57, 110)
			self.alignList.SetPosition(0, 0)
			self.alignList.Show()
			
			self.alignListScrollBar = ui.ScrollBar()
			self.alignListScrollBar.SetParent(self.alignListBase)
			self.alignListScrollBar.SetPosition(19, 4)
			self.alignListScrollBar.SetScrollBarSize(105)
			self.alignListScrollBar.SetWindowHorizontalAlignRight()
			self.alignListScrollBar.SetScrollEvent(ui.__mem_func__(self.OnScrollAlign))
			self.alignListScrollBar.Show()

			############################################################################################

			self.rTitle = 1.0
			self.gTitle = 1.0
			self.bTitle = 1.0

			self.rAlign = 1.0
			self.gAlign = 1.0
			self.bAlign = 1.0

			self.rTitleSlider.SetSliderPos(1.0)
			self.gTitleSlider.SetSliderPos(1.0)
			self.bTitleSlider.SetSliderPos(1.0)

			self.rAlignSlider.SetSliderPos(1.0)
			self.gAlignSlider.SetSliderPos(1.0)
			self.bAlignSlider.SetSliderPos(1.0)

			self.titleList.ClearItem()
			self.alignList.ClearItem()

			for i in xrange(len(TITLE_PREDEFINED)):
				if i == 0:
					continue
				self.titleList.InsertItem(i, "%s" % (TITLE_PREDEFINED[i]))
				self.titleList.SetEvent(ui.__mem_func__(self.OnSelectTitle))

			for i in xrange(len(ALIGN_PREDEFINED)):
				if i == 0:
					continue
				self.alignList.InsertItem(i, "%s" % (ALIGN_PREDEFINED[i]))
				self.alignList.SetEvent(ui.__mem_func__(self.OnSelectAlign))

			self.titleInput.SetText(TITLE_PREDEFINED[0])
			self.preview_title.SetPackedFontColor(grp.GenerateColor(self.rTitle, self.gTitle, self.bTitle, 1.0))
			self.alignInput.SetText(ALIGN_PREDEFINED[0])
			self.preview_align.SetPackedFontColor(grp.GenerateColor(self.rAlign, self.gAlign, self.bAlign, 1.0))
		except:
			import exception
			exception.Abort("NewTitleWindow.LoadScript")

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def Close(self):
		self.Hide()

	def Show(self):
		ui.ScriptWindow.Show(self)
		self.LoadWindow()

		self.SetCenterPosition()
		self.SetTop()

	def OnRender(self):
		self.preview_title.SetText(self.titleInput.GetText())
		self.preview_title.SetPackedFontColor(grp.GenerateColor(self.rTitle, self.gTitle, self.bTitle, 1.0))
		self.preview_title.SetPosition(self.board_title.GetWidth() - 2 * len(self.preview_title.GetText()) - 545, 255)

		self.preview_align.SetText(self.alignInput.GetText())
		self.preview_align.SetPackedFontColor(grp.GenerateColor(self.rAlign, self.gAlign, self.bAlign, 1.0))
		self.preview_align.SetPosition(self.board_title.GetWidth() - 2 * len(self.preview_align.GetText()) - 127, 255)

	def OnSelectTitle(self):
		self.preview_title.SetText(TITLE_PREDEFINED[self.titleList.GetSelectedItem()])
		self.titleInput.SetText(TITLE_PREDEFINED[self.titleList.GetSelectedItem()])
		
	def OnSelectAlign(self):
		self.preview_align.SetText(ALIGN_PREDEFINED[self.alignList.GetSelectedItem()])
		self.alignInput.SetText(ALIGN_PREDEFINED[self.alignList.GetSelectedItem()])

	def confirm_title_btn(self):
		if self.preview_title.GetText() != TITLE_PREDEFINED[0]:
			self.rTitle = int(self.rTitleSlider.GetSliderPos()*255)
			self.gTitle = int(self.gTitleSlider.GetSliderPos()*255)
			self.bTitle = int(self.bTitleSlider.GetSliderPos()*255)

			if self.preview_title.GetText() in TITLE_PREDEFINED:
				player.SetNewTitle(True, self.preview_title.GetText(), self.rTitle, self.gTitle, self.bTitle, 255)
			else:
				player.SetNewTitle(False, self.preview_title.GetText(), self.rTitle, self.gTitle, self.bTitle, 255)

			self.Close()
		else:
			chat.AppendChat(1, "Trebuie sa alegi un titlu ca sa il poti seta.")

	def remove_title_btn(self):
		player.RemoveNewTitle()
		self.Close()

	def confirm_align_btn(self):
		if self.preview_align.GetText() != ALIGN_PREDEFINED[0]:
			self.rAlign = int(self.rAlignSlider.GetSliderPos()*255)
			self.gAlign = int(self.gAlignSlider.GetSliderPos()*255)
			self.bAlign = int(self.bAlignSlider.GetSliderPos()*255)

			if self.preview_align.GetText() in ALIGN_PREDEFINED:
				player.SetNewAlign(True, self.preview_align.GetText(), self.rAlign, self.gAlign, self.bAlign, 255)
			else:
				player.SetNewAlign(False, self.preview_align.GetText(), self.rAlign, self.gAlign, self.bAlign, 255)

			self.Close()
		else:
			chat.AppendChat(1, "Trebuie sa alegi un grad ca sa il poti seta.")

	def remove_align_btn(self):
		player.RemoveNewAlign()
		self.Close()

	def redTitle_slider(self):
		self.rTitle = self.rTitleSlider.GetSliderPos()

	def greenTitle_slider(self):
		self.gTitle = self.gTitleSlider.GetSliderPos()

	def blueTitle_slider(self):
		self.bTitle = self.bTitleSlider.GetSliderPos()

	def redAlign_slider(self):
		self.rAlign = self.rAlignSlider.GetSliderPos()

	def greenAlign_slider(self):
		self.gAlign = self.gAlignSlider.GetSliderPos()

	def blueAlign_slider(self):
		self.bAlign = self.bAlignSlider.GetSliderPos()

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def OnScrollTitle(self):
		viewItemCount = self.titleList.GetViewItemCount()
		itemCount = self.titleList.GetItemCount()
		pos = self.titleListScrollBar.GetPos() * (itemCount - viewItemCount)
		self.titleList.SetBasePos(int(pos))

	def OnScrollAlign(self):
		viewItemCount = self.alignList.GetViewItemCount()
		itemCount = self.alignList.GetItemCount()
		pos = self.alignListScrollBar.GetPos() * (itemCount - viewItemCount)
		self.alignList.SetBasePos(int(pos))