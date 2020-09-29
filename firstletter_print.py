 #create a list of the first letters of every word in the string below:
 
 
st = 'Create a list of the first letters of every word in this string'
val =[]
for i in st.split():
  val.append(i[0])
print (val)
