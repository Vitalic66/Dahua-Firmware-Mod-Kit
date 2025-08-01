from .config import *

DAHUA_FILES = OrderedDict([
	("hwid", {
		"required": True,
		"type": DAHUA_TYPE.Plain
	}),
	("Install", {
		"required": True,
		"type": DAHUA_TYPE.Plain
	}),
	("dhboot.bin.img", {
		"required": True,
		"type": DAHUA_TYPE.uImage | DAHUA_TYPE.Plain,
		"size": 0x000c0000
	}),
	("check.img", {
		"required": True,
		"type": DAHUA_TYPE.uImage | DAHUA_TYPE.Plain
	}),
	("romfs-x.squashfs.img", {
		"required": True,
		"type": DAHUA_TYPE.uImage | DAHUA_TYPE.SquashFS,
		"size": 0x02000000
	}),
	("kernel.img", {
		"required": True,
		"type": DAHUA_TYPE.Plain,
		"size": 0x00400000
	}),
	("pd-x.squashfs.img", {
		"required": True,
		"type": DAHUA_TYPE.uImage | DAHUA_TYPE.SquashFS,
		"size": 0x00460000
	}),
	("web-x.squashfs.img", {
		"required": True,
		"type": DAHUA_TYPE.uImage | DAHUA_TYPE.SquashFS,
		"size": 0x00800000
	}),
	("partition-x.cramfs.img", {
		"required": True,
		"type": DAHUA_TYPE.uImage | DAHUA_TYPE.CramFS,
		"size": 0x00100000
	}),
	("sign.img", {
		"required": True,
		"type": DAHUA_TYPE.Plain
	})
])
