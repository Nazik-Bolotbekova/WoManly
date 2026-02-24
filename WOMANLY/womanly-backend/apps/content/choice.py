from django.db import models

class StaffPosition(models.TextChoices):
    admin = 'ADMIN','admin'
    editor = 'EDITOR','editor'
    manager = 'MANAGER','manager'
    volunteer = 'VOLUNTEER','volunteer'
    developer = 'DEV','developer'
    team_staff = 'TEAM','team staff'

class Status(models.TextChoices):
    new = 'NEW','new'
    in_progress = 'IN_PROGRESS','in_progress'
    resolved = 'RESOLVED','resolved'
    closed = 'CLOSED','closed'

class Priority(models.TextChoices):
    low = 'LOW','low'
    medium = 'MEDIUM','medium'
    high = 'HIGH','high'