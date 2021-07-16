class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        p = []
        for i in self.ingredients:
            for t in self.toppings:
                it = [i, t]
                p.append(it)
        return p

      
def unique_names(names1, names2):
    names = []
    for name in names1:
        if name not in names:
            names.append(name)
        for n in names2:
            if n not in names:
                names.append(n)
    return names

 
def toAscii85(data):
    h_str = ''
    result = ''
    for c in data:
        h_str += format(ord(c), '02x')
    index = 0
    while index < len(h_str):
        pad = max(((index + 8) - len(h_str)) / 2, 0)
        encode_block = h_str[index:index + 8] if pad == 0 else h_str[index:] + '00' * int(pad)
        if encode_block == '0' * 8 and pad == 0:
            result += 'z'
        else:
            encode_block_int = int(encode_block, 16) / (85 ** pad)
            encode_block_result = ''
            for _ in range(5 - int(pad)):
                encode_block_int, remainder = divmod(encode_block_int, 85)
                encode_block_result = chr(remainder + 33) + encode_block_result
            result += encode_block_result
        index += 8
    return '<~' + result + '~>'


def fromAscii85(data):
    result = ''
    chars = [' ', '\n', '\t', '\0']
    for c in chars:
        data = data.replace(c, '')
    data = data[2:-2]

    index = 0
    while index < len(data):
        if data[index] == 'z':
            result += '\0' * 4
            index += 1
        else:
            pad = max(index + 5 - len(data), 0)
            encoded_block = data[index:index + 5] if pad == 0 else data[index:] + 'u' * pad
            encoded_num = 0
            for i, c in enumerate(encoded_block[::-1]):
                encoded_num += (ord(c) - 33) * (85 ** i)
            encoded_byte = format(encoded_num, '08x')
            if pad > 0:
                encoded_byte = encoded_byte[:-pad * 2]
            index += 5
            result += ''.join([chr(int(encoded_byte[i:i + 2], 16)) for i in range(0, len(encoded_byte), 2)])
    return result
