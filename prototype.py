from soya import *

def prompt(obj):
    return obj.get_name() + ':' + obj.get_responder_name() + '> '

print('AI system prototype : soya')
soya = Soya('soya')

while True:
    inputs = input(' > ')
    if not inputs:
        print('じゃあね')
        break
    response = soya.dialogue(inputs)
    print(prompt(soya), response)
