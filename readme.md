# Enhanced Clipboard Reading
This add-on enhances the default NVDA+C command to read the contents of the clipboard.

## Configuring a character limit
By default, if the clipboard contains more than 1023 characters, NVDA+C won't read the text and will instead tell this to you.

With this add-on installed and enabled, you can configure a custom character limit by using the "Enhanced Clipboard Reading" settings panel in the NVDA settings dialog. As long as there is less text on the clipboard than the configured limit, NVDA+C will read the text directly, and NVDA+C twice will spell it. Be careful: some synthesizers may crash if sending large amounts of text to them, experiment and notice which limit is safe for your particular synthesizer.

## Browseable messages
If NVDA+C is pressed three times, a browseable message with the contents of the clipboard will be shown for easier reviewing.

This message will always be shown on a single press if there is more text on the clipboard than the configured character limit, instead of NVDA simply reporting that the clipboard contains a large amount of text.

## Credits
- NV Access and the NVDA community: for developing NVDA, as well as the add-on template.
- Claude Code: for coding assistance.
- Translators: for making the add-on globally accessible to everybody!