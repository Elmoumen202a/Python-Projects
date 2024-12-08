
# 🚗 Car Rental System

A Python project to manage car rentals for a company. This system allows you to:

- Add cars to the rental inventory.
- Rent cars to customers.
- Return cars after use.
- List all available and rented cars.

## Project Structure

```bash
rent_car_project/
├── main.py
├── tests.py
├── readme.md
```
## 💡 Features

1. **Add Cars:** Add new cars to the system with a unique ID, model, and rent per day.
2. **Rent Cars:** Mark a car as rented if available.
3. **Return Cars:** Mark a car as returned.
4. **List Cars:** View all cars with their current status.


## 🛠️ Setup

1. Clone the repository.
2. Run `main.py` to interact with the system.
3. Use `tests.py` to run unit tests.

---

## 🧪 Testing

To test the functionality, run:
```bash
python tests.py
```

## 🚀 Example

```python
rental_system = CarRental()
rental_system.add_car(1, "Toyota Corolla", 40)
print(rental_system.list_cars())
```

## 🔗 License

This project is open-source and free to use. Feel free to contribute!

Enjoy managing your car rentals! 🚘
