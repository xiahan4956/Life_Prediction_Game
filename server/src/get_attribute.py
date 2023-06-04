import random
import logging

logger = logging.getLogger(__name__)

def generate_attribute():
    logger.info("Choosing attributes")

    beauty = random.randint(0, 10)
    health = random.randint(0, 10)
    intelligence = random.randint(0, 10)
    family = random.randint(0, 10)

    total_points = beauty + health + intelligence + family
    remaining_points = 20 - total_points

    while remaining_points > 0:
        attribute = random.choice(["beauty", "health", "intelligence", "family"])
        if eval(attribute) < 10:
            exec(f"{attribute} += 1")
            remaining_points -= 1

    attributes = {"beauty": beauty, "health": health, "intelligence": intelligence, "family": family}
    logger.info(f"****Attributes generated: {attributes}******")
    return attributes
