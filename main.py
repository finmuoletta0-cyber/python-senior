
class DogLife:
    total_months_passed = 0

    def __init__(self, name="Айворі", breed="Бордер Коллі"):
        self.name = name
        self.breed = breed
        self.happiness = 80
        self.energy = 100
        self.height = 0

        print("Початок життя")
        print(f"Щеня народилося! Та кличку йому дали... Кличка: {self.name}, Порода: {self.breed}")

    def grow(self, height=1):
        self.height += height

    def live_month(self, season):
        print(f"Сезон: {season}")
        DogLife.total_months_passed += 3

        if season == "Зима":
            print(f"{self.name} вивчає трюки дома та вже трохи підрастає")
            self.grow(20)

        elif season == "Весна":
            print(f"{self.name} активно бігає за фрізбі на вулиці")
            self.grow(15)

        elif season == "Літо":
            print(f"{self.name} довго гуляє на вулиці та плаває у басейні")
            self.grow(10)

        elif season == "Осінь":
            print(f"{self.name} стрибає в купу листя та шукає каштани")
            self.grow(2)


first_student = DogLife(name="Айворі")

first_student.live_month("Зима")
first_student.live_month("Весна")
first_student.live_month("Літо")
first_student.live_month("Осінь")

print(f"Всього місяців прожито(поки що): {DogLife.total_months_passed}")
print(f"Зріст: {first_student.height}")








