def my_substr(string, start, fin):
 
  if start < 0 or fin < start:
    print ('Хуй те барыга!')
    return False
  elif fin <= 0 or fin > len(string):
    print("Нихуя не получится у тебя, сука!")
    return False

  
  index = start
  result = '' 

  
  while index <= fin:
    result = result + string[index]
    index += 1

    
  print(result[::-1].replace(" ",""))
  return result

my_substr('Представим расширгумента: строку, индекс и', 11, 32)