import pygame

class Collision_controller():
    def __init__(self):
        pass

    def is_collided_with(self, obj1, obj2):
        if obj1.state == "Attacking":
            return obj1.rect.colliderect(obj2.rect)

