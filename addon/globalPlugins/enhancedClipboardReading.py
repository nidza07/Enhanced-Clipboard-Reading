import addonHandler
import globalPluginHandler
import ui
import api
import speech
import scriptHandler
from scriptHandler import script
import config
from gui import settingsDialogs, guiHelper, nvdaControls

addonHandler.initTranslation()

config.conf.spec["enhancedClipboardReading"] = {
	"maxLength": "integer(default=1023, min=1, max=1000000)",
}


class EnhancedClipboardSettingsPanel(settingsDialogs.SettingsPanel):
	# Translators: The title of the Enhanced Clipboard Reading settings panel.
	title = _("Enhanced Clipboard Reading")

	def makeSettings(self, sizer):
		sHelper = guiHelper.BoxSizerHelper(self, sizer=sizer)
		# Translators: Label for the maximum clipboard length spin control.
		self.maxLengthCtrl = sHelper.addLabeledControl(
			_("&Maximum clipboard length before using browsable message (characters):"),
			nvdaControls.SelectOnFocusSpinCtrl,
			min=1,
			max=1000000,
			initial=config.conf["enhancedClipboardReading"]["maxLength"],
		)

	def onSave(self):
		config.conf["enhancedClipboardReading"]["maxLength"] = self.maxLengthCtrl.GetValue()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):

	def __init__(self):
		super().__init__()
		settingsDialogs.NVDASettingsDialog.categoryClasses.append(EnhancedClipboardSettingsPanel)

	def terminate(self):
		settingsDialogs.NVDASettingsDialog.categoryClasses.remove(EnhancedClipboardSettingsPanel)

	@script(
		# Translators: Input help mode message for the enhanced clipboard reading command.
		description=_(
			"Reports the text on the Windows clipboard. "
			"Pressing twice spells this information. "
			"Pressing three times displays the clipboard contents in a browsable window. "
			"If the clipboard exceeds the configured character limit, a browsable window is shown "
			"on the first press, and additional presses are ignored."
		),
		gesture="kb:NVDA+c",
		speakOnDemand=True,
	)
	def script_reportClipboardText(self, gesture):
		try:
			text = api.getClipData()
		except Exception:
			text = None
		if not text or not isinstance(text, str) or text.isspace():
			# Translators: Presented when there is no text on the clipboard.
			ui.message(_("There is no text on the clipboard"))
			return
		maxLength = config.conf["enhancedClipboardReading"]["maxLength"]
		repeatCount = scriptHandler.getLastScriptRepeatCount()
		if len(text) <= maxLength:
			if repeatCount == 0:
				ui.message(text)
			elif repeatCount == 1:
				speech.speakSpelling(text, useCharacterDescriptions=False)
			elif repeatCount == 2:
				# Triple press: show browsable message
				ui.browseableMessage(
					text,
					# Translators: Title of the browsable message showing clipboard contents.
					title=_("Clipboard contents"),
				)
		else:
			# Over the limit: only first press does anything (opens browsable window)
			if repeatCount == 0:
				ui.browseableMessage(
					text,
					# Translators: Title of the browsable message showing clipboard contents.
					title=_("Clipboard contents"),
				)
