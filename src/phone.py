class Phone:
    def __init__(
        self,
        brand: str,
        model: str,
        price: float,
        color: str,
        storage_gb: int,
        is_in_stock: bool
    ) -> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.storage_gb = storage_gb
        self.is_in_stock = is_in_stock

    def get_full_name(self) -> str:
        return f"{self.brand} {self.model}"

    def apply_discount(self, discount_percent: float) -> None:
        if discount_percent < 0:
            raise ValueError("Процент скидки не может быть отрицательным")
        if discount_percent > 100:
            raise ValueError("Процент скидки не может превышать 100%")
        self.price *= (1 - discount_percent / 100)

    def check_availability(self) -> str:
        return "В наличии" if self.is_in_stock else "Нет в наличии"

    def __str__(self) -> str:
        availability = self.check_availability()
        return (
            f"📱 {self.get_full_name()} ({self.color}, {self.storage_gb} ГБ)\n"
            f"   Цена: {self.price:.2f} ₽\n"
            f"   Статус: {availability}"
        )


# Демонстрация работы класса
if __name__ == "__main__":
    phone1 = Phone("Apple", "iPhone 15", 89990.0, "Синий", 128, True)
    phone2 = Phone("Samsung", "Galaxy S24", 75990.0, "Чёрный", 256, False)
    phone3 = Phone("Xiaomi", "Redmi Note 13", 24990.0, "Зелёный", 128, True)
    phone4 = Phone("Google", "Pixel 8", 69990.0, "Белый", 256, True)

    print("=== Полные названия ===")
    for phone in [phone1, phone2, phone3, phone4]:
        print(phone.get_full_name())

    print("\n=== Проверка наличия ===")
    for phone in [phone1, phone2, phone3, phone4]:
        print(f"{phone.get_full_name()}: {phone.check_availability()}")

    print("\n=== Применение скидки 10% к iPhone ===")
    print(f"До скидки: {phone1.price:.2f} ₽")
    phone1.apply_discount(10)
    print(f"После скидки: {phone1.price:.2f} ₽")

    print("\n=== Строковое представление телефонов ===")
    print(phone1)
    print()
    print(phone2)
    print()
    print(phone3)
