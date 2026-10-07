from pyscript import document, display

members = ["Ellie Goulding", "Kitchie Nadal", "Lizzy McAlpine", "Gracie Abrams", "Emmy Rossum"]

def check_member(e):
    first = document.getElementById("firstname").value
    last = document.getElementById("lastname").value

    full_name = first + " " + last 
        #combines the first name and last name user inputs

    is_member = full_name in members 
        #to check if fullanem (first name and last name combined) is part of the list of members.


# tuple containing 2 messages (values)
    messages = (
    "Sorry " + full_name + ", your name is not on the list.", #sorry message index is 0
    "Congratulations " + full_name + "! You are now part of the ICT club."  ) #congrats message index is 1

    document.getElementById("result").innerHTML = messages[is_member]

    #display depends whether is_member is true or false
    #if input ISNT part of the list, this registers as: messages[false] --> messages[0] --> will show the sorry message of index 0
    #if input IS part of the list, this registers as: messages[true] --> messages[1] --> will show the sorry message of index 1 
