'''
Quick Check: Booleans and truthiness
Decide whether the following statements are true or false:
 1, 0, -1, [0], 1 and 0, 1 > 0 or [].
'''

print("1", 1 == True)                            #True
print("0", 0 == True)                            #False
print("-1", -1 == True)                          #False
print("[0]", [0] is True)						 #False
print("1 and 0", 1 and 0 == True)				 #False
print("1 > 0 or []", 1 > 0 or [] is True)		 #True

