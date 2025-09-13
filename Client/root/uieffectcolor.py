import app
import net
import chr
import chrmgr
import player
import ui
import uiCommon
import grp
import wndMgr
import uiScriptLocale
import localeInfo
import chat
import uiToolTip
import item
import grpText
import hexColorInfo
import renderTarget

class EffectColor(ui.ScriptWindow):
	RENDER_TARGET_INDEX = 2
	
	def __init__(self):
		ui.Window.__init__(self)
		self.isLoaded = False

		self.pickerPos = (0, 0)
		self.colorHexCodes = hexColorInfo.HEX_CODES
		self.genColor = None
		self.colorMarker = None
		self.toolTip = None
		self.popup = None
		self.selectedColor = False
		self.srcSlotPos = 0
		self.itemVnum = 0
		self.isEquip = False
		self.confirm = False

		self.effectColor_a = 255
		self.effectColor_b = 255
		self.effectColor_c = 255
		self.effectPower = 0

	def __del__(self):
		ui.Window.__del__(self)

	def LoadWindow(self):
		if self.isLoaded == 1:
			return

		self.isLoaded = 1

		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "UIScript/effectcolor.py")
		except:
			import exception
			exception.Abort("EffectColorWindow.LoadWindow.LoadScriptFile")

		try:
			self.GetChild("Board").SetCloseEvent(ui.__mem_func__(self.Close))
			self.board = self.GetChild("Board")
			self.thinBoard = self.GetChild("ThinBoard")
			self.bgColorBar = self.GetChild("BGColorBar")
			self.bgImg = self.GetChild("BGImage")
			self.bgColorPickerImg = self.GetChild("BGColorPickerImage")
			self.bgColorPickerButton = self.GetChild("BGColorPickerButton")
			self.bgColorPickerDotImg = self.GetChild("BGColorPickerDotImage")
			self.bgColorPickerDotImg.Hide()
			self.confirmButton = self.GetChild("ConfirmButton")
			self.cancelButton = self.GetChild("CancelButton")
			self.specularIntensity = self.GetChild("SpecularIntensity")
			self.specularIntensity.Hide()
			
			self.renderTarget = self.GetChild("RenderTarget")
			
			self.buttons = {
				"moveUp" : self.GetChild("mvUpCmrBtn"),
				"moveDown" : self.GetChild("mvDownCmrBtn"),
				"rotateLeft" : self.GetChild("rotLeftBtn"),
				"rotateRight" : self.GetChild("rotRightBtn"),

				"moveReset" : self.GetChild("mvResetBtn"),

				"zoomIn" : self.GetChild("zumInBtn"),
				"zoomOut" : self.GetChild("zumOutBtn"),
			}

			self.buttons["moveUp"].SetEvent(ui.__mem_func__(self.__ModelUpDownCameraProgress))
			self.buttons["moveDown"].SetEvent(ui.__mem_func__(self.__ModelUpDownCameraProgress))
			self.buttons["rotateLeft"].SetEvent(ui.__mem_func__(self.__ModelRotationProgress))
			self.buttons["rotateRight"].SetEvent(ui.__mem_func__(self.__ModelRotationProgress))
			self.buttons["moveReset"].SetEvent(ui.__mem_func__(self.__ResetSettings))
			self.buttons["zoomIn"].SetEvent(ui.__mem_func__(self.__ModelZoomProgress))
			self.buttons["zoomOut"].SetEvent(ui.__mem_func__(self.__ModelZoomProgress))
		except:
			import exception
			exception.Abort("EffectColorWindow.LoadWindow.__Objects")

		try:
			if self.bgColorPickerButton:
				self.bgColorPickerButton.SetEvent(ui.__mem_func__(self.OnClickColorPicker))

			if self.confirmButton:
				self.confirmButton.SetEvent(ui.__mem_func__(self.OnClickConfirmButton))

			if self.cancelButton:
				self.cancelButton.SetEvent(ui.__mem_func__(self.OnClickCancelButton))
			
			if self.specularIntensity:
				self.specularIntensity.SetEvent(ui.__mem_func__(self.OnSetSpecularIntensity))
		except:
			import exception
			exception.Abort("EffectColorWindow.LoadWindow.__Functions")

		self.toolTip = uiToolTip.ToolTip()
		self.toolTip.ClearToolTip()
		self.popup = uiCommon.PopupDialog()

	def Destroy(self):
		self.ClearDictionary()
		self.pickerPos = (0, 0)
		self.genColor = None
		self.colorMarker = None
		self.toolTip = None
		self.popup = None
		self.selectedColor = False
		self.srcSlotPos = 0
		self.itemVnum = 0
		self.isEquip = False
		self.confirm = False

		self.effectColor_a = 255
		self.effectColor_b = 255
		self.effectColor_c = 255
		self.effectPower = 0

	def Open(self, itemVnum, slotIndex, isEquip):
		if not self.isLoaded:
			self.LoadWindow()

		self.srcSlotPos = slotIndex
		self.itemVnum = itemVnum
		self.isEquip = isEquip
		
		r, g, b, a = player.GetSpecularColor(slotIndex)
		self.specularIntensity.SetSliderPos(float(a) / 255)
		self.effectPower = a
		
		if not isEquip:
			self.renderTarget.Show()
			self.board.SetSize(325 + 305, 340 + 14)
			self.SetSize(325 + 305, 340 + 14)
			
			renderTarget.SetBackground(self.RENDER_TARGET_INDEX, "d:/ymir work/ui/small_render_target.png")
			renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, True)
			renderTarget.SelectModel(self.RENDER_TARGET_INDEX, player.GetRace())
			renderTarget.ResetSettings(self.RENDER_TARGET_INDEX)
			
			item.SelectItem(itemVnum)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()
			
			if itemType == item.ITEM_TYPE_ARMOR and itemSubType == item.ARMOR_BODY or itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_BODY:
				renderTarget.SetArmor(self.RENDER_TARGET_INDEX, itemVnum)
			elif itemType == item.ITEM_TYPE_WEAPON:
				renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, itemVnum)
			elif itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_HAIR:
				renderTarget.SetHair(self.RENDER_TARGET_INDEX, item.GetValue(3))
			
			if app.ENABLE_COSTUME_WEAPON_SYSTEM:
				if itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_WEAPON:
					renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, itemVnum)
			
			if app.ENABLE_SASH_SYSTEM:
				if itemType == item.ITEM_TYPE_COSTUME and itemSubType == item.COSTUME_TYPE_SASH:
					renderTarget.SetSash(self.RENDER_TARGET_INDEX, itemVnum)
			
			# renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, GetFilterPart(itemVnum), r, g, b, a)
		else:
			self.renderTarget.Hide()
			self.board.SetSize(325, 340 + 14)
			self.SetSize(325, 340 + 14)
		
		self.SetCenterPosition()
		self.SetTop()
		self.Show()

	def OnSetSpecularIntensity(self):
		self.effectPower = int(self.specularIntensity.GetSliderPos()*255)

	def OnClickCancelButton(self):
		self.Close()

	def OnClickConfirmButton(self):
		self.confirm = True
		
		if self.isEquip:
			player.UpdateEffectColor(self.effectColor_a, self.effectColor_b, self.effectColor_c, self.effectPower)
			# player.RefreshEffect()
			
		net.SendSpecularColorPacket(self.srcSlotPos, self.effectColor_a, self.effectColor_b, self.effectColor_c, self.effectPower)
		self.Close()

	def Close(self):
		if not self.confirm:
			if self.isEquip:
				r, g, b, a = player.GetSpecularColor(self.srcSlotPos)
				player.UpdateEffectColor(r, g, b, a)

		self.pickerPos = (0, 0)
		self.genColor = None
		self.colorMarker = None
		self.selectedColor = False
		self.effectColor_a = 255
		self.effectColor_b = 255
		self.effectColor_c = 255
		self.effectPower = 0
		self.bgColorPickerDotImg.Hide()
		self.srcSlotPos = 0
		self.itemVnum = 0
		self.isEquip = False
		self.confirm = False
		self.Hide()

	def OnPressEscapeKey(self):
		self.Close()
		return True

	def OnClickColorPicker(self):
		rgbColor = self.GetRGBColor(self.pickerPos[0], self.pickerPos[1])

		if rgbColor[0] <= 20 and rgbColor[1] <= 20 and rgbColor[2] <= 20:
			rgbColorNew = list(rgbColor)
			rgbColorNew[0] = 0
			rgbColorNew[1] = 0
			rgbColorNew[2] = 0
			rgbColor = tuple(rgbColorNew)
			self.selectedColor = False
		else:
			self.selectedColor = True

		r, g, b = (float(rgbColor[0]) / 255, float(rgbColor[1]) / 255, float(rgbColor[2]) / 255)
		self.genColor = (r, g, b)

		if self.bgColorBar:
			self.bgColorBar.SetColor(grp.GenerateColor(r, g, b, 1.0))
			
			# if self.renderTarget.IsShow():
				# renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, GetFilterPart(self.itemVnum), rgbColor[0], rgbColor[1], rgbColor[2], self.effectPower)
			
			if self.isEquip:
				player.UpdateEffectColor(rgbColor[0], rgbColor[1], rgbColor[2], self.effectPower)

		if self.bgColorPickerDotImg:
			self.bgColorPickerDotImg.SetPosition(self.pickerPos[0] - (self.bgColorPickerDotImg.GetWidth()/2), self.pickerPos[1] - (self.bgColorPickerDotImg.GetHeight()/2))
			self.bgColorPickerDotImg.Show()

			colorMarker = ui.TextLine()
			colorMarker.SetParent(self.bgColorPickerDotImg)
			colorMarker.SetPosition(5, -15)
			colorMarker.SetHorizontalAlignCenter()
			colorMarker.SetText("%s" % self.colorHexCodes[str("%sx%s" % (self.pickerPos[0], self.pickerPos[1]))])
			colorMarker.Show()
			self.colorMarker = colorMarker

		tmpR, tmpG, tmpB = (float(rgbColor[0]), float(rgbColor[1]), float(rgbColor[2]))
		self.effectColor_a = tmpR
		self.effectColor_b = tmpG
		self.effectColor_c = tmpB

	def HexToRGB(self, strValue):
		strValue = strValue.lstrip("#")
		lv = len(strValue)
		rgbCode = (0, 0 ,0)
		try:
			rgbCode = tuple(int(strValue[i:i+int(lv/3)], 16) for i in range(0, lv, int(lv/3)))
		except:
			pass

		return rgbCode

	def GetRGBColor(self, x, y):
		pickerPos = "%dx%d" % (x, y)
		hexColorCode = self.colorHexCodes[str(pickerPos)].split("#")
		return self.HexToRGB(str(hexColorCode[1]))

	def ChangeColor(self, x, y):
		if x > 255:
			x = 255

		if y > 255:
			y = 255

		rgbColor = self.GetRGBColor(x, y)
		r, g, b = (float(rgbColor[0]) / 255, float(rgbColor[1]) / 255, float(rgbColor[2]) / 255)

		if self.bgColorBar:
			self.bgColorBar.SetColor(grp.GenerateColor(r, g, b, 1.0))
			
			# if self.renderTarget.IsShow():
				# renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, GetFilterPart(self.itemVnum), rgbColor[0], rgbColor[1], rgbColor[2], self.effectPower)
			
			if self.isEquip:
				player.UpdateEffectColor(rgbColor[0], rgbColor[1], rgbColor[2], self.effectPower)

	def OnUpdate(self):
		self.__ModelUpDownCameraProgress()
		self.__ModelRotationProgress()
		self.__ModelZoomProgress()
		
		if self.bgColorPickerButton.IsIn():
			xBtn, yBtn = self.bgColorPickerButton.GetGlobalPosition()
			btnHeight = self.bgColorPickerButton.GetHeight()
			xMousePos, yMousePos = wndMgr.GetMousePosition()

			if yMousePos - yBtn < btnHeight - 1:
				xMouse = xMousePos - xBtn
				yMouse = yMousePos - yBtn

				if xMouse > 255:
					xMouse = 255

				if yMouse > 255:
					yMouse = 255

				self.pickerPos = (xMouse, yMouse)
				self.ChangeColor(xMouse, yMouse)

				if self.toolTip:
					toolTipText = "%s" % (self.colorHexCodes[str("%sx%s" % (xMouse, yMouse))])
					arglen = len(str(toolTipText))
					self.toolTip.ClearToolTip()
					self.toolTip.SetThinBoardSize(8 * arglen)
					self.toolTip.AppendTextLine(toolTipText, 0xffffff00)
					self.toolTip.Show()
				else:
					self.toolTip.Hide()
		else:
			if self.genColor and self.bgColorBar:
				self.bgColorBar.SetColor(grp.GenerateColor(self.genColor[0], self.genColor[1], self.genColor[2], 1.0))
				
				# if self.renderTarget.IsShow():
					# renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, GetFilterPart(self.itemVnum), self.effectColor_a, self.effectColor_b, self.effectColor_c, self.effectPower)
				
				if self.isEquip:
					player.UpdateEffectColor(self.effectColor_a, self.effectColor_b, self.effectColor_c, self.effectPower)
			else:
				r, g, b, a = player.GetSpecularColor(self.srcSlotPos)
				self.bgColorBar.SetColor(grp.GenerateColor(float(r) / 255, float(g) / 255, float(b) / 255, 0.0))
				
				# if self.renderTarget.IsShow():
					# renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, GetFilterPart(self.itemVnum), r, g, b, self.effectPower)
				
				if self.isEquip:
					player.UpdateEffectColor(r, g, b, a)

			if self.toolTip:
				self.toolTip.Hide()

	def __ModelUpDownCameraProgress(self):
		if self.buttons["moveUp"].IsDown():
			renderTarget.SetRenderingPosition(self.RENDER_TARGET_INDEX, False)

		if self.buttons["moveDown"].IsDown():
			renderTarget.SetRenderingPosition(self.RENDER_TARGET_INDEX, True)

	def __ModelRotationProgress(self):
		if self.buttons["rotateLeft"].IsDown():
			renderTarget.SetMove(self.RENDER_TARGET_INDEX, False)

		if self.buttons["rotateRight"].IsDown():
			renderTarget.SetMove(self.RENDER_TARGET_INDEX, True)

	def __ModelZoomProgress(self):
		if self.buttons["zoomIn"].IsDown():
			renderTarget.SetZoom(self.RENDER_TARGET_INDEX, True)

		if self.buttons["zoomOut"].IsDown():
			renderTarget.SetZoom(self.RENDER_TARGET_INDEX, False)

	def __ResetSettings(self):
		renderTarget.ResetSettings(self.RENDER_TARGET_INDEX)


