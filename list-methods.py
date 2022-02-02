number=[1,10,5,3,7,8]
letter=["k","m","s","i","h"]

# Minimum Değer
val=min(number)
val=min(letter)
# Maximum Değer
val=max(number)
val=max(letter)

val=number[2:5]

number[4]=40


# Liste sonuna değer ekler 
number.append(41)

# İstenilen yere değer ekleme 
number.insert(3, 34)

# En son rakamı silme pop()
number.pop()

# Karakteri bul ve sil remove()
number.remove(5)

# Sayısal büyüklük olarak sıralama sort()
number.sort()

# Listeyi tersine çevirme reverse()
number.reverse()

# Listede kaç tane olduğunu saymak için count() kullanılır
print(number.count(8))


print(number)

print(val)