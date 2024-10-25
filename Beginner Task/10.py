class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage

    def display_info(self):
        return (f"Screen Type: {self.screen_type}, Network Type: {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")

class Apple(MobilePhone):
    def __init__(self, model, storage):
        super().__init__("Touch Screen", "5G", False, "12MP", "48MP", "4GB", storage)
        self.model = model

    def display_info(self):
        return f"Apple Model: {self.model}, {super().display_info()}"

class Samsung(MobilePhone):
    def __init__(self, model, storage, dual_sim):
        super().__init__("Touch Screen", "4G/5G", dual_sim, "16MP", "32MP", "4GB", storage)
        self.model = model

    def display_info(self):
        return f"Samsung Model: {self.model}, {super().display_info()}"

# Getting user input for Apple
apple_model = input("Enter the Apple model: ")
apple_storage = input("Enter storage for Apple (16GB, 32GB, 64GB): ")
apple_phone = Apple(apple_model, apple_storage)

# Getting user input for Samsung
samsung_model = input("Enter the Samsung model: ")
samsung_storage = input("Enter storage for Samsung (16GB, 32GB, 64GB): ")
dual_sim_input = input("Does the Samsung phone have dual SIM? (yes/no): ")
samsung_dual_sim = dual_sim_input.lower() == 'yes'
samsung_phone = Samsung(samsung_model, samsung_storage, samsung_dual_sim)

# Displaying information for both phones
print(apple_phone.display_info())
print(samsung_phone.display_info())

(2)

class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
        self.call_history = []

    def display_info(self):
        return (f"Screen Type: {self.screen_type}, Network Type: {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")

    def make_call(self, contact):
        print(f"Making a call to {contact}...")
        self.call_history.append(contact)

    def receive_call(self, caller):
        print(f"Receiving a call from {caller}...")

    def take_a_picture(self, camera_type):
        if camera_type.lower() == 'front':
            print(f"Taking a picture with the front camera: {self.front_camera}")
        elif camera_type.lower() == 'rear':
            print(f"Taking a picture with the rear camera: {self.rear_camera}")
        else:
            print("Invalid camera type. Please choose 'front' or 'rear'.")

class Apple(MobilePhone):
    def __init__(self, model, storage):
        super().__init__("Touch Screen", "5G", False, "12MP", "48MP", "4GB", storage)
        self.model = model

    def display_info(self):
        return f"Apple Model: {self.model}, {super().display_info()}"

class Samsung(MobilePhone):
    def __init__(self, model, storage, dual_sim):
        super().__init__("Touch Screen", "4G/5G", dual_sim, "16MP", "32MP", "4GB", storage)
        self.model = model

    def display_info(self):
        return f"Samsung Model: {self.model}, {super().display_info()}"

# Getting user input for Apple
apple_model = input("Enter the Apple model: ")
apple_storage = input("Enter storage for Apple (16GB, 32GB, 64GB): ")
apple_phone = Apple(apple_model, apple_storage)

# Getting user input for Samsung
samsung_model = input("Enter the Samsung model: ")
samsung_storage = input("Enter storage for Samsung (16GB, 32GB, 64GB): ")
dual_sim_input = input("Does the Samsung phone have dual SIM? (yes/no): ")
samsung_dual_sim = dual_sim_input.lower() == 'yes'
samsung_phone = Samsung(samsung_model, samsung_storage, samsung_dual_sim)

# Displaying information for both phones
print(apple_phone.display_info())
print(samsung_phone.display_info())

# Example interactions with the mobile phones
# Making calls
contact_name = input("Enter a contact name to call with Apple phone: ")
apple_phone.make_call(contact_name)

caller_name = input("Enter a caller name for Samsung phone: ")
samsung_phone.receive_call(caller_name)

# Taking pictures
camera_choice = input("Choose camera type for Apple phone (front/rear): ")
apple_phone.take_a_picture(camera_choice)

camera_choice = input("Choose camera type for Samsung phone (front/rear): ")
samsung_phone.take_a_picture(camera_choice)

(3)

class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
        self.call_history = []

    def display_info(self):
        return (f"Screen Type: {self.screen_type}, Network Type: {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")

    def make_call(self, contact):
        print(f"Making a call to {contact}...")
        self.call_history.append(contact)

    def receive_call(self, caller):
        print(f"Receiving a call from {caller}...")

    def take_a_picture(self, camera_type):
        if camera_type.lower() == 'front':
            print(f"Taking a picture with the front camera: {self.front_camera}")
        elif camera_type.lower() == 'rear':
            print(f"Taking a picture with the rear camera: {self.rear_camera}")
        else:
            print("Invalid camera type. Please choose 'front' or 'rear'.")

class Apple(MobilePhone):
    def __init__(self, model, storage):
        super().__init__("Touch Screen", "5G", False, "12MP", "48MP", "4GB", storage)  # Call to the parent constructor
        self.model = model

    def display_info(self):
        return f"Apple Model: {self.model}, {super().display_info()}"

class Samsung(MobilePhone):
    def __init__(self, model, storage, dual_sim):
        super().__init__("Touch Screen", "4G/5G", dual_sim, "16MP", "32MP", "4GB", storage)  # Call to the parent constructor
        self.model = model

    def display_info(self):
        return f"Samsung Model: {self.model}, {super().display_info()}"

# Getting user input for Apple
apple_model = input("Enter the Apple model: ")
apple_storage = input("Enter storage for Apple (16GB, 32GB, 64GB): ")
apple_phone = Apple(apple_model, apple_storage)

