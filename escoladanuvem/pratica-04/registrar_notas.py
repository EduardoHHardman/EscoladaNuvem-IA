"""
Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando
notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar
solicitando. No final, deve exibir a média da turma.
"""

def registrar_notas():
 notas_lista= []    

 while True:
        
    try:
      entrada = input("Digite uma nota ou digite 'fim' para encerrar: ")
      if entrada.lower() == "fim":
         break
      nota = float(entrada)
      if 0 <= nota <= 10:
         notas_lista.append(nota)
      else:
         print ("Nota inválida : Digite um valor entre 0 e 10.")    
      continue

    except ValueError:
     print(" Entrada Inválida. Insira, por favor, um número válido ou digite 'fim' para encerrar: ")

 if notas_lista:        
       media = sum(notas_lista) / len(notas_lista)
       print(f"\nA média dos alunos é {media:.2f}")
       print(f"o total de notas válidas é : {len(notas_lista)}") 
 else:
       print("Nenhuma nota foi registrada ainda.")         
      
registrar_notas()
