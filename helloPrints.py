<<<<<<< HEAD
HEAD
quiHaEditat = ["Vizuete"]
desDOnSHaEditat = [MVizuete]
opcionsMenu = ["Sortir","Printar editors de la branca","Printar branques origen"]
=======
quiHaEditat = ["P.Bonilla"]
desDOnSHaEditat = ["pbvCalamot"]
opcionsMenu = ["Sortir","Printar editors de la branca"]
origin/pbvCalamot
=======
quiHaEditat = ["P.Bonilla"]
desDOnSHaEditat = []
opcionsMenu = ["Sortir","Printar editors de la branca"]
fc798b0 (Afegida funcionalitat i Pedro com a editor)
=======
quiHaEditat = ["P.Bonilla"]
desDOnSHaEditat = []
opcionsMenu = ["Sortir","Printar editors de la branca"]
fc798b0 (Afegida funcionalitat i Pedro com a editor)
=======
quiHaEditat = ["P.Bonilla"]
desDOnSHaEditat = []
opcionsMenu = ["Sortir","Printar editors de la branca"]
>>>>>>> fc798b0 (Afegida funcionalitat i Pedro com a editor)

whatToDoNext = -1  # Defineixo variable per entrar al while (i jugar a jocs con>
while whatToDoNext != 0:   
   print("\n", "\n") # es cutre, pero no vull importar res a aquest examen.
   print("Hello World!")

   # printo les opcions disponible
   for i in range(len(opcionsMenu)):
      print(i , ": " , opcionsMenu[i])

   # M'asseguro que la opció es pot passar a sencer, i si no deso -1 
   try:
      whatToDoNext = int(input("Introdueix la opció desitjada : "))
   except:
      print("Has de introduir un número sencer")
      whatToDoNext = -1

   # Que fa cada opcion ) 0 no fa res, pq ja surt.
   if (whatToDoNext not in range(len(opcionsMenu))):
      print("Opcio Inválida")

   elif whatToDoNext == 1:
      print(" ====================")
      print(" Ha editat: ", end ="")
      for editor in quiHaEditat:
         print(editor, end = ", ")
      print("\n","====================")
<<<<<<< HEAD
HEAD

   elif whatToDoNext == 2:
      print(" ====================")
      print(" Branques amb edits: ", end ="")
      for branca in desDOnSHaEditat:
         print(branca, end = ", ")
      print("\n","====================")
fc798b0 (Afegida funcionalitat i Pedro com a editor)
=======
>>>>>>> fc798b0 (Afegida funcionalitat i Pedro com a editor)