# Getting user input for Samsung
samsung_model = input("Enter the Samsung model: ")
samsung_storage = input("Enter storage for Samsung (16GB, 32GB, 64GB): ")
dual_sim_input = input("Does the Samsung phone have dual SIM? (yes/no): ")
samsung_dual_sim = dual_sim_input.lower() == 'yes'
samsung_phone = Samsung(samsung_model, samsung_storage, samsung_dual_sim)

# Displaying information for both phones
print(apple_phone.display_info())
print(samsung_phone.display_info())

# Example interactions with the mobile phones
# Making calls
contact_name = input("Enter a contact name to call with Apple phone: ")
apple_phone.make_call(contact_name)

caller_name = input("Enter a caller name for Samsung phone: ")
samsung_phone.receive_call(caller_name)

# Taking pictures
camera_choice = input("Choose camera type for Apple phone (front/rear): ")
apple_phone.take_a_picture(camera_choice)

camera_choice = input("Choose camera type for Samsung phone (front/rear): ")
samsung_phone.take_a_picture(camera_choice)

(4)

class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
        self.call_history = []

    def display_info(self):
        return (f"Screen Type: {self.screen_type}, Network Type: {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")

    def make_call(self, contact):
        print(f"Making a call to {contact}...")
        self.call_history.append(contact)

    def receive_call(self, caller):
        print(f"Receiving a call from {caller}...")

    def take_a_picture(self, camera_type):
        if camera_type.lower() == 'front':
            print(f"Taking a picture with the front camera: {self.front_camera}")
        elif camera_type.lower() == 'rear':
            print(f"Taking a picture with the rear camera: {self.rear_camera}")
        else:
            print("Invalid camera type. Please choose 'front' or 'rear'.")

class Apple(MobilePhone):
    def __init__(self, model, storage):
        super().__init__("Touch Screen", "5G", False, "12MP", "48MP", "4GB", storage)  # Call to the parent constructor
        self.model = model

    def display_info(self):
        return f"Apple Model: {self.model}, {super().display_info()}"

class Samsung(MobilePhone):
    def __init__(self, model, storage, dual_sim):
        super().__init__("Touch Screen", "4G/5G", dual_sim, "16MP", "32MP", "4GB", storage)  # Call to the parent constructor
        self.model = model

    def display_info(self):
        return f"Samsung Model: {self.model}, {super().display_info()}"

# Create multiple Apple objects with different properties
apple_phone1 = Apple("iPhone 14", "64GB")
apple_phone2 = Apple("iPhone 13", "128GB")
apple_phone3 = Apple("iPhone SE", "256GB")

# Displaying information for each Apple phone
print(apple_phone1.display_info())
print(apple_phone2.display_info())
print(apple_phone3.display_info())

# Example interactions with one of the Apple phones
contact_name = input("Enter a contact name to call with iPhone 14: ")
apple_phone1.make_call(contact_name)

camera_choice = input("Choose camera type for iPhone 14 (front/rear): ")
apple_phone1.take_a_picture(camera_choice)

(5)

class MobilePhone:
    def __init__(self, screen_type, network_type, dual_sim, front_camera, rear_camera, ram, storage):
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage
        self.call_history = []

    def display_info(self):
        return (f"Screen Type: {self.screen_type}, Network Type: {self.network_type}, "
                f"Dual SIM: {self.dual_sim}, Front Camera: {self.front_camera}, "
                f"Rear Camera: {self.rear_camera}, RAM: {self.ram}, Storage: {self.storage}")

    def make_call(self, contact):
        print(f"Making a call to {contact}...")
        self.call_history.append(contact)

    def receive_call(self, caller):
        print(f"Receiving a call from {caller}...")

    def take_a_picture(self, camera_type):
        if camera_type.lower() == 'front':
            print(f"Taking a picture with the front camera: {self.front_camera}")
        elif camera_type.lower() == 'rear':
            print(f"Taking a picture with the rear camera: {self.rear_camera}")
        else:
            print("Invalid camera type. Please choose 'front' or 'rear'.")

class Apple(MobilePhone):
    def __init__(self, model, storage):
        super().__init__("Touch Screen", "5G", False, "12MP", "48MP", "4GB", storage)
        self.model = model

    def display_info(self):
        return f"Apple Model: {self.model}, {super().display_info()}"

class Samsung(MobilePhone):
    def __init__(self, model, storage, dual_sim):
        super().__init__("Touch Screen", "4G/5G", dual_sim, "16MP", "32MP", "4GB", storage)
        self.model = model

    def display_info(self):
        return f"Samsung Model: {self.model}, {super().display_info()}"

# Creating multiple Samsung objects with user input
samsung_phones = []
for i in range(3):  # Creating three Samsung objects
    model = input(f"Enter the model for Samsung phone {i + 1}: ")
    storage = input(f"Enter storage for Samsung phone {i + 1} (16GB, 32GB, 64GB): ")
    dual_sim_input = input(f"Does Samsung phone {i + 1} have dual SIM? (yes/no): ")
    dual_sim = dual_sim_input.lower() == 'yes'
    samsung_phone = Samsung(model, storage, dual_sim)
    samsung_phones.append(samsung_phone)

# Displaying information for each Samsung phone
for phone in samsung_phones:
    print(phone.display_info())

# Example interactions with the first Samsung phone
contact_name = input("Enter a contact name to call with the first Samsung phone: ")
samsung_phones[0].make_call(contact_name)

camera_choice = input("Choose camera type for the first Samsung phone (front/rear): ")
samsung_phones[0].take_a_picture(camera_choice)
