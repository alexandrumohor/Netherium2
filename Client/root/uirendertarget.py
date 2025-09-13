import ui
import wndMgr
import renderTarget
import player
import chr
import item
import app
import constInfo

class RenderTarget(ui.ScriptWindow):
	RENDER_TARGET_INDEX = 1
	Window = None

	def __init__(self):
		ui.ScriptWindow.__init__(self)

		self.max_pos_x = wndMgr.GetScreenWidth()
		self.max_pos_y = wndMgr.GetScreenHeight()


		self.Initialize()
		self.Init()

	def Initialize(self):
		self.interface = None

	@staticmethod
	def Get():
		if RenderTarget.Window == None:
			RenderTarget.Window = RenderTarget()

		return RenderTarget.Window

	def __del__(self):
		ui.ScriptWindow.__del__(self)
		self.Initialize()

	def DisplayUser(self, vRace=0, vItemWeapon=0, vItemArmor=0, vItemHair=0, vItemSash=0, vItemCrown=0, slotIndex = -1):
		renderTarget.SetBackground(self.RENDER_TARGET_INDEX, "d:/ymir work/ui/render_target.tga")
		renderTarget.SetVisibility(self.RENDER_TARGET_INDEX, True)
		renderTarget.SelectModel(self.RENDER_TARGET_INDEX, vRace)
		renderTarget.ResetSettings(self.RENDER_TARGET_INDEX)
		# renderTarget.SetEffect(self.RENDER_TARGET_INDEX)

		if vRace > 7:
			return

		playerRace = player.GetRace()

		if vItemArmor != 0:
			if app.ENABLE_SPECULAR_SYSTEM:
				if slotIndex != -1:
					r, g, b, a = player.GetSpecularColor(slotIndex)
            
					if r > 0 or g > 0 or b > 0 or a > 0:
						renderTarget.SetArmor(self.RENDER_TARGET_INDEX, vItemArmor, True)
						renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(vItemArmor), r, g, b, a)
					else:
						renderTarget.SetArmor(self.RENDER_TARGET_INDEX, vItemArmor)
				else:
					renderTarget.SetArmor(self.RENDER_TARGET_INDEX, vItemArmor)
			else:
				renderTarget.SetArmor(self.RENDER_TARGET_INDEX, vItemArmor)
		else:
			if playerRace == vRace:
				if player.GetItemIndex(item.COSTUME_SLOT_START) == 0:
					if app.ENABLE_SPECULAR_SYSTEM:
						r, g, b, a = player.GetSpecularColor(player.EQUIPMENT_SLOT_START)
						
						if r > 0 or g > 0 or b > 0 or a > 0:
							renderTarget.SetArmor(self.RENDER_TARGET_INDEX, player.GetItemIndex(player.EQUIPMENT_SLOT_START), True)
							renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(player.GetItemIndex(player.EQUIPMENT_SLOT_START)), r, g, b, a)
						else:
							renderTarget.SetArmor(self.RENDER_TARGET_INDEX, player.GetItemIndex(player.EQUIPMENT_SLOT_START))
					else:
						renderTarget.SetArmor(self.RENDER_TARGET_INDEX, player.GetItemIndex(player.EQUIPMENT_SLOT_START))
				else:
					if app.ENABLE_SPECULAR_SYSTEM:
						r, g, b, a = player.GetSpecularColor(item.COSTUME_SLOT_START)
                    
						if r > 0 or g > 0 or b > 0 or a > 0:
							renderTarget.SetArmor(self.RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_START), True)
							renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(player.GetItemIndex(item.COSTUME_SLOT_START)), r, g, b, a)
						else:
							renderTarget.SetArmor(self.RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_START))
					else:
						renderTarget.SetArmor(self.RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_START))
			else:
				renderTarget.SetArmor(self.RENDER_TARGET_INDEX, 0)

		if vItemWeapon != 0:
			if app.ENABLE_SPECULAR_SYSTEM:
				if slotIndex != -1:
					r, g, b, a = player.GetSpecularColor(slotIndex)
					
					if r > 0 or g > 0 or b > 0 or a > 0:
						renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, vItemWeapon, True)
						renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(vItemWeapon), r, g, b, a)
					else:
						renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, vItemWeapon)
				else:
					renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, vItemWeapon)
			else:
				renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, vItemWeapon)
		else:
			#if playerRace == vRace:
			#	if  player.GetItemIndex(item.COSTUME_SLOT_WEAPON) == 0:
			#		if app.ENABLE_SPECULAR_SYSTEM:
			#			r, g, b, a = player.GetSpecularColor(player.EQUIPMENT_SLOT_START+4)
            #        
			#			if r > 0 or g > 0 or b > 0 or a > 0:
			#				renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, player.GetItemIndex(player.EQUIPMENT_SLOT_START+4), True)
			#				renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(player.GetItemIndex(player.EQUIPMENT_SLOT_START+4)), r, g, b, a)
			#			else:
			#				renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, player.GetItemIndex(player.EQUIPMENT_SLOT_START+4))
			#		else:
			#			renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, player.GetItemIndex(player.EQUIPMENT_SLOT_START+4))
			#	else:
			#		if app.ENABLE_SPECULAR_SYSTEM:
			#			r, g, b, a = player.GetSpecularColor(item.COSTUME_SLOT_WEAPON)
            #        
			#			if r > 0 or g > 0 or b > 0 or a > 0:
			#				renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_WEAPON), True)
			#				renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(player.GetItemIndex(item.COSTUME_SLOT_WEAPON)), r, g, b, a)
			#			else:
			#				renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_WEAPON))
			#		else:
			#			renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, player.GetItemIndex(item.COSTUME_SLOT_WEAPON))
			#else:
			renderTarget.SetWeapon(self.RENDER_TARGET_INDEX, 0)

		if vItemHair != 0:
			if app.ENABLE_SPECULAR_SYSTEM:
				if slotIndex != -1:
					r, g, b, a = player.GetSpecularColor(slotIndex)
            
					if r > 0 or g > 0 or b > 0 or a > 0:
						renderTarget.SetHair(self.RENDER_TARGET_INDEX, vItemHair, True)
						renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(player.GetItemIndex(slotIndex)), r, g, b, a)
					else:
						renderTarget.SetHair(self.RENDER_TARGET_INDEX, vItemHair)
				else:
					renderTarget.SetHair(self.RENDER_TARGET_INDEX, vItemHair)
			else:
				renderTarget.SetHair(self.RENDER_TARGET_INDEX, vItemHair)
		else:
			if playerRace == vRace:
				if app.ENABLE_SPECULAR_SYSTEM:
					r, g, b, a = player.GetSpecularColor(item.COSTUME_SLOT_START+1)
                
					if r > 0 or g > 0 or b > 0 or a > 0:
						renderTarget.SetHair(self.RENDER_TARGET_INDEX, chr.GetHair(), True)
						renderTarget.UpdateSpecularColor(self.RENDER_TARGET_INDEX, constInfo.GetFilterPart(player.GetItemIndex(item.COSTUME_SLOT_START+1)), r, g, b, a)
					else:
						renderTarget.SetHair(self.RENDER_TARGET_INDEX, chr.GetHair())
				else:
					renderTarget.SetHair(self.RENDER_TARGET_INDEX, chr.GetHair())
			else:
				renderTarget.SetHair(self.RENDER_TARGET_INDEX, 0)

	def Init(self):
		try:
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/RenderTargetWindow.py")
		except:
			import exception
			exception.Abort("RenderTargetWindow.LoadDialog.LoadScript")

		try:
			self.titleBar = self.GetChild("TitleBar")
			self.titleBar.CloseButton("show")
			self.titleBar.SetCloseEvent(self.Close)

			self.board = self.GetChild("board")

			self.RenderTarget = self.GetChild("RenderTarget")

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

			self.SetCenterPosition()

		except:
			import exception
			exception.Abort("RenderTargetWindow.LoadDialog.BindObject")

	def BindInterface(self, interface):
		self.interface = interface

	def Destroy(self):
		self.Close()
		self.Initialize()

	def Close(self):
		self.Hide()

	def Open(self):
		self.Show()
		self.SetTop()

	def OnPressEscapeKey(self):
		self.Close()

	def MINMAX(self, min, value, max):

		if value < min:
			return min
		elif value > max:
			return max
		else:
			return value

	def OnUpdate(self):
		self.__ModelUpDownCameraProgress()
		self.__ModelRotationProgress()
		self.__ModelZoomProgress()

		x, y = self.GetGlobalPosition()

		pos_x = self.MINMAX(0, x, self.max_pos_x)
		pos_y = self.MINMAX(0, y, self.max_pos_y)

		self.SetPosition(pos_x, pos_y)

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
