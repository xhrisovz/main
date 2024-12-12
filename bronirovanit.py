import random
import time

class Event:
    def __init__(self, name, date, available_tickets):
        self.name = name
        self.date = date
        self.available_tickets = available_tickets

    def show_event(self):
        return f"Мероприятие: {self.name}, Дата: {self.date}, Доступные билеты: {self.available_tickets}"

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def register(self):
        print(f"Пользователь {self.username} зарегистрирован с email {self.email}")

class PaymentSystem:
    @staticmethod
    def process_payment(amount):
        print(f"Обрабатывается платеж на сумму {amount} руб.")
        time.sleep(4)
        if random.choice([True, False]):
            print("Платеж успешно обработан!")
            return True
        else:
            print("Ошибка при обработке платежа.")
            return False

class TicketBookingSystem:
    def __init__(self):
        self.events = []
        self.users = []

    def add_event(self, name, date, available_tickets):
        self.events.append(Event(name, date, available_tickets))

    def list_events(self):
        print("Доступные мероприятия:")
        for event in self.events:
            print(event.show_event())

    def book_ticket(self, user, event_name, num_tickets):
        for event in self.events:
            if event.name == event_name:
                if event.available_tickets >= num_tickets:
                    print(f"Вы выбрали {num_tickets} билетов на мероприятие '{event.name}'.")
                    if PaymentSystem.process_payment(num_tickets * 500):  # Стоимость билета 500 руб.
                        event.available_tickets -= num_tickets
                        print(f"Билеты на '{event.name}' успешно забронированы для пользователя {user.username}.")
                        return
                    else:
                        print("Не удалось забронировать билеты из-за ошибки платежа.")
                else:
                    print(f"Недостаточно билетов на мероприятие '{event.name}'. Доступно всего {event.available_tickets} билетов.")
                return
        print("Мероприятие не найдено.")

# Пример использования системы
booking_system = TicketBookingSystem()

# Добавление мероприятий
random_bilet1 = random.randint(0, 256)
random_bilet2 = random.randint(0, 256)
booking_system.add_event("Вечеринка в Строителе", "2024-12-20", random_bilet1)
booking_system.add_event("Концерт в Форуме", "2024-12-22", random_bilet2)

# Регистрация пользователя
user = User("Рома", "xasanator@mail.ru")
user.register()

# Просмотр доступных мероприятий
booking_system.list_events()

# Бронирование билетов
random_bron = random.randint(1,5)
event_names = [event.name for event in booking_system.events]
random_event_name = random.choice(event_names)
booking_system.book_ticket(user, random_event_name, random_bron)
