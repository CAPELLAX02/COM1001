# users.txt de şu anda Ahmet\n Mehmet\n Ömer\n yazıyor.

# main() fonksiyonu, users.txt dosyasına Fatma, Ayse, Merve isimlerini ekler.

def main():
  outfile = open('users.txt', 'a')
  
  newNames = ['Fatma\n', 'Ayse\n']

  outfile.writelines(newNames)
  outfile.write('Merve\n')
  outfile.close()

main()