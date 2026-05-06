import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
  
  def update(self, dt):
    self.position += (self.velocity * dt)
  
  def split(self):
    pygame.sprite.Sprite.kill(self)
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    else:
      log_event("asteroid_split")
      random_angle = random.uniform(20, 50)
      rotate_one = pygame.math.Vector2.rotate(self.velocity, random_angle)
      rotate_two = pygame.math.Vector2.rotate(self.velocity, -random_angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS
      first_new = Asteroid(self.position.x, self.position.y, new_radius)
      second_new = Asteroid(self.position.x, self.position.y, new_radius)
      first_new.velocity = rotate_one
      second_new.velocity = rotate_two