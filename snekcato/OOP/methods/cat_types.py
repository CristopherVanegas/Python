class Cat:
	type= "normal"	# CAT TYPE

	# METHOD
	def speak(self):
		print(f"Meow uwu, I'm a {self.type} cat")


Tabby= Cat()		# INSTANCE FROM CAT CLASS TO CREATE "Tabby CAT".
Tabby.type= "Tabby"	# ACCESSED TO type VARIABLE AND "normal" CHANGED TO "Tabby", EXPRESSION TO ACCESS THE type VARIABLE AND MODIFY "normal".
Tabby.speak()		# INVOKED THE Tabby Object and speak() INSTANCED FROM CAT.


Gray= Cat()		# INSTANCE FROM CAT CLASS TO CREATE "Gray CAT".
Gray.type="Gray"	# ACCESSED TO type VARIABLE AND "normal" CHANGED TO "Gray", EXPRESSION TO ACCESS THE type VARIABLE AND MODIFY "normal".
Gray.speak()		# INVOKED THE Gray Object and speak() INSTANCED FROM CAT.

