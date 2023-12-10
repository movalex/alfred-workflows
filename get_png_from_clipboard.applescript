on run argv
	set clipboardImage to the clipboard as «class PNGf»
	set filePath to "/tmp/clipboard_image.png"
	set fileRef to open for access (POSIX file filePath as string) with write permission
	write clipboardImage to fileRef
	close access fileRef
end run