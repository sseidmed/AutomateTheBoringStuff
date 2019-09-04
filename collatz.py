def collatz(number):
    if number == 0:
        
        return "No zero"       
    elif number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result



while True:    
  mynum = input("Give me a number above 0: ")   
  try:            
      while mynum != 1:
          mynum = collatz(int(mynum))  
      print("Done!")
      break  
  except (ValueError, TypeError) as e:
    try:
      not_zero = input("Number should be above 0 or should be an integer ")
      while not_zero != 1:
        not_zero = collatz(int(not_zero))
      print("Done!")
      break  
    except(ValueError, TypeError)  as e:
      input("Stahp with zeros and random letters! ")
