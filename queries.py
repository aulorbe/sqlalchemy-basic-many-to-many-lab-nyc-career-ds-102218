from seed import *

def return_christian_bales_roles(session):
    return session.query(Role).join(ActorRole).join(Actor).filter(Actor.name == 'Christian Bale').all()



def return_catwoman_actors(session):
    return session.query(Actor).join(ActorRole).join(Role).filter(Role.character=='Catwoman').all()




def return_number_of_batman_actors(session):
    return len(session.query(Actor).join(ActorRole).join(Role).filter(Role.character=='Batman').all())
