from celery.task import task
from celery import signature, group

#@task
#def add(x,y):
#    return x + y

#@task
#def double(x):
#    return x * 2

#@task
#def triple(x):
#    return x * 3

@task
#def test_grouping(x,y):
#    chain = (add.s(x,y) | group(double.s(), triple.s()))
#    chain.delay()
#    return "Kicked Off tasks"

@task
def dice_sides(sides):
   return random.randrange(sides) + 1

@task
def multi_dice(number, sides):
    dice = range(number)
    result = []
    for i in dice:
        result.append(dice_sides(sides))
    return result

@task
def dice_roll_chain(number, sides):
    chain = (dice_sides.s(sides) | multi_dice.s(number,sides)
    chain.delay()
    return "Kicked off tasks"
