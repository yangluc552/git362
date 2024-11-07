import random
import unittest
from credit_card_validator import credit_card_validator


def generate_random_visa():
    return "4" + "".join(str(random.randint(0, 9)) for _ in range(15))


def generate_random_mastercard():
    if random.choice([True, False]):
        prefix = str(random.randint(51, 55))
    else:
        prefix = str(random.randint(2221, 2720))
    return prefix + "".join(str(random.randint(0, 9)) for _ in range(16 - len(prefix)))


def generate_random_american_express():
    prefix = random.choice(["34", "37"])
    return prefix + "".join(str(random.randint(0, 9)) for _ in range(15))


class credit_card_validator_tests(unittest.TestCase):
    def test_visa(self):
        for _ in range(10000):
            visa_card = generate_random_visa()
            credit_card_validator(visa_card)

    def test_mastercard(self):
        for _ in range(10000):
            mastercard = generate_random_mastercard()
            credit_card_validator(mastercard)

    def test_american_express(self):
        for _ in range(10000):
            amex_card = generate_random_american_express()
            credit_card_validator(amex_card)

    def test_invalid_prefix(self):
        for _ in range(10000):
            invalid_visa = "3" + \
                "".join(str(random.randint(0, 9)) for _ in range(15))
            credit_card_validator(invalid_visa)

        for _ in range(10000):
            invalid_mastercard = "40" + \
                "".join(str(random.randint(0, 9)) for _ in range(14))
            credit_card_validator(invalid_mastercard)

        for _ in range(10000):
            invalid_amex = "5" + \
                "".join(str(random.randint(0, 9)) for _ in range(14))
            credit_card_validator(invalid_amex)

    def test_invalid_length(self):
        for _ in range(10000):
            invalid_length_card = "".join(str(random.randint(0, 9)) for _ in range(
                random.choice(range(1, 10)) + random.choice(range(20, 25))))
            credit_card_validator(invalid_length_card)

    def test_invalid_check_digit(self):
        for _ in range(10000):
            card_number = generate_random_visa(
            )[:-1] + str((int(generate_random_visa()[-1]) + 5) % 10)
            credit_card_validator(card_number)

    def test_invalid_cards(self):
        for _ in range(10000):
            invalid_card = "".join(str(random.randint(0, 9))
                                   for _ in range(random.randint(1, 25)))
            credit_card_validator(invalid_card)

    def test_invalid_visa_cards(self):
        for _ in range(100000):
            visa_card = "".join(str(random.randint(0, 9))
                                for _ in range(random.randint(1, 25)))
            credit_card_validator(visa_card)

    def test_invalid_visa_cards_random_length(self):
        for _ in range(10000):
            visa_card = "".join(str(random.randint(0, 9))
                                for _ in range(random.randint(1, 25)))
            credit_card_validator(visa_card)


if __name__ == '__main__':
    unittest.main()
