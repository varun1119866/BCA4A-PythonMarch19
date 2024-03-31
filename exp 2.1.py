
sample_string = "Hello, World!"

print("Original string:", sample_string)
print("First five characters:", sample_string[:5])  
print("Characters after index 7:", sample_string[7:])  
print("Characters between index 2 and 7:", sample_string[2:7])  
print("Every second character:", sample_string[::2])  

print("Last five characters:", sample_string[-5:])
print("Every second character in reverse:", sample_string[::-2])


modified_string = sample_string[:5] + " Python!" 
print("Modified string:", modified_string)
