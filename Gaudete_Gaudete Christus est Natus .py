###  Gaudete, Gaudete Christus est Natus !!!!!

def display_chanson_lyrics(chanson):
  if chanson == "Gaute":
    print("Gaudete, gaudete! Christus est natus Ex Maria Virgine, Gaudete!  Tempus adest gratiae Hoc quod optabamus,Carmina laetitiae Devote redamus.")
  elif chanson == "Rejoyce":
    print("Lyrics for Gaute in English")
  else:
    print("Invalid chanson selection.")

chanson = input("Select Gaute or Rejoyce: ")
display_chanson_lyrics(chanson)
