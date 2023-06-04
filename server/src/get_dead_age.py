import random
import logging

logger = logging.getLogger(__name__)

def generate_dead_age(attribute) -> int:
    logger.info("Generating dead age")
    health = attribute["health"]
    family = attribute["family"]

    # Check for appropriate input
    if not (0 <= health <= 10) or not (0 <= family <= 10):
        raise ValueError("Health and family values must be in the range [0, 10]")

    # Average the attributes as a basic measure of overall wellness
    average_wellness = (health + family) / 2

    # Translate wellness to a base age range
    # An average_wellness of 0 corresponds to a base age of 20
    # An average_wellness of 10 corresponds to a base age of 70
    base_age = 20 + (average_wellness * 5)

    # Add some randomness to the age
    # This will result in an age within +/- 15 years of the base age
    random_age_adjustment = random.uniform(-15, 15)

    dead_age = base_age + random_age_adjustment

    # Check that the resulting age is within a realistic range
    if dead_age < 0:
        dead_age = 0
    elif dead_age > 100:
        dead_age = 100

    dead_age = int(dead_age)

    logger.info(f"===== ------Generated dead age: {dead_age}---- ======")

    return dead_age
