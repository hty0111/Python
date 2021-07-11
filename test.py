from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex

# 要加密的明文
data = 'NB!'
# 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
# 目前AES-128足够用
key = b'this is a 16 key'
# 生成长度等于AES块大小的不可重复的密钥向量
iv = Random.new().read(AES.block_size)

# 使用key和iv初始化AES对象, 使用MODE_CFB模式
mycipher = AES.new(key, AES.MODE_CFB, iv)
# 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
# 将iv（密钥向量）加到加密的密文开头，一起传输
ciphertext = iv + mycipher.encrypt(data.encode())

# 解密的话要用key和iv生成新的AES对象
mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# 使用新生成的AES对象，将加密的密文解密
decrypttext = mydecrypt.decrypt(ciphertext[16:])

print('密钥k为：', key)
print('iv为：', b2a_hex(ciphertext)[:16])
print('加密后数据为：', b2a_hex(ciphertext)[16:])
print('解密后数据为：', decrypttext.decode())



