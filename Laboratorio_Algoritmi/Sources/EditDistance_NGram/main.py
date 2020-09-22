import inquirer
from Edit_Distance_Search import Edit_Distance_Search
from N_Gram_Search import N_Gram_Search

while(1):
    questions = [inquirer.List('lessico',
    message="Scegli su che dizionario effettuare la Edit-Distance",
    choices=['Lessico_completo', '2_gram', '3_gram'],),]
    answers = inquirer.prompt(questions)
    
    if(answers["lessico"] == 'Lessico_completo'):
        Edit_Distance_Search()
    else:
        N_Gram_Search(answers["lessico"])
        

