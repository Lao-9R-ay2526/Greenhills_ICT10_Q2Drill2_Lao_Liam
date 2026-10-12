# Science Club Applicants
from pyscript import display, document

def name_verify(e):
    document.getElementById('div1').innerHTML = ' '


    names = ['liam lao' ,'daphne mariano' ,'maria agatha sia', 'juan piansay']
    f = document.getElementById('fname').value
    l = document.getElementById('lname').value
    apply = f + ' ' + l

    name1 = apply.lower().strip() in names


    display_message = ('Sorry This Applicant Has Not Been Registered' , f' {apply} is in the list')

    display(display_message[name1], target='div1')