'''
Quick Check: What can be a key?
Decide which of the following expressions can be a dictionary key:
 1; 'bob'; ('tom', [1, 2, 3]); ["filename"]; "filename"; ("filename", "extension")
'''

1; 							#can, 	number: immutable, hashable
'bob'; 						#can, 	string: immutable, hashable
('tom', [1, 2, 3]); 		#cannot, 	list item in a tuple: mutable
["filename"];				#cannot, 	list: mutable
"filename"; 				#can, 	string: immutable, hashable
("filename", "extension") 	#can, 	tuple with string items