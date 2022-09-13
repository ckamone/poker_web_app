import random
from pywebio.input import *
from pywebio.output import *

def odds():    
    put_markdown("""# Pot odds
    
    Pot odds (шансы банка) - это отношение вашей ставки к сумме банка.
    Шансы карт (считается по аутам) должны быть выше шансов банка...
    
    ## Odds calculation

    """, strip_indent=4)

    #show answer
    def check(val1,val2,name):
        if val1==val2:
            put_text('For',name,'your answer is right:',val2)
        else:
            put_text('For',name,'right answer:',val2,'; your answer was:',val1)

    #how many $ in the bank already
    bank=random.randint(1,9)*100

    #op bet
    b=random.randint(1,5)
    if b==1:
        bet=bank #x1
    elif b==2:
        bet=bank/2 #x1/2
    elif b==3:
        bet=bank/4 #x1/4
    elif b==4:
        bet=bank*2 #x2
    elif b==5:
        bet=(bank/4)*3 #x3/4

    #how many $ you need to call
    call=bet

    #show task
    put_text('1) Bank=',bank,'; \n2) Oponent bet=',bet,'\n3) Do you need to call?')

    #user input calculations
    info = input_group('Odds calculation', [
        input("pot=bank+op.bet=", name="pot", type=FLOAT),
        input("odds=pot/call=", name="odds", type=FLOAT),
        input("odds%=100/(odds+1)=", name="percent", type=FLOAT),
    ])

    #auto calculations
    pot=bank+bet
    oddsC=round(pot/call,1)
    perc=100/(oddsC+1)
    oddsP=round(100-(perc*oddsC),1)

    #use user answers to check
    p=info['pot']
    oddsU=info['odds']
    per=info['percent']

    #show user errors
    check(pot,p,'pot')
    check(oddsU,oddsC,'odds')
    check(per,oddsP,'odds %')