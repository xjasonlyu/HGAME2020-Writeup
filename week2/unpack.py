b = (
    0x68, 0x68, 0x63, 0x70, 0x69, 0x80, 0x5B,
    0x75, 0x78, 0x49, 0x6D, 0x76, 0x75, 0x7B,
    0x75, 0x6E, 0x41, 0x84, 0x71, 0x65, 0x44,
    0x82, 0x4A, 0x85, 0x8C, 0x82, 0x7D, 0x7A,
    0x82, 0x4D, 0x90, 0x7E, 0x92, 0x54, 0x98,
    0x88, 0x96, 0x98, 0x57, 0x95, 0x8F, 0xA6,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    )


flag = ''
for i in range(42):
    flag += chr(b[i]-i)

print(flag)
